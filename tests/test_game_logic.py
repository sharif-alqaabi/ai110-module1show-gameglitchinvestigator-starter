from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"


def test_check_guess_messages():
    assert check_guess(75, 50)[1] == "📉 Way too high — go way lower."
    assert check_guess(55, 50)[1] == "📉 A bit high — go a bit lower."
    assert check_guess(25, 50)[1] == "📈 Way too low — go way higher."
    assert check_guess(45, 50)[1] == "📈 A bit low — go a bit higher."


def test_check_guess_message_boundary_at_10():
    assert check_guess(60, 50)[1] == "📉 A bit high — go a bit lower."
    assert check_guess(40, 50)[1] == "📈 A bit low — go a bit higher."


def test_parse_guess_valid_integer():
    ok, guess, err = parse_guess("42")
    assert ok is True
    assert guess == 42
    assert err is None


def test_parse_guess_rejects_decimal():
    ok, guess, err = parse_guess("10.5")
    assert ok is False
    assert guess is None
    assert err == "That is not a whole number."


def test_get_range_for_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 200)


def test_update_score_win_and_miss():
    assert update_score(0, "Too Low", 1) == -5
    assert update_score(10, "Too High", 2) == 5
    assert update_score(0, "Win", 1) == 100
