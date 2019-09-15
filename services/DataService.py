import services.Reader as reader
import cv2

dataset_path = r"E:\Projects\DataSets\age_recognition\wiki_crop"

which_data = r"\test"
start_from = 85
end_file_name = 21
number_of_imgs_per_cat = 50

#training >>Finished at file: 73<< 2000
#validation from 73 >>Finished at file: 85<< 300
#test from 85 >>Finished at file: 88<< 50

data_path_20 = r"E:\Projects\DataSets\age_recognition\using" + which_data + r"\_20"
data_path_21_35 = r"E:\Projects\DataSets\age_recognition\using" + which_data + r"\21_35"
data_path_36_60 = r"E:\Projects\DataSets\age_recognition\using" + which_data + r"\36_60"
data_path_60_ = r"E:\Projects\DataSets\age_recognition\using" + which_data + r"\60_"

data_training = r"E:\Projects\DataSets\age_recognition\using\training"
data_validation = r"E:\Projects\DataSets\age_recognition\using\validation"
data_test = r"E:\Projects\DataSets\age_recognition\using\test"

def transfer_image(image, category_path):
    print(image)
    img = cv2.imread(image)

    if img.shape[0] < 5:
        return False

    cv2.imwrite(category_path + "\\" + image.split("\\")[-1], img)
    return True

def get_age(image_path):
    image_name = image_path.split("\\")[-1].split("_")
    born = int(image_name[1].split("-")[0])
    pic_taken = int(image_name[2].split(".jpg")[0])
    return pic_taken - born

