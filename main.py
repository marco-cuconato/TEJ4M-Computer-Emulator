#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in May 2022
# Code runner for 8-bit code


def startup():
    registers = [0 for x in range(8)]
    op_codes = {
        "0000": "NOP",
        "0001": "LDA",
        "0010": "ADD",
        "0011": "SUB",
        "0100": "STA",
        "0101": "LDI",
        "0110": "JMP",
        "1110": "OUT",
        "1111": "HLT",
    }

    with open('main.eb') as file_content:
        lines = file_content.readlines()



if __name__ == "__main__":
    startup()
