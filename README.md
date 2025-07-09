# 🧠 SecondBrain

SecondBrain is an AI-powered knowledge assistant that connects to your personal knowledge hub—including your Obsidian vault (hosted on MinIO) and Raindrop bookmarks—and allows you to query it using natural language. It turns your saved notes and bookmarks into a searchable, private, AI-powered second brain.

---

## 🚀 Features

- 🧠 **Personal Knowledge Retrieval**: Query your pre-existing Second Brain (Obsidian Vault) using natural language questions.
- ☁️ **Remote Storage via MinIO**: Connect and retrieve notes securely from your self-hosted MinIO server.
- 🔖 **Bookmark Intelligence**: Seamlessly integrates with Raindrop.io to utilize your saved web content as context.
- 🤖 **AI-Powered Q&A**: Uses LLMs to answer questions based on your private knowledge base—nothing is hallucinated.
- 🔐 **Privacy-First Architecture**: All knowledge stays private and under your control; no cloud syncing unless you want it.
- 🛠️ **Custom Context Indexing**: Automatically indexes your notes and bookmarks to serve as rich semantic context for the AI.

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/SecondBrain.git
cd SecondBrain
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run main.py
```

---

## 📁 Project Structure

```
.
├── main.py                 # Entry point for the app
├── .env                    # Your Environment Variables
├── requirement.txt         # Packages needs to run this project
├── README.md               # You're here!
```

---

## 📚 Technologies Used

- 🐍 Python 3.10+
- 🤖 OpenAI GPT-4 / LLMs
- 🪣 MinIO (S3-Compatible Object Storage)
- 🔖 Raindrop.io API
- 🧠 LangChain / LlamaIndex
- 📄 Markdown + JSON parsers

---

## 💡 Usage Ideas

- Ask questions like: _“What were my notes on async Python?”_
- Get AI summaries of related notes and saved bookmarks
- Use it to reflect on journal entries or past research
- Stay in full control of your Second Brain—privately

---

## 🛠️ Contribution

We welcome contributions! Feel free to fork this repository and adapt it to suit your needs or personal workflow.
