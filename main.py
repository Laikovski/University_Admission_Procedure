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

number_of_students = int(input())
# open and read file
f = open('applicants.txt', "rt")


#create dictionary
dic_student = []
GPA = {
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
    dic_student.append({'name': str[0] + ' ' + str[1], 'ball': str[2], 'depart': [str[3], str[4], str[5]]})

# add students to GPA
for student in dic_student:
    for sub in GPA:
        if student['depart'][0] == sub:
            GPA[sub].append([student['name'],student['ball']])

# sort and filter student
c = 0

for i in GPA:
    GPA[i] = sorted(GPA[i], key= lambda elem: elem[0])
    GPA[i] = sorted(GPA[i], key= lambda elem: elem[1], reverse=True)
    GPA[i] = GPA[i][:number_of_students]
    print(GPA[i])
