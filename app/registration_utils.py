from datetime import datetime

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

def count_companies_by_status(companies):
    status_count={"pending":0,"approved":0,"rejected":0}
    for company in companies:
        status = company["status"]
        status_count[status]+=1
    return status_count

def find_stale_registrations(registrations):
    stale_company_id=[]
    reference_date = datetime.strptime("2026-10-27", "%Y-%m-%d").date()
    for company in registrations:
        if company["status"]=="pending":
            last_update=datetime.strptime(company["last_updated"],"%Y-%m-%d").date()
            time_update=reference_date-last_update
            if time_update.days>7:
                stale_company_id.append(company["company_id"])
    return stale_company_id

def reconcile_companies(crm_companies, event_companies):
    crm=set()
    event=set()
    
    for company in crm_companies:
        crm.add(company["company_id"])
        
    for company in event_companies:
        event.add(company["company_id"])
            
    output={
        "only_in_crm":sorted(crm-event),
        "only_in_events":sorted(event-crm),
        "in_both":sorted(crm & event)
    }

    return output