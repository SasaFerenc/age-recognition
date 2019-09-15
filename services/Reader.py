import pandas as pd
import math as math
import numpy as np
import scipy.io as scio
import os
from keras.models import load_model

resources_path = r"E:\Projects\NeuralNetwork\resources\\"


def read_dataset(dataset_path, start_from, end_file_name):
    print(">>Reading dataset from " + dataset_path + "<<")
    images = []
    for file_num in range(start_from, end_file_name):
        file_path = dataset_path + "\\" + get_file_num_path(file_num)
        print("Path: " + file_path)
        images.append(list_all_images(file_path))

    return images

def list_all_images(file_path):
    files = []
    for root, directory, images in os.walk(file_path):
        for image in images:
            if '.jpg' in image:
                files.append(os.path.join(root, image))
    return files


def get_file_num_path(file_num):
    if file_num < 10:
        return "0" + str(file_num)
    return str(file_num)


def save_model(model, file_name):
    print(">>Saving model<<")
    model.save(resources_path + file_name)

def read_model(file_name):
    print(">>Loading model<<")
    return load_model(resources_path + file_name)

# def mat_to_csv():
#     imdb_mat_file = "imdb.mat"
#     print(">>Reading .mat file<<")
#     mat_file = scio.loadmat(dataset_path + "\\" + imdb_mat_file)
#     print(">>Converting to .csv<<")
#     for line in mat_file:
#         print(line)
#         #if '__' not in line and 'readme' not in line:
#          #   np.savetxt((dataset_path + "\\" + line + ".csv"), mat_file[line], fmt='%s', delimiter=',')
#     print(">>Converting finished<<")