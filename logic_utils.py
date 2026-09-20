class GuessResult(tuple):
    """Tuple-like result that also compares sensibly to a single outcome string."""

    def __new__(cls, outcome, message):
        return super().__new__(cls, (outcome, message))

    def __eq__(self, other):
        if isinstance(other, str):
            return self[0] == other
        return super().__eq__(other)


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret): #FIX: Swapped too high/Too low messages using co pilot. moved app.py
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return GuessResult("Win", "🎉 Correct!")

    try:
        if guess > secret:
            return GuessResult("Too High", "📉 Go LOWER!")
        return GuessResult("Too Low", "📈 Go HIGHER!")
    except TypeError:
        g = str(guess)
        if g == secret:
            return GuessResult("Win", "🎉 Correct!")
        if g > secret:
            return GuessResult("Too High", "📉 Go LOWER!")
        return GuessResult("Too Low", "📈 Go HIGHER!")


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
