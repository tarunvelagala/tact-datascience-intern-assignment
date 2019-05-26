import inspect
import os
import re
from collections import Counter
from matplotlib import pyplot as plt
import numpy
import pandas as pd


def main():
    os.chdir('E:\\Intern Work TeamTact')  # change the current root directory
    np_methods_list = []
    lines_with_np_methods = []
    method_count_list = []
    fetch_np_methods(np_methods_list)
    file_fetch(lines_with_np_methods)
    find_methods_in_lines(lines_with_np_methods, np_methods_list, method_count_list)
    plot_top_20(method_count_list)


# For extracting all the methods in Numpy Package
def fetch_np_methods(np_methods_list):
    np_methods = inspect.getmembers(numpy, inspect.isfunction)
    for i in np_methods:
        np_methods_list.append(i[0])


# for fetching the files from the directories and searching for numpy entries
def file_fetch(lines_with_np_methods):
    # looping over the files through walker
    for path, subdirs, files in os.walk(os.getcwd()):
        for name in files:
            if name.endswith('.py') or name.endswith('.ipynb'):  #
                with open(os.path.join(path, name), 'r', encoding="utf8") as f:  # opening the files
                    for line in f:
                        # finding all lines with numpy methods
                        if re.findall(r'np\.[a-z]+\(*', line) or re.findall(r'numpy\.[a-z]+\(*',
                                                                            line):  # searching for words like np.* or numpy.*
                            lines_with_np_methods.append(line.strip())  # removing all the white spaces from the code


# finding all the methods in comparision with numpy methods
def find_methods_in_lines(lines_with_np_methods, np_methods_list, method_count_list):
    for i in lines_with_np_methods:
        for xs in np_methods_list:
            if 'np.' + xs in i:
                method_count_list.append(str(xs))


# plot top 20 methods used in all files
def plot_top_20(method_count_list):
    letter_counts = Counter(method_count_list)  # Making a dictionary of frequencies of methods used
    df = pd.DataFrame.from_dict(letter_counts, orient='index')
    df = df.nlargest(20, df.columns)  # Finding nlargest from the entries
    print(df)
    df.plot(kind='bar')
    plt.show()


if __name__ == '__main__':
    main()
