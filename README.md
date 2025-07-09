# 🧠 SecondBrain

SecondBrain is an AI-powered productivity assistant designed to capture, organize, and retrieve your thoughts, tasks, and knowledge effortlessly. Inspired by the concept of a second brain, this tool helps you stay organized, make decisions faster, and never lose a valuable idea again.

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
npm install
```

Start the application:

```bash
npm run dev
```

---

## 📁 Project Structure

```
.
├── components/          # Reusable UI components
├── pages/               # Application routes and logic
├── lib/                 # Utilities and helper functions
├── public/              # Static assets
├── styles/              # Global styles and theming
├── README.md            # You're here!
```

---

## 📚 Technologies Used

- 🧠 GPT-4 / LLMs
- ⚛️ React / Next.js
- 🧪 TypeScript
- 🗃️ SQLite / Local Storage
- 🎨 Tailwind CSS

---

## 💡 Usage Ideas

- Track your ideas, notes, and research across projects
- Maintain a knowledge base of your work and learnings
- Use as a daily journal with auto-tagging and reflection
- Plan your day with actionable task suggestions from your notes

---

## 🛠️ Contribution

Pull requests are welcome! If you’d like to contribute, fork the repo and open a PR with your changes.

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for details.
