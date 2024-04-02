arrival_time = {}
turnaround_time = {}
process_count = int(input("How many processes would you like to simulate?\n"))
a_t = list(input("Indicate the arrival time of each process \
(please separate each arrival time with a space\n)").split(" "))
for i in range(process_count): # populates 'arrival_time' dictionary
    arrival_time[i] = a_t[i]

t_t = list(input("Indicate the the turnaround time of each process.\n"))


3. Asks the user to indicate the the turnaround time of each process
4. Asks the user which scheduling algorithm they would like to simulate (the choices are SJF
Preemptive and Round Robin (if Round Robin is chosen, the user is asked for the time
quantum) )
5. Computes and returns the Average Waiting Time to the user
