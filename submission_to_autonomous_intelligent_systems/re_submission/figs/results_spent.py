"""Create RMSE comparison figure for SPENT vs KF
Saves output to: figs/spent_rmse.pdf
"""
import matplotlib.pyplot as plt
import numpy as np

# Data from Table 1 in MOT_ML.tex
labels = ["Training\n562 tracks", "Validation\n31 tracks", "Test\n31 tracks"]
spent = np.array([0.025, 0.027, 0.029])
kf = np.array([0.066, 0.065, 0.066])

x = np.arange(len(labels))
width = 0.35

plt.style.use('seaborn-v0_8-darkgrid')
# Double font sizes because figure will be small when embedded
plt.rcParams.update({'font.size': 16})
fig, ax = plt.subplots(figsize=(6, 3.5))

# Main chart (bars: KF first)
rects_kf = ax.bar(x - width/2, kf, width, label='KF', color='#5797be')
rects_spent = ax.bar(x + width/2, spent, width, label='SPENT', color='#2b8f8d')

# Labels (no title)
ax.set_ylabel('RMSE', fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=16)
# Move legend slightly down using bbox_to_anchor (axes fraction coordinates)
ax.legend(loc='upper right', bbox_to_anchor=(1, 0.9), fontsize=16, frameon=True, edgecolor='black', facecolor='white', framealpha=1.0)

# Annotate bars with values
for rect in list(rects_kf) + list(rects_spent):
    height = rect.get_height()
    ax.annotate(f'{height:.3f}',
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 6),  # 6 points vertical offset (larger font)
                textcoords="offset points",
                ha='center', va='bottom', fontsize=16)

fig.tight_layout()
import pathlib
outpath = pathlib.Path(__file__).resolve().parent / 'spent_rmse.pdf'
fig.savefig(outpath, bbox_inches='tight')
print(f'Saved RMSE figure to: {outpath}')
