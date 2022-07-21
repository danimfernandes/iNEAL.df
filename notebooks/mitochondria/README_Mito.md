## Mitochondria phylogeny

### 1) align the multiple mitochondria sequences with clustal omega

    cd /home/jovyan/notebooks/mitochondria/
    clustalo -i 5humans_9Nea_Den_Allq30.fas  -o 5humans_9Nea_Den_Allq30.aln

### 2) Create a ML tree with the raxml output using 100 Bootstrap replications
See the manual of raxml for the options, but in gerneral the only real importnat ones are: -m (substitution model) / -o (root) and -N (bootsrap value) // different parameteres could lead to other trees

    raxmlHPC  -s 5humans_9Nea_Den_Allq30.aln -n tree-noad-tree -f a -T 6 -m GTRGAMMA -x 5415145 -N 100 -p 874684758 -o Denisova_8

### 3) Visualize the tree copying the output of the file (RAxML_bestTree.tree-noad-tree) into this online tree viewer

    https://itol.embl.de/upload.cgi
