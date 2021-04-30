## Stage 1/7: No one is left behind!
    At this stage, your program should:

    - Take three inputs as integer numbers. They are the exam results.
    - Calculate the mean score of all three numbers. If the mean is a fractional number, don't discard the fractional part.
    - Print the resulting number.
    - Print the Congratulations, you are accepted! line.

## Stage 2/7: Raising the bar
    - At this stage, your program should:

    - Read the numbers and output the mean score, as in the previous stage.
    - If the mean score is equal to or greater than 60.0, output the following message: Congratulations, you are accepted!
    - If the mean score is less than 60.0, output the following message: We regret to inform you that we will not be able to offer you admission.

## Stage 3/7: Going big 
    At this stage, your program should:

    - Read the first input, an N integer representing the total number of applicants.
    - Read the second input, an M integer representing the number of applicants that should be accepted to the university.
    - Read N lines from the input. Each line contains the first name, the last name, and the applicant's GPA. These values are separated by one whitespace character. A GPA is a floating-point number with two decimals.
    - Output the Successful applicants: message.
    - Output M lines for applicants with the top-ranking GPAs. Each line should contain the first and the last name of the applicant separated by a whitespace character. Successful applicants' names should be printed in descending order depending on the GPA — first, the applicant with the best GPA, then the second-best, and so on.
    - If two applicants have the same GPA, rank them in alphabetical order using their full names (we know it's not really fair to choose students by their names, but what choice do we have?)

## Stage 4/7: Choose your path
    At this stage, your program should:

    - Read an N integer from the input. This integer represents the maximum number of students for each department.
    - Read the file named applicants.txt (this file is already included in the project's files, even though it is not visible; so you only need to download it if you want to take a closer look at it). Each line equals one applicant, their first name, last name, GPA, first priority department, second priority department, and third priority department. Columns with values are separated by whitespace characters. For example, Laura Spungen 3.71 Physics Engineering Mathematics.
    - Sort applicants according to their GPA and priorities (and names, if their GPA score is the same). As in the previous stage, if two applicants to the same department have the same GPA, sort them by their full names in alphabetical order.
    - For each department, choose the N best candidates. Some departments are less popular than others, so there may be fewer available candidates for a department. However, their number shouldn't be more than N.
    - Print the departments in the alphabetic order (Biotech, Chemistry, Engineering, Mathematics, Physics), output the names and the GPA of enrolled applicants for each department. Separate the name and the GPA with a whitespace character. Here's an example (you may add empty lines between the departments' lists to increase the text readability):
