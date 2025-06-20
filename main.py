from game_logic import choices, get_ollama_move, get_winner

player_score = 0
computer_score = 0
tie_score = 0
player_history = {"rock": 0, "paper": 0, "scissors": 0}

print("🎮 Rock-Paper-Scissors with LLaMA 3 AI")
print("Type 'rock', 'paper', or 'scissors'. Type 'quit' to exit.\n")

while True:
    player = input("Your move: ").lower()

    if player == "quit":
        print("\nThanks for playing!")
        break

    if player not in choices:
        print("❌ Invalid choice! Try again.\n")
        continue

    player_history[player] += 1
    computer = get_ollama_move(player_history)
    print(f"💻 AI chose: {computer}")

    winner = get_winner(player, computer)

    if winner == "tie":
        print("🤝 It's a tie!")
        tie_score += 1
    elif winner == "player":
        print("✅ You win!")
        player_score += 1
    else:
        print("💻 AI wins!")
        computer_score += 1

    print(f"📊 Score => You: {player_score}, AI: {computer_score}, Ties: {tie_score}")
    print("-" * 40)
