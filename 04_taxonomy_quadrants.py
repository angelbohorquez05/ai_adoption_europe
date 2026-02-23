"""
Phase 3: Strategic Classification
PURPOSE: Classify all 27 EU countries into 4 strategic groups
based on their 2025 AI adoption rate and unemployment rate,
using medians as benchmarks.
"""

from config import *

fig, ax = plt.subplots(figsize=(14, 9), facecolor=BG) ##
fig.canvas.manager.set_window_title("Chart 4 — Country Taxonomy: Strategic Quadrants")
ax.set_facecolor(BG)

# ── Quadrant shading ──────────────────────────────────────────────────────────
ax.fill_between([AI25_MED, 50], [UN25_MED, UN25_MED], [16, 16], color=GA, alpha=0.12)  # A green
ax.fill_between([0, AI25_MED],  [UN25_MED, UN25_MED], [16, 16], color=GB, alpha=0.10)  # B amber
ax.fill_between([0, AI25_MED],  [0, 0], [UN25_MED, UN25_MED],   color=GC, alpha=0.09)  # C red
ax.fill_between([AI25_MED, 50], [0, 0], [UN25_MED, UN25_MED],   color=GD, alpha=0.09)  # D dark green

# ── Median reference lines ────────────────────────────────────────────────────
ax.axvline(AI25_MED, color=C2, linewidth=1.5, linestyle='--', alpha=0.5)
ax.axhline(UN25_MED, color=C2, linewidth=1.5, linestyle='--', alpha=0.5)

# ── Quadrant labels ───────────────────────────────────────────────────────────
label_kw = {'fontsize': 9.5, 'fontweight': 'bold'}
ax.text(AI25_MED + 0.8, 15.3, 'GROUP A: TECHNOLOGICAL VANGUARD\nHigh AI · High Unemployment',  color=GA, **label_kw)
ax.text(0.8,            15.3, 'GROUP B: STRUCTURAL LAG\nLow AI · High Unemployment',           color=GB, **label_kw)
ax.text(0.8,            0.5,  'GROUP C: TRADITIONAL RESILIENCE\nLow AI · Low Unemployment',    color=GC, **label_kw)
ax.text(AI25_MED + 0.8, 0.5,  'GROUP D: DIGITAL FRONTIER\nHigh AI · Low Unemployment',        color=GD, **label_kw)

# ── Country scatter points (color = quadrant) ──────────────────puntos de paises
for _, row in merged.iterrows():
    dot_color = GROUP_COLORS[row['group']]
    ax.scatter(row['ai25'], row['un25'], s=160, color=dot_color,
               edgecolors=WHITE, linewidth=1.5, zorder=10, alpha=0.95)
    ax.annotate(row['COUNTRY'], (row['ai25'], row['un25']),
                xytext=(5, 5), textcoords='offset points',
                fontsize=8.5, color=C2, fontweight='bold')

# ── Axis formatting ───────────────────────────────────────────────────────────
ax.set_xlabel('AI Adoption Rate — 2025 (%)',    fontweight='bold', color=C2, fontsize=11, labelpad=10)
ax.set_ylabel('Unemployment Rate — 2025 (%)',   fontweight='bold', color=C2, fontsize=11, labelpad=10)
ax.set_xlim(0, 50);  ax.set_ylim(0, 16)
ax.grid(True, linestyle=':', alpha=0.20)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# ── Legend ────────────────────────────────────────────────────────────────────
patches = [mpatches.Patch(color=GROUP_COLORS[g], label=f'Group {g}: {GROUP_NAMES[g]}')
           for g in ['A', 'B', 'C', 'D']]
ax.legend(handles=patches, loc='lower right', fontsize=9, frameon=True,
          facecolor=WHITE, edgecolor=C2)

fig.suptitle('STRATEGIC TAXONOMY',
             fontsize=14, fontweight='bold', color=C1)

plt.tight_layout()
plt.subplots_adjust(top=0.92)
plt.show()
