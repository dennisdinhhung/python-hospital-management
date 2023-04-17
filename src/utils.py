import datetime


def invalid_id(id, para: str):
    """
    Return 1 if invalid | 0 if valid\n
    Exp: ("D-123", "D-") => Valid\n
        ("s-12", "D-")  => Invalid
    """
    while True:
        try:
            id_num = int(id[-3:])
            if id[:2] != para or len(id) != 5:
                return 1
            else:
                return 0
        except ValueError:
            return 1

def invalid_gender(gender):
    if gender != "M" and gender != "F":
        return 1
    else: return 0

def invalid_gend(gend):
    if gend != "M" and gend != "F":
        return 1
    else: return 0

def invalid_dob(dob):
    while True:
        try:
            dd_check = int(dob[:2])
            mm_check = int(dob[:5][-2:])
            yyyy_check = int(dob[-4:])
            check1 = dob[:3][-1:]
            check2 = dob[:6][-1:]
            if len(dob) != 10:
                return 1
            elif check1!="/" or check2!="/":
                return 1
            elif dd_check<1 or dd_check>31:
                return 1
            elif mm_check<1 or mm_check>12:
                return 1
            else: return 0
        except ValueError:
            return 1

def invalid_phone(phone):
    while True:
        try:
            phone_check = int(phone)
            return 0
        except ValueError:
            return 1

def invalid_salary(salary):
    while True:
        try:
            salary_check = float(salary)
            if salary_check >= 0:
                return 0
            else: return 1
        except ValueError:
            return 1

def invalid_debt(debt):
    while True:
        try:
            debt_check = float(debt)
            if debt_check >= 0:
                return 0
            else: return 1
        except ValueError:
            return 1

def invalid_price(price):
    while True:
        try:
            price_check = float(price)
            if price_check >= 0:
                return 0
            else: return 1
        except ValueError:
            return 1