import os
from glob import glob

dirs = [
    "Training_Batch_Files",
    "Prediction_Batch_files"
]

# **Note:** Thisis the command for dvc add training and prediction.
# git rm -r --cached "Training_Batch_Files/*.csv"
# git rm -r --cached "Prediction_Batch_files/*.csv"
# git commit -m "Training_Batch_Files/*.csv and Prediction_Batch_Files/*.csv"
# and then run python template.py in terminal to successfully run dvc add command.

for dir in dirs:
    files =glob(dir + r"/*.csv")
    for filepath in files:
        os.system(f"dvc add {filepath}")


print("\n #### all files added to dvc ####")