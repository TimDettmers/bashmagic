import subprocess

from os import listdir
from os.path import isfile, join


def get_files_paths_for_folder(path):
    files = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
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
