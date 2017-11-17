import pandas
import pygal
import numpy
import project_module as project

def main():
    """main controller"""
    data_frame = pandas.read_csv('Video-Game-Sales/videoGameSales.csv')
    create_chart(data_frame)

def create_chart(data_frame):
    """for create chart"""
    data = numpy.array(data_frame.groupby('Genre', as_index=False).count()[['Genre', 'Rank']]).tolist()
    chart = pygal.Pie()
    for i in data:
        chart.add(i[0], i[1])
    chart.render_to_file('Genre_ratio.svg')
main()
