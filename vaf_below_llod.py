#! /usr/bin/env python3

# 2026-01-16
# Iain Bancarz, ibancarz@oicr.on.ca

import math

def prob_depth(y, c):
    # y = depth of coverage at locus
    # c = mean depth of coverage
    # from Illumina tech note, probability = c**y * exp(-c) / factorial(y)
    # take logs on both sides of the numerator to avoid large-integer errors
    ln_numerator = float(y)*math.log(c) - c
    p = math.exp(ln_numerator) / math.factorial(y)
    return p

y_cover = 9
z_cover = 71
llod = 0.1

probability_below_llod = 0
for y in range(171):
    for z in range(171):
        # count instances where VAF is below LLOD
        if y+z==0:
            # if variant/not-variant depths are zero, it counts as below LLOD
            pass
        elif float(y)/(y+z) >= llod:
            # above LLOD
            continue
        p_y = prob_depth(y, y_cover)
        p_z = prob_depth(z, z_cover)
        probability_below_llod += (p_y*p_z)

print("Probability of VAF below LLOD =", probability_below_llod)
