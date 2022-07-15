#!/usr/bin/python3
__author__ = 'daniel'

import os

script = open("indfile_correction_bash.R", 'w')
script.write('setwd("')
cwdBIN = os.getcwd()
script.write(cwdBIN)


script.write('")\nwdfiles=list.files(getwd())\nfor(i in wdfiles) {\n  if(grepl(".ind$",i)==TRUE) {\n    cena=read.table(i)\n    cena$V3=strsplit(as.character(cena$V1),":")\n    cena$V3=sapply(cena$V3,function(x) x[1])\n    cena$V1=strsplit(as.character(cena$V1),":")\n    cena$V1=sapply(cena$V1,function(x) x[2])\n    if((NA %in% cena$V1) == FALSE) {write.table(cena, as.character(i), sep=" ",quote=FALSE,col.names=FALSE,row.names=FALSE)}\n  }\n}')
script.close()
os.system("R CMD BATCH indfile_correction_bash.R")
os.remove("indfile_correction_bash.R")
os.remove("indfile_correction_bash.Rout")
