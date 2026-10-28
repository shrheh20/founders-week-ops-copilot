from app.registration_utils import combine_paginated_companies, count_companies_by_status, find_missing_pages, get_pending_companies, process_crm_response, reconcile_companies
from app.registration_utils import validate_required_fields
from app.registration_utils import find_duplicate_companies
from app.registration_utils import count_companies_by_status
from app.registration_utils import extract_pending_companies
from app.registration_utils import combine_paginated_companies

import pytest

# def test_pending_companies():
#     registrations = [
#         {"company": "Alpha AI", "status": "confirmed"},
#         {"company": "Beta Labs", "status": "pending"},
#         {"company": "Gamma Tech", "status": "pending"}
#     ]

#     expected = ["Beta Labs", "Gamma Tech"]

#     actual = get_pending_companies(registrations)

#     assert actual == expected

# def test_no_pending_companies():
#     registrations = [
#         {"company": "Alpha AI", "status": "confirmed"},
#         {"company": "Beta Labs", "status": "cancelled"},
#     ]

#     expected = []

#     actual = get_pending_companies(registrations)

#     assert actual == expected

# def test_empty_registrations():
#     registrations = []

#     expected = []

#     actual = get_pending_companies(registrations)

#     assert actual == expected

# def test_validate_required_fields():
#     company = {
#         "company_id": 111,
#         "name": "Aurits",
#         "status": "unknown"
#     }
#     expected = False

#     actual = validate_required_fields(company)
#     assert actual == expected

# def test_find_duplicate_companies():
#     companies = [
#         {"company_id": 101, "name": "Acme AI"},
#         {"company_id": 101, "name": "Beta Robotics"},
#         {"company_id": 101, "name": "Gamma Labs"},
#         {"company_id": 102, "name": "Acme AI"},
#         {"company_id": 102, "name": "Delta Tech"},
#         {"company_id": 102, "name": "Beta Robotics"}
#     ]
#     expected = [101,102]
#     actual = find_duplicate_companies(companies)
#     assert actual == expected

# def test_invalid_company_status():
#     company = {
#         "company_id": 105,
#         "name": "Gamma Labs",
#         "status": "in_progress"
#     }

#     expected=False
#     actual=validate_required_fields(company)
#     assert actual==expected

# def test_count_company_status():
#     companies = [
#         {"company_id": 101, "name": "Acme AI", "status": "pending"},
#         {"company_id": 102, "name": "Beta Labs", "status": "approved"},
#         {"company_id": 103, "name": "Gamma Tech", "status": "pending"},
#         {"company_id": 104, "name": "Delta AI", "status": "rejected"},
#         {"company_id": 105, "name": "Echo Systems", "status": "approved"},
#         {"company_id": 106, "name": "Nova Robotics", "status": "pending"}
#     ]

#     expected={"pending":3,"approved":2,"rejected":1}
#     actual=count_companies_by_status(companies)
#     assert actual==expected

# def test_last_update():
#     registrations = [
#         {"company_id": 101, "status": "pending",
#         "last_updated": "2026-10-15"},

#         {"company_id": 102, "status": "approved",
#         "last_updated": "2026-10-10"},

#         {"company_id": 103, "status": "pending",
#         "last_updated": "2026-10-23"},

#         {"company_id": 104, "status": "pending",
#         "last_updated": "2026-10-18"}
#     ]

#     expected=[101,104]
#     actual=find_stale_registrations(registrations)

#     assert actual==expected

# def test_reconcile_data():
#     crm_companies = [
#         {"company_id": 101, "name": "Acme AI"},
#         {"company_id": 102, "name": "Beta Labs"},
#         {"company_id": 103, "name": "Gamma Tech"}
#     ]

#     event_companies = [
#         {"company_id": 101, "name": "Acme AI"},
#         {"company_id": 103, "name": "Gamma Tech"},
#         {"company_id": 104, "name": "Delta AI"}
#     ]

#     expected={
#         "only_in_crm": [102],
#         "only_in_events": [104],
#         "in_both": [101, 103]
#     }

#     actual=reconcile_companies(crm_companies,event_companies)
#     assert actual==expected

# def test_reconcile_data_edge():
#     crm_companies = [
#     ]

#     event_companies = [
       
#     ]

#     expected={
#         "only_in_crm": [],
#         "only_in_events": [],
#         "in_both": []
#     }
#     actual=reconcile_companies(crm_companies,event_companies)
#     assert actual==expected 

def test_extract_pending_companies():
    api_response = {
        "status": "success",
        "data": {
            "companies": [
                {
                    "id": 101,
                    "name": "Alpha AI",
                    "registration": {
                        "status": "pending",
                        "registered_at": "2026-10-20"
                    },
                    "contact": {
                        "name": "Alice",
                        "email": "alice@alpha.com"
                    }
                },
                {
                    "id": 102,
                    "name": "Beta Robotics",
                    "registration": {
                        "status": "approved",
                        "registered_at": "2026-10-18"
                    },
                    "contact": {
                        "name": "Bob",
                        "email": "bob@beta.com"
                    }
                },
                {
                    "id": 103,
                    "name": "Gamma Health",
                    "registration": {
                        "status": "pending",
                        "registered_at": "2026-10-22"
                    },
                    "contact": {
                        "name": "Charlie",
                        "email": "charlie@gamma.com"
                    }
                },
                {    
                    "id": 104,
                    "name": "Delta Tech",
                    "registration": {
                        "status": "pending"
                    }
                }
            ]
        }
    }

    expected=[
        {
            "company_id": 101,
            "company_name": "Alpha AI",
            "status": "pending",
            "email": "alice@alpha.com"
        },
        {
            "company_id": 103,
            "company_name": "Gamma Health",
            "status": "pending",
            "email": "charlie@gamma.com"
        },
        {
            "company_id": 104,
            "company_name": "Delta Tech",
            "status": "pending",
            "email": None
        }
    ]

    actual=extract_pending_companies(api_response)
    assert expected==actual

def test_empty_companies():
    api_response = {
        "status": "success",
        "data": {
            "companies": []
        }
    }
    expected=[]
    actual=extract_pending_companies(api_response)
    assert expected==actual

def test_no_pending_companies():
    api_response = {
        "status": "success",
        "data": {
            "companies": [
                {
                    "id": 105,
                    "name": "Omega Labs",
                    "registration": {
                        "status": "approved"
                    },
                    "contact": {
                        "email": "hello@omega.com"
                    }
                }
            ]
        }
    }

    expected=[]
    actual=extract_pending_companies(api_response)
    assert actual==expected

def test_crm_success():
    response_body = {
        "status": "success",
        "data": {
            "companies": [
                {
                    "id": 101,
                    "name": "Alpha AI",
                    "registration": {
                        "status": "pending"
                    },
                    "contact": {
                        "email": "alice@alpha.com"
                    }
                }
            ]
        }
    }

    expected = [
        {
            "company_id": 101,
            "company_name": "Alpha AI",
            "status": "pending",
            "email": "alice@alpha.com"
        }
    ]

    actual=process_crm_response(200,response_body)
    assert expected==actual

def test_crm_unauthorized():
    with pytest.raises(PermissionError, match="CRM authentication failed"):
        process_crm_response(401,response_body={})

def test_crm_server_error():
    with pytest.raises(RuntimeError, match="CRM server error"):
        process_crm_response(500,response_body={})


def test_crm_unexpected_status():
    with pytest.raises(ValueError, match="Unexpected HTTP status: 404"):
        process_crm_response(404,response_body={})

def test_combine_multiple_pages():
    pages = [
        {
            "data": {
                "companies": [
                    {"id": 101, "name": "Alpha AI"},
                    {"id": 102, "name": "Beta Robotics"}
                ]
            },
            "pagination": {"page": 1, "total_pages": 3}
        },
        {
            "data": {
                "companies": [
                    {"id": 103, "name": "Gamma Health"}
                ]
            },
            "pagination": {"page": 2, "total_pages": 3}
        },
        {
            "data": {
                "companies": [
                    {"id": 104, "name": "Delta Tech"}
                ]
            },
            "pagination": {"page": 3, "total_pages": 3}
        }
    ]

    expected = [
        {"id": 101, "name": "Alpha AI"},
        {"id": 102, "name": "Beta Robotics"},
        {"id": 103, "name": "Gamma Health"},
        {"id": 104, "name": "Delta Tech"}
    ]

    actual=combine_paginated_companies(pages)
    assert expected==actual

def test_empty_pages():
    pages=[]
    expected=[]
    actual=combine_paginated_companies(pages)
    assert expected==actual

def test_combine_page_with_no_companies():
    pages=[
        {
            "data": {
                "companies": []
            },
            "pagination": {"page": 1, "total_pages": 1}
        }
    ]

    expected=[]
    actual=combine_paginated_companies(pages)
    assert expected==actual

def test_find_missing_pages():
    pages = [
        {
            "pagination": {
                "page": 1,
                "total_pages": 3
            }
        },
        {
            "pagination": {
                "page": 3,
                "total_pages": 3
            }
        }
    ]

    expected=[2]

    actual=find_missing_pages(pages)
    assert expected==actual

def test_find_all_pages():
    pages = [
        {
            "pagination": {
                "page": 1,
                "total_pages": 2
            }
        },
        {
            "pagination": {
                "page": 2,
                "total_pages": 2
            }
        }
    ]

    expected=[]

    actual=find_missing_pages(pages)

    assert expected==actual