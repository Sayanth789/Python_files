
# School trip:
# _______________________________________________________________________________________________________________
# Problem Statement

# A school is organizing a trip. Students from four year groups contribute different amounts of money toward the trip:

# 1st year student → $12

# 2nd year student → $10

# 3rd year student → $7

# 4th year student → $5

# You are given:

# The required amount of money for the trip.

# The number of students in each year group (four integers).

# The total number of students.

# Your task is to determine whether the money collected is enough.

# If the collected money is less than the required amount, output "yes" (indicating more fundraising is needed).

# If the collected money is greater than or equal to the required amount, then assume that half of the collected money is spent on the party.

# If the remaining half is at least the required amount, output "no".

# Otherwise, output "yes".

# Input Format

# An integer R — the required amount of money.

# Four space-separated integers — the number of students in 1st, 2nd, 3rd, and 4th year.

# An integer N — the total number of students.


# An idea used to solve the problem is: total no:students * fraction gives the number of students at that year: Thus multiplying it with the charge of corresponding year
# will give the amount paid by that year , we do it for all years and then calculate the half, compare to the input().      

# Here we take 10 datasets as  input
# YEAR_COST = [12, 10, 7, 5] # This is a constant variable , for it python convention is to write in capital letters

# for dataset in range(10):  # The  input has 10 test cases thus the rest of the program is inside the for  loop.
#     trip_cost = int(input())
#     proportions = input().split()   # The secod line has 4 lines of input thus we split it into a list of 4 strings. 
#     num_students = int(input())

#     for i in range(len(proportions)):  # Using range  for loop to convert each of the strings to a float 
#         proportions[i] = float(proportions[i])

#     students_per_year = [] 

#     for proportion in proportions:
#         students = int(num_students * proportions)   # calculate the  number of students in each year
#         students_per_year.append(students)
#     total_raised = 0

#     for i in range(len(students_per_year)):
#         total_raised = total_raised + students_per_year[i] * YEAR_COST[i]

#     if total_raised / 2 < trip_cost:
#         print('YES')
#     else:
#         print('NO')

# #  The implementation above is a not so full version of the question, the real version has to take in to account the roundoff due to floating numbers.\
# # eg: if the multiplication (fraction * num_student ) is 9.7 then it rounds to 9 and we add the remaining fraction as 1 to the multiplication value that is the largest.

# # The refined version is:
# YEAR_COST = [12, 10, 7, 5]

# for data in range(10):
#     trip_cost = int(input())
#     proportions = input().split()
#     num_students = int(input())

#     for i in range(len(proportions)):
#         proportions[i] = float(proportions[i])

#     students_per_year = []

#     for proportion in proportions:
#         students = int(num_students * proportions)
#         students_per_year.append(students)

#     counted = sum(students_per_year)  
#     uncounted = num_students -  counted
#     most = max(students_per_year)  # Which year currently has most students
#     where = students_per_year.index(most)   # Find the index of the year that  has most students
#     students_per_year[where] = students_per_year[where] + uncounted   # Put all remaining students to the year that already has the most students.

#     total_raised = 0

#     for i in range(len(students_per_year)):
#         total_raised = total_raised + students_per_year[i] + YEAR_COST[i]

#     if total_raised / 2 < trip_cost:
#         print("YES")
#     else:
#         print("NO")