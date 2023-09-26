def age_milestones(age):
    if age < 18:
        return "you are too young"
    message = ""
    if age >= 18:
         message = message + "You may apply to join the military. "
    if age >= 21:
        message = message + "You may drink. "
    if age >= 35:
        message = message + "You may run for president."
    
    return message

def main():
    print(age_milestones(0))
    print(age_milestones(18))
    print(age_milestones(21))
    print(age_milestones(42))
main()