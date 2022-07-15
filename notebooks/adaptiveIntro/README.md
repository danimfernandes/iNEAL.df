# Practical Training Session II: Adaptive Introgression in Modern and Archaic Humans #

We will show how to detect an example fragment in modern human data that also shows a signature of positive selection. We will compare the state of specific archaic-like SNPs in archaic and modern genomes.

# Isolate wanted SNPs #

The dataset we are giving you ("iNEAL_TLRadapInto") includes plenty more SNPs that are not of interest for what we want to show you.

So first, to expedite the analysis, we should isolate the SNPs we want to look at in the TLR cluster from this large dataset:

    rs11466640
    rs5743563
    rs5743560
    rs11725779

Let's create a new test file and add this information to it.

Now, we can use the following commands with the software PLINK to reduce our huge dataset into only these SNPs:

    plink --bfile iNEAL_TLRadapInto --extract extract_SNPsTLR --make-bed --out iNEAL_TLRadapInto_subset

The dataset provided comes with the following populations/individuals. Modern population codes are listed here:
https://www.ensembl.org/Help/Faq?id=532

    Denisova.DG
    Altai_Neanderthal.DG
    DenisovaNeanderthalMix.SG
    Chagyrskaya_Neanderthal.SG
    Mezmaiskaya2_Neanderthal.SG
    Vindija.DG
    Goyet_Neanderthal.SG
    LesCottes_Neanderthal.SG
    Spy_Neanderthal.SG
    
    BEB.SG (Bengali from Bangladesh)
    CHS.SG (Southern Han Chinese)
    JPT.SG (Japanese in Tokyo, Japan)
    CEU.SG (Utah Residents with Northern and Western European ancestry)
    FIN.SG (Finnish in Finland)
    IBS.SG (Iberian population in Spain)
    ESN.SG (Esan in Nigeria)
    YRI.SG (Yoruba in Ibadan, Nigera)
    LWK.SG (Luhya in Webuye, Kenya)   

We can now use PLINK to calculate the allele frequencies of all these populations/individuals:

    plink --bfile iNEAL_TLRadapInto_subset --freq --family

Let's now open the output file and look a the frequencies of the alleles of those SNPs in these populations.

To help visualize the results, we're going to do this in Excel.

