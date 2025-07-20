import matplotlib.pyplot as plt
import numpy as np

years = np.array([2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019])
boys =   [110, 185, 240, 285, 305, 310, 315, 315]
girls =  [85, 175, 225, 295, 280, 315, 305, 320]

bar_width = 0.35
index = np.arange(len(years))

plt.figure(figsize=(9, 6))
plt.bar(index, boys, bar_width, color='#FFA54F', label='Boys', edgecolor='black')
plt.bar(index + bar_width, girls, bar_width, color='#FFFFB3', label='Girls', edgecolor='black')


plt.xlabel('Year', fontsize=12)
plt.ylab('Number of students', fontsize=12)
plt.title('Chart 5.2.2\nStudents who own a smartphone at Redwood School, by gender, 2012 to 2019', 
          loc='left', fontsize=12, fontweight='bold')
plt.xticks(index + bar_width / 2, years)
plt.yticks(np.arange(0, 351, 50))
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.12), ncol=2)
plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.show()