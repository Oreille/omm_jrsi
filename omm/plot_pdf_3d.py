import os,sys
import scipy as sp
import matplotlib.tri as tri
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams
params = {'backend': 'ps',
      'font.family':'serif',
      'font.serif':'Computer Modern Roman',
          'axes.labelsize': 18,
          'text.fontsize': 10,
          'legend.fontsize': 14,
          'xtick.labelsize': 16,
          'ytick.labelsize': 16,
          'lines.markersize':5,
          'text.usetex': True,
    }
rcParams.update(params)
caseName = 'normal'
#pdf = sp.loadtxt('/home/ROCQ/reo/etixier/Dev/remote/results/'+caseName+'/pdf.txt')
pdf = sp.loadtxt(sys.argv[1])
dim = pdf.shape[1]-1

s = ((1,1),(1,2),(2,2),(2,2),(2,3),(2,3),(2,4),(2,4))


triang = tri.Triangulation(pdf[:,0],pdf[:,1])



zmax = 0.5


fig1 = plt.figure(figsize=[13.,6.])

ax = fig1.add_subplot(111, projection='3d')
ax.plot_trisurf(pdf[:,0],pdf[:,1],pdf[:,2],cmap=cm.jet,linewidth=0.1)
ax.view_init(elev=25., azim=300.)
te=ax.text(2.5, 3.5, .7*sp.amax(pdf[:,2]), 'ESTIMATED PDF', None,fontsize=16,family='sans-serif',weight='heavy')
te.set_bbox(dict(facecolor='white',boxstyle='round',pad=0.5,edgecolor=[.1,.1,.8]))
plt.xlabel('$\\theta_1$');plt.ylabel('$\\theta_2$');ax.set_zlabel('$\\rho$')
ax.set_zlim(0.,zmax)

# Z = sp.loadtxt(sys.argv[2])
# ax2 = fig1.add_subplot(121, projection='3d')
# ax2.plot_trisurf(pdf[:,0],pdf[:,1],Z,cmap=cm.jet,linewidth=.1)
# ax2.view_init(elev=25., azim=300.)
# te2=ax2.text(2.5, 3.5, .7*sp.amax(pdf[:,2]), 'TRUE PDF', None,fontsize=16,family='sans-serif',weight='heavy')
# te2.set_bbox(dict(facecolor='white',boxstyle='round',pad=0.5,edgecolor=[.1,.1,.8]))
# plt.xlabel('$\\theta_1$');plt.ylabel('$\\theta_2$');ax.set_zlabel('$\\rho$')
# ax2.set_zlim(0.,zmax)


fig1.tight_layout(pad=0.1,h_pad=1.0,w_pad=0.)
#fig1.subplots_adjust(bottom=.07)
plt.show()

fig1.savefig('distribs_log-normal.eps',bbox_inches='tight')
