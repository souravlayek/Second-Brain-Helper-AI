from llama_index.core import VectorStoreIndex
from llama_index.readers.minio import MinioReader
import os
from llama_index.core.storage.storage_context import StorageContext

from llama_index.core.indices.loading import load_index_from_storage

from dotenv import load_dotenv

load_dotenv()

persist_dir="dataset_index"

def loadAndMakeIndex():
    # Configuration for your MinIO instance
    reader = MinioReader(
        minio_endpoint="minioapi.souravlayek.com",     # Or your MinIO endpoint
        minio_access_key="MINIO_ACCESS_KEY",
        minio_secret_key="KlETYA2FZVWsWAApM7Kf7tvAKxmt8XYAPrzY9VTB",
        minio_secure=True,
        bucket="obsidiannotes",
        prefix="Project Ideas/"

    )

    # Load documents from a specific bucket and prefix
    docs = reader.load_data()

    # Build index
    index = VectorStoreIndex.from_documents(docs)

    return index

index = None

if os.path.exists(persist_dir):
    storage_context = StorageContext.from_defaults(
      persist_dir=persist_dir,
     )
    load_index_from_storage(
        storage_context=storage_context
    )
else:
    index = loadAndMakeIndex()

index.storage_context.persist(persist_dir)