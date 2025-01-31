grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(grades[0])
print(sum(grades[0])/len(grades[0]))
print(grades[1])
print(sum(grades[1])/len(grades[1]))
print(grades[2])
print(sum(grades[2])/len(grades[2]))
print(grades[3])
print(sum(grades[3])/len(grades[3]))
print(grades[4])
print(sum(grades[4])/len(grades[4]))
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(list(students))
students.remove('Bilbo')
print(students)
students.remove('Khendrik')
print(students)
students.remove('Johnny')
print(students)
students.remove('Steve')
print(students)
students = list(students)
print(students)
students.append('Bilbo')
print(students)
students.append('Johnny')
print(students)
students.append('Khendrik')
print(students)
students.append('Steve')
print(students)
grades = [4.0, 2.25, 4.0, 3.66, 4.8]
students = ['Aaron', 'Bilbo', 'Johnny', 'Khendrik', 'Steve']
students_ = dict(zip(students, grades))
print(students_)



