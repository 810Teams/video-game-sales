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
    #DataFrame
    data_frame = project.platform_convert_df(pandas.read_csv('videoGameSales.csv'))

    #List of platform
    platform = data_frame.groupby('Platform', as_index=False).count()['Platform'].tolist()

    #Count and sales lists by platform
    count_platform = numpy.array(data_frame.groupby(['Platform', 'Year'], as_index=False).count()[['Platform', 'Year', 'Rank']]).tolist()
    sales_platform = numpy.array(data_frame.groupby(['Platform', 'Year'], as_index=False).sum()[['Platform', 'Year', 'Global_Sales']]).tolist()

    #Count and sales lists by overall
    count_overall = numpy.array(data_frame.groupby('Year', as_index=False).count()[['Year', 'Rank']]).tolist()
    sales_overall = numpy.array(data_frame.groupby('Year', as_index=False).sum()[['Year', 'Global_Sales']]).tolist()

    #Chart Basics
    chart = pygal.Dot(stroke_style={'width': 1.75}, dots_size=1.75)
    chart.style = NeonStyle

    #Title
    chart.title = 'Average sales per game by platform type (1980-2016)'
    chart.x_title = 'Year'
    chart.y_title = 'Average sales per game (in millions)'

    #Labels
    chart.x_labels = [i for i in data_frame.groupby('Year', as_index=False).count()['Year'].tolist() if i < 2017]
    chart.x_labels_major_count = 8
    chart.show_minor_x_labels = False
    #chart.y_labels = [i*0.1 for i in range(0, 66, 5)]
    #chart.y_labels_major = [i for i in range(0, 8, 2)]
    chart.truncate_label = 20

    #Legend
    chart.legend_at_bottom = True
    chart.truncate_legend = 50

    #Adding data
    _ = [chart.add(platform[i], [j[1] for j in project.fill_missing_year([[count_platform[j][1], sales_platform[j][2]/count_platform[j][2]] for j in range(len(count_platform)) if count_platform[j][0] == platform[i] and count_platform[j][1] < 2017])]) for i in range(len(platform))]
    chart.add('Overall', [sales_overall[i][1]/count_overall[i][1] for i in range(len(count_overall)) if count_overall[i][0] < 2017])

    #Render
    chart.render_to_file('avgsales_platform_year.svg')

main()
