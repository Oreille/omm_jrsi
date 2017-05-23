import os,sys
import itertools as ito
import scipy as sp
import scipy.linalg as lin
from sklearn.neighbors import KDTree
from ioBin import *
import multiprocessing


def readLogFile(logFile):
  with open(logFile,'r') as f: lines = f.readlines()
  caseName = lines[0][:-1]; print "\n  caseName: ", caseName,
  nProcs = int(lines[1]); print " | nProcs = ", nProcs, " | ",
  nC = int(lines[2]); print "nC = ", nC, " | ",
  neighbour_regularization = int(lines[3]); print "neighbor_reg = ",neighbour_regularization
  return caseName, nProcs, nC, neighbour_regularization

def collMatrix(u, u0):
  a = 2./(sp.amax(u,0)-sp.amin(u,0))
  b = -(sp.amax(u,0)+sp.amin(u,0))/(sp.amax(u,0)-sp.amin(u,0))
  x = a*u+b; x0 = a*u0 + b # rescaling so that -1 <= x,x0 <= 1
  nx = x.shape[0]
  x = sp.hstack(( sp.ones((nx,1)),x )); x0 = sp.hstack((1.,x0))
  P = sp.zeros((nx, numCol))
  D = sp.zeros((numCol,dim))
  for col, t in enumerate(colList):
    P[:,col] = x[:,t[0]]*x[:,t[1]]
    for d in range(dim):
      if   (t.count(d+1)==0): D[col,d] = 0.
      elif (t.count(d+1)==1): D[col,d] = x0[t[1-t.index(d+1)]]
      elif (t.count(d+1)==2): D[col,d] = 2.*x0[d+1]
  D *= a # Because of the x = a*u+b rescaling
  return P,D

def mp_deriv(it):
  dfdx = sp.zeros((nC,dim))
  n2Err = sp.zeros((nC,))
  for i in range(nC):
    x0 = th[i,:]
    dist,idx = tree.query(x0,k=K)
    idx = sp.reshape(idx,(K,))
    x = th[idx,:]
    y = G[idx,it]
    P,D = collMatrix(x,x0)
    q = lin.lstsq(P,y)[0]
    n2Err[i] = lin.norm(sp.dot(P,q) - y)/lin.norm(y)
    dfdx[i,:] = sp.dot(q,D)
  return (dfdx,n2Err)

if (len(sys.argv) != 2):
  sys.exit("Error. There should be ONE argument. Specify the name of your log file.")
logFile = sys.argv[1]

#### Read log file ####
caseName, nProcs, nC, neighbour_regularization = readLogFile(logFile)
#-----------------------

dirName = '../omm/'+caseName
thName = dirName+'/simulations/collocation.bin'
gName = dirName+'/simulations/data.bin'

th = readLargeBin(thName)[:nC,:]
dim = th.shape[1]
tree = KDTree(th)

G = readLargeBin(gName)[:nC,:]
nT = G.shape[1]

colList = list(ito.combinations_with_replacement(range(dim+1),2))
numCol = len(colList)
K = numCol + neighbour_regularization #  neighbour_regularization should be >=0

if __name__ == "__main__": 
  p = multiprocessing.Pool(nProcs)

print '\n  Computing the derivatives for '+str(nT)+' time steps...',
sys.stdout.flush()
P = p.map(mp_deriv,range(nT))
print ' done.'

output = sp.asarray([p[0] for p in P])
n2Err = sp.asarray([p[1] for p in P])

os.system('mkdir -pv '+caseName)
for d in range(dim):
  fileName = caseName+'/dgdx'+str(d+1)+'.bin'
  print '  Writing to ',fileName
  i = writeLargeBin(fileName,output[:,:,d])

print '\n'
sp.savetxt(caseName+'/mean_fitting_error.txt',sp.mean(n2Err,1))
