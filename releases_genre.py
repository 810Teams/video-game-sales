import numpy
import pandas
import pygal
from project_module import project
def main():
    """This function is read data """
    data_game = pandas.read_csv("vgsales.csv")
    data_Year = numpy.array(data_game.groupby(["Genre", "Year"], as_index=False).count()[["Genre","Year", "Rank"]]).tolist()
    data_Genre = [i for i in (data_game.groupby(["Genre"], as_index=False).count()["Genre"]).tolist()]
    chart = pygal.Dot()
    chart.x_labels = range(1980, 2017)
    chart.x_labels_major_count = 8
    chart.show_minor_x_labels = False
    chart.truncate_label = 5
    chart.legend_at_bottom = True
    chart.x_title = "Years"
    chart.y_title  ="Genres"
    chart.title = "Each Genre of games count in each year"
    for i in data_Genre:
        temp = project.fill_missing_year([[j[1], j[2]] for j in data_Year if j[0] == i])
        #print(i, [j[1] for j in temp])
        chart.add(i, [j[1] for j in temp])
    chart.render_to_file("project.svg")
main()
