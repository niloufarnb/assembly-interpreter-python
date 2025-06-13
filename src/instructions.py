from register import *
from flag import set_flag
from convert import *


def mov(des, source):
    flag = False
    if source in all_registers:
        src_value = get_value(source)
    else:
        src_value, flag = convert_to_hex(source)
    res = set_value(des, src_value, flag)


def add(des, source, is_neg=False):
    if source[0] == "-":
        is_neg = True

    if source in all_registers:
        src_value = get_value(source)
    else:
        src_value, flag = convert_to_hex(source)
    des_value = get_value(des)

    if len(src_value) < len(des_value) and is_neg:
        src_value = (len(des_value) - len(src_value)) * "f" + src_value

    res = int(des_value, 16) + int(src_value, 16)
    res = hex(res)
    res = res[2:]

    carry_flag = False
    if len(res) > len(des_value):
        carry_flag = True
        res = res[1:]

    res = set_value(des, res)
    set_flag("ADD", res, des, src_value, des_value, carry_flag)


def sub(des, source):
    if source[0] == "-":
        source = source[1:]
        add(des, source)
        return

    if source[0] == "0" and source[len(source) - 1] == "H":
        source = source[1:len(source) - 1]
        source = two_complement(source)
        source = source + "H"
        add(des, source, True)
        return

    if source[len(source) - 1] == "H":
        source = source[:len(source) - 1]
        source = two_complement(source)
        source = source + "H"
        add(des, source, True)
        return

    if source[len(source) - 1] == "B":
        source = source[:len(source) - 1]
        source = hex(int(source, 2))
        source = source[2:]
        source = two_complement(source)
        source = source + "H"
        add(des, source, True)
        return


def bitwise_and(des, source):
    is_neg = False

    if source[0] == "-":
        is_neg = True

    if source in all_registers:
        src_value = get_value(source)
    else:
        src_value, flag = convert_to_hex(source)
    des_value = get_value(des)

    if len(src_value) < len(des_value) and is_neg:
        x = len(des_value) - len(src_value)
        src_value = x * "f" + src_value

    res = int(des_value, 16) & int(src_value, 16)
    res = hex(res)
    res = res[2:]

    if len(res) > len(des_value):
        res = res[1:]

    res = set_value(des, res)
    set_flag("AND", res, des)


def bitwise_or(des, source):
    is_neg = False

    if source[0] == "-":
        is_neg = True

    if source in all_registers:
        src_value = get_value(source)
    else:
        src_value, flag = convert_to_hex(source)
    des_value = get_value(des)

    if len(src_value) < len(des_value) and is_neg:
        x = len(des_value) - len(src_value)
        src_value = x * "f" + src_value

    res = int(des_value, 16) | int(src_value, 16)
    res = hex(res)
    res = res[2:]

    if len(res) > len(des_value):
        res = res[1:]
    res = set_value(des, res)
    set_flag("OR", res, des)


def bitwise_xor(des, src):
    if src in all_registers:
        src_value = get_value(src)
    else:
        src_value = convert_to_hex(src)
    des_value = get_value(des)

    res = int(des_value, 16) ^ int(src_value, 16)
    res = hex(res)
    res = res[2:]
    set_value(des, res)
