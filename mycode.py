def add_positive(a, b):
    if a > 0 and b > 0:
        return a + b
    else:
        raise ValueError("Both numbers must be positivee")

def add_zero(a, b):
    if a == 0 or b == 0:
        return a + b
    else:
        raise ValueError("At least one number must be zero")

def add_negative(a, b):
    if a < 0 and b < 0:
        return a + b
    else:
        raise ValueError("Both numbers must be negative")
