"""
PSIT Data Analysis Project
Chart: Average Sales by Genre
NOTE: Chart Unused!
"""

import numpy, pandas, pygal
from pygal.style import NeonStyle
from project_module import project

def main():
    """ Main function """
    #DataFrame
    data_frame = pandas.read_csv('videoGameSales.csv')

    #List of genre
    genre = data_frame.groupby('Genre', as_index=False).count()['Genre'].tolist()

    #Count and sales lists by genre
    count_genre = numpy.array(data_frame.groupby(['Genre', 'Year'], as_index=False).count()[['Genre', 'Year', 'Rank']]).tolist()
    sales_genre = numpy.array(data_frame.groupby(['Genre', 'Year'], as_index=False).sum()[['Genre', 'Year', 'Global_Sales']]).tolist()

    #Count and sales lists by overall
    count_overall = numpy.array(data_frame.groupby('Year', as_index=False).count()[['Year', 'Rank']]).tolist()
    sales_overall = numpy.array(data_frame.groupby('Year', as_index=False).sum()[['Year', 'Global_Sales']]).tolist()

    #Chart Basics
    chart = pygal.Dot(stroke_style={'width': 0.75}, dots_size=1)

    #Title
    chart.title = 'Average sales per game by genre (1980-2016)'
    chart.x_title = 'Year'
    chart.y_title = 'Average sales per game (in millions)'

    #Labels
    chart.x_labels = [i for i in data_frame.groupby('Year', as_index=False).count()['Year'].tolist() if i < 2017]
    chart.x_labels_major_count = 8
    chart.show_minor_x_labels = False
    #chart.y_labels = [i*0.1 for i in range(0, 111, 10)]
    #chart.y_labels_major = [i for i in range(0, 11, 2)]
    chart.truncate_label = 20

    #Legend
    chart.legend_at_bottom = True
    chart.truncate_legend = 50

    #Adding data
    _ = [chart.add(genre[i], [j[1] for j in project.fill_missing_year([[count_genre[j][1], sales_genre[j][2]/count_genre[j][2]] for j in range(len(count_genre)) if count_genre[j][0] == genre[i] and count_genre[j][1] < 2017])]) for i in range(len(genre))]
    chart.add('Overall', [sales_overall[i][1]/count_overall[i][1] for i in range(len(count_overall)) if count_overall[i][0] < 2017])

    #Render
    chart.render_to_file('avgsales_genre.svg')

main()
