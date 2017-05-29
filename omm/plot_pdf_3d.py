import os,sys
import scipy as sp
import matplotlib.tri as tri
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams
params = {
    'axes.titlesize': 16,
    'axes.labelsize': 16,
    'font.family': 'sans-serif',
    'font.sans-serif': 'Arial',
    'mathtext.default':'regular'
    }
rcParams.update(params)


pdf = sp.loadtxt(sys.argv[1])
dim = pdf.shape[1]-1
s = ((1,1),(1,2),(2,2),(2,2),(2,3),(2,3),(2,4),(2,4))
triang = tri.Triangulation(pdf[:,0],pdf[:,1])

#zmax = 0.5
fig1 = plt.figure(figsize=[13.,6.])
ax = fig1.add_subplot(111, projection='3d')
ax.plot_trisurf(pdf[:,0],pdf[:,1],pdf[:,2],cmap=cm.jet,linewidth=0.1)
ax.view_init(elev=25., azim=300.)
ax.set_title('ESTIMATED PDF')
plt.xlabel('$\\theta_1$');plt.ylabel('$\\theta_2$');ax.set_zlabel('$\\rho$')
#ax.set_zlim(0.,zmax)


fig1.tight_layout(pad=0.1,h_pad=1.0,w_pad=0.)

plt.show()

#fig1.savefig('distribs_log-normal.eps',bbox_inches='tight')
