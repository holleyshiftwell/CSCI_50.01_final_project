# initialize dictionaries
arrival_time = {}
turnaround_time = {}


# asks for process count
process_count = int(input("How many processes would you like to simulate?\n"))


# populates 'arrival_time' dictionary
a_t = list(input("Indicate the arrival time of each process \
(please separate each arrival time with a space\n) ").split(" "))
for i in range(process_count):
    arrival_time[i] = a_t[i]


# populates 'turnaround_time' dictionary
t_t = list(input("Indicate the the turnaround time of each process.\
(please separate each turnaround time with a space\n) ").split(" "))
for i in range(process_count):
    turnaround_time[i] = t_t[i]


# asks for scheduling algorithm
scheduling_algo = input("What scheduling algorithm would you like to simulate?\
 (type 'SJF' or 'Round Robin')\n")
if scheduling_algo == "Round Robin":
    time_quantum = input("What is the time quantum?\n")
