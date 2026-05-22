from os import listdir
from os.path import isfile, join
import scipy
import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
import seaborn as sns




def df_rebase(
        df: pd.DataFrame,
        target_list: list,
        ref_list: list
) -> pd.DataFrame:
    """Changes the order and name of DataFrame columns to the project's needs
        for readability.

    Args:
        df: The pandas DataFrame.
        order_list: List object that contains the proper order of the default
             column names.
        ref_list: List object that contains the renaming list based
            on the project needs.

    Returns:
        A DataFrame with the new columns order and names.
    """
    print("Initial columns:", list(df.columns))

    if are_lists_equal(list(df.columns), ref_list):
        pass

    else:
        if len(target_list) == len(ref_list): 
            # keep and re-order only the necessary columns of the initial DataFrame
            df = df[target_list]
            rename_dict = dict(zip(target_list, ref_list))
            df = df.rename(columns=rename_dict)  # rename the columns
        else:
            print("The length of the target list and the reference list is not equal.")

    print("Processed columns:", list(df.columns))

    return df



def encode_labels(instances_list) -> np.ndarray:
    """Encodes target labels.

    Args:
        instances_list: List of instances to be encoded.

    Returns:
        The encoded array.
    """
    le = preprocessing.LabelEncoder()
    le.fit(instances_list)
    instances_arr = le.transform(instances_list)

    return instances_arr


def list_files_in_folder(folder_path) -> list:
    """Returns a list of all CSV files within the specified folder.

    Args:
        folder_path (str): The directory path to search for files.

    Returns:
        list: A list containing the filenames (strings) of all files
              in the directory that end with the '.csv' extension.
    """
    files_list = list()
    for f in listdir(folder_path):
        if isfile(join(folder_path, f)):
            if f.endswith(".csv"):
                files_list.append(f)

    return files_list
