# this function converts kilograms to pounds
def kg_to_lbs():
    kilos = float(input())
    pounds = kilos * 2.205
    return round(pounds,2)
print(kg_to_lbs())

# this function converts liters to gallons
def liters_to_gallons():
    liters = input()
    liters_int = float(liters)
    gallons = liters_int/3.785
    return round(gallons,2)
print(liters_to_gallons())


