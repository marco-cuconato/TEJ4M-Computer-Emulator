#!/usr/bin/env python3

# Created by Ryan C.
# Created in May 2022
# Code runner for 8-bit code

from enum import Enum
import sys

class CPU:
    def __init__(self):
        # RAM
        self.memory = [0] * 16
        # Program Counter
        self.program_counter = 0

        # Registers
        self.A = 0b0000
        self.B = 0b0000
        self.IR = 0b0000

        # Flags
        self.CF = False
        self.ZF = False
        self.HALT = False
        self.DEBUG = False
    
    def load_program(self):
        try:
            with open("main.ebit", encoding="utf_8") as file_content:
                instruction_array = file_content.readlines()
                file_content.close()
                self.execute_program(instruction_array)
        except OSError:
            print("Error: Unable to open file.")
            sys.exit()

    
    def execute_program(self, instruction_array):
        instructions = {
            "NOP": format(int("0000", 2), '#06b'),
            "LDA": format(int("0001", 2), '#06b'),
            "ADD": format(int("0010", 2), '#06b'),
            "SUB": format(int("0011", 2), '#06b'),
            "STA": format(int("0100", 2), '#06b'),
            "LDI": format(int("0101", 2), '#06b'),
            "JMP": format(int("0110", 2), '#06b'),
            "DEBUG": format(int("1001", 2), '#06b'),
            "OUT": format(int("1110", 2), '#06b'),
            "HLT": format(int("1111", 2), '#06b'),
        }

        for line in instruction_array:
            self.program_counter += 1
            try:
                operator = format(int(line[:4], 2), '#06b')
                if operator == instructions["NOP"]:
                    pass
                elif operator == instructions["LDA"]:
                    # TODO
                    pass
                elif operator == instructions["ADD"]:
                    operand = format(int(line[4:], 2), '#06b')
                    self.A = format(int(self.A, 2) + int(operand, 2), '#06b')
                    if self.DEBUG:
                        print(f"Added \"A\" register with operand {operand}, equals to {self.A}.")
                    self.CF = int(self.A, 2) > 15
                    self.ZF = int(self.A, 2) == 0
                elif operator == instructions["SUB"]:
                    operand = format(int(line[4:], 2), '#06b')
                    self.A = format(int(self.A, 2) - int(operand, 2), '#06b')
                    if self.DEBUG:
                        print(f"Subtracted \"A\" register with operand {operand}, equals to {self.A}")
                    self.CF = int(self.A, 2) < 0
                    self.ZF = int(self.A, 2) == 0
                elif operator == instructions["STA"]:
                    # TODO
                    pass
                elif operator == instructions["LDI"]:
                    operand = format(int(line[4:], 2), '#06b')
                    self.A = operand
                    if self.DEBUG:
                        print(f"Updated \"A\" register to {operand}.")
                elif operator == instructions["JMP"]:
                    # TODO
                    pass
                elif operator == instructions["DEBUG"]:
                    # Toggle debug mode
                    self.DEBUG = not self.DEBUG
                    print(f"Debug is on: {self.DEBUG}")
                elif operator == instructions["OUT"]:
                    print(f"Value of \"A\" register: {self.A}")
                elif operator == instructions["HLT"]:
                    self.HALT = True
                else:
                    print(f"Invalid opcode {operator}.")
                    raise ValueError
            except ValueError:
                print(f"Error in line {self.program_counter}!")
                self.HALT = True
            
            # If debug mode is on, and any of the flags are enabled, print a warning.
            if self.CF and self.DEBUG:
                print(f"Warning: Carry out detected in line {self.program_counter}.")
                self.CF = False
            elif self.ZF and self.DEBUG:
                print(f"Warning: Zero value detected in line {self.program_counter}.")
                self.ZF = False

            if self.HALT:
                print("Done. Halting Computer...")
                sys.exit()


if __name__ == "__main__":
    CPU().load_program()