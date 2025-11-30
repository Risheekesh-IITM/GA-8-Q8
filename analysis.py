import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
satisfaction_scores = [-2.02, 3.22, 7.61, 3.23]
industry_target = 4.5
average_score = np.mean(satisfaction_scores)

# Create the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(quarters, satisfaction_scores, color='skyblue', label='Quarterly Score')

# Add a line for the industry target
plt.axhline(y=industry_target, color='r', linestyle='--', label=f'Industry Target ({industry_target})')

# Add a line for the average score
plt.axhline(y=average_score, color='g', linestyle='-', label=f'Average Score ({average_score:.2f})')

# Add labels and title
plt.xlabel('Quarter')
plt.ylabel('Patient Satisfaction Score')
plt.title('Quarterly Patient Satisfaction Scores vs. Industry Target')
plt.legend()

# Add data labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:.2f}', va='bottom' if yval >= 0 else 'top')

# Save the chart
plt.savefig('patient_satisfaction_chart.png')

print(f"Average Patient Satisfaction Score: {average_score:.2f}")
print("Chart saved as patient_satisfaction_chart.png")
