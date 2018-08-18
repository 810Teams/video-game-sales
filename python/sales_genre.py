"""
PSIT Data Analysis Project
Chart: Sales by Genre
"""

import pandas, numpy, pygal
from project_module import project

data_frame = pandas.read_csv('vgsales.csv')

def main():
    """ Main Function """
    action = project.fill_missing_year(summed_genre_sales('Action'))
    adventure = project.fill_missing_year(summed_genre_sales('Adventure'))
    figthing = project.fill_missing_year(summed_genre_sales('Fighting'))
    misc = project.fill_missing_year(summed_genre_sales('Misc'))
    platform = project.fill_missing_year(summed_genre_sales('Platform'))
    puzzle = project.fill_missing_year(summed_genre_sales('Puzzle'))
    racing = project.fill_missing_year(summed_genre_sales('Racing'))
    role_playing = project.fill_missing_year(summed_genre_sales('Role-Playing'))
    shooter = project.fill_missing_year(summed_genre_sales('Shooter'))
    simulation = project.fill_missing_year(summed_genre_sales('Simulation'))
    sports = project.fill_missing_year(summed_genre_sales('Sports'))
    strategy = project.fill_missing_year(summed_genre_sales('Strategy'))
    create_chart(action, adventure, figthing, misc, platform, puzzle, racing, role_playing, shooter, simulation, sports, strategy)

#############################################################

def summed_genre_sales(genre):
    """ This Function for Summed Sales of Years in Zone """
    genre_sales = []
    all_genre_list = numpy.array(data_frame.groupby(['Year', 'Genre'], as_index=False).sum()[['Year', 'Genre', 'Global_Sales']]).tolist()
    for i in all_genre_list:
        selected = [i[0], i[2]]
        if i[1] == genre:
            genre_sales.append(selected)
    return genre_sales

##############################################################

def create_chart(ac, ad, fi, mi, pl, pu, ra, ro, sh, si, sp, st):
    """ This Function for create chart """
    chart = pygal.StackedLine(dots_size=1.75, legend_at_bottom=True, interpolate='cubic', fill=True)

    chart.x_title = 'Year'
    chart.y_title = 'Sales (in millions)'

    chart.x_labels = [i for i in range(1980, 2017)]
    chart.x_labels_major_count = 8
    chart.show_minor_x_labels = False
    chart.y_labels = [i for i in range(0, 701, 100)]
    chart.truncate_label = 5
    chart.legend_box_size = 16

    chart.add("Action", [i[1] for i in ac])
    chart.add("Adventure", [i[1] for i in ad])
    chart.add("Fighting", [i[1] for i in fi])
    chart.add("Misc", [i[1] for i in mi])
    chart.add("Platform", [i[1] for i in pl])
    chart.add("Puzzle", [i[1] for i in pu])
    chart.add("Racing", [i[1] for i in ra])
    chart.add("Role-Playing", [i[1] for i in ro])
    chart.add("Shooter", [i[1] for i in sh])
    chart.add("Simulation", [i[1] for i in si])
    chart.add("Sports", [i[1] for i in sp])
    chart.add("Strategy", [i[1] for i in st])

    chart.render_to_file('sales_genre.svg')

main()
