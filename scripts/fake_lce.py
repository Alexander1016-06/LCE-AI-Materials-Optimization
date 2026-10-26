import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
intensity = np.linspace(0.1,1.0,30)
freq = 2.5*intensity + rng.normal(0,0,30)

plt.scatter(intensity,freq)
plt.xlabel("light intensity (W/cm2)")
plt.ylabel("response frequency (Hz)")
plt.savefig("figures/fake_lce_clean.png",dpi = 150)
print("done")