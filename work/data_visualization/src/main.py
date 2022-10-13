import approximation
import visualisation

# for data storage
degree_of_discovery = []
time_moment = 0
all_time = []

# read data with primary data processing
print("enter the file name:\n")
file_name = input()
work_file = open(file_name, 'r')
for line in work_file.readlines():
    line = line.replace("\n", "")
    line_parts = line.split(';')
    if int(float(line_parts[2]) > 0):
        time_moment += int(line_parts[0])
        all_time.append(time_moment)
        degree_of_discovery.append(float(line_parts[2]))
print("data have been read\n")

# proc - processing
proc_degree_of_discovery = []
proc_all_time = []

temp_degree_of_discovery = []
temp_all_time = []

# secondary data processing - data approximation or cutting
repeat_proc = 'y'
action = '1'
while repeat_proc == 'y':
    print("choose the mode of data processing:\n"
          "1 - \"right neighbor\" approximation\n"
          "2 - \"up-down\" approximation\n"
          "3 - \"critical percent\" approximation\n"
          "4 - cut right border of data\n"
          "5 - cut left border of data\n"
          "6 - cut range of data\n"
          "7 - without processing\n"
          "your action: ")
    action = input()

    temp_degree_of_discovery = []
    temp_all_time = []
    if len(proc_degree_of_discovery) == 0:
        temp_degree_of_discovery = degree_of_discovery.copy()
        temp_all_time = all_time.copy()
    else:
        temp_degree_of_discovery = proc_degree_of_discovery.copy()
        temp_all_time = proc_all_time.copy()
        proc_degree_of_discovery.clear()
        proc_all_time.clear()

    if action == '1':
        approximation.count_right_neighbor_approximation(temp_degree_of_discovery, temp_all_time,
                                                         proc_degree_of_discovery, proc_all_time)
    elif action == '2':
        approximation.count_up_down_approximation(temp_degree_of_discovery, temp_all_time,
                                                  proc_degree_of_discovery, proc_all_time)
    elif action == '3':
        approximation.count_critical_percent_approximation(temp_degree_of_discovery, temp_all_time,
                                                           proc_degree_of_discovery, proc_all_time)
    elif action == '4':
        approximation.cut_right_border(temp_degree_of_discovery, temp_all_time,
                                       proc_degree_of_discovery, proc_all_time)
    elif action == '5':
        approximation.cut_left_border(temp_degree_of_discovery, temp_all_time,
                                      proc_degree_of_discovery, proc_all_time)
    elif action == '6':
        approximation.cut_range(temp_degree_of_discovery, temp_all_time,
                                proc_degree_of_discovery, proc_all_time)
    # without approximation
    elif action == '7':
        proc_degree_of_discovery = temp_degree_of_discovery.copy()
        proc_all_time = temp_all_time.copy()
        break

    print("processing has been done\n")
    general_percent = 100.0 - 100.0 * float(len(proc_degree_of_discovery) / len(degree_of_discovery))
    print("general percent of data reduction: ", general_percent, "%")
    intermediate_percent = 100.0 - 100.0 * float(len(proc_degree_of_discovery) / len(temp_degree_of_discovery))
    print("intermediate percent of data reduction: ", intermediate_percent, "%")
    print("\nenter y to repeat the processing or n to continuation: ")
    repeat_proc = input()


print("choose the mode of data visualisation\n"
      "1 - with scaling (1 graph)\n"
      "2 - 2 graphs\n"
      "3 - 4 graphs\n"
      "4 - without mode (1 graph)\n"
      "mode: ")
mode_visualisation = input()

if mode_visualisation == '1':
    visualisation.zoom_visualisation(proc_all_time, proc_degree_of_discovery)
elif mode_visualisation == '2':
    visualisation.double_visualisation(proc_all_time, proc_degree_of_discovery)
elif mode_visualisation == '3':
    visualisation.quad_visualisation(proc_all_time, proc_degree_of_discovery)
elif mode_visualisation == '4':
    visualisation.clean_visualisation(proc_all_time, proc_degree_of_discovery)
