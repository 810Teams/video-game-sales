"""
PSIT Project: Video Game Sales
Chart: Average sales per game by platform type in each year
By Teerapat Kraisrisirikul (60070183)
"""

import numpy, pandas, pygal
from pygal.style import NeonStyle
from project_module import project

def main():
    """ Main function """
    data_frame = project.platform_convert_df(pandas.read_csv('videoGameSales.csv'))
    create_chart(data_frame)

def create_chart(data_frame):
    """ Create chart """
    #Data Frame Management
    data_count = numpy.array(data_frame.groupby('Year', as_index=False).count()[['Year', 'Rank']]).tolist()
    data_sales = numpy.array(data_frame.groupby('Year', as_index=False).sum()[['Year', 'Global_Sales']]).tolist()

    #Data List of Platforms
    data = [[int(data_count[i][0]), data_sales[i][1]/data_count[i][1]] for i in range(len(data_count)) if data_count[i][0] <= 2016]

    #Chart Basics
    chart = pygal.Line()
    chart.style = NeonStyle

    #Titles
    chart.title = 'Average sales per game in each year'
    chart.x_title = 'Year'
    chart.y_title = 'Sales (in millions)'

    #Labels
    chart.x_labels = [i[0] for i in data]
    chart.x_labels_major_count = 8
    chart.show_minor_x_labels = False
    chart.y_labels = [i*0.1 for i in range(0, 70, 5)]
    chart.y_labels_major = [i for i in range(0, 7, 1)]
    chart.truncate_label = 4

    #Legend
    chart.show_legend = False

    #Adding data to a chart
    chart.add('Average', [i[1] for i in sorted(data)])

    #Render
    chart.render_to_file('avgsales_all_year.svg')

main()
