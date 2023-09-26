def max31(material):
    if material == "wood":
        return "yes"
    if material == "steel":
        return "no"
    else:
        return "try again"
print(max31("steel"))