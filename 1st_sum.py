##############################################################
#                                                            #
#                    Global sales Summed                     #
# NA, EU, JP, Other and Global Sales Summed From 1980 - 2016 #
#                                                            #
##############################################################

import pandas, numpy, pygal
from pygal.style import NeonStyle
from project_module import project

def main():
    """Main Function"""
    data_frame = pandas.read_csv('D:\Work\KMITL\T1_Y1_2560\PSIT\Project\Pgsales.csv')
    NA_Sales = project.fill_missing_year(summed_sales(data_frame, 'NA_Sales'))
    EU_Sales = project.fill_missing_year(summed_sales(data_frame, 'EU_Sales'))
    JP_Sales = project.fill_missing_year(summed_sales(data_frame, 'JP_Sales'))
    OT_Sales = project.fill_missing_year(summed_sales(data_frame, 'Other_Sales'))
    GB_Sales = project.fill_missing_year(summed_sales(data_frame, 'Global_Sales'))
    create_chart(NA_Sales, EU_Sales, JP_Sales, OT_Sales, GB_Sales)

##############################################################

def summed_sales(data_frame, zone):
    """This Function for Summed Sales of Years in Zone"""
    sum_of_sales_in_years = numpy.array(data_frame.groupby('Year', as_index=False).sum()[['Year', zone]]).tolist()

    return sum_of_sales_in_years

###############################################################

def create_chart(na_sa, eu_sa, jp_sa, ot_sa, gb_sa):
    """This Function for create chart"""
    chart = pygal.Line(style=NeonStyle)
    chart.title = "NA, EU, JP, Other and Global Sales Summed From 1980 - 2016"
    chart.x_labels = [str(int(i[0])) for i in na_sa]
    chart.add("North America Sales", [i[1] for i in na_sa])
    chart.add("Europe Sales", [i[1] for i in eu_sa])
    chart.add("Japan Sales", [i[1] for i in jp_sa])
    chart.add("Other Sales", [i[1] for i in ot_sa])
    chart.add("Global Sales", [i[1] for i in gb_sa])
    chart.render_to_file('1st_chart.svg')

###############################################################

def remove_2017_2020_year(sales):
    for item in sales:
        if [-1] == 2017.0:
            sales.pop(-1)
        if item[0] == 2020.0:
            sales.remove(item)

    return sales


main()