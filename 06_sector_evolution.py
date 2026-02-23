"""
Phase 4: The Sectoral Factor
PURPOSE: Show that AI adoption is not uniform across economic sectors.
"""

from config import *

fig, ax = plt.subplots(figsize=(13, 8), facecolor=BG) ##
fig.canvas.manager.set_window_title("Chart 6 — AI Adoption Evolution by Economic Sector (NACE)")
ax.set_facecolor(BG)

index      = np.arange(len(df_nace))
bar_height = 0.25

# ── Horizontal grouped bars per year  ───────────##
b1 = ax.barh(index - bar_height, df_nace['2023'], bar_height, label='2023', color=C3, alpha=0.85)
b2 = ax.barh(index,              df_nace['2024'], bar_height, label='2024', color=C4, alpha=0.85)
b3 = ax.barh(index + bar_height, df_nace['2025'], bar_height, label='2025', color=C5, alpha=0.90)

# ── Value labels at the end of each bar ──────────────────────────────────────
label_colors = [C3, '#2E595B', '#1A5276']
for rects, lc in zip([b1, b2, b3], label_colors):
    for rect in rects:
        w = rect.get_width()
        ax.text(w + 0.5, rect.get_y() + rect.get_height() / 2,
                f'{w:.1f}%', ha='left', va='center',
                fontsize=7.5, fontweight='bold', color=lc)

# ── Axis formatting ───────────────────────────────────────────────────────────
ax.set_yticks(index)
ax.set_yticklabels(df_nace['NACE'], fontsize=9.5, fontweight='bold', color=C2)
ax.set_xlabel('AI Adoption Rate (%)', fontsize=11, fontweight='bold', color=C2, labelpad=10)
ax.set_ylabel('Economic Sector (NACE Classification)', fontsize=10, fontweight='bold', color=C2, labelpad=15)
ax.set_xlim(0, 80)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='x', linestyle=':', alpha=0.25)
ax.legend(loc='lower right', fontsize=10, frameon=False)

fig.suptitle('AI ADOPTION BY ECONOMIC SECTOR (2023–2025)\n'
             'Digital sectors lead; physical sectors lag.',
             fontsize=13, fontweight='bold', color=C1)

plt.tight_layout(rect=[0.0, 0, 1, 1])
plt.subplots_adjust(left=0.22, top=0.90)
plt.show()
