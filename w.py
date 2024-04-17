# turnaround_time = {0: 5, 1: 3, 2: 3, 3: 2, 4: 2}

# def lowest_TT(turnaround_time, n):
#     lowest = 99999999
#     counter = 1
#     index = [range(n)]
#     for i in turnaround_time:
#         if turnaround_time[i] < lowest:
#             lowest = turnaround_time[i]
#             counter = 1
#             index.clear()
#             index.append(i)
#         elif turnaround_time[i] == lowest:
#             counter += 1
#             index.append(i)
    
#     print(f"there are {counter} instances of {lowest}")
#     print(index)

# lowest_TT(turnaround_time, 5)

# print(len(turnaround_time))

dict = {0: 0, 
        1: 1, 
        2: 2,
}

list = [1]

if dict[list[0]]:
    print("hello")

