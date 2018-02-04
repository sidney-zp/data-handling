import xlrd,xlwt
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


file_list = os.listdir(base_dir+"/log/handle/")
# print(file_list)

class result_to_excel(object):
    def __init__(self,s_time,e_time):
        self.s_time = s_time
        self.e_time = e_time

    def save_result_excel(self):
        my_workbook = xlwt.Workbook()

        myworkbook1 = xlrd.open_workbook((base_dir+"/log/handle/" + self.s_time + "-cmep_to_excel.xls"))
        myworkbook2 = xlrd.open_workbook((base_dir+"/log/handle/" + self.e_time + "-cmep_to_excel.xls"))
        dif_sheets = set(myworkbook1.sheet_names()) - set(myworkbook2.sheet_names())
        if dif_sheets:
            for dif_sheet in dif_sheets:
                with open(self.s_time + "-" + self.e_time + "log.txt","a") as f:
                    if dif_sheet in myworkbook1.sheet_names():
                        f.write(self.s_time + dif_sheet + "-------这个项目未找到；\n")
                    else:
                        f.write(self.e_time + dif_sheet + "-------这个项目未找到；\n")     
                

        for i in range(len(myworkbook1.sheets())):
            for j in range(len(myworkbook2.sheets())):
                if myworkbook1.sheet_names()[i] == myworkbook2.sheet_names()[j]:
                    my_sheet = my_workbook.add_sheet(myworkbook1.sheet_names()[i])

                    rows_num = myworkbook1.sheets()[i].nrows                   #获取行数
                    # print(rows_num)
                    #在每个表单的头一行添加表头
                    my_sheet.write(0,0,"数据类型")
                    my_sheet.write(0,1,"日期")
                    my_sheet.write(0,2,"数据")
                    my_sheet.write(0,3,"单位")
                    m = 1
                    n = 0
                    while n < rows_num:
                        
                        out_file = myworkbook1.sheets()[i].cell(n,0).value
                        re_time = myworkbook1.sheets()[i].cell(n,1).value
                        energy1 = float(myworkbook1.sheets()[i].cell(n,2).value)
                        unit = myworkbook1.sheets()[i].cell(n,3).value

                        energy2 = float(myworkbook2.sheets()[j].cell(n,2).value)
                        energy_output = energy2 - energy1
                        my_sheet.write(m,0,out_file)
                        my_sheet.write(m,1,re_time)
                        my_sheet.write(m,2,energy_output)
                        my_sheet.write(m,3,unit)

                        m +=1
                        n +=1

            my_workbook.save(base_dir+"/log/result/" + self.s_time + "-" + self.e_time + "result.xls")


