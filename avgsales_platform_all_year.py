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
    data_count_platform = sorted(numpy.array(data_frame.groupby(['Platform', 'Year'], as_index=False).count()[['Platform', 'Year', 'Rank']]).tolist())
    data_sales_platform = sorted(numpy.array(data_frame.groupby(['Platform', 'Year'], as_index=False).sum()[['Platform', 'Year', 'Global_Sales']]).tolist())
    data_count = numpy.array(data_frame.groupby('Year', as_index=False).count()[['Year', 'Rank']]).tolist()
    data_sales = numpy.array(data_frame.groupby('Year', as_index=False).sum()[['Year', 'Global_Sales']]).tolist()

    #Data List of Platforms
    data_handhelds = fill_missing([[int(data_count_platform[i][1]), data_sales_platform[i][2]/data_count_platform[i][2]] for i in range(len(data_count_platform)) if data_count_platform[i][0] == 'HandheldGameConsoles' and data_count_platform[i][1] <= 2016])
    data_consoles  = fill_missing([[int(data_count_platform[i][1]), data_sales_platform[i][2]/data_count_platform[i][2]] for i in range(len(data_count_platform)) if data_count_platform[i][0] == 'HomeVideoGameConsoles' and data_count_platform[i][1] <= 2016])
    data_windows   = fill_missing([[int(data_count_platform[i][1]), data_sales_platform[i][2]/data_count_platform[i][2]] for i in range(len(data_count_platform)) if data_count_platform[i][0] == 'MicrosoftWindows' and data_count_platform[i][1] <= 2016])
    data = [[int(data_count[i][0]), data_sales[i][1]/data_count[i][1]] for i in range(len(data_count)) if data_count[i][0] <= 2016]

    #Chart Basics
    chart = pygal.Line()
    chart.style = NeonStyle

    #Titles
    chart.title = 'Average sales per game by platform type in each year'
    chart.x_title = 'Year'
    chart.y_title = 'Sales (in millions)'

    #Labels
    chart.x_labels = [i[0] for i in data_consoles]
    chart.x_labels_major_count = 8
    chart.show_minor_x_labels = False
    chart.y_labels = [i*0.1 for i in range(0, 70, 5)]
    chart.y_labels_major = [i for i in range(0, 7, 1)]
    chart.truncate_label = 4
    chart.legend_at_bottom = True
    chart.truncate_legend = 50

    #Adding data to a chart
    chart.add('Handheld Game Consoles', [i[1] for i in sorted(data_handhelds)])
    chart.add('Home Video Game Consoles', [i[1] for i in sorted(data_consoles)])
    chart.add('Microsoft Windows', [i[1] for i in sorted(data_windows)])
    chart.add('Overall', [i[1] for i in sorted(data)])

    #Render
    chart.render_to_file('avgsales_platform_all_year.svg')

def fill_missing(data):
    """ Fill missing year data """
    data = dict(data)
    for i in range(1980, 2017):
        if (i in data) == False:
            data[i] = 0
    return [[i, data[i]] for i in sorted(data)]

main()
