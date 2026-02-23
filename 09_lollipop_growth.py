"""
Final Overview: Who Moved and How Much?
----------------------------------------------------------------
PURPOSE: For each EU country, show two things side by side:
  · How much AI adoption GREW (2023 - 2025)  — colored by strategic group
  · How much unemployment CHANGED (2023 -  2025) — grey, positive/negative
"""

from config import *
from matplotlib.lines import Line2D

# ── Compute growth deltas ─────────────────────────────────────────────────────
merged['ai_growth'] = merged['ai25'] - merged['ai23']
merged['un_change'] = merged['un25'] - merged['un23']
df = merged.sort_values('ai_growth', ascending=True) 

n = len(df)
y = np.arange(n)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 10), facecolor=BG,
                                gridspec_kw={'width_ratios': [2, 1]})
fig.canvas.manager.set_window_title("Chart 8 — AI Growth vs Unemployment Change (2023–2025)")
ax1.set_facecolor(BG)
ax2.set_facecolor(BG)

# ── LEFT PANEL: AI adoption growth lollipop ───────────────────────────────────
for i, (_, row) in enumerate(df.iterrows()):
    col = GROUP_COLORS[row['group']]
    ax1.hlines(i, 0, row['ai_growth'], color=col, linewidth=2.5, alpha=0.7)
    ax1.scatter(row['ai_growth'], i, color=col, s=120, zorder=5,
                edgecolors=WHITE, linewidth=1.2)
    ax1.text(row['ai_growth'] + 0.3, i, f"+{row['ai_growth']:.1f}pp",
             va='center', fontsize=7.5, color=col, fontweight='bold')

ax1.axvline(0, color=C2, linewidth=1, alpha=0.4)
ax1.set_yticks(y)
ax1.set_yticklabels(df['COUNTRY'], fontsize=9, fontweight='bold', color=C2)
ax1.set_xlabel('Percentage Points Gained (2023 → 2025)',
               fontweight='bold', color=C2, fontsize=10)
ax1.set_title('AI ADOPTION GROWTH\n(percentage point increase)',
              fontsize=11, fontweight='bold', color=C1, pad=12)
ax1.set_xlim(-1, df['ai_growth'].max() + 5)
ax1.grid(axis='x', linestyle=':', alpha=0.25)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# ── RIGHT PANEL: Unemployment change lollipop (pos = worse, neg = better) ────
for i, (_, row) in enumerate(df.iterrows()):
    change = row['un_change']
    col = '#f87171' if change > 0 else '#4ade80'   # red = rose, green = fell
    ax2.hlines(i, 0, change, color=col, linewidth=2.5, alpha=0.8)
    ax2.scatter(change, i, color=col, s=120, zorder=5,
                edgecolors=WHITE, linewidth=1.2)
    label = f"+{change:.1f}" if change > 0 else f"{change:.1f}"
    ax2.text(change + (0.08 if change >= 0 else -0.08), i, f"{label}pp",
             va='center', ha='left' if change >= 0 else 'right',
             fontsize=7.5, color=col, fontweight='bold')

ax2.axvline(0, color=C2, linewidth=1.5, alpha=0.6)
ax2.set_yticks(y)
ax2.set_yticklabels([])   # shared y-axis with left panel
ax2.set_xlabel('Percentage Points Change (2023 → 2025)',
               fontweight='bold', color=C2, fontsize=10)
ax2.set_title('UNEMPLOYMENT CHANGE\n(▲ rose  ▼ fell)',
              fontsize=11, fontweight='bold', color=C2, pad=12)
ax2.set_xlim(df['un_change'].min() - 0.8, df['un_change'].max() + 1.2)
ax2.grid(axis='x', linestyle=':', alpha=0.25)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

# ── Legend for strategic groups ───────────────────────────────────────────────
patches = [mpatches.Patch(color=GROUP_COLORS[g], label=f'Group {g}: {GROUP_NAMES[g]}')
           for g in ['A', 'B', 'C', 'D']]
patches += [
    mpatches.Patch(color='#4ade80', label='Unemployment fell ▼'),
    mpatches.Patch(color='#f87171', label='Unemployment rose ▲'),
]
fig.legend(handles=patches, loc='lower center', ncol=3, fontsize=9,
           frameon=True, facecolor=WHITE, edgecolor=C2,
           bbox_to_anchor=(0.5, -0.02))

fig.suptitle('AI ADOPTION GROWTH vs UNEMPLOYMENT CHANGE BY COUNTRY (2023–2025)\n'
             'Fast AI growth does not systematically push unemployment in one direction.',
             fontsize=13, fontweight='bold', color=C1, y=1.01)

plt.tight_layout()
plt.subplots_adjust(bottom=0.10, wspace=0.05)
plt.show()
