def get_pending_companies(registrations):
    input_list = []
    for registration in registrations:
        if registration["status"] =="pending":
            input_list.append(registration["company"])
    return input_list

def validate_required_fields(company):
    required_fields = ["company_id", "name","status"]
    for field in required_fields:
        if field not in company:
            return False
        if type(company["company_id"]) != int:
            return False
        if type(company["name"]) != str:
            return False
        if type(company["status"]) != str:
            return False
        if company["name"].strip() == "":
            return False
        if company["company_id"] <=0:
            return False
        if company["status"] not in ["pending", "approved", "rejected"]:
            return False
    return True

def find_duplicate_companies(companies):
    seen_ids = set()
    duplicate_companies = []
    for company in companies:
        if company["company_id"] in seen_ids:
            if company["company_id"] not in duplicate_companies:
                duplicate_companies.append(company["company_id"])
        seen_ids.add(company["company_id"])
    return duplicate_companies