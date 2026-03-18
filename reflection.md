# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
Hint behavior was wrong: when my guess was not the secret, the app gave misleading hint text (Go HIGHER / Go LOWER) that didn’t match the actual comparison result.
New Game button was broken: clicking New Game did not fully reset the game state.
Guess/result consistency bug: on some turns, the game compared different data types for the secret value, which caused unreliable outcomes and made debugging confusing.

--- The first time I ran the game, I opened the Developer Debug Info and saw the secret number was `77`, then I entered `77` and got a win message. I also tested non-winning guesses and noticed the hint text was inconsistent with the actual guess result: when the outcome said `Too High`, the UI still told me to "Go HIGHER," and when it said `Too Low`, it told me to "Go LOWER." The expected behavior is the opposite hint direction (high guess should say lower, low guess should say higher).

I found a second bug with the New Game flow: after clicking `New Game`, the app did not fully reset game state. The expected behavior is that New Game resets all round state cleanly (secret, attempts, status, and history) for a fresh start.

I also noticed the Submit button sometimes felt broken: after a win/loss state, clicking Submit did nothing, and invalid/empty submits still consumed attempts. The expected behavior is that Submit should only count valid guesses and should work normally after a proper New Game reset.


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used ChatGPT as my main AI tool for this project. One correct suggestion was that Hard mode should not have a smaller range than Normal mode, so I changed it to a larger range and verified it by checking the sidebar range values in the app. Another correct suggestion was to reset all game state on New Game (status, score, and history), and I verified this by starting a new round and confirming old state did not carry over.

One misleading suggestion was to convert values to strings to avoid a type error during guess comparison. I tested that idea and saw it gave inconsistent higher/lower results because string comparison is not numeric comparison, so I removed that approach and kept guess/secret as integers.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---I treated a bug as fixed only after I tested the exact same steps that showed the bug before. I checked both the visible game behavior and the Developer Debug Info values (secret, attempts, score, and history). If expected behavior and actual behavior matched repeatedly, I marked it as fixed.

I ran pytest on tests/test_game_logic.py and got 8 passed. These tests confirmed that check_guess returns the correct outcome, parse_guess rejects decimal input, difficulty ranges are correct, and score updates work correctly. I also manually tested New Game reset behavior and confirmed old state no longer carried over.

Yes. AI helped me identify what to test, especially edge cases like decimal input, hint direction correctness, and reset behavior. It also helped me align test assertions with the actual return type from check_guess (tuple format). I still verified each suggestion by running tests and checking app behavior myself.


## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

--- Streamlit reruns mean the whole script runs again every time you click a button, change input, or interact with the app. If you use normal variables, they reset on every rerun. st.session_state is like memory for the app, so values like score, attempts, and history stay saved between reruns.



## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse is testing after every small fix instead of changing many things at once. I will keep using short test cycles with manual checks and pytest so I can quickly see what worked and what still needs fixing.

Next time, I would ask AI for smaller, step-by-step fixes and verify each step before moving on. I would also ask AI to explain why each change is needed, so I can catch misleading suggestions earlier and avoid adding new bugs.

This project taught me that AI code can look correct but still have hidden logic and state bugs. I now treat AI as a helper, not a final authority, and I always verify behavior with tests and manual checks.
