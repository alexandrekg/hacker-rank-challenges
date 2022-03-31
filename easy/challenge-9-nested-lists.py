if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        if score not in scores:
            scores.append(score)

        students.append({'name': name, 'score': score})

    second_lowest_score = sorted(scores)[1]
    students_with_second_lowest_score = [student for student in students if student['score'] == second_lowest_score]

    lowest_score_students = sorted(students_with_second_lowest_score, key=lambda d: d['name'])

    for student in lowest_score_students:
        print(student['name'])
