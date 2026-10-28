from app.registration_utils import count_companies_by_status, find_stale_registrations, get_pending_companies, reconcile_companies
from app.registration_utils import validate_required_fields
from app.registration_utils import find_duplicate_companies
from app.registration_utils import count_companies_by_status

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

def test_count_company_status():
    companies = [
        {"company_id": 101, "name": "Acme AI", "status": "pending"},
        {"company_id": 102, "name": "Beta Labs", "status": "approved"},
        {"company_id": 103, "name": "Gamma Tech", "status": "pending"},
        {"company_id": 104, "name": "Delta AI", "status": "rejected"},
        {"company_id": 105, "name": "Echo Systems", "status": "approved"},
        {"company_id": 106, "name": "Nova Robotics", "status": "pending"}
    ]

    expected={"pending":3,"approved":2,"rejected":1}
    actual=count_companies_by_status(companies)
    assert actual==expected

def test_last_update():
    registrations = [
        {"company_id": 101, "status": "pending",
        "last_updated": "2026-10-15"},

        {"company_id": 102, "status": "approved",
        "last_updated": "2026-10-10"},

        {"company_id": 103, "status": "pending",
        "last_updated": "2026-10-23"},

        {"company_id": 104, "status": "pending",
        "last_updated": "2026-10-18"}
    ]

    expected=[101,104]
    actual=find_stale_registrations(registrations)

    assert actual==expected

def test_reconcile_data():
    crm_companies = [
        {"company_id": 101, "name": "Acme AI"},
        {"company_id": 102, "name": "Beta Labs"},
        {"company_id": 103, "name": "Gamma Tech"}
    ]

    event_companies = [
        {"company_id": 101, "name": "Acme AI"},
        {"company_id": 103, "name": "Gamma Tech"},
        {"company_id": 104, "name": "Delta AI"}
    ]

    expected={
        "only_in_crm": [102],
        "only_in_events": [104],
        "in_both": [101, 103]
    }

    actual=reconcile_companies(crm_companies,event_companies)
    assert actual==expected

def test_reconcile_data_edge():
    crm_companies = [
    ]

    event_companies = [
       
    ]

    expected={
        "only_in_crm": [],
        "only_in_events": [],
        "in_both": []
    }
    actual=reconcile_companies(crm_companies,event_companies)
    assert actual==expected