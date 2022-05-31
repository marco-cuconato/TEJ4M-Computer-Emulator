#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in May 2022
# Code runner for 8-bit code


def run_program(lines):
    for line in lines:
        match line[:5]:
            # NOP
            case "0000":
                print("Hello, World!")
            # LDA
            case "0001":
                print("Hello, World!")
            # ADD
            case "0010":
                print("Hello, Worldasdasdasdasd!")
            # SUB
            case "0011":
                print("Hello, World!")
            # STA
            case "0100":
                print("Hello, World!")
            # LDI
            case "0101":
                print("Hello, World!")
            # JMP
            case "0110":
                print("Hello, World!")
            # OUT
            case "1110":
                print("Hello, World!")
            # HLT
            case "1111":
                print("Hello, World!")


def startup():
    registers = [0 for x in range(8)]

    with open("main.ebit") as file_content:
        lines = file_content.readlines()
        run_program(lines)


if __name__ == "__main__":
    startup()
