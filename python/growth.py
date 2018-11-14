"""
    PSIT Data Analysis Project
    Chart: Growth of Video Games Amount
    by Supakit Theanthunyakit (POKINBKK)
"""

import pandas, numpy, pygal
from pygal.style import CleanStyle
from project_module import project

data_frame = pandas.read_csv('vgsales.csv')
df_change_platform = project.platform_convert_df(data_frame)
year_pf_list = numpy.array(df_change_platform[['Year','Platform']]).tolist()

def main():
    """ Main function """
    df_change_platform = project.platform_convert_df(data_frame)
    game_type = ['Home Video Game Consoles','Handheld Game Consoles', 'Microsoft Windows']
    game_in_years = numpy.array(data_frame.groupby('Year', as_index=False).count()[['Year', 'Rank']]).tolist()
    g_in_year = numpy.array(data_frame.groupby('Year', as_index=False).count()[['Year', 'Rank']]).tolist()

    for i in range(len(game_in_years)):
        if i == 0:
            continue
        else:
            game_in_years[i][1] += game_in_years[i-1][1]

    game_in_years = project.fill_missing_year(game_in_years)

    amount_of_HVGC = pf_count_by_all('Home Video Game Consoles')
    amount_of_HHGC = pf_count_by_all('Handheld Game Consoles')
    amount_of_MSW = pf_count_by_all('Microsoft Windows')

    create_chart(amount_of_HVGC, amount_of_HHGC, amount_of_MSW)

def pf_count_by_all(platform):
    """ Count game in a specific Platform in Each year """
    amount = []
    count = 0
    for i in range(1980, 2017):
        for item in year_pf_list:
            if item[0] == i and item[1] == platform:
                count += 1
        amount.append(count)
    return amount

def create_chart(hvgc, hhgc, msw):
    """ Create chart """
    chart = pygal.StackedBar(truncate_label=5, style=CleanStyle, fill=True, dots_size=1.75, interpolate='cubic')

    chart.x_title = 'Year'
    chart.y_title = 'Video Games Amount'

    chart.x_labels = [i for i in range(1980, 2017)]
    chart.x_labels_major_count = 8
    chart.show_minor_x_labels = False
    chart.y_labels = [i for i in range(0, 18001, 2000)]

    chart.legend_at_bottom = True
    chart.legend_at_bottom_columns = 3
    chart.legend_box_size = 16

    chart.add("Home Video Game Consoles", hvgc)
    chart.add("Handheld Game Consoles", hhgc)
    chart.add("Microsoft Windows", msw)

    chart.render_to_file('growth.svg')

main()
