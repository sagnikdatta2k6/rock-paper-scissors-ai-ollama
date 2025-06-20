import requests
import random

# Valid game choices
choices = ["rock", "paper", "scissors"]

# Emoji display for each choice
move_display = {
    "rock": "🪨 Rock",
    "paper": "📄 Paper",
    "scissors": "✂️ Scissors"
}

# 🧠 Get move from LLaMA 3 via Ollama
# This function uses Ollama's local HTTP API to query the llama3 model
def get_ollama_move(player_history):
    prompt = (
        f"You are playing rock-paper-scissors. "
        f"The player has played 'rock' {player_history['rock']} times, "
        f"'paper' {player_history['paper']} times, and "
        f"'scissors' {player_history['scissors']} times. "
        f"Based on this, what move would you choose next to win? "
        f"Just reply with one word: rock, paper, or scissors."
    )

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": False}
        )
        move = response.json()['response'].strip().lower()
        if move in choices:
            return move
        else:
            print("⚠️ Unexpected AI response. Falling back to random choice.")
    except Exception as e:
        print("❌ Ollama error:", e)

    print("🔁 Falling back to random choice.")
    return random.choice(choices)

# 🔍 Determine winner based on RPS rules
def get_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

# 🧪 Optional test cases
if __name__ == "__main__":
    print("Testing get_winner()...")
    print("rock vs scissors →", get_winner("rock", "scissors"))  # player
    print("scissors vs paper →", get_winner("scissors", "paper"))  # player
    print("rock vs rock →", get_winner("rock", "rock"))  # tie
