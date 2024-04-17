# initialize dictionaries
arrival_time = {}
turnaround_time = {}


# asks for process count
process_count = int(input("How many processes would you like to simulate?\n"))


# populates 'arrival_time' dictionary
a_t = list(input("Indicate the arrival time of each process \
(please separate each arrival time with a space\n) ").split(" "))
for i in range(process_count):
    arrival_time[i] = int(a_t[i])


# populates 'turnaround_time' dictionary
t_t = list(input("Indicate the the turnaround time of each process.\
(please separate each turnaround time with a space\n) ").split(" "))
for i in range(process_count):
    turnaround_time[i] = int(t_t[i])


# asks for scheduling algorithm
scheduling_algo = input("What scheduling algorithm would you like to simulate?\
 (type 'SJF' or 'Round Robin')\n")
if scheduling_algo == "Round Robin":
    time_quantum = input("What is the time quantum?\n")


# finds the process/processes with the lowest arrival time
def lowest_AT(arrival_time):
    lowest = 99999999
    global indices
    indices = []
    # iterates through the arrival_time dictionary
    # stores the index of the process with the lowest AT in "indices"
    # if there are multiple processes with the same AT,
    # append the index to "indices"
    for i in arrival_time:
        if arrival_time[i] < lowest:
            lowest = arrival_time[i]
            indices.clear()
            indices.append(i)
        elif arrival_time[i] == lowest:
            indices.append(i)

# creates the order at which the processes will be run
def order(arrival_time, turnaround_time):
    global process_order
    process_order = []
    # check which process has the lowest AT
    lowest_AT(arrival_time)
    # if multiple processes share the same AT
    # check which process has the lowest TT
    # append the index of the lowest AT && TT process to "process_order"
    if len(indices) > 1:
        lowest_TT = 99999999
        for i in indices:
            if turnaround_time[i] < lowest_TT:
                lowest_TT = i
        process_order.append(lowest_TT)
    # else if there is a singular lowest AT,
    # store the index of the lowest AT process to "process_order"
    elif len(indices) == 1:
        process_order[0] = lowest_AT[0]





def SJF(process_count, arrival_time, turnaround_time):

        

            














# TRASH TO TREASURE?

# def compare(arrival_time, turnaround_time, indices):
#     lowest = 99999999

#     for i in indices:
#         if turnaround_time[i] < lowest:
#             lowest = turnaround_time[i]
