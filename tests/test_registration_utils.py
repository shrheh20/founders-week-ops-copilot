from app.registration_utils import get_pending_companies
from app.registration_utils import validate_required_fields
from app.registration_utils import find_duplicate_companies

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

def test_validate_required_fields():
    company = {
        "company_id": 111,
        "name": "Aurits",
        "status": "unknown"
    }
    expected = False

    actual = validate_required_fields(company)
    assert actual == expected

def test_find_duplicate_companies():
    companies = [
        {"company_id": 101, "name": "Acme AI"},
        {"company_id": 101, "name": "Beta Robotics"},
        {"company_id": 101, "name": "Gamma Labs"},
        {"company_id": 102, "name": "Acme AI"},
        {"company_id": 102, "name": "Delta Tech"},
        {"company_id": 102, "name": "Beta Robotics"}
    ]
    expected = [101,102]
    actual = find_duplicate_companies(companies)
    assert actual == expected

def test_invalid_company_status():
    company = {
        "company_id": 105,
        "name": "Gamma Labs",
        "status": "in_progress"
    }

    expected=False
    actual=validate_required_fields(company)
    assert actual==expected