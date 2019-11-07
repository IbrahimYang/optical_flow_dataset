"""
*****************************************************************************
*******************Ibrahim,CBICR,Tsinghua University*************************
*****************************************************************************
File name:    aedat.py
Description:  Human retina sensor simulator
Author:       Ibrahim Yang
Version:      V1.0
Date:         2019-6-9
History:
*****************************************************************************
"""
import dv
from dv import AedatFile
from dv import LegacyAedatFile

import os
import shutil

import numpy as np
import hdf5storage
import cv2
import torch
import glob
import pandas as pd
import math
import utils.util as utils
from sklearn.preprocessing import MinMaxScaler
import imutils


class aedatfile(object):
    """
    Class:
        aedatfile
    Parameters:

    Returns:
      None
    """
    def __init__(self):
        matfile = "mat"
        aedatfile = "aedat4"
        legacyaedatfile = "aedat"

    def read_aedatfile(self, aedat_path):
        """
         Function:
             read_aedatfile
         Parameters:
           aedat_path: input the aedat path
         Returns:
           output 'aedat_file'
         """
        with AedatFile(aedat_path) as aedat_file:
            # list all the names of streams in the file
            print(aedat_file.names)
            return aedat_file

    def read_old_version_aedatfile(self, aedat_path):
        """
         Function:
             read_old_version_aedatfile
         Parameters:
           aedat_path: input the aedat path
         Returns:
           output 'aedat_file'
         """
        with LegacyAedatFile(aedat_path) as aedat_file:
            # list all the names of streams in the file
            print(aedat_file.names)
            return aedat_file

    def show_aedatfile_events(self, aedat_path, save_path):
        """
         Function:
             show_aedatfile
         Parameters:
           aedat_path: input the path
           save_path: output the numpy format
         Returns:
           output 'aedat_file'
         """
        aedat_file = self.read_aedatfile(aedat_path)
        time_window = 2000

        time_start = 0
        time_now = 0
        dvs_show = np.zeros((260, 346, 3))

        for counter, event in enumerate(aedat_file['events']):
            if counter:
                if (time_now - time_start) < time_window:
                    if event.polarity:
                        dvs_show[event.y, event.x, 2] += 1
                    else:
                        dvs_show[event.y, event.x, 1] += 1
                    time_now = event.timestamp
                else:
                    cv2.imshow("DVS", dvs_show)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                    dvs_show = np.zeros((260, 346, 3))
                    time_start = time_now
            # init
            else:
                time_start = event.timestamp
                time_now = event.timestamp

    def show_aedatfile_frames(self, aedat_path, save_path):
        """
         Function:
             show_aedatfile
         Parameters:
           aedat_path: input the path
           save_path: output the numpy format
         Returns:
           output 'aedat_file'
         """
        aedat_file = self.read_aedatfile(aedat_path)
        for aps in aedat_file['frames']:
            cv2.imshow('out', aps.image)
            cv2.waitKey(30)


