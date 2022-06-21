#!/usr/bin/env python3

# Created by Ryan C.
# Created in May 2022
# Code runner for 8-bit code

import sys


class CPU:
    def __init__(self):
        # RAM
        self.memory = [0] * 16
        # Program Counter
        self.program_counter = 0

        # Registers
        self.register_a = 0b0000
        self.register_b = 0b0000
        self.register_ir = 0b0000

        # Flags
        self.flag_cf = False
        self.flag_zf = False
        self.flag_halt = False
        self.flag_debug = False

    def load_program(self):
        try:
            with open("main.bin", encoding="utf_8") as file_content:
                instruction_array = file_content.readlines()
                file_content.close()
                self.execute_program(instruction_array)
        except OSError:
            print("Error: Unable to open file.")
            sys.exit()

    def execute_program(self, instruction_array):
        instructions = {
            "NOP": format(int("0000", 2), "#06b"),
            "LDA": format(int("0001", 2), "#06b"),
            "ADD": format(int("0010", 2), "#06b"),
            "SUB": format(int("0011", 2), "#06b"),
            "STA": format(int("0100", 2), "#06b"),
            "LDI": format(int("0101", 2), "#06b"),
            "JMP": format(int("0110", 2), "#06b"),
            "DEBUG": format(int("1001", 2), "#06b"),
            "OUT": format(int("1110", 2), "#06b"),
            "HLT": format(int("1111", 2), "#06b"),
        }

        for line in instruction_array:
            self.program_counter += 1
            try:
                operator = format(int(line[:4], 2), "#06b")
                if operator == instructions["NOP"]:
                    pass
                elif operator == instructions["LDA"]:
                    # TODO
                    pass
                elif operator == instructions["ADD"]:
                    operand = format(int(line[4:], 2), "#06b")
                    self.register_a = format(
                        int(self.register_a, 2) + int(operand, 2), "#06b"
                    )
                    if self.flag_debug:
                        print(
                            f'Added "A" register with operand {operand}, equals to {self.register_a}.'
                        )
                    self.flag_cf = int(self.register_a, 2) > 15
                    self.flag_zf = int(self.register_a, 2) == 0
                elif operator == instructions["SUB"]:
                    operand = format(int(line[4:], 2), "#06b")
                    self.register_a = format(
                        int(self.register_a, 2) - int(operand, 2), "#06b"
                    )
                    if self.flag_debug:
                        print(
                            f'Subtracted "A" register with operand {operand}, equals to {self.register_a}'
                        )
                    self.flag_cf = int(self.register_a, 2) < 0
                    self.flag_zf = int(self.register_a, 2) == 0
                elif operator == instructions["STA"]:
                    # TODO
                    pass
                elif operator == instructions["LDI"]:
                    operand = format(int(line[4:], 2), "#06b")
                    self.register_a = operand
                    if self.flag_debug:
                        print(f'Updated "A" register to {operand}.')
                elif operator == instructions["JMP"]:
                    # TODO
                    pass
                elif operator == instructions["DEBUG"]:
                    # Toggle debug mode
                    self.flag_debug = not self.flag_debug
                    print(f"Debug is on: {self.flag_debug}")
                elif operator == instructions["OUT"]:
                    print(f'Output: Value of "A" register: {self.register_a}')
                elif operator == instructions["HLT"]:
                    self.flag_halt = True
                else:
                    print(f"Invalid opcode {operator}.")
                    raise ValueError
            except ValueError:
                print(f"Error in line {self.program_counter}!")
                self.flag_halt = True

            # If debug mode is on, and any of the flags are enabled, print a warning.
            if self.flag_cf and self.flag_debug:
                print(f"Warning: Carry out detected in line {self.program_counter}.")
                self.flag_cf = False
            elif self.flag_zf and self.flag_debug:
                print(f"Warning: Zero value detected in line {self.program_counter}.")
                self.flag_zf = False

            if self.flag_halt:
                print("Done. Halting Computer...")
                sys.exit()


if __name__ == "__main__":
    CPU().load_program()
