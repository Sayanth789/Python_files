# Answer to the question "wild willow"
# ____________________________________________________________________________________________________________________________

# A cat (Wiilow) takes T days to play with box. If the owner brought new Box, she will wait until bored with existing one.Then takes the new box.

# Here the input is T, N and 'N' days behavior of the owner , 'B' if box is brought, 'E' if empty handed.
#  Given these inputs we need to output the number of days that Willow will be playing with the boxes after the N 
#  days given in the dataset.Taking 10 datasets at a time.


for datasets in range(10):
    N,T = map(int, input().split())  # Use split to read both integers from the same line,and convert them to integers using map(int, ...)

    
    #Read the next N lines (each day)
    days = [input().strip() for _ in range(N)]  

    willow_free_day = 0 # The earliest day willow is free to start a new box

    for i in range(N):
        if days[i] == 'B':
            if i >= willow_free_day:
                # Willow is free, start now
                willow_free_day = i + T 
            else:
                # Willow is busy, queue the new box
                willow_free_day += T
    # Output the delay after the last day
    delay = max(0, willow_free_day - N)
    print(delay)



#  An alternative version is:
def process_dataset(N , T, actions):
    willow_free_day = 0

    current_day = 0
    for action in actions:
        if actions == 'B':
            # If willow is free, she starts playing today.
            if current_day >= willow_free_day:
                willow_free_day = current_day + T
            else:
                # Willow is still playing . queue the box
                willow_free_day += T
        
        # Move to the next day
        current_day += 1

    return max(0, willow_free_day - N)
# Process 10 datasets
for _ in range(10):
    N, T = map(int, input().split())
    actions = [input().strip() for _ in range(N)]
    delay = process_dataset(N, T ,actions)
    print(delay)