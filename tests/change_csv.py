import pandas as pd

def get_s3_path(local_path):
    bucket_name = 'noodle-finder'
    bucket_path = 'caxton/data'
    local_path = local_path.split('/')
    full_path = [f's3://{bucket_name}', bucket_path, local_path[-2], local_path[-1]]
    return '/'.join(full_path)

csv_file = 'data/caxton_dataset/caxton_dataset_filtered.csv'
dataframe = pd.read_csv(csv_file)
img_paths_s3 = dataframe['img_path'].apply(get_s3_path).tolist()
print(img_paths_s3)
