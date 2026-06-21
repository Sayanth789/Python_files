login_count = 0 
attendance_count = 0 
error_count = 0 

with open("attendance.log", "r") as file:
    for line in file:

        if "logged in" in line:
            login_count += 1 
        if "marked attendance" in line:
            attendance_count += 1 
        if "ERROR" in line:
            error_count += 1

print("Login Count:", login_count)
print("Attendance Count:", attendance_count)
print("Error Count:", error_count)
