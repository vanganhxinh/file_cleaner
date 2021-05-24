import os

# Function to remove unwanted files recursively in a folder
# Input parameter 1: path to the folder - string (e.g.: "C:\\test_file_removal")
# Input parameter 2: ending of the filename - string (e.g.: "_TN.png")


def remove_files(folder_path, file_ending):
    # use os.walk
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for name in files:
            if name.endswith(file_ending):
                # print(f"Found [{name}] in [{root}]")
                del_path = os.path.join(root, name)
                # print list of the files found
                print(f"  >> erase {del_path}")
                # remove the files
                # os.remove(del_path)


if __name__ == '__main__':
    remove_files("C:\\test_file_removal", "_TN.png")
