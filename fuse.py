import pandas, numpy, pygal
from pygal.style import NeonStyle
from project_module import project

data_frame = pandas.read_csv('C:/Users/fuse2/Desktop/GIT PSIT/Video-Game-Sales/videoGameSales.csv')

def main():
    """Main Function"""
    genre_list = numpy.array(data_frame.groupby('Genre', as_index=False).count()['Genre']).tolist()
    year_list = numpy.array(data_frame.groupby('Year', as_index=False).count()['Year']).tolist()
    action_count = count_by_year('Action')
    adventure_count = count_by_year('Adventure')
    fighting_count = count_by_year('Fighting')
    misc_count = count_by_year('Misc')
    platform_count = count_by_year('Platform')
    puzzle_count = count_by_year('Puzzle')
    racing_count = count_by_year('Racing')
    role_count = count_by_year('Role-Playing')
    shooter_count = count_by_year('Shooter')
    simulation_count = count_by_year('Simulation')
    sports_count = count_by_year('Sports')
    strategy_count = count_by_year('Strategy')
    create_chart(action_count, adventure_count, fighting_count, misc_count, platform_count\
    , puzzle_count, racing_count, role_count, shooter_count, simulation_count, sports_count, strategy_count)

def count_by_year(genre):
    """This Function for Summed Sales of Years in Zone"""
    year_genre_list = numpy.array(data_frame[['Year','Genre']]).tolist()
    year_count = []
    for i in range(1980, 2017):
        count = 0
        for item in year_genre_list:
            if genre == item[1] and i == item[0]:
                count += 1
        year_count.append(count)
    return year_count

def create_chart(action_count, adventure_count, fighting_count, misc_count, platform_count, puzzle_count, racing_count, role_count, shooter_count, simulation_count, sports_count, strategy_count):
    """This Function for create chart"""
    chart = pygal.Dot(style=NeonStyle, x_title='Years(From 1980 - 2016)', y_title='Each game in the year', x_labels_major_every=6, show_minor_x_labels=False, width=1200, height=600)
    
    chart.title = "Each genre of games gobla sale summed in each year"
    chart.x_labels = [i for i in range(1980, 2017)]
    chart.add("action", action_count)
    chart.add("adventure", adventure_count)
    chart.add("fighting", fighting_count)
    chart.add("misc", misc_count)
    chart.add("platform", platform_count)
    chart.add("puzzle", puzzle_count)
    chart.add("racing", racing_count)
    chart.add("role-Playing", role_count)
    chart.add("shooter", shooter_count)
    chart.add("simulation", simulation_count)
    chart.add("sports", sports_count)
    chart.add("strategy", strategy_count)
    chart.render_to_file('C:/Users/fuse2/Desktop/GIT PSIT/Video-Game-Sales/each_genre_byfuse.svg')
main()
    