"""
Dictionary Comprehension Examples
---------------------------------
This script demonstrates various levels of dictionary comprehension,
from basic to advanced, with explanatory docstrings and comments.
"""

import random
# ----------------------------------------
# BASIC: Create a dictionary from two lists using comprehension
# ----------------------------------------
names = ["Alex", "Bob", "Dan", "Sam", "John"]

# Randomly assign a score between 45 and 100 for each student
students_scores = {name: random.randint(45, 100) for name in names}
print("All students' scores:")
print(students_scores)

# ----------------------------------------
# INTERMEDIATE: Filter items with a condition
# ----------------------------------------
# Keep only students who scored 60 or above
passed_students = {name: score for name, score in students_scores.items() if score >= 60}
print("\nStudents who passed (score >= 60):")
print(passed_students)

# ----------------------------------------
# INTERMEDIATE+: Transforming values
# ----------------------------------------
# Convert scores to letter grades using comprehension
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

students_grades = {name: get_grade(score) for name, score in students_scores.items()}
print("\nStudents with letter grades:")
print(students_grades)

# ----------------------------------------
# ADVANCED: Nested dictionary comprehension
# ----------------------------------------
# Suppose we have subjects and want to assign random scores to each student per subject
subjects = ["Math", "Science", "History"]

"""
Nested comprehension:
Outer loop → iterate through students
Inner loop → iterate through subjects
Creates: {student: {subject: random_score}}
"""
student_report = {
    name: {subject: random.randint(45, 100) for subject in subjects}
    for name in names
}
print("\nNested dictionary comprehension (student reports):")
print(student_report)

# ----------------------------------------
# ADVANCED+: Conditional logic and transformation inside comprehension
# ----------------------------------------
"""
We can include conditional logic and transformations directly.
Example: create a dictionary showing each student's average score,
rounded to 2 decimal places, and only include if average >= 60.
"""
average_scores = {
    name: round(sum(subjects_scores.values()) / len(subjects_scores), 2)
    for name, subjects_scores in student_report.items()
    if sum(subjects_scores.values()) / len(subjects_scores) >= 60
}
print("\nAverage scores (students with avg >= 60):")
print(average_scores)

# ----------------------------------------
# EXPERT: Inverting keys and values safely
# ----------------------------------------
"""
If we want to invert a dictionary where multiple students may have the same score,
we can group them using a comprehension with setdefault().
"""

# Example: invert {name: score} into {score: [names]}
inverted_scores = {}
for name, score in students_scores.items():
    inverted_scores.setdefault(score, []).append(name)

print("\nInverted dictionary (score → list of students):")
print(inverted_scores)

# ----------------------------------------
# EXPERT+: Dictionary comprehension with enumeration
# ----------------------------------------
"""
Sometimes we need both an index and a value.
Using enumerate(), we can build indexed dictionaries quickly.
"""
indexed_names = {index + 1: name for index, name in enumerate(names)}
print("\nIndexed student names:")
print(indexed_names)
