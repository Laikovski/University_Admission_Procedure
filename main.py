# one, two, three = int(input()), int(input()), int(input())
# mean_score = (one + two + three) / 3
# if mean_score >= 60:
#     print(f'''{mean_score}
# Congratulations, you are accepted!''')
#
# else:
#     print(f'''{mean_score}
# We regret to inform you that we will not be able to offer you admission.''')


# Stage 3/7: Going big
# n, m = int(input()), int(input())
# new_arr = []
# for i in range(n):
#     student = input()
#     student = student.split(' ')
#     num = student.pop()
#     new_arr.append([' '.join(student), float(num)])
#
# def take_second(elem):
#     return elem[1]
# sorted_list = sorted(new_arr, key = take_second, reverse=True)
# print('Successful applicants:')
# for i in range(m):
#     print(sorted_list[i][0])

# Stage 4/7: Choose your path

# number_of_students = int(input())
# # open and read file
# f = open('applicants.txt', "rt")
#
# #create dictionary
# dic_student = []
#
# subjects = {
#     'Biotech': [],
#     'Chemistry': [],
#     'Engineering': [],
#     'Mathematics': [],
#     'Physics': []
# }
# while True:
#     line = f.readline()
#     if not line:
#         break
#     str = line.strip().split(' ')
#     dic_student.append((str[0] + ' ' + str[1], str[2], [str[3], str[4], str[5]]))
#
# # sort student
# temp = sorted(dic_student, key=lambda pga: pga[0])
# new = sorted(temp, key=lambda pga: pga[1], reverse=True)
# rolled = []
# for i in range(3):
#
#     for student in new:
#         if student[2][i] == ' ':
#             continue
#         elif len(subjects[student[2][i]]) < number_of_students:
#             subjects[student[2][i]].append([student[0], student[1]])
#
#             student[2][0] = ' '
#             student[2][1] = ' '
#             student[2][2] = ' '
#
# for item in subjects:
#     x = sorted(subjects[item], key=lambda x: x[1], reverse=True)
#     # print(x)
#     print(item, len(subjects[item]))
#     for student in x:
#         print(f'{student[0]} {student[1]}')
#     print('')

# Stage 5/7: Special knowledge

number_of_students = int(input())
# open and read file
f = open('applicants.txt', "rt")

#create dictionary
dic_student = []

subjects = {
    'Biotech': [],
    'Chemistry': [],
    'Engineering': [],
    'Mathematics': [],
    'Physics': []
}
while True:
    line = f.readline()
    if not line:
        break
    str = line.strip().split(' ')
    dic_student.append((str[0] + ' ' + str[1], str[2], [str[3], str[4], str[5]]))

# sort student
temp = sorted(dic_student, key=lambda pga: pga[0])
new = sorted(temp, key=lambda pga: pga[1], reverse=True)
rolled = []
for i in range(3):

    for student in new:
        if student[2][i] == ' ':
            continue
        elif len(subjects[student[2][i]]) < number_of_students:
            subjects[student[2][i]].append([student[0], student[1]])

            student[2][0] = ' '
            student[2][1] = ' '
            student[2][2] = ' '

for item in subjects:
    x = sorted(subjects[item], key=lambda x: x[1], reverse=True)
    # print(x)
    print(item, len(subjects[item]))
    for student in x:
        print(f'{student[0]} {student[1]}')
    print('')
