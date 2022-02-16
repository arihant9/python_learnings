"""
Question_4. If the marks obtained by the student in five different subject is in input through the keyboard, find the aggregate marks and percentage marks obtained by the student. Assume that the maximum marks that can be scored by student in each subject is 100.

"""

marks=[]
sum = 0;
for i in range(0, 5):
 subMark = float(input('Enter the marks '))
 marks.append(subMark)
 sum = sum + subMark

print('Aggregate of marks obtained', sum )
print('Percenatge scored ', sum / 5, " %")   
