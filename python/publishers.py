"""
    PSIT Data Analysis Project
    Chart: Top 16 Publishers
    by Teerapat Kraisrisirikul (810Teams)
"""

import pandas, numpy, pygal

def main():
    """ Main function """
    create_chart(pandas.read_csv('vgsales.csv'))

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

    # get_data(ranking, data) # Turn off comment to get more data
    # get_html(ranking, data) # Turn off comment to get more data

def get_data(ranking, data):
    """ Get data """
    #All sales
    allsales = sum([i[1] for i in ranking])

    #Sales and percent of top 16
    for i in ranking[0:16]:
        print('{:>38} - {:.2f} million sales ({:.2f}%)'.format(i[0], i[1], (i[1]/allsales)*100))

    print('Others - {:.2f} million sales ({:.2f}%)'.format(sum([i[1] for i in ranking[16:]]), sum([i[1] for i in ranking[16:]])/allsales*100))

    #Total percent of top 16
    print('Top 16 - {:.2f}%'.format(sum([(i[1]/allsales)*100 for i in ranking[0:16]])))

    print('Total Companies -', len(ranking))

def get_html(ranking, data):
    """ Get HTML-formatted data """
    #All sales
    allsales = sum([i[1] for i in ranking])

    #Sales and percent of top 16
    print('<center><table>')

    for i in ranking[0:16]:
        print('<tr><td><b>{}</b></td><td style=\"text-indent: 1em;\">{:.2f} million sales <i>({:.2f}%)</i></td></tr>'.format(i[0], i[1], (i[1]/allsales)*100))

    print('<tr><td><b>Others</b></td><td style=\"text-indent: 1em;\">{:.2f} million sales <i>({:.2f}%)</i></td></tr>'.format(sum([i[1] for i in ranking[16:]]), sum([i[1] for i in ranking[16:]])/allsales*100))
    print('</table></center>')

main()
