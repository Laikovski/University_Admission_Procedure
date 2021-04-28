one, two, three = int(input()), int(input()), int(input())
mean_score = (one + two + three) / 3
if mean_score >= 60:
    print(f'''{mean_score}
Congratulations, you are accepted!''')

else:
    print(f'''{mean_score}
We regret to inform you that we will not be able to offer you admission.''')
