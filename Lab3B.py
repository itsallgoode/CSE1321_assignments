c1 = int(input("Course 1 hours: "))
g1 = int(input("Grade for course 1: "))
c2 = int(input("Course 2 hours: "))
g2 = int(input("Grade for course 2: "))
c3 = int(input("Course 3 hours: "))
g3 = int(input("Grade for course 3: "))
c4 = int(input("Course 4 hours: "))
g4 = int(input("Grade for course 4: "))
total_hours = c1 + c2 + c3 + c4
total_grades = g1*c1 + g2*c2 + g3*c3 + g4*c4
gpa = round(total_grades / total_hours, 2)
print(f"Total hours: {total_hours}")
print(f"Total quality points: {total_grades}")
print(f"Your GPA for this semester is {gpa}")
