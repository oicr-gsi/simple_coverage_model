#! /usr/bin/env python3

# Iain Bancarz, ibancarz@oicr.on.ca

from argparse import ArgumentParser
from scipy.stats import poisson

desc = 'Simple model of the probability of VAF falling below lower limit of detection (LLOD)'
epilog = '- Appropriate min/max arguments depend on the depth of coverage. The script will sum over all coverage pairs (y,z) within the min/max ranges. The defaults are appropriate for WGTS at 80X. For TAR, z-max and z-min equal to z-cover plus or minus 1000 are recommended.'
parser = ArgumentParser(prog='vaf_below_llod', description=desc, epilog=epilog)
parser.add_argument('--llod', type=float, default=0.1, help="Lower limit of detection (must be between 0 and 1, default=0.1)")
parser.add_argument('--y-cover', required=True, type=int, help='Mean sequenced depth of the variant allele')
parser.add_argument('--y-min', default=0, type=int, help='Minimum variant coverage to model (default=0)')
parser.add_argument('--y-max', default=100, type=int, help='Maximum variant coverage to model (default=100)')
parser.add_argument('--z-cover', required=True, type=int, help='Mean sequenced depth of the non-variant allele')
parser.add_argument('--z-min', default=0, type=int, help='Minimum variant coverage to model (default=0)')
parser.add_argument('--z-max', default=200, type=int, help='Maximum variant coverage to model (default=200)')
args = parser.parse_args()

y_cover = args.y_cover
z_cover = args.z_cover
llod = args.llod
if (llod < 0 or llod > 1):
    raise ValueError("LLOD must be between 0 and 1, received {0}".format(llod))

probability_below_llod = 0
for y in range(args.y_min, args.y_max):
    for z in range(args.z_min, args.z_max):
        # count instances where VAF is below LLOD
        if y+z==0:
            # both coverages == 0 counts as below LLOD
            pass
        elif float(y)/(y+z) >= llod:
            # coverage above LLOD
            continue
        p_y = poisson.pmf(y, y_cover)
        p_z = poisson.pmf(z, z_cover)
        probability_below_llod += (p_y*p_z)

print("Probability of VAF below LLOD =", round(probability_below_llod, 3))
