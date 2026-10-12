import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

print("Python    :", sys.version.split()[0])
print("numpy     :", np.__version__)
print("pandas    :", pd.__version__)
print("matplotlib:", matplotlib.__version__)

x = np.linspace(0, 2*np.pi, 200)
plt.figure(figsize=(6,3))
plt.plot(x, np.sin(x))
plt.title("env check: sin(x)")
plt.savefig("figures/env_check.png", dpi=300)
print("figure saved -> figuers/env_check.png")