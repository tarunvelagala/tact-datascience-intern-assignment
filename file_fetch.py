import inspect
import os
import re

import numpy

os.chdir('E:\\Intern Work TeamTact')  # change the current root  directory
np_methods_list = []
lines_with_np_methods = []


def fetch_np_methods():
    np_methods = inspect.getmembers(numpy, inspect.isfunction)
    for i in np_methods:
        np_methods_list.append(i[0])
    # print(np_methods_list)


fetch_np_methods()


def file_fetch():
    for path, subdirs, files in os.walk(os.getcwd()):  # looping over the files through walker
        for name in files:
            if name.endswith('.py'):  #
                # file_list.append(os.path.join(path, name))
                with open(os.path.join(path, name), 'r', encoding="utf8") as f:
                    for line in f:
                        if re.findall(r'np\.[a-z]+\(*', line):  # finding all lines with numpy methods
                            lines_with_np_methods.append(line.strip())
    print(lines_with_np_methods)


file_fetch()
