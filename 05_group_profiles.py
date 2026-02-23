"""
Phase 3: Within-Group Country Profiles
PURPOSE: Zoom into each strategic group (A, B, C, D) and compare
AI adoption vs unemployment for each country within it.
"""

from config import *
from matplotlib.lines import Line2D

group_order = ['B', 'A', 'C', 'D']

fig, axes = plt.subplots(2, 2, figsize=(16, 14), facecolor=BG) ##
fig.canvas.manager.set_window_title("Chart 5 — Country Profiles by Strategic Group")
fig.patch.set_facecolor(BG)
axes_flat = axes.flatten()

for idx, g in enumerate(group_order):
    ax  = axes_flat[idx]
    ax.set_facecolor(BG)
    col = GROUP_COLORS[g]

    # Filter and sort countries in this group by AI adoption
    gdf = merged[merged['group'] == g].sort_values('ai25', ascending=False)
    x_g = np.arange(len(gdf))

    # ── Grouped bars ────────────────────────────────────────────────##grafico
    ax.bar(x_g - 0.2, gdf['ai25'], 0.38, color=col, alpha=0.85)
    ax.bar(x_g + 0.2, gdf['un25'], 0.38, color=C3,  alpha=0.50)

    # ── Reference lines ───────────────────────────────────────────────────────
    ax.axhline(AI25_MED, color=col, linestyle='--', alpha=0.35, linewidth=1.5)
    ax.axhline(UN25_MED, color=C3,  linestyle='--', alpha=0.45, linewidth=1.5)

    # ── Dynamic y-limit: 55% headroom so title text never touches bars ────────
    max_val = max(gdf['ai25'].max(), gdf['un25'].max())
    ax.set_ylim(0, max_val * 1.55)

    # ── X-axis country labels ─────────────────────────────────────────────────
    ax.set_xticks(x_g)
    ax.set_xticklabels(gdf['COUNTRY'], rotation=45, ha='right',
                       fontsize=9, color=C2)

    # ── Spines and grid ───────────────────────────────────────────────────────
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', linestyle=':', alpha=0.20)

    if idx % 2 == 0:
        ax.set_ylabel('Rate (%)', fontweight='bold', color=C2, fontsize=10)

    ax.text(0.02, 0.99, f'GROUP {g}: {GROUP_NAMES[g].upper()}',
            transform=ax.transAxes,
            fontsize=11, fontweight='bold', color=col,
            va='top', ha='left')

    # ── Stats box top-right ───────────────────────────────────────────────────
    stats = (f"Countries: {len(gdf)}\n"
             f"μ AI:    {gdf['ai25'].mean():.1f}%\n"
             f"μ Unemp: {gdf['un25'].mean():.1f}%")
    ax.text(0.98, 0.99, stats,
            transform=ax.transAxes,
            fontsize=8.5, va='top', ha='right', color=C2, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.45', facecolor=WHITE,
                      edgecolor=C2, alpha=0.85))

    if g == 'B':
        legend_handles = [
            mpatches.Patch(facecolor=WHITE, edgecolor=C2, hatch='////',
                           label='AI Adoption 2025 (%) — color varies by group'),
            mpatches.Patch(facecolor=C3, alpha=0.50, edgecolor=C2,
                           label='Unemployment 2025 (%)'),
            Line2D([0], [0], color=C2, linestyle='--', linewidth=1.5,
                   alpha=0.55, label=f'EU AI Median ({AI25_MED:.1f}%)'),
            Line2D([0], [0], color=C3, linestyle='--', linewidth=1.5,
                   alpha=0.55, label=f'EU Unemployment Median ({UN25_MED:.1f}%)')
        ]
        ax.legend(handles=legend_handles, loc='upper left', fontsize=7,
                  frameon=True, facecolor=WHITE, edgecolor=C2,
                  framealpha=0.95, borderpad=0.5, handlelength=1.2,
                  bbox_to_anchor=(0.02, 0.93)) 

# ── Main title ────────────────────────
fig.suptitle('COUNTRY PROFILES BY STRATEGIC GROUP — AI ADOPTION vs UNEMPLOYMENT (2025)',
             fontsize=14, fontweight='bold', color=C1)

plt.tight_layout()
plt.subplots_adjust(top=0.92, bottom=0.10, hspace=0.45)
plt.show()
