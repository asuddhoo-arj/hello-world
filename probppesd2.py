# -*- coding: utf-8 -*-
"""
Created on Thu May 14 17:46:36 2020

@author: arjsu
"""

#def prob_of_infect (jday, testing, daystarttest, dayendtest, probtest, ppe, daystartppe, dayendppe, probppe, socdis, daystartsd, dayendsd, probsd):


def prop_test(jday,testing, daystarttest, dayendtest, probtest):
    
    if testing == True:
        if jday >= daystarttest and jday <= dayendtest:
            prob = probtest
            pm1 = 1 - prob
        else:
            prob = 0.0
            pm1 = 1 - prob
    return prob, pm1


def prob_ppe(jday, daystartppe, dayendppe, probppe):
    
    if jday >= daystartppe and jday <= dayendppe:
        prob = probppe
        pm1 = 1 - prob
    else:
        prob = 0.0
        pm1 = 1 - prob
    return prob, pm1

        
def prob_sd(jday, daystartsd, dayendsd, probsd):
    
    if jday >= daystartsd and jday <= dayendsd:
        prob = probsd
        pm1 = 1 - prob
    else:
        prob = 0.0
        pm1 = 1 - prob
    return prob, pm1


def prob_ppesd(jday,daystartppe, dayendppe, probppe, daystartsd, dayendsd, probsd):
    
    if jday < daystartppe and jday < daystartsd:
        probppesd = 0.0
        pm1 = 1 - probppesd
        
    elif jday < daystartppe and jday >= daystartsd:
        probppesd = probsd
        pm1 = 1 - probppesd

    elif jday >= daystartppe and jday < daystartsd:
        probppesd = probppe
        pm1 = 1 - probppesd

    elif jday > dayendppe and jday <= dayendsd:
        probppesd = probsd
        pm1 = 1 - probppesd

    elif jday > dayendppe and jday > dayendsd:
        probppesd = 0.0
        pm1 = 1 - probppesd

    elif jday > dayendppe and jday > dayendsd:
        probppesd = probppe
        pm1 = 1 - probppesd
        
    else:
        probppesd = probppe * probsd
        pm1 = 1 - probppesd

        
    return probppesd, pm1

        
#jday = 36
#
#
#daystartppe = 7
#dayendppe = 27
#
#daystartsd = 10
#dayendsd = 35
#
#probppe = 0.5
#probsd = 0.1
#
#probppesd, pm1 = prob_of_infect(jday, daystartppe,daystartsd, dayendppe, dayendsd, probppe, probsd)
#    
#print("jday= ", jday, "daystartppe = ", daystartppe, "dayendppe =", dayendppe,"daystartsd = ", daystartsd, "dayendsd =", dayendsd,"probppe = ", probppe, "probsd= ", probsd)
#print("******    probppesd = ", probppesd, "pm1 = ", pm1)
#    
#

        