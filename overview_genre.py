"""
PSIT Data Analysis Project
Chart: Overview of Genre Types
"""

import pandas, numpy, pygal
from project_module import project

def main():
    """ Main function """
    data_frame = pandas.read_csv('videoGameSales.csv')
    create_chart(data_frame)

def create_chart(data_frame):
    """ For creating chart """
    data = numpy.array(data_frame.groupby('Genre', as_index=False).count()[['Genre', 'Rank']]).tolist()

    chart = pygal.Pie()

    for i in data:
        chart.add(i[0], i[1])

    chart.title = 'Video Games Amount by Genre'
    chart.legend_at_bottom = True
    chart.legend_box_size = 12
    chart.render_to_file('overview_genre.svg')

main()
