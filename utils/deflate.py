import os, sys
import scipy as sp
sys.path.append('../utils')
from ioBin import *


binFile =  sys.argv[1]
asciiFile = binFile[:-3]+'txt'
print '\n deflating ', binFile, ' -> ', asciiFile,'...',; sys.stdout.flush()
D = readLargeBin(binFile)
sp.savetxt(asciiFile,D)
print ' done.'
