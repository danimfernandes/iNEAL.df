# Practical Training Session II #
# Adaptive Introgression in Modern and Archaic Humans #

We will show how to detect an example fragment in modern human data that also shows a signature of positive selection. We will compare the state of specific archaic-like SNPs in archaic and modern genomes.

# Isolate wanted SNPs #

The dataset we are giving you ("iNEAL_TLRadapInto") includes plenty more SNPs that are not of interest for what we want investigate.

So first, to expedite the analysis, we should isolate the SNPs we want to look at in the TLR cluster from this large dataset. These are the SNP IDs:

    rs11466640
    rs5743563
    rs5743560
    rs11725779

We now need to create a new text file and add this information to it.

Now, we can use the following command with the software PLINK to reduce our huge dataset into only these SNPs:

    plink --bfile iNEAL_TLRadapInto --extract extract_SNPsTLR --make-bed --out iNEAL_TLRadapInto_subset

The dataset provided comes with the following populations/individuals. Modern population codes are listed here, but described below nevertheless:
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
    Karitiana.SDG (Western Amazonian, Brazil)
    Papuan.SDG (Indonesia and Papua New Guinea)

# Calculate Allele Frequencies #

We can now use PLINK to calculate the allele frequencies of the 4 SNPs we isolated, in all these populations/individuals:

    plink --bfile iNEAL_TLRadapInto_subset --freq --family

Let's now open the output file and understand what each column means:

    CHR          SNP     CLST                           A1   A2      MAF    MAC  NCHROBS
    4       rs11466640   Altai_Neanderthal.DG           A    G        1      2        2 
    4       rs11466640   BEB.SG                         A    G   0.1744     30      172 
    4       rs11466640   CEU.SG                         A    G   0.1616     32      198 
    4       rs11466640   Chagyrskaya_Neanderthal.SG     A    G        1      2        2 
    (...)

Now, to help visualize and interpret the results, we're going to move our data into Excel.
