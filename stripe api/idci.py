def id_checker_payment(api_data):
    a=(api_data["data"][0]["charges"]["data"][0]["id"])
    return a

def id_checker_invoice(api_data):
    b=(api_data["data"][0]["id"])
    return b