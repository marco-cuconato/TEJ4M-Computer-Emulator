#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in May 2022
# Code runner for 8-bit code

import sys
from cpu import CPU


def run_program(instructions_array):
    cpu = CPU

    for line in instructions_array:
        match line[:4]:
            case cpu.Opcode.NOP:
                pass
            case cpu.Opcode.LDA:
                cpu.register["A"] = cpu.memory[cpu.register["IR"]]
            case cpu.Opcode.ADD:
                cpu.register["A"] = format(
                    int(cpu.register["A"], 2) + int(line[4:], 2), "#010b"
                )
            case cpu.Opcode.SUB:
                cpu.register["A"] = format(
                    int(cpu.register["A"], 2) - int(line[4:], 2), "#010b"
                )
                print(cpu.register["A"])
            case cpu.Opcode.STA:
                print("Hello, World!")
            case cpu.Opcode.LDI:
                cpu.register["IR"] = line[:4]
                cpu.register["A"] = format(int(line[4:], 2), "#010b")
                print(cpu.register["A"])
            case cpu.Opcode.JMP:
                print("Hello, World!")
            case cpu.Opcode.OUT:
                print("Hello, World!")
            case cpu.Opcode.HLT:
                cpu.flag["HALT"] = True

        if cpu.flag["HALT"]:
            print("Stopping cpu...")
            sys.exit()


def startup():
    try:
        with open("main.ebit", encoding="utf_8") as file_content:
            content_array = file_content.readlines()
            file_content.close()
            run_program(content_array)
    except OSError:
        print("Error: Unable to open file.")
        sys.exit()


if __name__ == "__main__":
    startup()
