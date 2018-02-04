""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

------------------本文件是用于写单独的settings.json文件，一般不需要运行--------------------------

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


import json
import os,sys

base_dir = os.path.dirname(os.path.abspath(__file__))
print(base_dir)
sys.path.append(base_dir)


file_list = os.listdir(base_dir + "/data/")
# print(file_list)

output_data = {"items":[]}

for filename in file_list:
    with open(base_dir + "/data/" + filename) as f:
        lines = f.readlines() 
        # print(lines)
        line_number = []
        for nums,line in enumerate(lines):
            if line.split(",")[7].split("|")[1] == "121" or line.split(",")[7].split("|")[1] == "123" or line.split(",")[7].split("|")[1] == "3204":
                line_number.append(nums)
               
        out_filename = filename.split("_GHP")[0].split("SSTJEC_")[1]
        print(out_filename)
        data = {"item":out_filename,"download_line":line_number}
        output_data["items"].append(data)
        
with open("settings.json","w") as f1:
    json.dump(output_data,f1)
                

                