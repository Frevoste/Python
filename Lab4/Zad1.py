kandydat1 = {
    'min_salary' : 12000
}

stanowisko1 = {
    'max_pay' : 20000
}

def jobmatching(kandydat, stanowisko):
    try:
        if stanowisko['max_pay'] + stanowisko['max_pay']*0.1 >= kandydat['min_salary']:
            return True
        else:
            return False
    except KeyError as e:
        raise ValueError(f"Brak kluczowej wartości:{e}.")
    
if jobmatching(kandydat1,stanowisko1):
    print("Dobre stanowisko")
else:
    print("Złe stanowisko.")