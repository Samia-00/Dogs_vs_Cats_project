import os

import os

nb_train_samples = 25000
nb_test_samples = 12500
nb_classes = 2

img_size = 200
img_channel = 3
img_shape =(img_size,img_size,img_channel)
lr = 0.001
batch_size = 200
nb_epochs = 60

def root_path():
    return os.path.dirname(__file__)

def checkpoint_path():
    return os.path.join(root_path(),"checkpoint")

def dataset_path():
    return os.path.join(root_path(),"dataset")

def src_path():
    return os.path.join(root_path(),"src")

def submission_path():
    return os.path.join(root_path(),"submission")

def output_path():
    return os.path.join(root_path(),"output")

print(src_path())