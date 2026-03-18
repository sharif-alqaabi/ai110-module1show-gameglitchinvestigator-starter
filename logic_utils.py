def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # Problem: Hard range was wrong and made difficulty confusing.
    # Fixed: set clear ranges (Easy 1-20, Normal 1-100, Hard 1-200).
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    cleaned = raw.strip()
    if cleaned == "":
        return False, None, "Enter a guess."

    # Problem: decimal/non-integer input was being changed silently.
    # Fixed: only accept whole numbers and show a clear error otherwise.
    try:
        guess_int = int(cleaned)
    except ValueError:
        return False, None, "That is not a whole number."

    return True, guess_int, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    difference = abs(guess - secret)

    if guess > secret:
        if difference > 10:
            return "Too High", "📉 Way too high — go way lower."
        return "Too High", "📉 A bit high — go a bit lower."

    if difference > 10:
        return "Too Low", "📈 Way too low — go way higher."
    return "Too Low", "📈 A bit low — go a bit higher."


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = max(10, 110 - (attempt_number * 10))
        return current_score + points
    if outcome in ("Too High", "Too Low"):
        return current_score - 5
    return current_score
