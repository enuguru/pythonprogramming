import csv
import matplotlib.pyplot as plt
import numpy as np

# Read data from CSV to ensure values match the source exactly
csv_path = 'students_bar_chart.csv'
subjects = []
students_2019 = []
students_2020 = []
with open(csv_path, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        subjects.append(row['Subject'])
        students_2019.append(int(row['Students_2019']))
        students_2020.append(int(row['Students_2020']))

x = np.arange(len(subjects))
width = 0.35

fig, ax = plt.subplots(figsize=(6, 4))

# Match colors and style exactly
bars1 = ax.bar(x - width/2, students_2019, width, label='Students in 2019', color='#00bcd4')
bars2 = ax.bar(
    x + width/2,
    students_2020,
    width,
    label='Students in 2020',
    color='white',
    edgecolor='#00bcd4',
    hatch='xx'
)

# Add numbers on top of bars (no decimals)
for bar in bars1:
    height = int(bar.get_height())
    ax.annotate(
        f'{height}',
        xy=(bar.get_x() + bar.get_width() / 2, height),
        xytext=(0, 3),
        textcoords='offset points',
        ha='center',
        va='bottom',
        fontsize=10
    )
for bar in bars2:
    height = int(bar.get_height())
    ax.annotate(
        f'{height}',
        xy=(bar.get_x() + bar.get_width() / 2, height),
        xytext=(0, 3),
        textcoords='offset points',
        ha='center',
        va='bottom',
        fontsize=10
    )

ax.set_ylabel('Number of Students')
ax.set_xticks(x)
ax.set_xticklabels(subjects)
ax.set_ylim(0, 120)
ax.legend()
plt.tight_layout()
plt.savefig('students_bar_chart.png')
plt.close()
print('Bar chart saved as students_bar_chart.png')
