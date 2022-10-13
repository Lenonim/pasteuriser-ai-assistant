def count_right_neighbor_approximation(degree=[], all_time=[], appr_degree=[], appr_all_time=[]):
    for iterator in range(0, len(degree), 2):
        if iterator == len(degree) - 1:
            appr_degree.append(degree[iterator])
            appr_all_time.append(all_time[iterator])
        else:
            appr_degree.append((degree[iterator] + degree[iterator + 1]) / 2.0)
            appr_all_time.append(all_time[iterator + 1])


def count_up_down_approximation(degree=[], all_time=[], appr_degree=[], appr_all_time=[]):
    iterator = 0
    while iterator <= len(degree) - 1:
        temp_degrees = degree[iterator]
        temp_moments = all_time[iterator]
        appr_degree.append(temp_degrees)
        appr_all_time.append(temp_moments)
        if iterator != len(degree) - 1 and degree[iterator] < degree[iterator + 1]:
            while True:
                if iterator != len(degree) - 1 and degree[iterator] < degree[iterator + 1]:
                    temp_degrees = degree[iterator + 1]
                    temp_moments = all_time[iterator + 1]
                    iterator += 1
                else:
                    appr_degree.append(temp_degrees)
                    appr_all_time.append(temp_moments)
                    break
        elif iterator != len(degree) - 1 and degree[iterator] > degree[iterator + 1]:
            while True:
                if iterator != len(degree) - 1 and degree[iterator] > degree[iterator + 1]:
                    temp_degrees = degree[iterator + 1]
                    temp_moments = all_time[iterator + 1]
                    iterator += 1
                else:
                    appr_degree.append(temp_degrees)
                    appr_all_time.append(temp_moments)
                    break
        iterator += 1


def count_critical_percent_approximation(degree=[], all_time=[], appr_degree=[], appr_all_time=[]):
    iterator = 0
    temp_degree = []
    critical_percent = 10.0
    len_degree = len(degree) - 1
    while iterator <= len_degree:
        temp_degree.clear()
        temp_degree.append(degree[iterator])
        appr_sum = degree[iterator]
        appr_percent = appr_sum / critical_percent
        temp_moment = all_time[iterator]
        while True:
            if iterator != len_degree:
                if iterator != len_degree and degree[iterator] < degree[iterator + 1]:
                    if degree[iterator] + appr_percent >= degree[iterator + 1]:
                        temp_degree.append(degree[iterator + 1])
                        temp_moment = all_time[iterator + 1]
                        appr_sum = count_appr_sum(temp_degree)
                        appr_percent = appr_sum / critical_percent
                        iterator += 1
                        continue
                elif iterator != len_degree and degree[iterator] >= degree[iterator + 1]:
                    if degree[iterator] - appr_percent <= degree[iterator + 1]:
                        temp_degree.append(degree[iterator + 1])
                        temp_moment = all_time[iterator + 1]
                        appr_sum = count_appr_sum(temp_degree)
                        appr_percent = appr_sum / critical_percent
                        iterator += 1
                        continue
                appr_degree.append(appr_sum)
                appr_all_time.append(temp_moment)
                iterator += 1
                break
            else:
                appr_degree.append(appr_sum)
                appr_all_time.append(temp_moment)
                iterator += 1
                break


def count_appr_sum(temp_degree=[]):
    appr_sum = 0.0
    for i in range(0, len(temp_degree)):
        appr_sum += temp_degree[i]
        if i == len(temp_degree) - 1:
            appr_sum /= float(len(temp_degree))
    return appr_sum


def cut_right_border(degree=[], all_time=[], cut_degree=[], cut_all_time=[]):
    print("enter the border position, if the quantity of elements is ", len(degree), ' ')
    position = int(input())
    if len(degree) > position > 0:
        copy_list(degree, cut_degree, 0, position)
        copy_list(all_time, cut_all_time, 0, position)


def cut_left_border(degree=[], all_time=[], cut_degree=[], cut_all_time=[]):
    print("enter the border position, if the quantity of elements is ", len(degree), ' ')
    position = int(input())
    if len(degree) > position > 0:
        copy_list(degree, cut_degree, position, len(degree))
        copy_list(all_time, cut_all_time, position, len(degree))


def cut_range(degree=[], all_time=[], cut_degree=[], cut_all_time=[]):
    print("enter the left border position, if the quantity of elements is ", len(degree), ' ')
    left_position = int(input())
    print("enter the right border position: ")
    right_position = int(input())
    if len(degree) > left_position > 0 and len(degree) > right_position > 0 and left_position < right_position:
        copy_list(degree, cut_degree, left_position, right_position)
        copy_list(all_time, cut_all_time, left_position, right_position)


def copy_list(out_list=[], in_list=[], left_border=0, right_border=1):
    for i in range(left_border, right_border):
        in_list.append(out_list[i])
