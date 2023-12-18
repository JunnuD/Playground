def turn_clockwise(v):

    if v == "N":
        return "E"
    elif v == "E":
        return "S"
    elif v == "S":
        return "W"
    elif v == "W":
        return "N"
    else:
        return ("None")

a = turn_clockwise("S") == "N"
b = turn_clockwise("W") == "N"

print(a)
print(b)

