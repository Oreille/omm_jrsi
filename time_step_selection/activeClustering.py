import os,sys
import scipy as sp
import scipy.linalg as lin
sys.path.append('../utils')
from ioBin import *
from sklearn.cluster import AgglomerativeClustering

def readLogFile(logFile):
  with open(logFile,'r') as f: lines = f.readlines()
  caseName = lines[0][:-1]; print "|  caseName: ", caseName,
  N = int(lines[2]); print " | N = ", N,
  maxK = int(lines[4]); print " | maxK = ", maxK, " | ",
  ev_threshold = float(lines[5]); print "ev_threshold ", ev_threshold, " | ",
  vol = float(lines[6]); print "vol ", vol,
  glob_iter = int(lines[7]); print " | iter = ", glob_iter
  return caseName, N, maxK, ev_threshold, vol, glob_iter

def readPDF(caseName, glob_iter, N, vol):
  if (glob_iter==0):
    th = readLargeBin('../omm/'+caseName+'/simulations/collocation.bin')
    dim = th.shape[1]
    rho = th[:,0]*0. + (1./vol)
    sp.savetxt(caseName+'/pdf_0.txt',rho)
    rho = rho[:N]
  else:
    pdfName = caseName+'/pdf_'+str(glob_iter)+'.txt'
    pdf = sp.loadtxt(pdfName)[:N,:]
    dim = pdf.shape[1]-1
    rho = pdf[:,dim]
  return rho, dim


if (len(sys.argv) != 2):
  sys.exit("Error. There should be ONE argument. Specify the name of your log file.")
logFile = sys.argv[1]

#### Read log file ####
print '-------------------'*5
caseName, N, maxK, ev_threshold, vol, glob_iter = readLogFile(logFile)
print '-------------------'*5
#-----------------------

# PDF at previous iteration
rho, dim = readPDF(caseName, glob_iter, N, vol)


# Load derivatives
print ('Loading the derivatives... ='),;sys.stdout.flush()
fileName = caseName + '/dgdx1.bin'
dgdx = readLargeBin(fileName)[:,:N]
nT = dgdx.shape[0]
DGDX = sp.zeros((nT,N,dim))
DGDX[:,:,0] = dgdx
for d in xrange(dim-1):
  print ('='),;sys.stdout.flush()
  fileName = caseName + '/dgdx' + str(d+2) + '.bin'
  dgdx = readLargeBin(fileName)[:,:N]
  DGDX[:,:,d+1] = dgdx
print ' done.'


trace = sp.zeros((nT,))
E = []
print ('Looping on physical points... '), ;sys.stdout.flush()
for i in xrange(nT):
  if (i%100==0): print ('='),;sys.stdout.flush()
  dfdx = DGDX[i,:,:]
  C = (1./N)*sp.dot(rho*dfdx.T,dfdx)
  lam,ee = lin.eigh(C)
  trace[i] = sp.sum(lam)
  E.append(ee[:,sp.argmax(lam)])
print ' done.'

idx = sp.nonzero(trace >= (trace.max())*ev_threshold)[0]
numAS = len(idx)
print str(numAS) + '/' + str(nT) + ' physical DOFs selected after thresholding.'
maxK = min(maxK,numAS)
X = sp.array(E)[idx,:]
D = 1.-sp.absolute(sp.dot(X,X.T))

print 'Agglomerative Clustering:'
print ' - Initializing Clustering Tree...',
est = AgglomerativeClustering(linkage="complete",affinity='precomputed',compute_full_tree=True,memory='./cache')
print ' done.'

S = []

print ' - Agglomerative Clustering for K = 1 to '+str(maxK)+'...',
for nK in range(1,maxK+1):
  #print nK
  est.set_params(n_clusters = nK)
  est.fit(D)
  labels = est.labels_

  selec = []
  for k in range(nK):
    idk = sp.nonzero(labels==k)[0]
    best_k = idx[idk[sp.argmax(trace[idx[idk]])]]
    selec.append(best_k)
  S.append(selec)

print ' done.'
print 'Write list of clusters...',
f = open(caseName+'/selList_'+str(glob_iter)+'.txt', 'w')
for s in S:
    f.writelines(["%u " % item for item in s])
    f.write("\n")
f.close()
print ' done.\n'
