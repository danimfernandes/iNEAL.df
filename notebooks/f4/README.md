# Practical Training Session I #
# Introduction to Ancient Population Genetics for Non-Geneticists (Part 2) #

We will guide you through some of the most commonly used methods in Neanderthal paleogenomics, and help you produce some simple statistical tests and plots. These will include mitochondrial DNA neighbour-joining trees, f4-statistics, and estimates of introgression quantification using f4-ratio.

# f4-statistics #
## Replicating Qin & Stoneking 2015 ##

Qin & Stoneking used f4-statistics to investigate how many alleles modern populations (X) shared with Neanderthals versus Denisovans (or vice versa).

    f4(Yoruba, X; Neanderthal, Denisovan)
    f4 > 0      X closer to Neanderthal than to Denisovan
    f4 < 0      X closer to Denisovan than to Neanderthal

However, as shown in the paper's figure legend, all f4 values they obtained were < 0, but some were *more negative* than others.

To investigate the results of these tests, let's do some ourselves. We're going to need the software "qpDstat" from the ADMIXTOOLS package.

    qpDstat




## Replicating Hajdinjak et al. 2021 ##







## Replicating Mafessoni et al. 2020 ##

