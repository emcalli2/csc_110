def validate_age(age):
   if age.isnumeric() and int(age) >= 0 and int(age) <= 110:
       return True
   else:
       return False

def check_eligibility(age):
    return age >= 18
