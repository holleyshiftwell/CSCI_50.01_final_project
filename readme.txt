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

