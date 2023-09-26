# this is a fuction that converts celsius to fahrenheit 
def celsius_to_fahrenheit(celsius):
    return (round((celsius * (9/5)) + 32,2))
# end function

print(celsius_to_fahrenheit(100.6666666))

# this is a fuction that converts fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
    return (round((fahrenheit - 32) * (5/9),2))
# end function

print(fahrenheit_to_celsius(117))
