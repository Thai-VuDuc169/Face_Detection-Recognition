import os
import sys
import pathlib
from tqdm import tqdm
import shutil

current_folder_path = str(pathlib.Path(__file__).parent.absolute())
os.chdir(current_folder_path)
print("Hello {}!, the current folder path is '{}' in this system"
      .format(os.getlogin(), os.getcwd()))

PATH_READ_FOLDER = current_folder_path + r"\WIDERFACE\Images"
PATH_WRITE_FOLDER = current_folder_path + r"\WIDERFACE\Splited_Images"


# for sub_folder in tqdm(os.listdir(current_folder_path + PATH_READ_FOLDER)):
sub_folder = os.listdir(PATH_READ_FOLDER)[0]
for file in os.listdir( PATH_READ_FOLDER + "\\" + sub_folder ):
   shutil.copyfile( PATH_READ_FOLDER + r"\{}\{}".format(sub_folder,file) , 
                     PATH_WRITE_FOLDER)

