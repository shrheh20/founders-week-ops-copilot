import pytest
from app.AI_Goveranance import count_authorised_companies, filter_authorized_companies

def test_viewer_access():
    companies = [
        {"id": 101, "name": "Alpha AI", "program_id": "FW2026"},
        {"id": 102, "name": "Beta Robotics", "program_id": "ACC2026"},
        {"id": 103, "name": "Gamma Health", "program_id": "FW2026"}
    ]

    user = {
        "user_id": "user_001",
        "role": "viewer",
        "allowed_programs": ["FW2026"]
    }

    expected = [
        {"id": 101, "name": "Alpha AI", "program_id": "FW2026"},
        {"id": 103, "name": "Gamma Health", "program_id": "FW2026"}
    ]

    actual=filter_authorized_companies(companies,user)
    assert expected==actual

def test_admin_access():
    companies = [
        {"id": 101, "name": "Alpha AI", "program_id": "FW2026"},
        {"id": 102, "name": "Beta Robotics", "program_id": "ACC2026"},
        {"id": 103, "name": "Gamma Health", "program_id": "FW2026"}
    ]

    user = {
        "user_id": "user_001",
        "role": "admin",
        "allowed_programs": ["FW2026"]
    }

    expected = [
        {"id": 101, "name": "Alpha AI", "program_id": "FW2026"},
        {"id": 102, "name": "Beta Robotics", "program_id": "ACC2026"},
        {"id": 103, "name": "Gamma Health", "program_id": "FW2026"}
    ]

    actual=filter_authorized_companies(companies,user)
    assert expected==actual

def test_viewer_no_permissions():
    companies = [
        {"id": 101, "name": "Alpha AI", "program_id": "FW2026"},
        {"id": 102, "name": "Beta Robotics", "program_id": "ACC2026"},
        {"id": 103, "name": "Gamma Health", "program_id": "FW2026"}
    ]

    user = {
        "user_id": "user_001",
        "role": "viewer",
        "allowed_programs": []
    }

    expected = []

    actual=filter_authorized_companies(companies,user)
    assert expected==actual

def test_unauthorized_role():
    companies = [
        {"id": 101, "name": "Alpha AI", "program_id": "FW2026"},
        {"id": 102, "name": "Beta Robotics", "program_id": "ACC2026"},
        {"id": 103, "name": "Gamma Health", "program_id": "FW2026"}
    ]

    user = {
        "user_id": "user_001",
        "role": "database",
        "allowed_programs": []
    }

    with pytest.raises(PermissionError, match="Unauthorized role"):
        filter_authorized_companies(companies,user)

def test_authorized_access():
    companies = [
        {"id": 101, "name": "Alpha AI", "program_id": "FW2026"},
        {"id": 102, "name": "Beta Robotics", "program_id": "ACC2026"},
        {"id": 103, "name": "Gamma Health", "program_id": "FW2026"}
    ]

    user = {
        "user_id": "user_001",
        "role": "viewer",
        "allowed_programs": ["FW2026"]
    }

    expected = 2

    actual=count_authorised_companies(companies,user)
    assert expected==actual