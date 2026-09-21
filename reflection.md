# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  When the game first ran it was pretty much broken and only allowed for one full play before it froze. It would also give inccorect hints and could not change difficulty
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
    1. Hint was inverted so there was no way of knowing if you were close to winning
    2. The game would never reset after loosing making it impossible to replay
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|----------|---------------------|-----------------|------------------------|
 Guessed 1    Correct or Go Higher   Go Lower          Hint text is inverted

Clicked new   Game Resets           Shows New game      Game  never resets
game after                         started but 
losing                             stuck on old
                                   game

Selected Easy   New secret #       Secret # stays       New game hardcoded at 100
difficulty      should be at       at 100               No difficulty range
after new       1-20
game
 
Choose           display            doesnt display      incorrect UI change
difficulty       new range          correct range
and see 
range change


Selecting new     clears             old text            visual bug
game wont         text               stays
refresh text
box
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used the built in AI with VS code (co-pilot) and Claude for pointers.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  Co-pilot correclty swapped "Too High" --> "Go Lower" and "Too Low" --> "Go Higher" when prompted. I was able to verify it both on a new pytest and actually playing the game.

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
  The text box not clearing when needing to do so. The first approach co-pilot made looked reasonable but did not actually work in the live app due to a streamlit quirk qith widget key reuse. I caught it instantly upon re-testing and asked to fix it with the round counter approach which did work.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I looked over the majority of the code. When going over the logic i could tell something would be off with the actual system itself of the game telling you which direction to go but could not be certain. It was not after testing the game that it comfirmed my guess. Upon playing there were a few bugs aswell but the one seemed the the definitive one as it guided the player towards a loss or win.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code
  One manual test I ran was with the New Game fixes. Rather than relying on pytest I had to manually hardkill the server and re run it verify everything checked out. I had to loose a game and confirm that upon clicking new game that it would refresh instead of being stuck on the old instance.

- Did AI help you design or understand any tests? How?
 Yes, I asked my AI assistant to write the test_hint_direction_for_high_and_low_guesses test rather than writing it myself, giving it a specific instruction (test guess 60 vs secret 50, and guess 40 vs secret 50) so it would actually exercise the bug I'd found rather than something generic.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Every click or input reruns the whole script from top to bottom. Normal variables would reset each time, so anything that needs to persist (score, attempts, secret number) has to live in st.session_state instead.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  I would say that one habit I hope to reuse is that checking out the logic first rather than throwing it into the AI first to verify that everyhting makes sense before making changes
- What is one thing you would do differently next time you work with AI on a coding task?

  Giving it better prompts and learning how to fine tune wording so that it can accuratley pinpoint where issues are at in the code.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  I would say that it is very impressive but some form of human input is required to make sure everything is correct. After it is trained on humand data and humans make mistakes all the time.
