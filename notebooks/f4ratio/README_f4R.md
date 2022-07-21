## f4 ratio

Population combination f4(A,O; X,C)/ f4(A,O; B, C) 

We use a population input list in the form:: A 0 : X C:: A 0 : B C

Example:

    Altai_Neanderthal.DG Chimp.REF : French.DG Yoruba.DG :: Altai_Neanderthal.DG Chimp.REF : Vindija.DG Yoruba.DG
    
### 1) Run the test
    
    cd /home/jovyan/notebooks/f4ratio
    qpF4ratio -p f4ratiopops
    
### 2) To understnd the results: https://github.com/DReichLab/AdmixTools/blob/master/README.F4RatioTest

Each result line is: 

    result:   Pop1 (A)  Pop2 (O) Pop3 (X)  Pop4 (C): Pop1 (A)  Pop2 (O) Pop5 (B)  Pop4 (C)  alpha  std. err  Z (null=0)
