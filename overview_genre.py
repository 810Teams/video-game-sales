"""..."""

import numpy, pandas, pygal
from project_module import project

def main():
    """main controller"""
    data_frame = pandas.read_csv('videoGameSales.csv')
    create_chart(data_frame)

def create_chart(data_frame):
    """for create chart"""
    data = numpy.array(data_frame.groupby('Genre', as_index=False).count()[['Genre', 'Rank']]).tolist()
    chart = pygal.Pie()
    for i in data:
        chart.add(i[0], i[1])
    chart.title = 'Genres of Video Games'
    chart.legend_at_bottom = True
    chart.render_to_file('overview_genre.svg')

main()