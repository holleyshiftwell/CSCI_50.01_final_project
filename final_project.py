def sjf_preemptive(processes, n):
    processes.sort(key=lambda x: x[1])  # Sort processes by arrival time
    remaining_time = [process[2] for process in processes]  # Remaining burst time for each process
    completed = 0  # Number of completed processes
    current_time = 0  # Current time
    total_waiting_time = 0  # Total waiting time for all processes

    while completed < n:
        shortest_index = None
        shortest_burst = float('inf')  # Initialize shortest burst time to infinity

        for i in range(n):
            if processes[i][1] <= current_time and remaining_time[i] < shortest_burst and remaining_time[i] > 0:
                shortest_index = i
                shortest_burst = remaining_time[i]

        if shortest_index is None:
            current_time += 1
            continue

        # Reduce remaining burst time of the selected process
        remaining_time[shortest_index] -= 1

        # If the process has completed execution
        if remaining_time[shortest_index] == 0:
            completed += 1
            end_time = current_time + 1
            waiting_time = end_time - processes[shortest_index][1] - processes[shortest_index][2]
            total_waiting_time += waiting_time

        # Move to the next time unit
        current_time += 1

    average_waiting_time = total_waiting_time / n
    return average_waiting_time


def round_robin(processes, n, time_quantum):
    total_waiting_time = 0
    burst_remaining = [process[2] for process in processes]
    current_time = 0
    while True:
        done = True
        for i in range(n):
            if burst_remaining[i] > 0:
                done = False
                if burst_remaining[i] > time_quantum:
                    current_time += time_quantum
                    burst_remaining[i] -= time_quantum
                else:
                    current_time += burst_remaining[i]
                    total_waiting_time += current_time - processes[i][1] - processes[i][2]
                    burst_remaining[i] = 0
        if done:
            break
    average_waiting_time = total_waiting_time / n
    return average_waiting_time


def main():
    n = int(input("Enter the number of processes: "))
    processes = []
    for i in range(n):
        arrival_time = int(input(f"Enter arrival time for process {i+1}: "))
        turnaround_time = int(input(f"Enter turnaround time for process {i+1}: "))
        processes.append((i+1, arrival_time, turnaround_time))
    algorithm = input("Choose scheduling algorithm (SJF Preemptive / Round Robin): ").lower()
    if algorithm == "sjf preemptive":
        average_waiting_time = sjf_preemptive(processes, n)
        print(f"Average Waiting Time: {average_waiting_time}")
    elif algorithm == "round robin":
        time_quantum = int(input("Enter time quantum: "))
        average_waiting_time = round_robin(processes, n, time_quantum)
        print(f"Average Waiting Time: {average_waiting_time}")
    else:
        print("Invalid scheduling algorithm choice.")


if __name__ == "__main__":
    main()
