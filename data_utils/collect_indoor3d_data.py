import os
import sys
from indoor3d_util import DATA_PATH, collect_point_label
import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)

# Create folder if not exist to save in .npy type
output_folder = os.path.join(ROOT_DIR, 'data/stanford_indoor3d')
if not os.path.exists(output_folder):
    os.mkdir(output_folder)


dataset_root = os.path.join(ROOT_DIR, 'data/MyDataset')
# Check all the files in the directory MyDataset
files_path = os.listdir(os.path.join(ROOT_DIR, 'data/MyDataset'))
original_size  = len(files_path)
test_size = 0.2 * original_size
begin_test = original_size - test_size
for k, ply_file in enumerate(files_path):
    try:
        k = k + 1
        print(k)
        if k < begin_test:
            out_filename = os.path.splitext(os.path.basename('Area_' + ply_file))[0] +'.npy' # input_pc.npy
        else:
            out_filename = os.path.splitext(os.path.basename('Area_5_' + ply_file))[0] +'.npy' # input_5_pc.npy
      
        collect_point_label(os.path.join(dataset_root, ply_file), os.path.join(output_folder, out_filename), 'numpy')
    except:
        print(ply_file, 'ERROR!!')
