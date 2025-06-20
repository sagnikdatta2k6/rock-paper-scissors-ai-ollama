# 🎮 Rock-Paper-Scissors AI (with LLaMA 3 + Ollama)

Play Rock-Paper-Scissors against a smart AI that learns your patterns!  
This project uses **Meta's LLaMA 3 model** served locally through [Ollama](https://ollama.com), wrapped in a clean and interactive **Streamlit web app**.

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-red?style=flat-square&logo=streamlit" />
  <img src="https://img.shields.io/badge/Model-LLaMA%203-blueviolet?style=flat-square" />
</p>

---

## 🧠 How It Works

- Tracks your move history (rock/paper/scissors count).
- Sends a prompt to **LLaMA 3 via Ollama** to predict the best AI move.
- Decides a winner and updates the score dynamically.
- Runs entirely **locally** — no cloud or API keys needed.

---

## 🛠️ Technologies Used

| Tech        | Description                                 |
|-------------|---------------------------------------------|
| 🐍 Python   | Core game logic and integration             |
| 🦙 Ollama   | Local LLaMA 3 model server                  |
| 🧠 LLaMA 3  | Meta’s advanced language model              |
| 🌐 Streamlit | Web interface for easy interaction         |

---

## 🚀 Getting Started

### 1. Clone the Repo

git clone https://github.com/your-username/rock-paper-scissors-ai-ollama.git
cd rock-paper-scissors-ai-ollama

### 2. Set Up Environment

Install dependencies:

pip install -r requirements.txt

### 3. Set Up Ollama

Install and run the model locally:

---

# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

---

# Pull and run the LLaMA 3 model
ollama pull llama3
ollama run llama3

Keep this terminal running while playing.

---

### 4. Run the App

streamlit run rps_app.py

---

## 🗃️ Project Structure

├── main.py           # CLI version of the game

├── rps_app.py        # Streamlit web app

├── game_logic.py     # AI integration & logic

├── requirements.txt  # Dependencies

├── .gitignore        # Ignored files

├── LICENSE           # MIT license

└── README.md         # This file

---

## 📈 Features

* ✅ Fun and intelligent gameplay
* 🧠 Learns from your move history
* ⚡ Fast and runs offline
* 🛠️ Easy to customize and extend
* 🌍 No API keys, no external dependencies

---

## 🧪 Sample AI Prompt

> “You are playing rock-paper-scissors.
> The player has played 'rock' 3 times, 'paper' 1 time, and 'scissors' 6 times.
> Based on this, what move would you choose next to win?”

---

## 📄 License

This project is licensed under the **MIT License**.
LLaMA 3 is provided and governed by [Meta's licensing terms](https://ai.meta.com/llama/license/).
Ollama usage is governed by [Ollama's terms](https://ollama.com).

---

## 🙌 Acknowledgements

* [Meta AI](https://ai.meta.com/llama) — for LLaMA 3
* [Ollama](https://ollama.com) — for local model serving
* [Streamlit](https://streamlit.io) — for the frontend

---

## ✨ Author

**Sagnik Datta**
Built with ❤️ using AI tools.
🔗 [GitHub](https://github.com/sagnikdatta2k6)
