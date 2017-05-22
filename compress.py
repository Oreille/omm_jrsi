import os, sys
import scipy as sp
from ioBin import *


fileName = sys.argv[1]
binFile = fileName[:-3]+'bin'
print binFile
D = sp.loadtxt(fileName)
writeLargeBin(binFile,D)
