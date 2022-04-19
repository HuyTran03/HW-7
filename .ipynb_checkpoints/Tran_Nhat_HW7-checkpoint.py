import numpy as np
from astropy import units as u
import matplotlib.pyplot as plt

data = np.loadtxt('/home/tran.n/AST4930/HW7/sed.txt', delimiter = ',')

wave_dimensionless = np.flip(data[:,0]) #flip data to make it in order this is also the dimensionless array to work with np.where
lum_dimensionless = np.flip(data[:,1]) #does this to both
wave = np.flip(data[:,0] * u.micron) #actual array to do stuff
lum = np.flip(data[:,1] * (u.Lsun/u.micron))

#finds the indices where 100<wavelength<1000
indices = np.where((wave_dimensionless >= 10) & (wave_dimensionless <= 1000))[0]

#returning an array of values base on indices indicated
x = np.take(wave,indices)
y = np.take(lum, indices)

#finding the area under the curve
area = np.trapz(y,x)
print(area) 

plt.plot(wave.value,lum.value) #plotting the values
plt.title('Black Body Spectra Graph') #title of graph
plt.yscale('log') #scaling the graphs
plt.xscale('log')
plt.xlim([1e-1,1e3]) #limiting the x-axis to make the graph looks nice
plt.fill_between(x.value,y.value)
plt.xlabel('Wavelength ($\mu$m)')
plt.ylabel('Specific Luminosity (Lsun/$\mu$m)')
plt.savefig('Blackbodyspectra.png')