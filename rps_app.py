import streamlit as st
from game_logic import choices, move_display, get_ollama_move, get_winner

# ⚙️ Page config
st.set_page_config(page_title="RPS with AI", page_icon="🤖")

# 🧠 Title and description
st.markdown("""
<h1 style='text-align: center; color: #00BFFF;'>🎮 Rock-Paper-Scissors with LLaMA 3 AI</h1>
<p style='text-align: center;'>Play against a local LLaMA 3 model (via Ollama) that learns your play patterns!</p>
<hr style="margin-top:10px;margin-bottom:20px">
""", unsafe_allow_html=True)

# ℹ️ Ollama must be running in background:
# Run in terminal: ollama run llama3

# 🧠 Session state setup
if "player_score" not in st.session_state:
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.tie_score = 0
    st.session_state.player_history = {"rock": 0, "paper": 0, "scissors": 0}

# 🎮 Move selection
player = st.radio("Choose your move:", choices, format_func=lambda x: move_display[x], horizontal=True)

if st.button("Play"):
    st.session_state.player_history[player] += 1
    computer = get_ollama_move(st.session_state.player_history)

    st.markdown(f"<h4 style='text-align: center;'>🧍 You chose: <code>{move_display[player]}</code></h4>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align: center;'>💻 LLaMA 3 chose: <code>{move_display[computer]}</code></h4>", unsafe_allow_html=True)

    winner = get_winner(player, computer)
    if winner == "tie":
        st.info("🤝 It's a tie!")
        st.session_state.tie_score += 1
    elif winner == "player":
        st.success("✅ You win!")
        st.session_state.player_score += 1
    else:
        st.error("💻 LLaMA 3 wins!")
        st.session_state.computer_score += 1

# 📊 Scoreboard
col1, col2, col3 = st.columns(3)
col1.metric("🧍 You", st.session_state.player_score)
col2.metric("💻 AI", st.session_state.computer_score)
col3.metric("🔁 Ties", st.session_state.tie_score)

# 🔄 Reset game button
if st.button("Reset Game"):
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.tie_score = 0
    st.session_state.player_history = {"rock": 0, "paper": 0, "scissors": 0}
    st.success("Game reset!")
