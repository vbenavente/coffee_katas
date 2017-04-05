from play_passphrase import play_pass


def test_same_phrase_is_not_returned():
    """Test phrase is changed."""
    result = play_pass("I love python 8765", 2)
    assert result != "I love python 8765"


def test_alpha_shift_works():
    """Test alpha shift is working."""
    result = play_pass("i love python 3 4", 3)
    assert result == "5 6 QrKwBs hYrO L"


def test_non_alpha_digit_char_kept():
    """Test non alpha or digit characters are kept."""
    result = play_pass("a!! b@@ c##", 1)
    assert result == "##D @@C !!B"


def test_upcase_even_downcase_odd():
    """Test letter in odd position downcase, even upcase."""
    result = play_pass("even odd", 0)
    assert result == "dDo nEvE"
