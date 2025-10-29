import random

names = ["Alex", "Bob", "Dan", "Sam", "John"]
students_scores = {name:random.randint(45, 100) for name in names}
print(students_scores)

passed_students = {name:score for name, score in students_scores.items() if score >= 60}
print(passed_students)

