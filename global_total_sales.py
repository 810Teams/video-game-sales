#############################################################
#                                                           #
#                     Global Total Sales                    #
# NA, EU, JP, Other and Global Total Sales From 1980 - 2016 #
#                                                           #
#############################################################

import pandas, numpy, pygal #อิมพอร์ต สิ่งที่ต้องใช้เข้ามา
from pygal.style import NeonStyle #อันนี้เปลี่ยนสไตล์นะ
from project_module import project #อันนี้อันที่เซ้นท์ทำ

def main():
    """Main Function"""
    data_frame = pandas.read_csv('D:\Work\KMITL\T1_Y1_2560\PSIT\Project\Pgsales.csv') #1.เปิดFile CSV เปลี่ยนPathเอา
    NA_Sales = project.fill_missing_year(summed_sales(data_frame, 'NA_Sales')) #2.เรียกฟังก์ชั่นsummed_sales
    EU_Sales = project.fill_missing_year(summed_sales(data_frame, 'EU_Sales')) #4.fill_missing_yearคือฟังก์ชั่นที่เซ้นต์ทำ เอามาตัดปี 2017 กับ 2020 ออก
    JP_Sales = project.fill_missing_year(summed_sales(data_frame, 'JP_Sales'))
    OT_Sales = project.fill_missing_year(summed_sales(data_frame, 'Other_Sales'))
    GB_Sales = project.fill_missing_year(summed_sales(data_frame, 'Global_Sales'))
    create_chart(NA_Sales, EU_Sales, JP_Sales, OT_Sales, GB_Sales) #5.เรียกฟังก์ชั่นCreate_chart

#############################################################

def summed_sales(data_frame, zone):
    """This Function for Summed Sales of Years in Zone"""
    sum_of_sales_in_years = numpy.array(data_frame.groupby('Year', as_index=False).sum()[['Year', zone]]).tolist()
    #3.groupby คือแบบข้อมูลที่เราจะเอามาคิดอ่ะแยกตามอะไร ในที่นี้ก็ปี ส่วน.sum()คือแบบเอาค่าที่โดนgroup.ในนั้นอ่ะมาบวกกัน
    return sum_of_sales_in_years

##############################################################

def create_chart(na_sa, eu_sa, jp_sa, ot_sa, gb_sa):
    """This Function for create chart"""
    chart = pygal.Line(style=NeonStyle, x_title='Years(From 1980 - 2016)', y_title='Total Sales in Millions', x_labels_major_every=6, show_minor_x_labels=False, width=1200, height=600)
    #6.เปิดฟังก์ชั่น Lineคือรูปแบบกราฟ x_labels_major_every=6 คือโชว์ปีข้างล่างทุกๆ 6 ปี show_minor_x_labels=False คือไม่โชว์ปีเล็กๆที่เหลือ
    chart.title = "NA, EU, JP, Other and Global Total Sales From 1980 - 2016"
    chart.x_labels = [str(int(i[0])) for i in na_sa] #7.นี่คือปีในแกนข้างล่าง เลือกมาอันเดียวเพราะปีมันเท่ากันหมด
    chart.add("North America Sales", [i[1] for i in na_sa]) #8.สร้างเส้น ทำให้ครบทุกเส้น จบ!
    chart.add("Europe Sales", [i[1] for i in eu_sa])
    chart.add("Japan Sales", [i[1] for i in jp_sa])
    chart.add("Other Sales", [i[1] for i in ot_sa])
    chart.add("Global Sales", [i[1] for i in gb_sa])
    chart.render_to_file('D:/Work/KMITL/T1_Y1_2560/PSIT/Project/1st_chart.svg')

main()