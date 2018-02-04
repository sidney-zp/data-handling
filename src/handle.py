import os,json
import xlwt

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#打开当前文件所在目录的settings.json文件
with open(base_dir + "/config/settings.json","r") as f1:
    settings = json.load(f1)


class HandleData(object):
    def __init__(self,start_time):
        self.start_time = start_time
        self.file_list = os.listdir(base_dir+"/log/data/" + self.start_time)

    def saveexcel(self):
        #以写的形式打开一个workbook
        my_workbook = xlwt.Workbook()

        for filename in self.file_list:
            year = filename.split("_")[-2][:4]
            date = filename.split("_")[-2][2:8]
            project_name = filename.split("_GHP")[0].split("SSTJEC_")[1]
            my_sheet = my_workbook.add_sheet(project_name)

            #从json文件中获取到每个项目的配置文件，然后下载相应的行到Excel里
            for setting in settings["items"]:

                if project_name == setting["item"]:

                    with open(base_dir+"/log/data/" + self.start_time +"/" + filename) as f2:
                        lines = f2.readlines()
                        step = 0

                        #把所需要的数据写到Excel中
                        for nums,line in enumerate(lines):
                            if nums in setting["download_line"]:
                                re_time = line.split(",")[6]
                                out_file = line.split(",")[7]
                                energy = line.split(",")[-2]
                                unit = line.split(",")[10]

                                my_sheet.write(step,0,out_file)
                                my_sheet.write(step,1,re_time)
                                my_sheet.write(step,2,energy)
                                my_sheet.write(step,3,unit)
                                step += 1

        my_workbook.save(base_dir+"/log/handle/" + self.start_time +"-cmep_to_excel.xls")
        





