info = 0 
warning = 0 
error = 0 
transactions =  0 

with open("bank.log", "r") as file:
    for line in file:

        if "INFO" in line:
            info += 1 
            transactions += 1
        elif "WARNING" in line:
            warning += 1 
        elif "ERROR" in line:
            error += 1 
print('BANK SYSTEM REPORT')
print(" -----------  ------------- ------------")
print("Total Transactions:", transactions)
print("Successful Actions:", info)
print("Warning (Overdrafts):", warning)
print("Error", error)
