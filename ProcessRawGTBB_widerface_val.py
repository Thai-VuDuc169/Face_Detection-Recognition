import numpy as np
import os
import sys
import pathlib

current_folder_path = str(pathlib.Path(__file__).parent.absolute())
print("Hello {}!, the current folder path is '{}' in this system"
      .format(os.getlogin(), current_folder_path ))

PATH_READ_FILE = r"\WIDERFACE\wider_face_val_bbx_gt.txt"
PATH_WRITE_FOLDER = r"\WIDERFACE\Processed_WIDERFACEValidation"


with open(current_folder_path + PATH_READ_FILE, "r") as read_f:
      while True:            
            temp_file_name = read_f.readline()
            if not temp_file_name:
                  break
            temp_file_name = temp_file_name.strip(".jpg\n").split("/")[1]
            num_faces = int(read_f.readline().strip())
            with open(current_folder_path + PATH_WRITE_FOLDER + "\\" + temp_file_name + r".txt", "w") as write_f:
            # print(current_folder_path + PATH_WRITE_FOLDER + "\\" + temp_file_name + r".txt")
                  for i in range(num_faces):
                        temp_line = read_f.readline().strip().split(" ")
                        x = temp_line[0]
                        y = temp_line[1]
                        w = temp_line[2]
                        h = temp_line[3]
                        # print("face {} {} {} {}\n".format(x,y,w,h))
                        write_f.write("face {} {} {} {}\n".format(x,y,w,h))