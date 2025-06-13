eax = "00000000"
ebx = "00000000"
ecx = "00000000"
edx = "00000000"

all_registers = ["EAX", "EBX", "ECX", "EDX",
                 "AX", "BX", "CX", "DX",
                 "AL", "AH", "BL", "BH",
                 "CL", "CH", "DL", "DH"]


def get_value(register):
    if "A" in register:
        if register == "EAX":
            return eax
        elif register == "AX":
            return eax[4:8]
        elif register == "AL":
            return eax[6:8]
        elif register == "AH":
            return eax[4:6]
    if "B" in register:
        if register == "EBX":
            return ebx
        elif register == "BX":
            return ebx[4:8]
        elif register == "BL":
            return ebx[6:8]
        elif register == "BH":
            return ebx[4:6]
    if "C" in register:
        if register == "ECX":
            return ecx
        elif register == "CX":
            return ecx[4:8]
        elif register == "CL":
            return ecx[6:8]
        elif register == "CH":
            return ecx[4:6]
    if "D" in register:
        if register == "EDX":
            return edx
        elif register == "DX":
            return edx[4:8]
        elif register == "DL":
            return edx[6:8]
        elif register == "DH":
            return edx[4:6]


def set_value(register, value, flag=False):
    char = "0"
    if flag:
        char = "f"

    global eax, ecx, edx, ebx

    if register in all_registers[:4]:
        if len(value) < 8:
            value = (8 - len(value)) * char + value
        if register == "EAX":
            eax = value
        elif register == "EBX":
            ebx = value
        elif register == "ECX":
            ecx = value
        else:
            edx = value
        return value
    elif register in all_registers[4:8]:
        if len(value) < 4:
            value = (4 - len(value)) * char + value
        if register == "AX":
            eax = eax[:4] + value
        elif register == "BX":
            ebx = ebx[:4] + value
        elif register == "CX":
            ecx = ecx[:4] + value
        else:
            edx = edx[:4] + value
        return value
    else:
        if len(value) < 2:
            value = (2 - len(value)) * char + value
        if register == "AL":
            eax = eax[:6] + value
        elif register == "AH":
            eax = eax[:4] + value + eax[6:]
        elif register == "BL":
            ebx = ebx[:6] + value
        elif register == "BH":
            ebx = ebx[:4] + value + ebx[6:]
        elif register == "CL":
            ecx = ecx[:6] + value
        elif register == "CH":
            ecx = ecx[:4] + value + ecx[6:]
        elif register == "DL":
            edx = edx[:6] + value
        else:
            edx = edx[:4] + value + edx[6:]
        return value
