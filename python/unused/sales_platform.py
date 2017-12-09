"""
PSIT Data Analysis Project
Chart: Sales by Platform Type
"""

import pandas, numpy, pygal
from project_module import project

data_frame = pandas.read_csv('videoGameSales.csv')

def main():
    """ Main Function """
    HVGC = project.fill_missing_year(summed_platform_sales('Home Video Game Consoles'))
    HGC = project.fill_missing_year(summed_platform_sales('Handheld Game Consoles'))
    MW = project.fill_missing_year(summed_platform_sales('Microsoft Windows'))

    create_chart(HVGC, HGC, MW)

#############################################################

def summed_platform_sales(genre):
    """ This Function for Summed Sales of Years in Zone """
    data_frame_convert = project.platform_convert_df(data_frame)
    genre_sales = []
    all_genre_list = numpy.array(data_frame.groupby(['Year', 'Platform'], as_index=False).sum()[['Year', 'Platform', 'Global_Sales']]).tolist()
    for i in all_genre_list:
        selected = [i[0], i[2]]
        if i[1] == genre:
            genre_sales.append(selected)
    return genre_sales

##############################################################

def create_chart(HVGC, HGC, MW):
    """ This Function for create chart """
    chart = pygal.StackedLine(dots_size=1.75, legend_at_bottom=True, interpolate='cubic', fill=True)

    chart.x_title = 'Year'
    chart.y_title = 'Sales (in millions)'

    chart.x_labels = [i for i in range(1980, 2017)]
    chart.x_labels_major_count = 8
    chart.show_minor_x_labels = False
    chart.truncate_label = 5
    chart.legend_box_size = 16
    chart.legend_at_bottom_columns = 3

    chart.add("Home Video Game Consoles", [i[1] for i in HVGC])
    chart.add("Handheld Game Consoles", [i[1] for i in HGC])
    chart.add("Microsoft Windows", [i[1] for i in MW])

    chart.render_to_file('sales_platform.svg')

main()
