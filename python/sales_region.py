"""
    PSIT Data Analysis Project
    Chart: Sales by Region
    by Supakit Theanthunyakit (POKINBKK)
"""

import pandas, numpy, pygal
from project_module import project

def main():
    """ Main Function """
    data_frame = pandas.read_csv('vgsales.csv')
    NA_Sales = project.fill_missing_year(summed_sales(data_frame, 'NA_Sales'))
    EU_Sales = project.fill_missing_year(summed_sales(data_frame, 'EU_Sales'))
    JP_Sales = project.fill_missing_year(summed_sales(data_frame, 'JP_Sales'))
    OT_Sales = project.fill_missing_year(summed_sales(data_frame, 'Other_Sales'))
    GB_Sales = project.fill_missing_year(summed_sales(data_frame, 'Global_Sales'))
    create_chart(NA_Sales, EU_Sales, JP_Sales, OT_Sales, GB_Sales)

def summed_sales(data_frame, zone):
    """ This Function for Summed Sales of Years in Zone """
    return numpy.array(data_frame.groupby('Year', as_index=False).sum()[['Year', zone]]).tolist()

def create_chart(na_sa, eu_sa, jp_sa, ot_sa, gb_sa):
    """ This Function for create chart """
    chart = pygal.StackedLine(dots_size=1.75, legend_at_bottom=True, interpolate='cubic', fill=True)

    chart.x_title = 'Year'
    chart.y_title = 'Sales (in millions)'

    chart.x_labels = [str(int(i[0])) for i in na_sa]
    chart.x_labels_major_count = 8
    chart.show_minor_x_labels = False
    chart.y_labels = [i for i in range(0, 701, 100)]
    chart.truncate_label = 5
    chart.legend_box_size = 16

    chart.add("North America Sales", [i[1] for i in na_sa])
    chart.add("Europe Sales", [i[1] for i in eu_sa])
    chart.add("Japan Sales", [i[1] for i in jp_sa])
    chart.add("Other Sales", [i[1] for i in ot_sa])

    chart.render_to_file('sales_region.svg')

main()
