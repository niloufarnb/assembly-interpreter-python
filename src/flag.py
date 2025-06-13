from register import all_registers

ZF = "0"
CF = "0"
OF = "0"
SF = "0"

negative_values = ["8", "9", "a", "b", "c", "d", "e", "f"]


def set_flag(instruction, res, destination, val1=None, val2=None, flag=False):
    global ZF, CF, OF, SF

    if res[0] in negative_values:
        SF = "1"
    else:
        SF = "0"

    if destination in all_registers[0:4]:
        if res == "00000000":
            ZF = "1"
        else:
            ZF = "0"
    elif destination in all_registers[4:8]:
        if res == "0000":
            ZF = "1"
        else:
            ZF = "0"
    else:
        if res == "00":
            ZF = "1"
        else:
            ZF = "0"

    if instruction == "AND" or instruction == "OR":
        CF = "0"
        OF = "0"

    if instruction == "ADD":
        if val1[0] in negative_values and val2[0] in negative_values and res[0] not in negative_values:
            OF = "1"
        elif val1[0] not in negative_values and val2[0] not in negative_values and res[0] in negative_values:
            OF = "1"
        else:
            OF = "0"

        if flag:
            CF = "1"
        else:
            CF = "0"

