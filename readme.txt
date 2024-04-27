def sjf_preemptive(processes, n):
    This function implements Shortest Job First (SJF) scheduling algorithm with preemption.
    It calculates the average waiting time for a given list of processes.


# Sort processes by arrival time
# Initialize remaining burst time for each process
# Initialize number of completed processes
# Initialize current time
# Initialize total waiting time for all processes
# Loop until all processes are completed
# Initialize shortest burst time to infinity
# Find the process with the shortest remaining burst time that has arrived
# If no process can exicute, move to the next time unit
# Decrement remaining burst time of the process
# If the process has completed execution
# Increment completed
# end_time = current_time + 1
# waiting_time = end_time - processes[shortest_index][1] - processes[shortest_index][2]
# increment total_waiting_time by waiting_time 
# Move to the next time unit and increment current_time
# Calculate average waiting time
# total waiting time divided by the number of processes
# return the average waiting time

def round_robin(processes, n, time_quantum):
    This function implements Round Robin scheduling. It calculates the average waiting time
    for a given list of processes and time quantum.

# Initialize total waiting time
# Create a list `burst_remaining` to hold the remaining burst time for each process
# Initialize current time to 0
# Continue the loop while there are unfinished processes
# Assume all processes are done
# Iterate through each process
# Check if the process has remaining burst time
# If remaining burst time is greater than the time quantum
    # Execute the process for `time_quantum` time units
    # Increment current time by `time_quantum`
    # Decrease remaining burst time for the process by `time_quantum`
# If remaining burst time is less than or equal to the time quantum
    # Execute the process for its remaining burst time
    # Increment current time by the remaining burst time
    # Calculate the waiting time as `current_time - processes[i][1] - processes[i][2]`
    # Add the waiting time to `total_waiting_time`
    # Set remaining burst time for the process to 0
# If a process has remaining burst time, set `done` to False
# If all processes are done (`done` is still True), exit the loop
# Calculate the average waiting time as `total_waiting_time / n`
# Return the calculated average waiting time
