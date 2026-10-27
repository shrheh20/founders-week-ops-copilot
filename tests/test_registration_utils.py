from app.registration_utils import get_pending_companies


def test_pending_companies():
    registrations = [
        {"company": "Alpha AI", "status": "confirmed"},
        {"company": "Beta Labs", "status": "pending"},
        {"company": "Gamma Tech", "status": "pending"}
    ]

    expected = ["Beta Labs", "Gamma Tech"]

    actual = get_pending_companies(registrations)

    assert actual == expected

def test_no_pending_companies():
    registrations = [
        {"company": "Alpha AI", "status": "confirmed"},
        {"company": "Beta Labs", "status": "cancelled"},
    ]

    expected = []

    actual = get_pending_companies(registrations)

    assert actual == expected

def test_empty_registrations():
    registrations = []

    expected = []

    actual = get_pending_companies(registrations)

    assert actual == expected   