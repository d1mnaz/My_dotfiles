#!/usr/bin/python

import os

path = "temp"
os.mkdir(path)
for fich in os.listdir("."):
    if fich[-3:] == "pdf":
        os.system("ps2pdf -dPDFSETTINGS=/ebook %s temp/%s" % (fich, fich))
