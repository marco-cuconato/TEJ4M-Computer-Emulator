#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in May 2022
# Code runner for 8-bit code


def op_code_match(op_codes):
    match line[:5]:
        case op_codes[0]:
            print("Hello, World!")


def run_program(lines, registers, op_codes):
    for line in len(lines):
        op_code_match(op_codes)


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

    with open('main.ebit') as file_content:
        lines = file_content.readlines()
        run_program(lines, registers, op_codes)



if __name__ == "__main__":
    startup()
