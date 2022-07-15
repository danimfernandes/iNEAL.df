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

To investigate the results of these tests, let's do some ourselves. First, we need to have our genetic data! We have prepared a datatset for you with 102 populations/individuals of interest for this practical, with data for 1.24 million positions across the human genome.

We can have a look at the top few lines of each file to understand what is inside:

    head iNEAL_f4v2_PAM.ind

    head iNEAL_f4v2_PAM.snp

We can also check the length of each of those files, which tell us how many individuals and how many SNPs are in the dataset:

    wc -l iNEAL_f4v2_PAM.ind

    wc -l iNEAL_f4v2_PAM.snp

The "wc -l iNEAL_f4v2_PAM.geno" file is in binary format and therefore can't be visualised as text, but it contains the genotype information for each individual, for each 1.24 million positions.

We included a total of 74 modern populations from all across the world, and the following 28 ancient individuals:

    Altai_Neanderthal.DG
    Austria_Krems1_1
    Belgium_UP_GoyetQ116_1
    Belgium_UP_GoyetQ_2
    Chagyrskaya_Neandert.SG
    China_Tianyuan
    Czech_Vestonice16
    Denisova.DG
    DenisovaNeanderthalMix.SG
    Goyet_Neanderthal.SG
    Greenland_Saqqaq.SG
    LesCottes_Neanderthal.SG
    Luxembourg_Loschbour.DG
    Mezmaiskaya1_Neander.SG
    Mezmaiskaya2_Neander.SG
    Romania_Muierii
    Romania_Oase
    Russia_HG_Karelia.SG
    Russia_Kostenki14.SG
    Russia_MA1_HG.SG
    Russia_Sunghir3.SG
    Russia_Ust_Ishim.DG
    Spain_ElMiron
    Spy_Neanderthal.SG
    Turkey_Epipaleolithic
    USA_Anzick.SG
    USA_WA_Kennewick.SG
    Vindija.DG

Now, to actually do some f4-statistics, we're going to need the software "qpDstat" from the ADMIXTOOLS package.

    qpDstat

This program requires a parameter file with all the information in it. This includes the name of our files and dataset, as well as a list of f4 tests we want to run. Let's open one of the provided parameter files.

    nano f4_parameters_QinStoneking_1a

This is what it looks like, and what each section represents:

    genotypename: iNEAL_f4v2_PAM.geno
    snpname: iNEAL_f4v2_PAM.snp
    indivname: iNEAL_f4v2_PAM.ind
    popfilename: f4_tests_QinStoneking_1a
    f4mode: YES
    details: YES

Note how a specific popfilename is already mentioned there ("f4_tests_QinStoneking_1a"). That is the first file with the f4-testes we want to run, and it looks like this:

    Yoruba.DG Spanish.DG Altai_Neanderthal.DG Denisova.DG
    Yoruba.DG French.DG Altai_Neanderthal.DG Denisova.DG
    Yoruba.DG Tuscan_1.DG Altai_Neanderthal.DG Denisova.DG
    Yoruba.DG Finnish.DG Altai_Neanderthal.DG Denisova.DG

Here, our X are the Spanish, French, Tuscan, and Finish populations. There are two more similar files to this one, where the tests were separated into small groups so that the Binder system doesn't run out of memory.

We now have everything we need to run our first f4-statistics!

    qpDstat -p f4_parameters_QinStoneking_1a
    
The output information we want to look at is the following, and here is what each column represents:

                PopA      PopB           PopC             PopD            f4            Z     BABA    ABBA   SNPS
    result:  Yoruba.DG Spanish.DG Altai_Neanderthal.DG Denisova.DG     -0.001129     -5.533   21757  22938 1045961 
    result:  Yoruba.DG  French.DG Altai_Neanderthal.DG Denisova.DG     -0.001194     -6.099   21793  23042 1046082 
    result:  Yoruba.DG Tuscan_1.DG Altai_Neanderthal.DG Denisova.DG     -0.001421     -7.053   21697  23184 1046007 
    result:  Yoruba.DG Finnish.DG Altai_Neanderthal.DG Denisova.DG     -0.001397     -7.087   21687  23148 1046076 
    
Now let's run the other two commands and get the remaining results.

    qpDstat -p f4_parameters_QinStoneking_1b
    qpDstat -p f4_parameters_QinStoneking_1c

And here are all the results combined:

                PopA      PopB           PopC             PopD            f4            Z     BABA    ABBA   SNPS
    result:  Yoruba.DG Spanish.DG Altai_Neanderthal.DG Denisova.DG     -0.001129     -5.533   21757  22938 1045961 
    result:  Yoruba.DG  French.DG Altai_Neanderthal.DG Denisova.DG     -0.001194     -6.099   21793  23042 1046082 
    result:  Yoruba.DG Tuscan_1.DG Altai_Neanderthal.DG Denisova.DG     -0.001421     -7.053   21697  23184 1046007 
    result:  Yoruba.DG Finnish.DG Altai_Neanderthal.DG Denisova.DG     -0.001397     -7.087   21687  23148 1046076 

    result:  Yoruba.DG Armenian.DG Altai_Neanderthal.DG Denisova.DG     -0.001363     -6.694   21642  23067 1046017 
    result:  Yoruba.DG Iranian.DG Altai_Neanderthal.DG Denisova.DG     -0.001199     -6.250   21631  22886 1046045 
    
    result:  Yoruba.DG Quechua.DG Altai_Neanderthal.DG Denisova.DG     -0.001498     -6.652   21665  23233 1046011 
    result:  Yoruba.DG   Mayan.DG Altai_Neanderthal.DG Denisova.DG     -0.001312     -5.913   21833  23205 1045905 
    result:  Yoruba.DG Karitiana.DG Altai_Neanderthal.DG Denisova.DG     -0.001316     -5.770   21834  23210 1046048 

    result:  Yoruba.DG Tibetan.DG Altai_Neanderthal.DG Denisova.DG     -0.001227     -5.802   21743  23027 1046002 
    result:  Yoruba.DG Sindhi_Pakistan.DG Altai_Neanderthal.DG Denisova.DG     -0.001005     -5.259   21684  22735 1045979 
    result:  Yoruba.DG     Han.DG Altai_Neanderthal.DG Denisova.DG     -0.001232     -5.907   21781  23070 1046067 
    result:  Yoruba.DG     Dai.DG Altai_Neanderthal.DG Denisova.DG     -0.001300     -6.733   21652  23012 1046097 
    result:  Yoruba.DG   Yakut.DG Altai_Neanderthal.DG Denisova.DG     -0.001538     -7.240   21553  23162 1045991 
    result:  Yoruba.DG  Papuan.DG Altai_Neanderthal.DG Denisova.DG     -0.000076     -0.297   22618  22698 1046060 
    result:  Yoruba.DG    Onge.DG Altai_Neanderthal.DG Denisova.DG     -0.001469     -6.741   21427  22963 1045475 

## Replicating Hajdinjak et al. 2021 ##







## Replicating Mafessoni et al. 2020 ##

