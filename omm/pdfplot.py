import os,sys
import scipy as sp
import matplotlib.pyplot as plt


pdf = sp.loadtxt(sys.argv[1])
dim = pdf.shape[1]-1

s = ((1,1),(1,2),(2,2),(2,2),(2,3),(2,3),(2,4),(2,4))

fig1 = plt.figure(figsize=[10.,6.])

for d in xrange(dim):
  ax = fig1.add_subplot(s[dim-1][0],s[dim-1][1],d+1)
  ax.plot(pdf[:,d],pdf[:,dim],'kh',alpha=.5)

fig1.tight_layout()
plt.show()
