# CHALLENGE LINK https://www.codewars.com/kata/filter-out-the-geese 
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    filtered_birds = [bird for bird in birds if bird not in geese]
    return filtered_birds
