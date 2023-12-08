import json
import shutil
import os

source_directory = 'images'
train_folder = 'data/custom/train2017'
validate_folder = 'data/custom/val2017'
parent_folder_path = 'data/custom'


if __name__== "__main__":
    images = os.listdir(source_directory)
    os.makedirs(os.path.join(parent_folder_path, 'val2017'))
    
    with open('data/custom/annotations/custom_val.json') as file:
        validation = json.load(file)
        
    validation_set = set()
    for image in validation['images']:
        validation_set.add(image['file_name'])
        
    for file_name in validation_set:
        source_file = os.path.join(source_directory, file_name)
        destination_file = os.path.join(validate_folder, file_name)
        shutil.move(source_file, destination_file)
        
    os.rename('images', os.path.join(os.path.dirname('images'), 'train2017'))
    
    shutil.move('train2017', train_folder)
