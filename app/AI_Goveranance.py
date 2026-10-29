def filter_authorized_companies(companies,user):
    authorized_companies=[]
    role=user["role"]
    if role=="admin":
        return companies
    elif role=="viewer":
        allowed_programs = set(user["allowed_programs"])
        for company in companies:
            if company["program_id"] in allowed_programs:
                authorized_companies.append(company)
    else:
        raise PermissionError("Unauthorized role")
    
    return authorized_companies

def count_authorised_companies(companies,user):
    authorized = filter_authorized_companies(companies,user)
    agg_companies=len(authorized)
    
    return agg_companies