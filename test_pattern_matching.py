

def test_it_stops_after_the_first_match():
    v = 0
    match 10:
        case x if x > 5:
            v = 1
        case x if x > 8:
            v = 2
    assert v == 1
