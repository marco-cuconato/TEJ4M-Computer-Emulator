#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in May 2022
# Code runner for 8-bit code

import cpu


def run_program(lines):
    computer = cpu.CPU

    for line in lines:
        match line[:4]:
            # NOP
            case computer.OpCodes.NOP:
                pass
            # LDA
            case computer.OpCodes.LDA:
                computer.registers["IR"] = line[:4]
                computer.registers["A"] = format(int(line[4:], 2), '#010b')
                print(computer.registers["A"])
            # ADD
            case computer.OpCodes.ADD:
                computer.registers["A"] = format(int(computer.registers["A"], 2) + int(line[4:], 2), '#010b')
            # SUB
            case computer.OpCodes.SUB:
                print("Hello, World!")
            # STA
            case computer.OpCodes.STA:
                print("Hello, World!")
            # LDI
            case computer.OpCodes.LDI:
                print("Hello, World!")
            # JMP
            case computer.OpCodes.JMP:
                print("Hello, World!")
            # OUT
            case computer.OpCodes.OUT:
                print("Hello, World!")
            # HLT
            case computer.OpCodes.HLT:
                print("Hello, World!")


def startup():
    with open("main.ebit", encoding="utf_8") as file_content:
        lines = file_content.readlines()
        run_program(lines)


if __name__ == "__main__":
    startup()
