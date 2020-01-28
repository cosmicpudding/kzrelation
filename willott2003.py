import os
import sys
from math import *
from numpy import *
from pylab import *
import pyfits
from matplotlib import rc
rc('font',**{'family':'serif','serif':['serif'],'size':16})
rc('text', usetex=True)
from astropy.io import ascii

# Redshift and k-band magnitude of source
src_x,src_y = 0.42,15.6
src_name = 'PKS 1657-298'

# Plot the relation as conveyed in Willott+2003
z = linspace(0.05,5)
K = 17.37 + 4.53*log10(z) - 0.31*(log10(z))**2.
print (z,K)

# Initialise the figure
figure(figsize=(10,6))

# Plot the source of interest
scatter(src_x,src_y,marker='o',alpha=1,facecolor='red',label=src_name,zorder=102,s=100,edgecolor='k')

d = ascii.read('data/3ckz.txt')
scatter(d['z'],d['Kemcorr'],marker='o',facecolor='',label='3CRR',s=30,edgecolor='k')

d = ascii.read('data/6cekz.txt')
scatter(d['z'],d['Kemcorr'],marker='s',facecolor='k',label='6CE',s=30,edgecolor='k')

d = ascii.read('data/6ckz.txt')
scatter(d['z'],d['Kemcorr'],marker='s',facecolor='',label='6C',s=30,edgecolor='k')

d = ascii.read('data/7ckz.txt')
scatter(d['z'],d['Kemcorr'],marker='^',facecolor='k',label='7C-I/II',s=30,edgecolor='k')

d = ascii.read('data/7ckz2.txt')
scatter(d['z'],d['Kemcorr'],marker='^',facecolor='',label='7C-III',s=30,edgecolor='k')

# Finalise plot
semilogx(z,K,'k-',label='Willott et al. 2003')
errorbar(src_x,src_y,yerr=0.127,fmt=None,linecolor='r')
grid(True,alpha=0.5)
xlim(0,5)
ylim(10,22)
xticks([0.1,1], ['0.1','1.0'])
legend(loc=2,numpoints=1,scatterpoints=1,fontsize=14,ncol=2)
xlabel('Redshift')
ylabel('K-band magnitude')
savefig('kzrelation_%s.pdf' % src_name,bbox_inches='tight')
