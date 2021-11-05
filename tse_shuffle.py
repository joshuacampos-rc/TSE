#!/usr/bin/python
"""A randomizer for Primary and Secondary triage schedule.
   Requirements: No consecutive repeats and Primary can not be secondary.

"""

"""to do: add logic for infinite loop case , possibly a try catch 
"""

import argparse
import os
import random


east_triage = {"William":0,"Jimmy":0,"Allison":0,"Spence":0,"Darrel":0}
east_triage_list = ["William","Jimmy","Allison","Spence","Darrel"]

shuffled_list = []
shuffled_secondary = []


ranx = 0
day = ""
west_secondary = {}

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument(
		help="Select west or east", type=str, 
		dest="coast", action="store")
	loop_counter=0
	
	args = parser.parse_args()
	print("""This is a work in progress, if it gets in a infinite loop
	       ...just force quit and re run, it eventually works..""")
	triage_days = 20
	
	shuffled_list = shuffle_it(args.coast,triage_days)
	
	while len(shuffled_list) == 0:
	    loop_counter+=1
	    shuffled_list = shuffle_it(args.coast,triage_days)
	    
	secondary_list = shuffle_it(args.coast,triage_days)
	while len(secondary_list) == 0:
	    loop_counter+1
	    secondary_list = shuffle_it(args.coast,triage_days)
	
	while check_both(shuffled_list,secondary_list) == "no":
	    loop_counter+=1
	    secondary_list = shuffle_it(args.coast,triage_days)
	    while len(secondary_list) == 0:
	        loop_counter+1
	        secondary_list = shuffle_it(args.coast,triage_days)
	    
	    
	print("took",loop_counter +1,"attempts")
	for counter,name in enumerate(secondary_list):
	    print(shuffled_list[counter],secondary_list[counter])


def check_both(primary,secondary):
    #print(len(primary),len(secondary))
    clean = ""
    for counter,name in enumerate(secondary):
        if secondary[counter] != primary[counter]:
            
            clean = "clean"
        else:
            #print("we found a match, redo")
            clean = "no"
            break
    #print(clean)
    return clean
       
def shuffle_it(coast,days):
    
    if coast == "west":
        primary_triage = []
        west_triage = {"Joshua":0,"James":0,"Justin":0,"Alex":0,"Michael":0}
        west_triage_list = ["Joshua","James","Justin","Alex","Michael"]
        triage = west_triage
        triage_list = west_triage_list
        pre_primary = ""
        triage_days = days
    
    if coast == "east":
        triage = east_triage
        triage_list = east_triage_list
        pre_primary = ""
        triage_days = days
    
        
    
    for x in range(triage_days):
       
        ran_x = random.randrange(0,5)
        primary = triage_list[ran_x]
        
        while triage[primary] >= (triage_days/5):#this last number is 2:10 ratio, 2 triage days per 10 days
            try:
                primary =  triage_list[random.randrange(0,5)]
                
            except:
                break
        
        primary_triage.append(primary)
        triage[primary] +=1
        pre_primary = primary
        
    
    #print(primary_triage)
    
    return check_it(primary_triage)
    
def check_it(randomlist):
    
    for x in range((len(randomlist) -1)):
        
        
        if randomlist[x] == randomlist[x+1]:
            randomlist = []
            return randomlist
    #print(randomlist)
    return randomlist  

            

    
    
if __name__ == '__main__':
	main()

