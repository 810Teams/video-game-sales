"""..."""

import numpy, pandas, pygal
from pygal.style import NeonStyle
from project_module import project

def main():
    """..."""
    data_frame = pandas.read_csv('videoGameSales.csv')
    data = numpy.array(data_frame.groupby(['Genre', 'Year'], as_index=False).count()[['Genre', 'Year', 'Rank']]).tolist()
    genres = [i for i in data_frame.groupby('Genre', as_index=False).count()['Genre'].tolist()]

    chart = pygal.Dot(style=NeonStyle)
    for i in genres:
        temp = project.fill_missing_year([[j[1], j[2]] for j in data if j[0] == i])
        chart.add(i, [j[1] for j in temp])

    #Title
    chart.title = 'Each genre of games count in each year'
    chart.x_title = 'Year'
    chart.y_title = 'Genres'

    #Label
    chart.x_labels = range(1980, 2017)
    chart.x_labels_major_count = 8
    chart.show_minor_x_labels = False
    chart.truncate_label = 5

    #Legend
    chart.legend_at_bottom = True

    chart.render_to_file('file.svg')

main()
