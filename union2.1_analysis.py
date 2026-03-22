import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt



#parameters and constants
H0 = 70
Om = 0.3
Ol = 0.7
c = 299792.458 #km/s

#H(z) in LCDM and matter-only
def H_LCDM(z):
    return H0 * np.sqrt(Om*((1+z)**3)+ Ol)

def H_m(z):
    return H0 * np.sqrt((1+z)**3)

#luminosity-distance function
def D_L(z, H):
    integral, _ = quad(lambda z: 1/H(z), 0, z)
    return (1+z) * c * integral 

#distance modulus
def mu(z, H):
    return (5 * np.log10(D_L(z, H))) + 25


#data
z_val = np.linspace(0.01, 2, 200)
data = np.genfromtxt("C:/Users/Pranav M/Documents/Python Scripts/SCPUnion2.1_mu_vs_z.txt")
z_data = data[:,1] #redshift
mu_data = data[:,2] #distance modulus
mu_err = data[:,3] #uncertainity

mu_LCDM = [mu(z, H_LCDM) for z in z_val]
mu_m = [mu(z, H_m) for z in z_val]

delta_mu = np.array(mu_LCDM) - np.array(mu_m)

#plots
plt.errorbar(z_data, mu_data, yerr=mu_err, fmt='o', markersize=3, alpha=0.6, label='Supernova data')


plt.plot(z_val, mu_LCDM, label='LCDM', color='red', linestyle='--')
plt.plot(z_val, mu_m, label='matter-only', color='blue', linestyle='--')
plt.xlabel('Redshift')
plt.ylabel('Distance modulus')
plt.legend()
plt.grid()



