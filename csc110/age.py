def calculate_year_born():
    age_string = input("What's your age?")
    age_int = int(age_string)
    year_born = 2023 - age_int
    return year_born

def main():
    print(calculate_year_born())
main()

# or this same code could be written like this:
def calculate_year_born():
    return 2023 - int(input("What's your age? "))
print(calculate_year_born())
