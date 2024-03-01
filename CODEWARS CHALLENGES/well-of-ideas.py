# CHALLENGE LINK https://www.codewars.com/kata/well-of-ideas-easy-version
def well(x):
    good_ideas = x.count('good')
    if good_ideas == 1 or good_ideas == 2:
        return 'Publish!'
    elif good_ideas > 2:
        return 'I smell a series!'
    else:
        return 'Fail!'