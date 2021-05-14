"""trt_mtcnn.py

This script demonstrates how to do real-time face detection with
Cython wrapped TensorRT optimized MTCNN engine.
"""
import time
import argparse
import cv2 as cv
# import sys
# sys.path.append('/home/thaivu/Projects/tensorrt_demos')

from utils.camera import add_camera_args, Camera
from utils.display import open_window, set_display, show_fps
from utils.mtcnn import TrtMtcnn
import os

PATH_RESULT = r"/home/thaivu/Projects/Face_Detection-Recognition/TRT_MTCNN/Benchmark_Result"
PATH_READ_FOLDER = r"/home/thaivu/Projects/Face_Detection-Recognition/WIDERFACE/Splited_Images"


def show_faces(boxes, landmarks):
    """Draw bounding boxes and face landmarks on image."""
    count = 1
    for bb, _ in zip(boxes, landmarks):
        x1, y1, x2, y2 = int(bb[0]), int(bb[1]), int(bb[2]), int(bb[3])
        w = x2 - x1
        h = y2 - y1
        print("face ID: {}".format(count))
        print("confidence= {}; x1= {}, y1= {}; w= {}, h={}".format(float(bb[4]),x1,y1,w,h))
        count += 1

def writeFacesResult(temp_image_name, boxes, landmarks):
    temp_image_name = temp_image_name.strip(".jpg")
    with open( PATH_RESULT + r"/" + temp_image_name + r".txt", "w") as write_f:
        for bb, _ in zip(boxes, landmarks):
            x1, y1, x2, y2 = int(bb[0]), int(bb[1]), int(bb[2]), int(bb[3])
            w = x2 - x1
            h = y2 - y1
            write_f.write("face {} {} {} {} {}\n".format(float(bb[4]), x1, y1, w, h))


def main():
    for temp_image_name in os.listdir(PATH_READ_FOLDER):
        temp_image = cv.imread(PATH_READ_FOLDER + r"/" + temp_image_name)

        mtcnn = TrtMtcnn()
        boxes, landmarks = mtcnn.detect(temp_image)
        # show_faces(boxes, landmarks)
        writeFacesResult(temp_image_name, boxes, landmarks)

if __name__ == '__main__':
    main()
