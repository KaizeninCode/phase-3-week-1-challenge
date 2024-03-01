# CHALLENGE LINK https://www.codewars.com/kata/grasshopper-debug
# BUGS IN THE CHALLENGE
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return float(celsius)

def weather_info(temp):
    celsius = convert_to_celsius(temp)
    if celsius > 0:
        return f"{celsius} is above freezing temperature"
    else:
        return f"{celsius} is freezing temperature"