import pandas as pd

# Load the dataset
df = pd.read_csv('task\\stackoverflow_qa.csv')

# 1. Find all questions that were created before 2014
df['creationdate'] = pd.to_datetime(df['creationdate'])
questions_before_2014 = df[df['creationdate'] < '2014-01-01']
print("Questions created before 2014:")
print(questions_before_2014)

# 2. Find all questions with a score more than 50
questions_score_gt_50 = df[df['score'] > 50]
print("\nQuestions with score more than 50:")
print(questions_score_gt_50)

# 3. Find all questions with a score between 50 and 100
questions_score_50_100 = df[(df['score'] >= 50) & (df['score'] <= 100)]
print("\nQuestions with score between 50 and 100:")
print(questions_score_50_100)

# 4. Find all questions answered by Scott Boston
questions_answered_by_scott = df[df['ans_name'] == 'Scott Boston']
print("\nQuestions answered by Scott Boston:")
print(questions_answered_by_scott)

# 5. Find all questions answered by the following 5 users (e.g., Scott Boston, Mike Pennington, etc.)
users = ['Scott Boston', 'Mike Pennington', 'Jason Strimpel', 'Unutbu', 'yueerhu']
questions_answered_by_users = df[df['ans_name'].isin(users)]
print("\nQuestions answered by specific 5 users:")
print(questions_answered_by_users)

# 6. Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5
questions_march_to_oct_2014 = df[(df['creationdate'] >= '2014-03-01') & (df['creationdate'] <= '2014-10-31')]
questions_unutbu_score_lt_5 = questions_march_to_oct_2014[(questions_march_to_oct_2014['ans_name'] == 'Unutbu') & (questions_march_to_oct_2014['score'] < 5)]
print("\nQuestions answered by Unutbu, created between March and October 2014 with score less than 5:")
print(questions_unutbu_score_lt_5)

# 7. Find all questions that have score between 5 and 10 or have a view count of greater than 10,000
questions_score_5_10_or_view_gt_10000 = df[((df['score'] >= 5) & (df['score'] <= 10)) | (df['viewcount'] > 10000)]
print("\nQuestions with score between 5 and 10 or view count greater than 10,000:")
print(questions_score_5_10_or_view_gt_10000)

# 8. Find all questions that are not answered by Scott Boston
questions_not_answered_by_scott = df[df['ans_name'] != 'Scott Boston']
print("\nQuestions not answered by Scott Boston:")
print(questions_not_answered_by_scott)

