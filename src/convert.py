def two_complement(value):
    one_comp = ""
    for digit in value:
        if digit == "0":
            one_comp += "F"
        elif digit == "1":
            one_comp += "E"
        elif digit == "2":
            one_comp += "D"
        elif digit == "3":
            one_comp += "C"
        elif digit == "4":
            one_comp += "B"
        elif digit == "5":
            one_comp += "A"
        elif digit == "6":
            one_comp += "9"
        elif digit == "7":
            one_comp += "8"
        elif digit == "8":
            one_comp += "7"
        elif digit == "9":
            one_comp += "6"
        elif digit == "a":
            one_comp += "5"
        elif digit == "b":
            one_comp += "4"
        elif digit == "c":
            one_comp += "3"
        elif digit == "d":
            one_comp += "2"
        elif digit == "e":
            one_comp += "1"
        else:
            one_comp += "0"

    two_comp = int(one_comp, 16) + 1
    two_comp = hex(two_comp)[2:]
    return two_comp


def convert_to_hex(value):
    flag = False
    index = len(value) - 1
    if value[0] == "0" and value[index] == "H":
        return value[1:index], flag
    elif value[index] == "H":
        return value[:index], flag
    elif value[index] == "B":
        value = value[:index]
        value = hex(int(value, 2))
        value = value[2:]
        return value, flag
    else:
        if value[index] == "D":
            value = value[:index]
        if value[0] == "-":
            value = value[1:]
            flag = True
        value = hex(int(value, 10))
        value = value[2:]
        if not flag:
            return value, flag
        else:
            two_comp = two_complement(value)
            return two_comp, flag

