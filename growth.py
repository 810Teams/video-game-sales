####################################################
#                                                  #
# Each Platform type of games stacked in each year #
#                                                  #
####################################################

import pandas, numpy, pygal
from pygal.style import RedBlueStyle
from project_module import project

data_frame = data_frame = pandas.read_csv('D:\Work\KMITL\T1_Y1_2560\PSIT\Project\Pgsales.csv')
df_chage_platform = project.platform_convert_df(data_frame)
year_pf_list = numpy.array(df_chage_platform[['Year','Platform']]).tolist()

####################################################

def main():
    """This is Main Function"""
    df_chage_platform = project.platform_convert_df(data_frame)
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

####################################################

def pf_count_by_all(platform):
    """This Function for count Game in a specific Platform in Each year"""
    amount = []
    count = 0
    for i in range(1980, 2017):
        for item in year_pf_list:
            if item[0] == i and item[1] == platform:
                count += 1
        amount.append(count)
    return amount

####################################################

def create_chart(hvgc, hhgc, msw):
    """This Function for create chart"""
    chart = pygal.StackedLine(fill=True, width=1200, shows_dot=False, interpolate='cubic', title=u'Each Platform type of games stacked in each year', x_title='Years(From 1980 - 2016)', x_labels_major_every=6, show_minor_x_labels=False, legend_at_bottom=True, legend_at_bottom_columns=3, legend_box_size=20, style=RedBlueStyle)
    chart.x_labels = [i for i in range(1980, 2017)]
    chart.add("Home Video Game Consoles", hvgc)
    chart.add("Handheld Game Consoles", hhgc)
    chart.add("Microsoft Windows", msw)
    chart.render_to_file('D:/Work/KMITL/T1_Y1_2560/PSIT/Project/growth.svg')

main()