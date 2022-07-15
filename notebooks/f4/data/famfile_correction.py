#!/usr/bin/python3
__author__ = 'daniel'

import os

script = open("famfile_correction_bash.R", 'w')
script.write('setwd("')
cwdBIN = os.getcwd()
script.write(cwdBIN)


script.write('")\nwdfiles=list.files(getwd())\nfor(i in wdfiles) {\n  if(grepl(".fam$",i)==TRUE) {\n    cena=read.table(i)\n    if(file.exists(paste0(strsplit(i,".fam"),".ind")) == TRUE) {\n      cenaInd=read.table(paste0(strsplit(i,".fam"),".ind"))\n      if(identical(cenaInd$V1,cena$V2) == TRUE) {\n        if(identical(cena$V1, 1:length(cena$V1)) == TRUE) {\n          cena$V1 = cenaInd$V3\n          if(identical(cena$V1, cenaInd$V3) == TRUE) {write.table(cena, as.character(i), sep=" ",quote=FALSE,col.names=FALSE,row.names=FALSE)}\n        }\n      }\n    }\n  }\n}')
script.close()
os.system("R CMD BATCH famfile_correction_bash.R")
#os.remove("famfile_correction_bash.R")
os.remove("famfile_correction_bash.Rout")