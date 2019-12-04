#!/usr/bin/python

import sys

if len(sys.argv) < 3:
    print "specify input file and search value"
    sys.exit(1)

def processUnit(tape, address):
    opcode = tape[address]
    address1 = tape[address+1]
    address2 = tape[address+2]
    parameter1 = tape[address1]
    parameter2 = tape[address2]
    result_address = tape[address+3]

    fns = [
            None,
            lambda a,b: a+b,
            lambda a,b: a*b,
            ]

    tape[result_address] = fns[opcode](parameter1, parameter2)

    return address + 4

def process(tape, noun, verb):
    tape[1] = noun
    tape[2] = verb

    instruction_pointer = 0
    while tape[instruction_pointer] != 99:
        instruction_pointer = processUnit(tape, instruction_pointer)
    return tape[0]

with open(sys.argv[1], 'r') as f:
    l = f.readline()
    l = l.strip()
    tape = [int(x) for x in l.split(',')]

def part1(tape):
    noun = 12
    verb = 2

    return process(tape, noun, verb)

def part2(tape, search):
    for noun in range(100):
        for verb in range(100):
            if search == process(list(tape), noun, verb):
                return 100 * noun + verb

print part1(list(tape))
print part2(tape, int(sys.argv[2]))

