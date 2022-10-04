import numpy as np


cmdStr = '^'

for i in range(192):
    wget_link = f"https://www.repository.cam.ac.uk/bitstream/handle/1810/339869/print{i}.zip?sequence={i + 7}&isAllowed=y"
    wget_cmd = f"wget -q --show-progress -O data/print{i}.zip \'{wget_link}\'"
    
    unzip_cmd = f"unzip -q data/print{i}.zip -d data/"
    aws_cp_cmd = f"aws s3 cp --recursive data/print{i} s3://noodle-finder/caxton/data/print{i}/"
    rm_cmd = f"rm -rf data/*"
    cmdStr += f"{wget_cmd} ^{unzip_cmd} ^{aws_cp_cmd} ^{rm_cmd} ^"
print(cmdStr)
