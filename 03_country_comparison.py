"""
Phase 2: Country-Level View
PURPOSE: Display AI adoption rates and unemployment rates side by side
for all 27 EU member states, sorted by AI adoption in 2025.
"""

from config import *

# ── Sort countries by AI adoption (2025)──────────────
df_ia_s  = df_ia.dropna(subset=YEARS).sort_values('2025', ascending=False)
df_emp_s = (df_emp.set_index('COUNTRY')
                  .reindex(df_ia_s['COUNTRY'])
                  .reset_index()
                  .dropna(subset=YEARS))
df_ia_s  = df_ia_s[df_ia_s['COUNTRY'].isin(df_emp_s['COUNTRY'])]

x     = np.arange(len(df_ia_s))
width = 0.25

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 12), facecolor=BG)##se crean dos paneles
fig.canvas.manager.set_window_title("Chart 3 — Country Comparison: AI Adoption & Unemployment")

for ax in (ax1, ax2):
    ax.set_facecolor(BG)

# ── Top panel: Enterprise AI adoption by country ────────────────────────────── ##
ax1.bar(x - width, df_ia_s['2023'], width, label='2023', color=C3, alpha=0.85)
ax1.bar(x,         df_ia_s['2024'], width, label='2024', color=C4, alpha=0.85)
ax1.bar(x + width, df_ia_s['2025'], width, label='2025', color=C5, alpha=0.85)

ax1.set_xticks(x)
ax1.set_xticklabels(df_ia_s['COUNTRY'], rotation=45, ha='right', fontsize=9)
ax1.set_ylabel('% of Enterprises Using AI', fontsize=10, fontweight='bold', color=C2)
ax1.legend(title='Year', fontsize=9, frameon=False)
ax1.grid(axis='y', linestyle='--', alpha=0.25)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# ── Bottom panel: Unemployment rate by country ──────────────────────────────── ##
ax2.bar(x - width, df_emp_s['2023'], width, label='2023', color=C3, alpha=0.85)
ax2.bar(x,         df_emp_s['2024'], width, label='2024', color=C4, alpha=0.85)
ax2.bar(x + width, df_emp_s['2025'], width, label='2025', color=C5, alpha=0.85)

ax2.set_title('UNEMPLOYMENT RATE BY COUNTRY',
              fontsize=13, fontweight='bold', color=C1, pad=12)
ax2.set_xticks(x)
ax2.set_xticklabels(df_ia_s['COUNTRY'], rotation=45, ha='right', fontsize=9)
ax2.set_ylabel('Unemployment Rate (%)', fontsize=10, fontweight='bold', color=C2)
ax2.legend(title='Year', fontsize=9, frameon=False)
ax2.grid(axis='y', linestyle='--', alpha=0.25)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

fig.suptitle('ENTERPRISES USING IA BY COUNTRY',
             fontsize=15, fontweight='bold', color=C1)

plt.tight_layout()
plt.subplots_adjust(top=0.93)
plt.show()
