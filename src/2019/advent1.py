#!/usr/bin/python

import sys

def calculate(num):
    num = int(num)
    num /= 3
    num -= 2
    return num

def calculate2(num):
    total_fuel = 0
    additional_fuel = calculate(num)
    while additional_fuel > 0:
        total_fuel += additional_fuel
        additional_fuel = calculate(additional_fuel)
    return total_fuel


if len(sys.argv) < 2:
    print "specify input file"
    sys.exit(1)

total = 0
total2 = 0

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        total += calculate(line)
        total2 += calculate2(line)

print total
print total2

