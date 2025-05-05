import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)


df1['Average'] = df1[['Math', 'English', 'Science']].mean(axis=1)


highest_avg_student = df1.loc[df1['Average'].idxmax()]


df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)


df1[['Math', 'English', 'Science']].mean().plot(kind='bar', title="Average Grades in Each Subject")

