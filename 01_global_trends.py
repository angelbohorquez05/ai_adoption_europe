"""
Phase 1: The European Paradox
PURPOSE: Show the divergence between AI adoption
and overall unemployment at the EU-27 level.
This "paradox" is the central question of the entire study.
"""

from config import *

fig, ax1 = plt.subplots(figsize=(10, 6), facecolor=BG)
fig.canvas.manager.set_window_title("Chart 1 — Global Trends: AI vs Unemployment")
ax1.set_facecolor(BG)

# ── Left axis: AI adoption ─────────────────────────
ax1.fill_between(YEARS, ai_eu, color=C4, alpha=0.20)
ax1.plot(YEARS, ai_eu,
         color=C4, marker='o', linewidth=3, markersize=13,
         markeredgecolor=C1, markeredgewidth=2,
         label='AI Adoption — % of Enterprises', zorder=5) ##

for i, v in enumerate(ai_eu):
    ax1.annotate(f'{v}%', (YEARS[i], v),
                 xytext=(0, 14), textcoords='offset points',
                 ha='center', fontweight='bold', color=C4, fontsize=11)

# ── Right axis: Unemployment rate ────────────────────────
ax2 = ax1.twinx() ##
ax2.fill_between(YEARS, un_eu, color=C3, alpha=0.12)
ax2.plot(YEARS, un_eu,
         color=C3, marker='s', linewidth=3, markersize=13,
         markerfacecolor=WHITE, markeredgecolor=C3, markeredgewidth=2.5,
         linestyle='--', label='Unemployment Rate (%)', zorder=5) ##

for i, v in enumerate(un_eu):
    ax2.annotate(f'{v}%', (YEARS[i], v),
                 xytext=(0, -22), textcoords='offset points',
                 ha='center', fontweight='bold', color=C3, fontsize=11)

# ── Axis formatting ───────────────────────────────────────────────────────────
ax1.set_ylim(0, 30);   ax2.set_ylim(4.5, 8)
ax1.set_ylabel('AI Adoption — % of Enterprises', fontweight='bold', color=C4, fontsize=11)
ax2.set_ylabel('Unemployment Rate (%)',           fontweight='bold', color=C3, fontsize=11)
ax1.set_xlabel('Year', fontweight='bold', color=C2, fontsize=11)
ax1.tick_params(axis='y', colors=C4)
ax2.tick_params(axis='y', colors=C3)
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)

# ── Legend combining both axes ────────────────────────────────────────────────
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2,
           loc='upper left', frameon=True, facecolor=WHITE, fontsize=10)

fig.suptitle('THE EUROPEAN PARADOX: AI RISES, UNEMPLOYMENT HOLDS STEADY (2023–2025)',
             fontsize=13, fontweight='bold', color=C1)

plt.tight_layout()
plt.subplots_adjust(top=0.90)
plt.show()
