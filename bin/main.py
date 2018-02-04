from src.download import DownloadFile
from src.handle import HandleData
from src.result import result_to_excel

import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_list = os.listdir(base_dir + '/log/data/')
time_list = []

def main():
    while True:
        input_time = input("请输入想要下载文件的日期（格式：20170101）：\n")
        if input_time != "q":
            if str(input_time) in file_list:
                time_list.append(input_time)
                print("您想要的已经下载过，是否还需要继续进行下载，如果是请输如相同格式的日期时间，否请输入'q':\n")
            else:
                download_file = DownloadFile(input_time)
                download_file.save_file()
                time_list.append(input_time)
                print("您是否还想继续下载，如果是请输如相同格式的日期时间，否请输入'q':\n")
        else:
            break

        handle_file = HandleData(input_time)
        handle_file.saveexcel()

    result_to_file = result_to_excel(time_list[0],time_list[-1])
    result_to_file.save_result_excel()

