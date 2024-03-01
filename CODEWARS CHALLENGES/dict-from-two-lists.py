# CHALLENGE LINK https://www.codewars.com/kata/5533c2a50c4fea6832000101
def create_dict(keys, values):
    new_dict = {}
    if len(keys) == len(values) | len(keys) < len(values) :
        for index, item in enumerate(keys):
            new_dict[item] = values[index]

    else:
        for index, item in enumerate(keys):   

            if index < len(values):                 
                new_dict[item] = values[index]
            else:
                new_dict[item] = None                            

    return new_dict