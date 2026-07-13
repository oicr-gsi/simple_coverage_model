#! /usr/bin/env python3

# 2026-06-30
# Iain Bancarz, ibancarz@oicr.on.ca

from scipy.stats import poisson

y_cover = 48
z_cover = 4600
llod = 0.01

probability_below_llod = 0
for y in range(100):
    for z in range(z_cover-1000, z_cover+1000):
        # count instances where VAF is below LLOD
        if float(y)/(y+z) >= llod:
            # above LLOD
            continue
        p_y = poisson.pmf(y, y_cover)
        p_z = poisson.pmf(z, z_cover)
        probability_below_llod += (p_y*p_z)

print("Probability of VAF below LLOD =", probability_below_llod)
