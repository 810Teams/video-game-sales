import numpy
import pygal
import pandas
from project_module import project as pj

def main():
    """create chart platform type of games count in each year """
    data_game = pandas.read_csv('vgsales.csv')
    data_game = pj.platform_convert_df(data_game)
    data_Year = numpy.array(data_game.groupby(["Platform", "Year"], as_index=False).count()[["Platform","Year", "Rank"]]).tolist()
    data_platform = [i for i in (data_game.groupby(["Platform"], as_index=False).count()["Platform"]).tolist()]
    chart = pygal.Dot()
    chart.x_labels = range(1980, 2017)
    chart.x_labels_major_count = 8
    chart.show_minor_x_labels = False
    chart.truncate_label = 5
    chart.legend_at_bottom = True
    chart.x_title = "Years"
    chart.y_title  ="Platforms"
    chart.title = "Each Platform type of games count in each year"
    for i in data_platform:
        temp = pj.fill_missing_year([[j[1], j[2]] for j in data_Year if j[0] == i])
        chart.add(i, [j[1] for j in temp])
    chart.render_to_file("Platforms.svg")
main()