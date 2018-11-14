"""
    PSIT Data Analysis Project
    Chart: Releases by Genre
    by Kazuya Komatsu (yakung)
"""

import numpy, pandas, pygal
from project_module import project

def main():
    """ Main function """
    data_game = pandas.read_csv("vgsales.csv")
    data_year = numpy.array(data_game.groupby(["Genre", "Year"], as_index=False).count()[["Genre", "Year", "Rank"]]).tolist()
    data_genre = [i for i in (data_game.groupby(["Genre"], as_index=False).count()["Genre"]).tolist()]

    chart = pygal.StackedLine(fill=True, interpolate='cubic', dots_size=1.75)
    chart.x_labels = range(1980, 2017)
    chart.x_labels_major_count = 8
    chart.show_minor_x_labels = False
    chart.y_labels = [i for i in range(0, 1601, 200)]
    chart.y_labels_major_every = 5
    chart.truncate_label = 5
    chart.legend_at_bottom = True
    chart.legend_box_size = 16
    chart.x_title = "Year"
    chart.y_title = "Video Games Amount"

    for i in data_genre:
        temp = project.fill_missing_year([[int(float(j[1])), j[2]] for j in data_year if j[0] == i])
        chart.add(i, [j[1] for j in temp])

    chart.render_to_file("releases_genre.svg")

main()
