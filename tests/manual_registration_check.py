from app.registration_utils import get_pending_companies
registrations = [
    {"company": "Alpha AI", "status": "confirmed"},
    {"company": "Beta Labs", "status": "confirmed"},
    {"company": "Gamma Tech", "status": "confirmed"},
    {"company": "Delta Analytics", "status": "cancelled"},
    {"company": "Epsilon AI", "status": "cancelled"}
]
assert get_pending_companies([
    {"company": "Alpha AI", "status": "confirmed"},
    {"company": "Gamma Tech", "status": "cancelled"}
]) == []
result = get_pending_companies(registrations)
print(result)

assert result == []