##########################################################
#                                                        #
# NA, EU, JP, other and Global sales summed in each year #
#                                                        #
##########################################################

import pandas, numpy, pygal
from pygal.style import RedBlueStyle
from project_module import project

##########################################################

def main():
    """Main Function"""
    data_frame = pandas.read_csv('D:\Work\KMITL\T1_Y1_2560\PSIT\Project\Pgsales.csv')
    NA_Sales = project.fill_missing_year(summed_sales(data_frame, 'NA_Sales'))
    EU_Sales = project.fill_missing_year(summed_sales(data_frame, 'EU_Sales'))
    JP_Sales = project.fill_missing_year(summed_sales(data_frame, 'JP_Sales'))
    OT_Sales = project.fill_missing_year(summed_sales(data_frame, 'Other_Sales'))
    GB_Sales = project.fill_missing_year(summed_sales(data_frame, 'Global_Sales'))
    create_chart(NA_Sales, EU_Sales, JP_Sales, OT_Sales, GB_Sales)

##########################################################

def summed_sales(data_frame, zone):
    """This Function for Summed Sales of Years in Zone"""
    sum_of_sales_in_years = numpy.array(data_frame.groupby('Year', as_index=False).sum()[['Year', zone]]).tolist()
    return sum_of_sales_in_years

###########################################################

def create_chart(na_sa, eu_sa, jp_sa, ot_sa, gb_sa):
    """This Function for create chart"""
    chart = pygal.StackedLine(style = RedBlueStyle,dots_size=2, truncate_label=5, legend_at_bottom=True, interpolate='cubic', fill=True, x_title='Year', y_title='Sales (in millions)', x_labels_major_count=8, show_minor_x_labels=False)
    chart.title = "NA, EU, JP, Other and Global Total Sales From 1980 - 2016"
    chart.x_labels = [i for i in range(1980, 2017)]
    chart.add("North America Sales", [i[1] for i in na_sa])
    chart.add("Europe Sales", [i[1] for i in eu_sa])
    chart.add("Japan Sales", [i[1] for i in jp_sa])
    chart.add("Other Sales", [i[1] for i in ot_sa])
    chart.add("Global Sales", [i[1] for i in gb_sa])
    chart.render_to_file('D:/Work/KMITL/T1_Y1_2560/PSIT/Project/sales_region.svg')

main()