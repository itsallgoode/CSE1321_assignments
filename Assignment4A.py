
def avg_value(category, *grades):
    valid_grades = [grade for grade in grades if grade != -1.0]

    if category == "labs":
        average = sum(valid_grades) / 12
    elif category == "assignments":
        average = sum(valid_grades[:7]) / 7
    elif category == "midterm":
        average = valid_grades[0]
    elif category == "exam":
        average = valid_grades[0]
    return average

def weight(average, weight):
    return average * weight

def main():

    print("[CSE 1321L Grade Calculator]")
    lab_grades = []
    print("Labs")

    for i in range(1, 13):
        grade = float(input(f"Enter Grade #{i}: "))
        lab_grades.append(grade)

    lab_avg = avg_value("labs", *lab_grades)
    lab_weight = weight(lab_avg, 0.10)
    print(f"Weighed Points: {lab_weight:.2f}")

    print()
    print("Assignments")
    assignment_grades = []

    for i in range(1, 8):
        grade = float(input(f"Enter Grade #{i}: "))
        assignment_grades.append(grade)

    assignment_avg = avg_value("assignments", *assignment_grades)
    assignment_weight = weight(assignment_avg, 0.40)    
    print(f"Weighed Points {assignment_weight:.2f}")

    print()
    print("Midterm")
    
    midterm_grade = float(input("Enter Grade #1: "))
    midterm_avg = avg_value("midterm", midterm_grade)
    midterm_weight = weight(midterm_avg, 0.20)
    print(f"Weighed Points: {midterm_weight:.2f}")

    print()
    print("Exam")

    exam_grade = float(input("Enter Grade #1: "))
    exam_avg = avg_value("exam", exam_grade)
    exam_weight = weight(exam_avg, 0.30)
    print(f"Weighed Points: {exam_weight:.2f}")

    final_grade = lab_weight + assignment_weight + midterm_weight + exam_weight
    print()
    print(f"Your final grade for CSE1321L is: {final_grade:.2f}")



if __name__ == "__main__":
    main()

    




