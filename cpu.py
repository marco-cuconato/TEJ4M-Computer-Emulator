from enum import Enum

class CPU:
    # RAM
    memory = [0] * 16
    # Program Counter
    program_counter = 0

    register = {
        "A": 0b0000,
        "B": 0b0000,
        "IR": 0b0000,
        "OUT": 0b000,
    }

    flag = {
        "CF": False,
        "ZF": False,
        "HALT": False,
        "DEBUG": False,
    }

    class Opcode(Enum):
        NOP = 0b0000
        LDA = 0b0001
        ADD = 0b0010
        SUB = 0b0011
        STA = 0b0100
        LDI = 0b0101
        JMP = 0b0110
        JC = 0b0111
        JZ = 0b1000
        DEBUG = 0b1001
        OUT = 0b1110
        HLT = 0b1111