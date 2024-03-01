# CHALLENGE LINK https://www.codewars.com/kata/grasshopper-personalized-message
def greet(name, owner):
    if name == owner:
        return 'Hello boss'
    else:
        return 'Hello guest'