import subprocess
import operator

from os import listdir
from os.path import isfile, join, isdir, splitext

def sort_dict_by_value(dictionary, reverse=False):
    return sorted(dictionary.items(), key=operator.itemgetter(1), reverse=reverse)

def get_files_paths_for_folder(path):
    files = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
    return files

def get_folder_paths_for_folder(path):
    files = [join(path, f) for f in listdir(path) if isdir(join(path, f))]
    return files

def wget(url, path):
    strCMD = 'wget {0} -P {1}'.format(url, path)
    return execute(strCMD)

def unzip(input_path, output_path=None):
    if output_path is None:
        strCMD = 'unzip {0}'.format(input_path)
    else:
        strCMD = 'unzip {0} -d {1}'.format(input_path, output_path)
    return execute(strCMD)

def execute(strCMD):
    return subprocess.call(strCMD, shell=True)


def get_files_by_filetype(path):
    filetype2paths = {}
    folders = get_folder_paths_for_folder(path)
    for folder in folders:
        files = get_files_paths_for_folder(folder)
        for f in files:
            _, ext = splitext(f)
            if ext not in filetype2paths: filetype2paths[ext] = []
            filetype2paths[ext].append(f)
    return filetype2paths
