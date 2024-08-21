marksDict = {'subject': ['Physics', 'Chemistry', 'Maths'], 'marks' : [40, 78, 82]}

subjects = marksDict['subject']
marks = marksDict['marks']

sum = 0
avg = 0

for i in range(len(marks)):
    sum += marks[i]
avg = sum/3

maxMarks = max(marks)
maxindex = marks.index(maxMarks)
subjectWithMaxMarks = subjects[maxindex]

print(f"The average of marks is: {avg}")
print(f"Aliza got highest marks in: {subjectWithMaxMarks}")
