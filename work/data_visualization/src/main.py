from matplotlib import pyplot
from matplotlib import style


class RowFromFile:
    def __init__(self, first_column, second_column, third_column):
        self.first_column = first_column
        self.second_column = second_column
        self.third_column = third_column

    def __str__(self):
        return f'{self.first_column};{self.second_column};{self.third_column}'

    def __repr__(self):
        return f'{self.first_column} {self.second_column} {self.third_column}'


dataList: list[RowFromFile] = []
abscissa = []
ordinate = []
applicate = []
time_moments = 1
moments = []

work_file = open("E:\work\mimpu\pasteuriser-ai-assistant\data\data_7.csv", 'r')
for i in work_file.readlines():
    str_list = i.split(';')
    RFF = RowFromFile(int(str_list[0]), int(str_list[1]), float(str_list[2]))
    dataList.append(RFF)
    moments.append(time_moments)
    time_moments += 1
    abscissa.append(int(str_list[0]))
    ordinate.append(int(str_list[1]))
    applicate.append(float(str_list[2]))

style.use('ggplot')
pyplot.figure(figsize=(12, 7))

pyplot.subplot(2, 3, 1)
pyplot.plot(moments, ordinate, 'r', linewidth=1)
pyplot.xlabel('time moments')
pyplot.ylabel('second column')
pyplot.grid(True)

pyplot.subplot(2, 3, 2)
pyplot.plot(moments, abscissa, 'g', linewidth=1)
pyplot.xlabel('time moments')
pyplot.ylabel('first column')
pyplot.grid(True)

pyplot.subplot(2, 3, 3)
pyplot.plot(moments, applicate, 'b', linewidth=1)
pyplot.xlabel('time moments')
pyplot.ylabel('third column')
pyplot.grid(True)

pyplot.subplot(2, 3, 4)
pyplot.plot(abscissa, ordinate, 'y', linewidth=1)
pyplot.xlabel('first column')
pyplot.ylabel('second column')
pyplot.grid(True)

pyplot.subplot(2, 3, 5)
pyplot.plot(abscissa, applicate, 'p', linewidth=1)
pyplot.xlabel('first column')
pyplot.ylabel('third column')
pyplot.grid(True)

pyplot.subplot(2, 3, 6)
pyplot.plot(ordinate, applicate, 'o', linewidth=1)
pyplot.xlabel('second column')
pyplot.ylabel('third column')
pyplot.grid(True)

pyplot.show()