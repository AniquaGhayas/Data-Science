import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 2, figsize = (12, 5))
fig.suptitle("Statistical Distributions", fontsize=16, fontweight='bold')

#=================================================================================
#1. Normal distribution
#=================================================================================

x = np.linspace(-5, 5, 300)
for mu, sigma, color, label in [
    (0, 1, 'blue', '\u03BC = 0, \u03C3 = 1'),
    (0, 2, 'red', '\u03BC = 0, \u03C3 = 2'),
    (2, 1, 'green', '\u03BC = 2, \u03C3 = 1')
]:
    axes[0].plot(
        x, 
        stats.norm.pdf(x, mu, sigma),
        color = color,
        linewidth = 2,
        label = label
    )
axes[0].set_title("Normal Distribution")
axes[0].legend()
axes[0].grid(True)

#=================================================================================
#2. Binomial Distribution
#=================================================================================

k = np.arange(0, 21)

for n, p, color, label in [
    (20, 0.5, 'blue', 'n = 20, p = 0.5'),
    (20, 0.3, 'red', 'n = 20, p = 0.3'),
    (20, 0.7, 'green', 'n = 20, p = 0.7')
]:
    axes[1].bar(
        k,
        stats.binom.pmf(k, n, p),
        alpha = 0.5,
        color = color,
        label = label,
        width = 0.3
    )
axes[1].set_title("Binomial Distribution")
axes[1].legend()
axes[1].grid(True)

plt.tight_layout
plt.show()