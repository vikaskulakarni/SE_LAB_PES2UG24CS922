

## Project: Number Guessing Repair Lab

### Developer
Vikas Kulakarni



---

# LLM Prompts Used During Development

## 1. Project Understanding and Requirement Analysis

I am working on a Python/Pygame Number Guessing Game for my Software
Engineering lab. I want to use an LLM as a debugging and pair-programming
assistant.

First, help me understand the existing project and its requirements. Analyze
the README and source code, identify the current functionality and missing
features, and map each requirement to the file or section where it should be
implemented.

Please do not modify the code yet. I want to first understand the project
structure, existing problems, required changes, and a clear implementation plan.

---

## 2. Investigating the Existing Crash

I found that the game crashes when I submit an empty input field.

Please inspect the guess submission logic and explain why this happens. Identify
the exact statement causing the problem and explain how the input should be
validated before converting it to an integer.

I want a minimal fix that does not affect the existing valid-guess behavior.

---

## 3. Implementing the Empty Input Fix

Let's implement the first requirement.

When the player submits an empty input:

- The game must not crash.
- `int()` should not be called on an empty string.
- The attempt count should not increase.
- The player should receive a clear validation message.
- Valid numerical guesses should continue working normally.

Please provide the required code changes and explain what was changed.

---

## 4. Reviewing the Empty Input Fix

Please review the implemented empty-input fix as a code reviewer.

Check that:
- Empty input does not crash the game.
- Attempts are not consumed.
- A useful message is displayed.
- Valid guesses still work.
- No unrelated game functionality was changed.

Tell me if anything needs to be corrected before moving to the next requirement.

---

## 5. Adding Dynamic Range Hints

Now I want to implement the second requirement.

The game should maintain a possible range for the secret number.

Start with:

`low_bound = 1`

`high_bound = 100`

If the player's valid guess is too low, update the lower bound to
`guess + 1`.

If the player's valid guess is too high, update the upper bound to
`guess - 1`.

Display the current possible range clearly on the screen.

The range should also reset when a new game starts.

Please implement this while preserving the existing functionality.

---

## 6. Reviewing Dynamic Range Logic

Please review the dynamic range implementation.

Check that:

- The initial range is 1 to 100.
- A low guess correctly increases the lower bound.
- A high guess correctly decreases the upper bound.
- The range never expands incorrectly.
- The range resets after pressing R.
- A correct guess still ends the game normally.

Please identify any issues before we continue.

---

## 7. Adding Guess History

I now want to implement the third requirement.

Add a visual guess-history section to the game.

The requirements are:

- Store valid guesses.
- Display the player's last five guesses.
- Indicate whether each guess was too high, too low, or correct.
- Use simple visual indicators such as arrows or labels.
- Do not record invalid empty submissions.
- Clear the history when the game is restarted.

Please integrate this with the existing game without breaking the previous features.

---

## 8. Reviewing Guess History

Please review the guess-history implementation.

Verify that:

1. Valid guesses are recorded.
2. Empty submissions are not recorded.
3. The correct result is associated with each guess.
4. Only the latest five guesses are displayed.
5. The history is cleared when a new game starts.
6. The display remains readable within the existing Pygame window.

---

## 9. Adding Maximum Attempts and GAME_OVER

Now I want to implement the fourth requirement.

The player should have a maximum of seven valid attempts.

After seven unsuccessful guesses:

- The game should enter a GAME_OVER state.
- The secret number should be revealed.
- Additional guesses should not be accepted.
- The player should be able to press R to start a new game.

Restarting should reset:

- Secret number
- Attempt counter
- Dynamic range
- Guess history
- Feedback
- Game state

The existing winning behavior should continue to work.

Please implement this without unnecessarily changing unrelated code.

---

## 10. Reviewing GAME_OVER and Restart

Please review the maximum-attempt and restart implementation.

Verify that:

- Only valid guesses count as attempts.
- The maximum is seven attempts.
- A correct guess can still produce a WIN state.
- Seven unsuccessful guesses produce GAME_OVER.
- The secret number is revealed after GAME_OVER.
- Additional guesses are blocked.
- Pressing R starts a fresh game.
- All relevant game state is reset.

---

## 11. Full Integration Testing

All four requirements have now been implemented.

Please perform a complete integration review of the game.

Check these scenarios:

1. Empty submission.
2. Valid low guess.
3. Valid high guess.
4. Multiple guesses.
5. Guess-history updates.
6. Dynamic range updates.
7. Seven unsuccessful attempts.
8. GAME_OVER state.
9. Correct guess / WIN state.
10. Restart using R.
11. New game after restart.

Identify any conflicts or regressions between the four features.

---

## 12. Final Code Review

The implementation is working now.

Please perform a final code review as a senior Python/Pygame developer.

Check:

- Code correctness
- Readability
- Variable naming
- Game-state management
- Input validation
- UI behavior
- Potential runtime errors
- Unnecessary changes
- Maintainability

Please focus only on issues that could affect the functionality or submission.

---

## 13. Final Requirements Verification

Please compare the completed implementation against the original lab
requirements.

Create a simple requirement-to-implementation checklist showing:

- Requirement
- How it was implemented
- Expected behavior
- Verification status

Make sure all four required tasks are covered and nothing important is missing.

---

## 14. Final Submission Check

I am preparing the final submission for my Software Engineering lab.

Please perform a final pre-submission check.

Verify that:

- All four required tasks are implemented.
- The original empty-input crash is fixed.
- The game runs correctly.
- The new features work together.
- The source files are organized correctly.
- The before-change video has been recorded.
- The after-change video has been recorded.
- The LLM conversation can be provided as evidence.
- The GitHub repository is ready for submission.

Provide a final checklist of anything that still needs to be done.

---

# Tools Used

The following tools were used during the development and verification of
the project:

### 1. ChatGPT
Used as an AI debugging and pair-programming assistant for:

- Understanding the existing code
- Identifying the empty-input bug
- Planning the implementation
- Implementing the required features
- Reviewing the code
- Checking integration between features
- Performing the final requirements review

### 2. GitHub
Used for:

- Accessing the project repository
- Reviewing the project README
- Managing the project source code
- Preparing the final project for submission

### 3. Python
Used as the programming language for the game implementation and testing.

### 4. Pygame
Used as the game-development framework for:

- Game window
- User input
- Buttons
- Text rendering
- Game states
- Visual feedback

### 5. Visual Studio Code / Code Editor
Used to create and modify the Python source files.

### 6. PowerShell / Terminal
Used to:

- Navigate the project directory
- Run the Python application
- Test the game
- Manage the Git repository
- Commit and push changes to GitHub

### 7. Screen Recording Tool
Used to record:

- The original game behavior before the fixes
- The final game after implementing the required features

---

# Development Outcome

The final game successfully addresses all four required repair and enhancement
tasks:

- Empty input no longer crashes the application.
- The possible number range updates dynamically.
- The last five guesses are displayed with result indicators.
- The game supports seven attempts, GAME_OVER, secret-number reveal, and
  restart functionality.

The project was tested after implementation and prepared for GitHub submission.
