"""
Final Overview: Country Trajectories by Strategic Group
PURPOSE: Four scatter plots, one per strategic group (A, B, C, D).
Each country is shown as a trajectory from 2023 - 2024 - 2025:
  · X axis = AI Adoption Rate (%)
  · Y axis = Unemployment Rate (%)
"""

from config import *
from matplotlib.lines import Line2D
import matplotlib.cm as cm

# ── 27 distinct country colors ───────────────────────────────────────────
countries_all = merged['COUNTRY'].tolist()
cmap1 = cm.tab20(np.linspace(0, 1, 20)) ##
cmap2 = cm.Set2(np.linspace(0, 1, 8)) ##
all_colors = list(cmap1) + list(cmap2[:7])
country_colors = {c: all_colors[i] for i, c in enumerate(countries_all)} #diccionario de colores

# ── Figure 2x2 ───────────────────────────────────────────────────────────##
group_order = ['B', 'A', 'C', 'D']

fig, axes = plt.subplots(2, 2, figsize=(20, 16), facecolor=BG) 
fig.canvas.manager.set_window_title("Chart 8 — Scatter Trajectories by Strategic Group")
fig.patch.set_facecolor(BG)
axes_flat = axes.flatten()

for idx, g in enumerate(group_order):
    ax  = axes_flat[idx]
    ax.set_facecolor(BG)
    col = GROUP_COLORS[g]

    # Countries in this group
    gdf = merged[merged['group'] == g]
    countries_g = gdf['COUNTRY'].tolist()

    yr_cols = [('ai23','un23'), ('ai24','un24'), ('ai25','un25')]
    alphas  = [0.30, 0.60, 1.00]

    for country in countries_g:
        row   = gdf[gdf['COUNTRY'] == country].iloc[0]
        ccol  = country_colors[country]

        xs = [row['ai23'], row['ai24'], row['ai25']]
        ys = [row['un23'], row['un24'], row['un25']]

        # Faint connecting line
        ax.plot(xs, ys, color=ccol, linewidth=1.0, alpha=0.35, zorder=2)

        # Dots with increasing opacity per year
        for j, (x, y, a) in enumerate(zip(xs, ys, alphas)):
            size = 80 + j * 40   # dots grow: 80 → 120 → 160
            ax.scatter(x, y, color=ccol, s=size, alpha=a,
                       edgecolors=WHITE, linewidth=1.0, zorder=3 + j)

        # Arrow 2024 - 2025
        ax.annotate('', xy=(xs[2], ys[2]), xytext=(xs[1], ys[1]),
                    arrowprops=dict(arrowstyle='->', color=ccol,
                                    lw=1.5, alpha=0.8))

        # Label at 2025 position
        ax.annotate(country, (xs[2], ys[2]),
                    xytext=(6, 4), textcoords='offset points',
                    fontsize=8.5, color=C2, fontweight='bold', zorder=8)

    # ── Trend line using 2025 positions of this group ─────────────────────────
    x25 = gdf['ai25'].values
    y25 = gdf['un25'].values
    if len(x25) > 1:
        m, b = np.polyfit(x25, y25, 1) ## linea de tendencia 
        x_line = np.linspace(x25.min() - 1, x25.max() + 1, 100)
        ax.plot(x_line, m * x_line + b,
                color=col, linewidth=2, linestyle='--',
                alpha=0.60, zorder=4, label=f'2025 trend  (slope {m:+.2f})')

    # ── EU median crosshairs for reference ────────────────────────────────────
    ax.axvline(AI25_MED, color=C2, linewidth=0.8, linestyle=':', alpha=0.30)
    ax.axhline(UN25_MED, color=C2, linewidth=0.8, linestyle=':', alpha=0.30)

    # ── Axis limits: dynamic per group with padding so dots spread out ────────
    all_x = [row['ai23'] for _, row in gdf.iterrows()] + \
            [row['ai24'] for _, row in gdf.iterrows()] + \
            [row['ai25'] for _, row in gdf.iterrows()]
    all_y = [row['un23'] for _, row in gdf.iterrows()] + \
            [row['un24'] for _, row in gdf.iterrows()] + \
            [row['un25'] for _, row in gdf.iterrows()]
    pad_x = (max(all_x) - min(all_x)) * 0.25
    pad_y = (max(all_y) - min(all_y)) * 0.35
    ax.set_xlim(max(0, min(all_x) - pad_x), max(all_x) + pad_x)
    ax.set_ylim(max(0, min(all_y) - pad_y), max(all_y) + pad_y)

    ax.set_xlabel('AI Adoption Rate (%)',  fontweight='bold', color=C2, fontsize=11)
    ax.set_ylabel('Unemployment Rate (%)', fontweight='bold', color=C2, fontsize=11)
    ax.grid(True, linestyle=':', alpha=0.15)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # ── Panel title ───────────────────────────────────────────────────────────
    ax.text(0.02, 0.99, f'GROUP {g}: {GROUP_NAMES[g].upper()}',
            transform=ax.transAxes, fontsize=11, fontweight='bold',
            color=col, va='top', ha='left')

    ax.legend(loc='lower right', fontsize=8, frameon=True,
              facecolor=WHITE, edgecolor=col, framealpha=0.9)

# ── Shared legend: year opacity guide ─────────────────────────────────────────
year_handles = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='grey',
           markersize=5,  alpha=0.30, label='2023  (faint)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='grey',
           markersize=7,  alpha=0.60, label='2024'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='grey',
           markersize=9,  alpha=1.00, label='2025  (solid)'),
    Line2D([0], [0], color='grey', linewidth=1.5,
           marker='>', markersize=6, label='Direction 2024 → 2025'),
]
fig.legend(handles=year_handles, loc='lower center', ncol=4,
           fontsize=9, frameon=True, facecolor=WHITE, edgecolor=C2,
           bbox_to_anchor=(0.5, -0.02))

fig.suptitle('COUNTRY TRAJECTORIES BY STRATEGIC GROUP',
             fontsize=14, fontweight='bold', color=C1)

plt.tight_layout()
plt.subplots_adjust(top=0.93, bottom=0.08, hspace=0.42, wspace=0.28)
plt.show()
