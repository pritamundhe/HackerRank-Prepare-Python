students = [[input(), float(input())] for _ in range(int(input()))]
scores = [student[1] for student in students]

result = sorted([student[0] for student in students if student[1] == sorted(list(set(scores)))[1]])

print(*result, sep='\n')
