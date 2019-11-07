"""
*****************************************************************************
*******************Ibrahim,CBICR,Tsinghua University*************************
*****************************************************************************
File name:    clean&rebuild_dir.py
Description:  clean&rebuild liver_database dir
Author:       Ibrahim Yang
Version:      V1.0
Date:         2018-11-12
History:
*****************************************************************************
"""
from __future__ import print_function

import src.aedat as aedat


def main():
    need_filter = "dvSave-2019_10_19_08_29_30.aedat4"

    aedatfile = aedat.aedatfile()
    # aedatfile.show_aedatfile_frames(need_filter, " ")
    aedatfile.show_aedatfile_events(need_filter, " ")


"""
Function:     main
Description:  convert png to nrrd image
Calls:        nrrd_convert
Called By:    none
Input:        none
Output:       none
Return:       ./*.nrrd
Others:       none
"""
if __name__ == '__main__':
    main()



