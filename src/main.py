# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 22:52:11 2014

@author: Andreea
"""

from __future__ import print_function
from experiment import *
     
def Plot_Upper_Limit(max_gap):
    import matplotlib.pyplot as plt
    from scipy.interpolate import interp1d
    
    x = max_gap[:,0]
    y = -np.log10(3.*SpeedOfLight**2*1e4*3600*24) + max_gap[:,0] + max_gap[:,1]
    interp = interp1d(x, y, kind = "cubic")
    plt.close
    x1 = np.linspace(x[0],x[-1],50)
    plt.plot(x, y, "o", x1, interp(x1))
    plt.xlabel('Log10(m [GeV])')
    plt.ylabel('Log10(sigma)')
    plt.show()

     
def main():
    exper_name = "CDMSlite2013CoGeNTQ"
    scattering_type = 'SD66'
    mPhi = 1000.
    fp = 1.
    fn = 0.
    delta = 0.
    
    exper = Experiment(exper_name, scattering_type, mPhi)
    print('name = ', exper.name)
    
    
    '''
#    ER = 6.
    mx = 10.
    Eee1 = 2
    Eee2 = 3
#    diff_resp = exper.DifferentialResponseSHM(ER, Eee1, mx, fp, fn, delta)
#    print("diff response = ", diff_resp)
#    print("response = ", exper.ResponseSHM(ER, Eee1, Eee2, mx, fp, fn, delta))
    print("int response = ", exper.IntegratedResponseSHM(Eee1, Eee2, mx, fp, fn, delta))
    #print("max gap = ", cl1.MaximumGapUpperBoundSHM(mx, fp, fn, delta))
    print("diff response calls = " , exper.count_diffresponse_calls)
    print("response calls = " , exper.count_response_calls)
    '''


    output_file = "./" + OUTPUT_DIR + "UpperLimitSHM_" + exper_name + "_mxsigma" \
        + FileNameTail(fp, fn) + "_py.dat" 

    '''        
    mx_min = 4
    mx_max = 100.
    num_steps = 30
    max_gap = exper.MaximumGapLimit(fp, fn, delta, mx_min, mx_max, num_steps)
    print("max gap = ", max_gap)
    print(output_file)
    np.savetxt(output_file, max_gap)
    '''
    max_gap = np.loadtxt(output_file)
    print("max_gap = ", max_gap)    
    Plot_Upper_Limit(max_gap)
    
    
if __name__ == '__main__':
    main()
#    profile.run("main()")

