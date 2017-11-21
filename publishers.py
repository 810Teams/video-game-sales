"""
PSIT Data Analysis Project
Chart: Top 16 Publishers
"""

import pandas, numpy, pygal

def main():
    """ Main function """
    create_chart(pandas.read_csv('C:/Users/fuse2/Desktop/PSIT/videoGameSales.csv'))

def create_chart(data_frame):
    """ Create chart """
    ranking = sorted(numpy.array(data_frame.groupby('Publisher', as_index=False).sum()[['Publisher', 'Global_Sales']]).tolist(), key=lambda data: (data[1], data[0]), reverse=True)
    data = numpy.array(data_frame[['Publisher', 'Global_Sales', 'Name']]).tolist()

    chart = pygal.Treemap()

    for i in ranking[0:16]:
        chart.add(i[0], [{'value': j[1], 'label': j[2]} for j in data if j[0] == i[0]])

    chart.legend_at_bottom = True
    chart.render_to_file('C:/Users/fuse2/Desktop/PSIT/publishers.svg')

    getdata(ranking, data)

def getdata(ranking, data):
    """ Get specific data """
    #Print total sales of top 16 company
    _ = [print(i) for i in ranking[0:16]]

    #Print sale percentage in the game market
    allsales = sum([i[1] for i in ranking])
    _ = [print(i[0], round(i[1]/allsales, 4)) for i in ranking[0:16]]

main()
