#%%
import numpy as np

exp_data = np.load('I_q_IPA_exp.npy')
theory_data = np.load('I_q_IPA_model.npy')

#Seperation of scattering vector and strength into two separate arrays for the experimental data and theoretical data
exp_q = exp_data[:, 0]
exp_Iq = exp_data[:, 1]

theory_q = theory_data[:, 0]
theory_Iq = theory_data[:, 1]

#Interpolation of the theorethical scattering strength into same q values as experimental data
from scipy.interpolate import interp1d

theory_Iq_interp = interp1d(theory_q, theory_Iq)(exp_q)

#Calculating the mean squared error between the experimental data and the scaled theoretical data

def mse(scaling_factor):
    scaled_theory_Iq = scaling_factor * theory_Iq_interp
    return np.mean((exp_Iq - scaled_theory_Iq) ** 2)

from scipy.optimize import minimize_scalar

result = minimize_scalar(mse)
best_scaling_factor = result.x

scaled_theory_Iq = best_scaling_factor * theory_Iq_interp

#plot the values
import matplotlib.pyplot as plt

plt.plot(exp_q, exp_Iq, label='Experimental')
plt.plot(exp_q, scaled_theory_Iq, label='Scaled theoretical')
plt.legend()
plt.show()

