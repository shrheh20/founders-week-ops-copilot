def get_pending_companies(registrations):
    input_list = []
    for registration in registrations:
        if registration["status"] =="pending":
            input_list.append(registration["company"])
    return input_list
    pass