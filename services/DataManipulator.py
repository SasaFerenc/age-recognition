import services.DataService as ds
import services.Reader as r

def split_data_num():
    category_0 = []
    category_1 = []
    category_2 = []
    category_3 = []

    file_num = ds.start_from
    while not isCategoryFull(category_0, category_1, category_2, category_3) or file_num >= 99:
        file_path = ds.dataset_path + "\\" + r.get_file_num_path(file_num)
        file_num += 1
        print("Path: " + file_path)
        all_files = r.list_all_images(file_path)

        for image in all_files:
            age = ds.get_age(image)

            if age <= 0:
                continue

            category_0 = append_to_cat(image, age, 20, category_0, ds.data_path_20)
            category_1 = append_to_cat(image, age, 35, category_1, ds.data_path_21_35)
            category_2 = append_to_cat(image, age, 60, category_2, ds.data_path_36_60)
            category_3 = append_to_cat(image, age, 9999, category_3, ds.data_path_60_)

    print(">>Finished at file: "+str(file_num)+"<<")

def append_to_cat(image, age, limit, category, path):
    if age < limit and category.__len__() < ds.number_of_imgs_per_cat:
        if ds.transfer_image(image, path):
            category.append(image)
    return category


def isCategoryFull(c0, c1, c2, c3):
    return c0.__len__() == ds.number_of_imgs_per_cat and c1.__len__() == ds.number_of_imgs_per_cat \
           and c2.__len__() == ds.number_of_imgs_per_cat and c3.__len__() == ds.number_of_imgs_per_cat
