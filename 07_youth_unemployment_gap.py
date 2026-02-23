"""
Phase 4: The Generational Factor
PURPOSE: Show the persistent structural gap between youth (<25) and adult
(25-74) unemployment in the EU-27 from 2023 to 2025.
"""

from config import *

# ── Extract EU-27 youth and adult unemployment rates ─────────────────────────
youth = df_age_eu[df_age_eu['AGE'].str.contains('Less')][YEARS].values[0].astype(float)
adult = df_age_eu[df_age_eu['AGE'].str.contains('From')][YEARS].values[0].astype(float)

fig, ax = plt.subplots(figsize=(12, 7), facecolor=BG) ##
fig.canvas.manager.set_window_title("Chart 7 — Youth vs Adult Unemployment Gap (EU-27)")
ax.set_facecolor(BG)

# ── Lines for youth and adult unemployment ──────────────────────────────##lineas
ax.plot(YEARS, youth, color='#1ABC9C', marker='o', linewidth=3,
        label='Youth (<25 years)', zorder=3)
ax.plot(YEARS, adult, color=C2,       marker='s', linewidth=3,
        label='Adult (25–74 years)', zorder=3)

# ── Shaded generational gap ───────────────────────────────────────────────────
ax.fill_between(YEARS, adult, youth, color='#1ABC9C', alpha=0.12, label='Generational Gap')

# ── Value labels on each point ────────────────────────────────────────────────
for i, v in enumerate(youth):
    ax.annotate(f'{v}%', (YEARS[i], youth[i]),
                xytext=(0, 12), textcoords='offset points',
                ha='center', fontweight='bold', color='#16A085', fontsize=10)

for i, v in enumerate(adult):
    ax.annotate(f'{v}%', (YEARS[i], adult[i]),
                xytext=(0, -18), textcoords='offset points',
                ha='center', fontweight='bold', color=C2, fontsize=10)

# ── Axis formatting ───────────────────────────────────────────────────────────
ax.set_ylabel('Unemployment Rate (%)', fontweight='bold', color=C2, fontsize=11)
ax.set_xlabel('Year',                  fontweight='bold', color=C2, fontsize=11)
ax.set_ylim(0, 18)
ax.grid(axis='y', linestyle='--', alpha=0.25)
ax.legend(loc='center left', fontsize=10, frameon=True, facecolor=WHITE,
          edgecolor=C2, borderpad=1)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.suptitle('YOUTH vs ADULT UNEMPLOYMENT\n'
             'Youth unemployment is ~3× higher and the gap shows no sign of closing.',
             fontsize=13, fontweight='bold', color=C1)

plt.tight_layout()
plt.subplots_adjust(top=0.88)
plt.show()
