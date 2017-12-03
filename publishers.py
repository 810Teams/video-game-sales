"""
PSIT Data Analysis Project
Chart: Top 16 Publishers
"""

import pandas, numpy, pygal

def main():
    """ Main function """
    create_chart(pandas.read_csv('videoGameSales.csv'))

def create_chart(data_frame):
    """ Create chart """
    ranking = sorted(numpy.array(data_frame.groupby('Publisher', as_index=False).sum()[['Publisher', 'Global_Sales']]).tolist(), key=lambda data: (data[1], data[0]), reverse=True)
    data = numpy.array(data_frame[['Publisher', 'Global_Sales', 'Name']]).tolist()

    chart = pygal.Treemap()

    for i in ranking[0:16]:
        chart.add(i[0], [{'value': j[1], 'label': j[2]} for j in data if j[0] == i[0]])

    chart.legend_at_bottom = True
    chart.truncate_legend = 19
    chart.legend_box_size = 16
    chart.render_to_file('publishers.svg')

    #getdata(ranking, data)

def getdata(ranking, data):
    """ Get data """
    #All sales
    allsales = sum([i[1] for i in ranking])

    #Sales and percent of top 16
    _ = [print('{:>38} - {:.2f} million sales ({:.2f}%)'.format(i[0], i[1], (i[1]/allsales)*100)) for i in ranking[0:16]]
    print('Others - {:.2f} million sales ({:.2f}%)'.format(sum([i[1] for i in ranking[16:]]), sum([i[1] for i in ranking[16:]])/allsales*100))

    #Total percent of top 16
    print(sum([(i[1]/allsales)*100 for i in ranking[0:16]]))

main()
