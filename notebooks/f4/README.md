# Practical Training Session I #
# Introduction to Ancient Population Genetics for Non-Geneticists (Part 2) #

We will guide you through some of the most commonly used methods in Neanderthal paleogenomics, and help you produce some simple statistical tests and plots. These will include mitochondrial DNA neighbour-joining trees, f4-statistics, and estimates of introgression quantification using f4-ratio.

# f4-statistics #
## Replicating Qin & Stoneking 2015 ##

Qin & Stoneking used f4-statistics to investigate modern populations (X) shared more alleles with Neanderthals versus Denisovans (or vice versa).

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

Hajdinjak and colleagues used f4-statistics to investigate if some ancient/archaic individuals (X) shared more alleles with the eastern Tianyuan or western Kostenki14.
With this they wanted to see if those individuals contributed more towards modern East or West Eurasians.

    D/f4(Tianyuan, Kostenki14; X, Mbuti) 
    f4(A, B; C, D) or f4(D, C; B, A)

    f4(Tianyuan, Kostenki14; X, Mbuti) 
    f4(Mbuti, X; Kostenki14, Tianyuan)

    D/f4 > 0        X closer to Tianyuan than to Kostenki14
    D/f4 < 0        X closer to Kostenki14 than to Tianyuan

We separated our data again, this time into 2 sets of files, so let's run the first one, then the second:

    qpDstat -p f4_parameters_Hajdinjak_2a
    qpDstat -p f4_parameters_Hajdinjak_2b

And here are the results:

    result: China_Tianyuan Russia_Kostenki14.SG Russia_Sunghir3.SG   Mbuti.DG     -0.012435    -15.004   41016  51074 808838 
    result: China_Tianyuan Russia_Kostenki14.SG Czech_Vestonice16   Mbuti.DG     -0.010691    -13.274   31323  37910 616144 
    result: China_Tianyuan Russia_Kostenki14.SG Belgium_UP_GoyetQ116_1   Mbuti.DG     -0.006486     -7.652   35397  39666 658252 
    result: China_Tianyuan Russia_Kostenki14.SG Luxembourg_Loschbour.DG   Mbuti.DG     -0.008428    -11.930   42232  48976 800247 
    result: China_Tianyuan Russia_Kostenki14.SG Russia_HG_Karelia.SG   Mbuti.DG     -0.004793     -6.619   38305  41683 704840 
    
    result: China_Tianyuan Russia_Kostenki14.SG Romania_Oase   Mbuti.DG      0.001606      1.760    9108   8835 169768 
    result: China_Tianyuan Russia_Kostenki14.SG Russia_Ust_Ishim.DG   Mbuti.DG     -0.000333     -0.449   42335  42590 766348 
    result: China_Tianyuan Russia_Kostenki14.SG USA_Anzick.SG   Mbuti.DG      0.003994      5.845   47439  44215 807327 
    result: China_Tianyuan Russia_Kostenki14.SG USA_WA_Kennewick.SG   Mbuti.DG      0.003807      5.091   24728  23106 425924 
    result: China_Tianyuan Russia_Kostenki14.SG Greenland_Saqqaq.SG   Mbuti.DG      0.005727      7.831   46410  41922 783674

## Replicating Mafessoni et al. 2020 ##

Mafessoni and colleagues tried to understand two things about published archaic individuals and their relationship towards Chagyrskaya 8:

a) were they closer to the newly presented 80 kyo Chagyrskaya individual, than to the 100 kyo Neanderthal from the nearby 100km Denisova Cave
b) or instead were they closer to the 50 kyo Vindija individual.

Again, we divided the data into 2 parts. Part 3a contains the tests against Altai_Neanderthal (AKA Denisova 5), and part 3b against Vindija33.19.

    qpDstat -p f4_parameters_Mafessoni_3a
    qpDstat -p f4_parameters_Mafessoni_3b

Here are the results for 3a (100 kyo Denisova 5 vs 80 kyo Chagyrskaya 8):

    result:  Chimp.REF LesCottes_Neanderthal.SG Altai_Neanderthal.DG Chagyrskaya_Neandert.SG      0.003413     18.195    6130   3330 820204 
    result:  Chimp.REF Spy_Neanderthal.SG Altai_Neanderthal.DG Chagyrskaya_Neandert.SG      0.003340     16.411    3538   1917 485146 
    result:  Chimp.REF Goyet_Neanderthal.SG Altai_Neanderthal.DG Chagyrskaya_Neandert.SG      0.003582     17.743    6059   3218 793119 
    result:  Chimp.REF Mezmaiskaya1_Neander.SG Altai_Neanderthal.DG Chagyrskaya_Neandert.SG      0.003322     16.482    4375   2400 594502 
    result:  Chimp.REF Vindija.DG Altai_Neanderthal.DG Chagyrskaya_Neandert.SG      0.003569     18.970    7759   4117 1020387 
    result:  Chimp.REF DenisovaNeanderthalMix.SG Altai_Neanderthal.DG Chagyrskaya_Neandert.SG      0.001598     11.833    4957   3565 871328 
    result:  Chimp.REF Denisova.DG Altai_Neanderthal.DG Chagyrskaya_Neandert.SG     -0.000282     -2.153    3941   4229 1020023 

And here are the results for 3b (50 kyo Vindija33.19 vs 80 kyo Chagyrskaya 8):

    result:  Chimp.REF LesCottes_Neanderthal.SG Vindija.DG Chagyrskaya_Neandert.SG     -0.001415     -9.747    2940   4100 820223 
    result:  Chimp.REF Spy_Neanderthal.SG Vindija.DG Chagyrskaya_Neandert.SG     -0.001927    -11.803    1582   2518 485176 
    result:  Chimp.REF Goyet_Neanderthal.SG Vindija.DG Chagyrskaya_Neandert.SG     -0.002280    -14.176    2584   4393 793141 
    result:  Chimp.REF Mezmaiskaya1_Neander.SG Vindija.DG Chagyrskaya_Neandert.SG     -0.000041     -0.292    2522   2546 594520 
    result:  Chimp.REF Altai_Neanderthal.DG Vindija.DG Chagyrskaya_Neandert.SG      0.000039      0.306    4158   4117 1020387 
    result:  Chimp.REF DenisovaNeanderthalMix.SG Vindija.DG Chagyrskaya_Neandert.SG      0.000197      1.800    3242   3070 871324 
    result:  Chimp.REF Denisova.DG Vindija.DG Chagyrskaya_Neandert.SG     -0.000022     -0.228    3001   3024 1020022 

