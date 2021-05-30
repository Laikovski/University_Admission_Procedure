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
import math
# number of students that can be accepted into each department
# N = int(input())
#
# departments = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}
# not_sorted_applicants = {}
#
# file = open('applicants.txt', encoding='utf-8')
# not_sorted_applicants = [line.rstrip('\n').split() for line in file]
# file.close()
#
# # applicant input
# # first name, last name, physics exam, chemistry exam, math exam, cs exam, first priority, second pr, third pr
#
# # sorting applicants by exam result, first name, last name
# physics_applicants = sorted(not_sorted_applicants, key=lambda x: (-int(x[2]), x[0], x[1]))
# chemistry_applicants = sorted(not_sorted_applicants, key=lambda x: (-int(x[3]), x[0], x[1]))
# math_applicants = sorted(not_sorted_applicants, key=lambda x: (-int(x[4]), x[0], x[1]))
# cs_applicants = sorted(not_sorted_applicants, key=lambda x: (-int(x[5]), x[0], x[1]))
#
# # copying full list of applicants
# not_accepted_applicants = physics_applicants[:]
#
#
# # enrolling students into each department by wave
# def applicants_waves(wave):
#     global departments
#     global not_accepted_applicants
#     for depart, students_list in departments.items():
#         if depart == 'Biotech' or depart == 'Chemistry':
#             subject_list = chemistry_applicants
#         elif depart == 'Engineering':
#             subject_list = cs_applicants
#         elif depart == 'Mathematics':
#             subject_list = math_applicants
#         else:
#             subject_list = physics_applicants
#
#         for student in subject_list:
#             if student[wave] == depart:
#                 if len(students_list) < N:
#                     students_list.append(student)
#                     not_accepted_applicants.remove(student)
#
#
# for i in range(6, 9):
#     applicants_waves(i)
#
#     # updating each list after every wave
#     physics_applicants = sorted(not_accepted_applicants, key=lambda x: (-int(x[2]), x[0], x[1]))
#     chemistry_applicants = sorted(not_accepted_applicants, key=lambda x: (-int(x[3]), x[0], x[1]))
#     math_applicants = sorted(not_accepted_applicants, key=lambda x: (-int(x[4]), x[0], x[1]))
#     cs_applicants = sorted(not_accepted_applicants, key=lambda x: (-int(x[5]), x[0], x[1]))
#
#
# for dep, students in departments.items():
#     print("\n" + dep)
#     if dep == 'Biotech':
#         sorted_students = sorted(students, key=lambda x: (-int(x[3]), x[0], x[1]))
#         for st in sorted_students:
#             print(st[0], st[1], st[3])
#     elif dep == 'Chemistry':
#         sorted_students = sorted(students, key=lambda x: (-int(x[3]), x[0], x[1]))
#         for st in sorted_students:
#             print(st[0], st[1], st[3])
#     elif dep == 'Engineering':
#         sorted_students = sorted(students, key=lambda x: (-int(x[5]), x[0], x[1]))
#         for st in sorted_students:
#             print(st[0], st[1], st[5])
#     elif dep == 'Mathematics':
#         sorted_students = sorted(students, key=lambda x: (-int(x[4]), x[0], x[1]))
#         for st in sorted_students:
#             print(st[0], st[1], st[4])
#     else:
#         sorted_students = sorted(students, key=lambda x: (-int(x[2]), x[0], x[1]))
#         for st in sorted_students:
#             print(st[0], st[1], st[2])

# Stage 6/7: Extensive training

N = int(input())

departments = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}
not_sorted_applicants = {}

file = open('applicants.txt', encoding='utf-8')
biotech_file = open('biotech.txt', 'a', encoding='utf-8')
chemistry_file = open('chemistry.txt', 'a', encoding='utf-8')
engineering_file = open('engineering.txt', 'a', encoding='utf-8')
mathematics_file = open('mathematics.txt', 'a', encoding='utf-8')
physics_file = open('physics.txt', 'a', encoding='utf-8')

not_sorted_applicants = [line.rstrip('\n').split() for line in file]
file.close()

# applicant input
# first name, last name, physics exam, chemistry exam, math exam, cs exam, first priority, second pr, third pr

# sorting applicants by exam result, first name, last name
physics_applicants = sorted(not_sorted_applicants, key=lambda x: (-int(x[2]), x[0], x[1]))
chemistry_applicants = sorted(not_sorted_applicants, key=lambda x: (-int(x[3]), x[0], x[1]))
math_applicants = sorted(not_sorted_applicants, key=lambda x: (-int(x[4]), x[0], x[1]))
cs_applicants = sorted(not_sorted_applicants, key=lambda x: (-int(x[5]), x[0], x[1]))

# copying full list of applicants
not_accepted_applicants = physics_applicants[:]


# enrolling students into each department by wave
N = int(input())

departments = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}
not_sorted_applicants = {}

file = open('applicants.txt', encoding='utf-8')
not_sorted_applicants = [line.rstrip('\n').split() for line in file]
file.close()

# applicant input
# first name, last name, physics exam, chemistry exam, math exam, cs exam, first priority, second pr, third pr

# sorting applicants by exam result, first name, last name
physics_applicants = sorted(not_sorted_applicants, key=lambda x: (-((float(x[2]) + float(x[4])) / 2), x[0], x[1]))
chemistry_applicants = sorted(not_sorted_applicants, key=lambda x: (-float(x[3]), x[0], x[1]))
math_applicants = sorted(not_sorted_applicants, key=lambda x: (-float(x[4]), x[0], x[1]))
cs_applicants = sorted(not_sorted_applicants, key=lambda x: (-((float(x[5]) + float(x[4])) / 2), x[0], x[1]))
biotech_applicants = sorted(not_sorted_applicants, key=lambda x: (-((float(x[2]) + float(x[3])) / 2), x[0], x[1]))

# applicants = sorted(not_sorted_applicants, key=lambda x: (-float(x[2]), x[0], x[1]))
not_accepted_applicants = physics_applicants[:]


def applicants_waves(wave):
    global departments
    global not_accepted_applicants
    for depart, students_list in departments.items():
        if depart == 'Biotech':
            subject_list = biotech_applicants
        elif depart == 'Chemistry':
            subject_list = chemistry_applicants
        elif depart == 'Engineering':
            subject_list = cs_applicants
        elif depart == 'Mathematics':
            subject_list = math_applicants
        else:
            subject_list = physics_applicants

        for student in subject_list:
            if student[wave] == depart:
                if len(students_list) < N:
                    students_list.append(student)
                    not_accepted_applicants.remove(student)


for i in range(6, 9):
    applicants_waves(i)
    physics_applicants = sorted(not_accepted_applicants, key=lambda x: (-((float(x[2]) + float(x[4])) / 2), x[0], x[1]))
    chemistry_applicants = sorted(not_accepted_applicants, key=lambda x: (-float(x[3]), x[0], x[1]))
    math_applicants = sorted(not_accepted_applicants, key=lambda x: (-float(x[4]), x[0], x[1]))
    cs_applicants = sorted(not_accepted_applicants, key=lambda x: (-((float(x[5]) + float(x[4])) / 2), x[0], x[1]))
    biotech_applicants = sorted(not_accepted_applicants, key=lambda x: (-((float(x[2]) + float(x[3])) / 2), x[0], x[1]))


for dep, students in departments.items():
    file = open(dep.lower() + '.txt', 'w', encoding='utf-8')
    if dep == 'Biotech':
        sorted_students = sorted(students, key=lambda x: (-((float(x[2]) + float(x[3])) / 2), x[0], x[1]))
        for st in sorted_students:
            file.write(st[0] + ' ' + st[1] + ' ' + str((float(st[2]) + float(st[3])) / 2) + '\n')
    elif dep == 'Chemistry':
        sorted_students = sorted(students, key=lambda x: (-int(x[3]), x[0], x[1]))
        for st in sorted_students:
            file.write(st[0] + ' ' + st[1] + ' ' + st[3] + '\n')
    elif dep == 'Engineering':
        sorted_students = sorted(students, key=lambda x: (-((float(x[5]) + float(x[4])) / 2), x[0], x[1]))
        for st in sorted_students:
            file.write(st[0] + ' ' + st[1] + ' ' + str((float(st[5]) + float(st[4])) / 2) + '\n')
    elif dep == 'Mathematics':
        sorted_students = sorted(students, key=lambda x: (-int(x[4]), x[0], x[1]))
        for st in sorted_students:
            file.write(st[0] + ' ' + st[1] + ' ' + st[4] + '\n')
    else:
        sorted_students = sorted(students, key=lambda x: (-((float(x[2]) + float(x[4])) / 2), x[0], x[1]))
        for st in sorted_students:
            file.write(st[0] + ' ' + st[1] + ' ' + str((float(st[2]) + float(st[4])) / 2) + '\n')
    file.close()