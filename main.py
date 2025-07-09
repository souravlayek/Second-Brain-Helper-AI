import streamlit as st
from dotenv import load_dotenv
import os
import datetime

from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.llms.openai import OpenAI  # ✅ Corrected import
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.base.llms.types import ChatMessage
from llama_index.readers.minio import MinioReader
from llama_index.core import Document

load_dotenv()

persist_dir = "dataset_index"
log_file = "last_sync.log"
index = None

def write_last_sync():
    os.makedirs(persist_dir, exist_ok=True)
    with open(log_file, "w") as f:
        f.write(datetime.datetime.now().isoformat())

def read_last_sync():
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            return f.read().strip()
    return None
import requests

def fetch_raindrop_bookmarks(api_token, collection_id=None, max_items=100):
    headers = {"Authorization": f"Bearer {api_token}"}
    url = "https://api.raindrop.io/rest/v1/raindrops/0"  # 0 = all collections
    if collection_id:
        url = f"https://api.raindrop.io/rest/v1/raindrops/{collection_id}"
    params = {"perpage": max_items}
    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    data = resp.json()
    docs = []
    for item in data.get("items", []):
        title = item.get("title", "")
        excerpt = item.get("excerpt", "")
        link = item.get("link", "")
        content = f"{title}\n{excerpt}\n{link}"
        doc = Document(text=content, metadata={"source": "raindrop", "id": item.get("_id")})
        docs.append(doc)
    return docs

@st.cache_resource(show_spinner=False)
def get_index(force_resync=False):
    if os.path.exists(persist_dir) and not force_resync:
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
        return load_index_from_storage(storage_context)
    else:
        # MinIO
        reader = MinioReader(
            minio_endpoint="minioapi.souravlayek.com",
            minio_access_key=os.getenv("MINIO_ACCESS_KEY"),
            minio_secret_key=os.getenv("MINIO_SECRET_KEY"),
            minio_secure=True,
            bucket="obsidiannotes",
            prefix="Knowlege Hub/"
        )
        docs = reader.load_data()
        # Raindrop.io
        raindrop_token = os.getenv("RAINDROP_API_TOKEN")
        if raindrop_token:
            raindrop_docs = fetch_raindrop_bookmarks(raindrop_token)
            docs.extend(raindrop_docs)
        index = VectorStoreIndex.from_documents(docs)
        index.storage_context.persist(persist_dir)
        write_last_sync()
        return index

# UI: Last sync and resync button
last_sync = read_last_sync()
col1, col2 = st.columns([3, 1])
with col1:
    st.title("🧠 SecondBrain - AI Assistant")
    if last_sync:
        st.caption(f"Last sync: {last_sync}")
    else:
        st.caption("No sync yet.")
with col2:
    resync = st.button("🔄 Resync")

# Resync logic
if 'index' not in st.session_state or resync:
    try:
        st.session_state['index'] = get_index(force_resync=resync)
    except Exception as e:
        print(e)
        st.error(f"Error during index loading or resync: {e}")
        st.stop()
index = st.session_state['index']

# Query Engine
retriever = VectorIndexRetriever(index=index)
query_engine = RetrieverQueryEngine(retriever=retriever)
query_engine.llm = OpenAI(model="gpt-4.1-nano-2025-04-14")

# Set a system prompt for the session
SYSTEM_PROMPT = "You are Braian an AI assistant that helps answer questions from the users notes and bookmarks Be concise helpful and reference sources when possible also share from where did you get that scan document metadata for that"
if hasattr(query_engine, 'system_prompt'):
    query_engine.system_prompt = SYSTEM_PROMPT
elif hasattr(query_engine.llm, 'system_prompt'):
    query_engine.llm.system_prompt = SYSTEM_PROMPT
# If neither, will need to pass as context in the query (handled below if needed)

# Streamlit UI
query = st.text_input("Ask something from your notes...")

if query:
    with st.spinner("Thinking..."):
        response = query_engine.query(query)
        st.markdown("### 🗨️ Answer")
        st.write(response.response)