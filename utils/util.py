"""
*****************************************************************************
*******************Ibrahim,CBICR,Tsinghua University*************************
*****************************************************************************
File name:    util.py
Description:  basic functions
Author:       Ibrahim Yang
Version:      V1.0
Date:         2019-6-9
History:
*****************************************************************************
"""
import json
from pathlib import Path
from datetime import datetime
from itertools import repeat
from collections import OrderedDict
import os
import shutil
import hdf5storage


def clean_mkdir(path):
    """
    Function:
        clean_mkdir(path)
    Parameters:
      path: input the path need to build
    Returns:
      if input folder not exist, then creat new finder
    """
    if os.path.exists(path) == 0:
        os.makedirs(path)
        print('creat_path:', path)


def force_mkdir(path):
    """
    Function:
        force_mkdir(path)
    Parameters:
      path: input the path need to clean and build
    Returns:
      a folder without file
    """
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
    print('force_creat_path:', path)


def WriteMatlab(data_np, VarName, FileName):
    """
    Function:
        WriteMatlab
    Parameters:
      data_np: input the path need to clean
      VarName:
      FileName:
    Returns:
      PIL format image
    """
    matcontent = {}
    matcontent[VarName] = data_np
    hdf5storage.write(matcontent, filename=FileName, matlab_compatible=True)


def ensure_dir(dirname):
    dirname = Path(dirname)
    if not dirname.is_dir():
        dirname.mkdir(parents=True, exist_ok=False)


def read_json(fname):
    with fname.open('rt') as handle:
        return json.load(handle, object_hook=OrderedDict)


def write_json(content, fname):
    with fname.open('wt') as handle:
        json.dump(content, handle, indent=4, sort_keys=False)


def inf_loop(data_loader):
    ''' wrapper function for endless data loader. '''
    for loader in repeat(data_loader):
        yield from loader


class Timer:
    def __init__(self):
        self.cache = datetime.now()

    def check(self):
        now = datetime.now()
        duration = now - self.cache
        self.cache = now
        return duration.total_seconds()

    def reset(self):
        self.cache = datetime.now()
