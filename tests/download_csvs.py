import boto3
import os

BUCKET_NAME = 'noodle-finder'
OBJECT_NAME = 'caxton/data/'
CSV_NAMES = ['caxton_dataset_filtered.csv',
                'caxton_dataset_filtered_no_outliers.csv',
                'caxton_dataset_filtered_no_outliers_img_info.csv',
                'caxton_dataset_final.csv',
                'caxton_dataset_full.csv']
OUT_DIR = 'data/caxton_dataset/'

s3 = boto3.client('s3')
for csv_name in CSV_NAMES:
    obj_name = os.path.join(OBJECT_NAME, csv_name)
    file_name_out = os.path.join(OUT_DIR, csv_name)
    s3.download_file(BUCKET_NAME, obj_name, file_name_out)
    print('saved ', csv_name)
print('done')