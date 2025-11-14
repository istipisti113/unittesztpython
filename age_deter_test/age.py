def categ_by_age(age: int):
    if age<=9:
        return "gyerek"
    elif age<=18:
        return "teenager"
    elif age<=64:
        return "adult"
    elif age<=120:
        return "golden age"
    else:
        return f"invalid: {age}"