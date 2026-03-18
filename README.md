# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
This game is a number guessing game made with Streamlit. The player picks a difficulty, enters guesses, and gets hints until they win or run out of attempts. It also tracks score, attempts, and guess history. The goal is to practice debugging AI code, state handling, and testing skills carefully.

- [ ] Detail which bugs you found.
I found several bugs in the starter code. Hint directions were reversed, so feedback was wrong. Hard mode used a smaller range than Normal mode. New Game did not fully reset state. Attempts were off by one. Secret type changed to string sometimes. Tests also expected the wrong return format.

- [ ] Explain what fixes you applied.
I moved core logic into logic_utils.py and fixed each bug. I corrected hint messages, set Hard range to 1-200, and rejected decimal guesses. I reset full session state on New Game and difficulty change. I counted attempts only for valid guesses and updated tests. Finally, all tests passed successfully now.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
