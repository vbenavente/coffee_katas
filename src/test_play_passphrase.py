from play_passphrase import play_pass


def test_same_phrase_is_not_returned():
    result = play_pass("I love python 8765", 2)
    assert result != "I love python 8765"


def test_alpha_shift_works():
    result = play_pass("i love python 3 4", 3)
    assert result == "l oryh sbwkrq 6 5"
