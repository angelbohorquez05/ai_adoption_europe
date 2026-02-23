"""
Phase 2: Dispersion Analysis
PURPOSE: Show that "Europe" is not a single block. The boxplot reveals
the growing inequality in AI adoption between member states (2023–2025).
"""

from config import *

fig, ax = plt.subplots(figsize=(10, 7), facecolor=BG)
fig.canvas.manager.set_window_title("Chart 2 — AI Adoption Dispersion Across EU Countries")
ax.set_facecolor(BG)

data_to_plot = [df_ia['2023'].dropna(), df_ia['2024'].dropna(), df_ia['2025'].dropna()]

# ── Boxplot  ────────────
box = ax.boxplot(data_to_plot, labels=YEARS, patch_artist=True,
                 notch=False, showfliers=False) ##

for patch, color in zip(box['boxes'], YEAR_COLORS):
    patch.set_facecolor(color)
    patch.set_alpha(0.50)
    patch.set_edgecolor(C2)
    patch.set_linewidth(2)

for median in box['medians']:
    median.set(color=C1, linewidth=3) 

for whisker in box['whiskers']:
    whisker.set(color=C2, linewidth=1.5, linestyle='--')

for cap in box['caps']:
    cap.set(color=C2, linewidth=2)

# ── Jitter points: one dot per EU country ────────────────────────────────────
for i, (col, color) in enumerate(zip(YEARS, YEAR_COLORS)):
    y = df_ia[col].dropna()
    x = np.random.normal(i + 1, 0.04, size=len(y))
    ax.scatter(x, y, alpha=0.85, color=WHITE, edgecolor=color,
               linewidth=1.5, s=50, zorder=3) ##

# ── Axis formatting ───────────────────────────────────────────────────────────
ax.set_ylabel('AI Adoption Rate (%)', fontsize=11, fontweight='bold', color=C2)
ax.set_xlabel('Reference Year',       fontsize=11, fontweight='bold', color=C2)
ax.grid(axis='y', linestyle='--', alpha=0.2, color=C3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.suptitle('AI ADOPTION DISPERSION ACROSS EU (2023–2025)\n'
             'Each dot = one EU member state. Wider box = greater inequality.',
             fontsize=13, fontweight='bold', color=C1)

plt.tight_layout()
plt.subplots_adjust(top=0.88)
plt.show()
