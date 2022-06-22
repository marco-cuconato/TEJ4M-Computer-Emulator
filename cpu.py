#!/usr/bin/env python3

# Created by Ryan C.
# Created in May 2022
# Code runner for 8-bit code

import sys
import time


class CPU:
    """_CPU class handling all the CPU operations_

    Raises:
        ValueError: _Error checking if there is any issues with the user-inputted lines of code_
    """

    def __init__(self):
        # RAM
        self.memory = [0] * 16
        # Program Counter
        self.program_counter = 0b0000

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
        """_Opens the file and parses it into an array_"""
        try:
            with open("main.bin", encoding="utf_8") as file_content:
                instruction_array = file_content.readlines()
                file_content.close()
                print("Starting computer...")
                self.execute_program(instruction_array)
        except OSError:
            print("Error: Unable to open file.")
            sys.exit()

    def execute_program(self, instruction_array):
        """_Executes the program written in the opened file, line by line_

        Args:
            instruction_array (_dict[str, str]_): _Instructions from the opened file_

        Raises:
            ValueError: _description_
        """
        # Hard-coded instruction set, formatted to 6 characters, accounting
        # for the python prefix of "0b", resulting in a 4 bit binary number
        instruction_set = {
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

        # Iterating line by line of the given main.bin file.
        for line in instruction_array:
            self.program_counter += 0b0001
            try:
                operator = format(int(line[:4], 2), "#06b")
                operand = format(int(line[4:9], 2), "#06b")
                if operator == instruction_set["NOP"]:
                    pass
                elif operator == instruction_set["LDA"]:
                    # TODO
                    pass
                elif operator == instruction_set["ADD"]:
                    self.register_a = format(
                        int(self.register_a, 2) + int(operand, 2), "#06b"
                    )
                    if self.flag_debug:
                        print(
                            f'Added "A" register with operand {operand}, '
                            + f"equals to {self.register_a}."
                        )
                    self.flag_cf = int(self.register_a, 2) > 15
                    if self.flag_cf:
                        self.register_a = self.register_a[:3] + self.register_a[3:]
                    self.flag_zf = int(self.register_a, 2) == 0
                elif operator == instruction_set["SUB"]:
                    self.register_a = format(
                        int(self.register_a, 2) - int(operand, 2), "#06b"
                    )
                    if self.flag_debug:
                        print(
                            f'Subtracted "A" register with operand {operand}, '
                            + f"equals to {self.register_a}"
                        )
                    self.flag_cf = int(self.register_a, 2) < 0
                    self.flag_zf = int(self.register_a, 2) == 0
                elif operator == instruction_set["STA"]:
                    # TODO
                    pass
                elif operator == instruction_set["LDI"]:
                    # Set the register A to the operand
                    self.register_a = operand
                    if self.flag_debug:
                        print(f'Updated "A" register to {operand}.')
                elif operator == instruction_set["JMP"]:
                    # TODO
                    pass
                elif operator == instruction_set["DEBUG"]:
                    # Toggle debug mode
                    self.flag_debug = not self.flag_debug
                    print(f"Debug is on: {self.flag_debug}")
                elif operator == instruction_set["OUT"]:
                    # Output register A to console
                    print(f'Output: Value of "A" register: {self.register_a}')
                elif operator == instruction_set["HLT"]:
                    # Halt the program
                    self.flag_halt = True
                else:
                    print(f"Invalid opcode {operator}.")
                    raise ValueError
            except ValueError:
                print(f"Error in line {self.program_counter}!")
                self.flag_halt = True

            if self.flag_halt:
                print("Done. Halting Computer...")
                sys.exit()
            if self.flag_debug:
                time.sleep(3)
            # If debug mode is on, and any of the flags are enabled, print a warning.
            if self.flag_cf and self.flag_debug:
                print(f"Warning: Carry out detected in line {self.program_counter}.")
                self.flag_cf = False
            elif self.flag_zf and self.flag_debug:
                print(f"Warning: Zero value detected in line {self.program_counter}.")
                self.flag_zf = False


if __name__ == "__main__":
    CPU().load_program()
