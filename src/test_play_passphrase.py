from play_passphrase import play_pass


def test_same_phrase_is_not_returned():
    """Test phrase is changed."""
    result = play_pass("I love python 8765", 2)
    assert result != "I love python 8765"


def test_alpha_shift_works():
    """Test alpha shift is working."""
    result = play_pass("i love python 3 4", 3)
    assert result == "l oryh sbwkrq 6 5"


def test_non_alpha_digit_char_kept():
    """Test non alpha or digit characters are kept."""
    result = play_pass("a!! b@@ c##", 1)
    assert result == "b!! c@@ d##"
