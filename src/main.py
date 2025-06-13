import flag
import register
from instructions import *


def write_to_file():
    file = open("result.txt", "w")
    file.write("eax: " + register.eax + "    " + "ebx: " + register.ebx + "\n")
    file.write("\n")
    file.write("ecx: " + register.ecx + "    " + "edx: " + register.edx + "\n")
    file.write("\n")
    file.write("Carry: " + flag.CF + "    " + "Overflow: " + flag.OF + "    " + "Sign: " + flag.SF + "    "
               + "Zero: " + flag.ZF + "\n" + "---------------------------------------------------" + "\n\n")
    file.close()


text_file = open("AssemblyCode.txt", "r")
code = text_file.read().split()
text_file.close()
code = [string.upper() for string in code]


def do_instruction(line):
    instruction = line[0]
    des = line[1]
    source = line[2]
    if instruction == "MOV":
        mov(des, source)
    if instruction == "ADD":
        add(des, source)
    if instruction == "SUB":
        sub(des, source)
    if instruction == "AND":
        bitwise_and(des, source)
    if instruction == "OR":
        bitwise_or(des, source)
    if instruction == "XOR":
        bitwise_xor(des, source)


for i in code:
    if i == ',':
        code.remove(i)

for i in range(len(code)):
    if ',' in code[i]:
        code[i] = code[i].replace(",", "")

length = len(code)
for i in range(length // 3 + 1):
    do_instruction(code[:3])
    if i != length // 3 - 1:
        code = code[3:]
    else:
        write_to_file()
        break

