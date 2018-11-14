"""
    PSIT Data Analysis Project
    Chart: Releases by Platform Type
    by Kazuya Komatsu (yakung)
"""

import numpy, pygal, pandas
from project_module import project as pj

def main():
    """create chart platform type of games count in each year """
    data_game = pandas.read_csv('vgsales.csv')
    data_game = pj.platform_convert_df(data_game)
    data_Year = numpy.array(data_game.groupby(["Platform", "Year"], as_index=False).count()[["Platform","Year", "Rank"]]).tolist()
    data_platform = [i for i in (data_game.groupby(["Platform"], as_index=False).count()["Platform"]).tolist()]
    overall = numpy.array(data_game.groupby(["Year"], as_index=False).count()[["Year","Name"]]).tolist()
    yearss = numpy.array(data_game.groupby(["Year"], as_index=False).count()["Year"]).tolist()
    data_Year1 = pj.fill_missing_year(overall)
    value = []

    for i in data_Year1:
        value.append(i[1])

    chart = pygal.StackedLine(fill=True, interpolate='cubic', dots_size=1.75)
    chart.x_labels = range(1980, 2017)
    chart.x_labels_major_count = 8
    chart.show_minor_x_labels = False
    chart.truncate_label = 5
    chart.y_labels = [i for i in range(0, 1601, 200)]
    chart.y_labels_major_every = 5
    chart.legend_at_bottom = True
    chart.legend_at_bottom_columns = 3
    chart.legend_box_size = 16
    chart.x_title = "Year"
    chart.y_title = "Video Games Amount"

    for i in ['Home Video Game Consoles', 'Handheld Game Consoles', 'Microsoft Windows']:
        temp = pj.fill_missing_year([[j[1], j[2]] for j in data_Year if j[0] == i])
        chart.add(i, [j[1] for j in temp])

    chart.render_to_file("releases_platform.svg")

main()
