#!/usr/bin/env python3

import sys
import os

class Bucket:
    def __init__(self, initial):
        self.red = initial
        self.white = 0

    def total(self):
        return self.red + self.white

    def getPercentWhite(self):
        return self.white / self.total()

    def __str__(self):
        return "red: %.2f white: %.2f total: %.2f pct_white: %.02f%%" % (
                self.red,
                self.white,
                self.total(),
                self.getPercentWhite()*100
                )

def mix(bucket, cup_size):
    total_size = bucket.red + bucket.white
    pct = cup_size / total_size

    # How much of the new mixture is leftover from the old mixture
    red_old = bucket.red / (1 + pct)
    white_old = bucket.white / (1 + pct)

    # How much of the new mixture is new from the other mixture
    red_new = bucket.white * pct / (1 + pct)
    white_new = bucket.red * pct / (1 + pct)

    bucket.red = red_old + red_new
    bucket.white = white_old + white_new

if __name__ == "__main__":
    bucket_size = float(sys.argv[1])
    cup_size = float(sys.argv[2])
    goal_pct = float(sys.argv[3])

    bucket = Bucket(bucket_size)

    i = 0
    print(bucket, "mixes:", i)
    while bucket.getPercentWhite() < (1 - goal_pct):
        i += 1
        mix(bucket, cup_size)
        print(bucket, "mixes:", i)

