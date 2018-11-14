"""
    PSIT Data Analysis Project
    Chart: Overview of Platform Types
    by Kawisara Bunyen (zelotype)
"""

import pandas, numpy, pygal
from project_module import project

def main():
    """ Main function """
    data_frame = project.platform_convert_df(pandas.read_csv('vgsales.csv'))
    create_chart(data_frame)

def create_chart(data_frame):
    """ For creating chart """
    data = numpy.array(data_frame.groupby('Platform', as_index=False).count()[['Platform', 'Rank']]).tolist()

    chart = pygal.Pie()

    for i in data:
        chart.add(i[0], [{'value': i[1], 'label': '{:.2f}%'.format(100*i[1]/sum([j[1] for j in data]))}])

    chart.legend_at_bottom = True
    chart.legend_at_bottom_columns = 3
    chart.legend_box_size = 16
    chart.render_to_file('overview_platform.svg')

main()
