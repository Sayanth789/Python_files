# Ques:  Deal or No Deal: You've 10 briefcases. Each case hides a fixed amount of money(given in amounts).
# Some number of cases are opened and removed from play. The banker then makes an offer.

# You must decide : Deal -> If the offer is greater than the expected value( average of remaining unopended cases.)

# "No Deal " -> Otherwise.
# ____________________________________________________________
#  Answer to the question 'Deal Or No Deal'

# amounts = [100, 500, 1000, 10000, 25000, 50000, 100000, 500000, 1000000]

# # Read the number of opened briefcases.
# n = int(input('Enter a number:'))

# # Mark which briefcase have been opened
# opened_cases = []
# for _ in range(n):
#     case_number = int(input())
#     opened_cases.append(case_number)

# #Read banker's offer.
# offer = int(input('Enter the offer amount: '))

# #Calculating total of remaining amount
# total = 0
# count = 0

# for i in range(1, len(amounts) + 1): # Case number 1 to 10
#     if i not in opened_cases:
#         total += amounts[i - 1] # convert case number to index
#         count += 1

# average = total / count
# if offer > average:
#     print("deal")
# else:
#     print("no deal") 

# # An alternative version:

amounts = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000,1000000]

n = int(input())

opened_cases = []
count = 0
while count < n:
    case_num = int(input())
    opened_cases.append(case_num)
    count += 1

offer = int(input())
#  The banker's offer

total = 0
remaining = 0

for i in range(1, 11):  # Case numbers are 1-based
    if i not in opened_cases:
        total += amounts[i - 1]
        remaining += 1
average = total / remaining
if offer > average:
    print("deal")
else:
    print("no deal")
