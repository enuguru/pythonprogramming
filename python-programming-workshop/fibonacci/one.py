import matplotlib.pyplot as plt
import numpy as np

# Data from the chart
years = np.array([2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019])
boys =   [110, 185, 240, 285, 305, 315, 320, 320]
girls =  [90, 175, 225, 295, 275, 320, 310, 325]

bar_width = 0.35
x = np.arange(len(years))

plt.figure(figsize=(10, 6))

# Bars for boys and girls
plt.bar(x - bar_width/2, boys, width=bar_width, color='#FFA54F', label='Boys', edgecolor='black')
plt.bar(x + bar_width/2, girls, width=bar_width, color='#FFFFB9', label='Girls', edgecolor='black')

# Titles and labels
plt.title('Chart 5.2.2\nStudents who own a smartphone at Redwood School, by gender, 2012 to 2019', loc='left', fontsize=12, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Number of students')
plt.xticks(x, years)
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.08), ncol=2)

plt.ylim(0, 350)
plt.tight_layout()