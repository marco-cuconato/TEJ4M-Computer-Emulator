from enum import Enum


class CPU:
    registers = {
        "A": 0,
        "B": 0,
        "IR": 0,
        "OUT": 0,
    }

    flags = {
        "CF": False,
        "ZF": False,
        "HALT": False,
    }

    class OpCodes(str, Enum):
        NOP = "0000"
        LDA = "0001"
        ADD = "0010"
        SUB = "0011"
        STA = "0100"
        LDI = "0101"
        JMP = "0110"
        OUT = "1110"
        HLT = "1111"
