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
      The purpose of the game is for the user to input an number and the system would give feed backl depending on how close they are while also decreasing the number of attempts they have. The range of the number changesd based on the actual difficultly that the user selects.
- [ ] Detail which bugs you found.
      The five main bugs that i found where was the hin system not working right. It would say go lower even when entering 1 as a guess. Next was the selecting a difficulty would not change the range of the numbers it would stay at 1-100 all the time. The third bug was that the game would not reset after clicking new game. The game would enter a frozen state in which no input would be recorded. The fourth bug was that new game would ignore diffculty and would always be stuck on normal. Finally there was a bug in which resetting the game would not clear the text box as it should.
- [ ] Explain what fixes you applied.
      1. Swapped the paired messages in check_guess so "Too High" returns "Go LOWER!" and "Too Low" returns "Go HIGHER!" I moved this function into logic_utils.py in the process and added a new pytest test (test_hint_direction_for_high_and_low_guesses) that checks the message text specifically, not just the outcome label.
      
      2. Added st.session_state.status = "playing" inside the New Game button's logic.

      3. Changed the secret reset to random.randint(low, high), reusing the same low/high variables the game already computes from get_range_for_difficulty(difficulty).

      4. Updated the info box to use an f-string with {low} and {high} instead of hardcoded numbers

      5. Added a round counter (st.session_state.round) that increments on every New Game click, and included it in the text input's key so Streamlit treats it as a genuinely new widget each round, forcing the box to clear.
## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects "Easy" difficulty (range 1-20)
2. User enters a guess of 5
3. Game returns "Too Low" with the message "Go HIGHER!"
4. User enters a guess of 18
5.  Game returns "Too High" with the message "Go LOWER!"
6. Score updates correctly after each guess
7. User enters a guess of 12 (the correct secret), game displays "Correct!" and the win message
8. User clicks "New Game", game resets with a fresh secret in the 1-20 range, status returns to "playing", and the guess input box is empty

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
