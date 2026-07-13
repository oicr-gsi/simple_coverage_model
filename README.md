# Introduction

This is a simple coverage model used to determine likelihood of known variants falling below the detection threshold, for example in proficiency testing. The model is implemented in a Python script: [vaf_below_llod.py](./vaf_below_llod.py)

# Example 1: WGTS

In the CAPNGSST proficiency test completed in January 2026, the Digital PCR VAF of the _MET_ variant was 11.7%. Sequencing at OICR detected a VAF of 5%, which fell below our LLOD of 10%. It is important to note that depth of coverage in sequencing is subject to random variation. To a first approximation it follows a Poisson distribution, as discussed in an [Illumina technical note](https://www.illumina.com/documents/products/technotes/technote_coverage_calculation.pdf).

We can estimate the probability that VAF for a particular variant will fall below the LLOD. Suppose we have sequenced to our standard mean depth of 80X. Then if coverage depth were perfectly smooth, a VAF of 11.7% would translate to 9 variant reads and 71 non-variant reads at the locus of interest. But depth of coverage is not perfectly smooth; for example, if by chance we have 7 variant and 72 non-variant reads, then the variant is below LLOD.

We can imagine two Poisson distributions, one for variant reads and one for non-variant reads, with mean depth of coverage 9 and 71 respectively. If we sum over coverages such that the VAF is less than 10%, we find there is a 37% chance of the _MET_ variant falling below LLOD by random variation in depth.

This is a simplified model which ignores second-order effects such as sequence context, but it indicates there is a substantial chance of this _MET_ variant being missed due to the variation inherent in short-read sequencing.

# Example 2: TAR

For TAR APT in July 2026, VAF of a variant in _CDH1_ was 0.9%, slightly below the assay detection threshold of 1%.

We can quantify the variability as follows. Suppose the “true” frequency of the _CDH1_ variant is 1%. We can imagine two  Poisson distributions, one for variant reads and one for non-variant reads, with mean depth of coverage 28 and 2,706 respectively. The value 28 is 1% of our observed depth of coverage 2,734 (rounded up), and similarly  2,706 is 99% of observed depth (rounded down).  If we sum over coverages such that the VAF is less than 1%, we find there is a 46% probability of the _CDH1_ variant falling below LLOD by random variation in depth.

# Additional Remarks

Release v0.0.2 has an updated version of the script which can process higher coverages, for example for TAR reporting where mean unique depth of coverage may exceed 5000X.

The model relies on the fact that the mean of a sum of independent random variables is equal to the sum of the means. See for example Grimmet & Welsh (1986), p. 42.

Further details are in a presentation given to GSI: [SimpleCoverageModel20260323.pdf](./SimpleCoverageModel20260323.pdf).

# Reference

Grimmet, G. & Welsh, D. (1986). Probability: An Introduction. Oxford University Press.

# Copyright and License

Copyright &copy; 2026 by Genome Sequence Informatics, Ontario Institute for Cancer Research.

Licensed under the [GPL 3.0 license](https://www.gnu.org/licenses/gpl-3.0.en.html).
