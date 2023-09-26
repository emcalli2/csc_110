def validate_age(age):
    return age.isnumeric()

def main():
    print(validate_age("20"))
    print(validate_age("3a"))
    print(validate_age("30.5"))
main()
