# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 22:52:11 2014

@author: Andreea
"""
from __future__ import print_function
from __future__ import division
#import profile
from runprogram import *

def main():
    implemented_exper = ["superCDMS", \
        "LUX2013zero", "LUX2013one", "LUX2013three", "LUX2013five", "LUX2013many", \
        "XENON10", "CDMSlite2013CoGeNTQ", "CDMSSi"]
    scattering_type = 'SD66'
    mPhi = 1000.
    fp = 1.
    fn = 0.
    delta = 0.

    mx_min = 3.18
    mx_max = 100.
    num_steps = 30

    '''
    global v0bar, vobs, vesc
    v0bar = 230 - 3 * 24.4
    vobs = v0bar + 12
    vesc = 544 - 3 * 39
    '''
    
#    inputs = [(0, 0, 3.18), (-1/16.4, 0, 3.18), (0, -30., 2.), (0, -50., 1.7)]
#    inputs = [(0, 50, 29)]
#    inputs = [(0, 0, 3.18), (0, -30., 2.), (0, -50., 1.7), \
#        (0, 50, 29)]
    inputs = [(0., 0., 3.)]

    RUN_PROGRAM = F
    MAKE_PLOT = T

    exper_list = implemented_exper[8:9]
    filename_tail_list = [""]
    plt.close()
    for exper_name in exper_list:
        for filename_tail in filename_tail_list:
            for (fn, delta, mx_min) in inputs[0:1]:
                run_program(exper_name, scattering_type, mPhi, fp, fn, delta, mx_min, mx_max, num_steps, \
                    RUN_PROGRAM, MAKE_PLOT, filename_tail, plot_dots = False)
    plt.show()
    
if __name__ == '__main__':
    main()
#    profile.run("main()")

