#Question 1 - Olympic Scenario
#Code for different combinations of optional technical clothing Johnny should wear at the start of each race to maximize chance of winning

import math

#welcome Message
print("Welcome to this olympic program. By completing the appropriate fields when indicated, you will be able to find out which technical clothing Johnny should wear to maximize his chance of winning the race")

#time function
def time(d,s):
    t=d/s
    return t

#input check for a positive number
#distance inputs for swimming, cycling and running
def input_check():
    valid = False
    while valid == False:
        
        d_swim = float(input("Enter swimming distance(km):"))  #inputs for swimming
        if d_swim < 0:
            print("Error, wrong swimming distance input.")
            d_swim = float(input("Enter swimming distance(km):"))
        else:
            print("Swimming input confirmed.")

        d_cycle = float(input("Enter cycling distance(km):"))  #inputs for cycling
        if d_cycle < 0:
            print("Error, wrong cycling ditance input.")
            d_cycle = float(input("Enter VALID cycling distance(km):"))
        else:
            print("Cycling input confirmed.")

        d_run = float(input("Enter running distance(km):")) #inputs for running
        if d_run < 0:
            print("Error, wrong swimming distance input.")
            d_run = float(input("Enter VALID running distance(km):"))
        else:
            print("Running input confrimed.")

        if d_swim > 0 and d_cycle > 0 and d_run > 0: #checking all inputs and if all valid, ending the while loop
            valid = True
            print("All inputs confirmed.", "\n")

    return d_swim, d_cycle, d_run

#bubblesort
def bubbleSort(alist,blist,clist,dlist,elist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp1 = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp1

                temp2 = blist[i]
                blist[i] = blist[i+1]
                blist[i+1] = temp2

                temp3 = clist[i]
                clist[i] = clist[i+1]
                clist[i+1] = temp3

                temp4 = dlist[i]
                dlist[i] = dlist[i+1]
                dlist[i+1] = temp4

                temp5 = elist[i]
                elist[i] = elist[i+1]
                elist[i+1] = temp5

#call input_check function
d_swim, d_cycle, d_run = input_check()

#average speeds without technical clothing - just triathlon suit
s_swim = 6.2
s_cycle = 52.8
s_run = 18.3

#time without appliances
t_swim = round(time(d_swim,s_swim),2)
t_cycle = round(time(d_cycle,s_cycle),2)
t_run = round(time(d_run,s_run),2)
t_total_time = round(t_swim + t_run + t_cycle,2)


#print time data in a table for when Johnny does not wear any of the optional clothing
from tabulate import tabulate

table = [["Swimming",t_swim],["Cycling",t_cycle],
         ["Running",t_run],["Total (sum of three events)",t_total_time],"\n"]

headers = ["Discipline", "Time Taken (s)"]

print(tabulate(table, headers, tablefmt="simple"))


#list containg speeds for shoes and eyewear
#cycling shoes[0], running shoes[1], flippers[2], goggles[3], sunglasses[4]
sswim = [0.9, 0.98, 1.6, 1.35, 0.9]
scycle = [1.12, 1.04, 0.95, 0.92, 1.08]
srun = [0.75, 1.25, 0.7, 0.88, 1.05]

items = ["cycling shoes","running shoes","flippers","goggles","sunglasses"]


#speed combinations for swim, cycle and run
s_swim_combs = []
for i in range(0,3): #going through the shoes (0,1,2)
    for k in range(3,5): #going through the eyewear (3,4)
        s_swim_combs.append(round(sswim[i]*sswim[k]*s_swim,2))

s_cycle_combs = []
for i in range(0,3):
    for k in range(3,5):
        s_cycle_combs.append(round(scycle[i]*scycle[k]*s_cycle,2))

s_run_combs = []
for i in range(0,3):
    for k in range(3,5):
        s_run_combs.append(round(srun[i]*srun[k]*s_run,2))

#combination of item names, need this when printing the tables out
item_combs = []
for i in range(0,3):
    for k in range(3,5):
        item_combs.append(items[i] + "-" + items[k] + ":")

#time combinations
t_swim_combs = []
for i in range(0,6):
    t_swim_combs.append(time(d_swim,s_swim_combs[i]))

t_cycle_combs = []
for i in range(0,6):
    t_cycle_combs.append(time(d_cycle,s_cycle_combs[i]))

t_run_combs = []
for i in range(0,6):
    t_run_combs.append(time(d_run,s_run_combs[i]))

t_total_time2 = []
for i in range(0,6):
    t_total_time2.append(round(t_swim_combs[i]+t_cycle_combs[i]+t_run_combs[i],2))


#bubble sorting the combinations
bubbleSort(t_total_time2,t_swim_combs,t_cycle_combs,t_run_combs,item_combs)

#output combinations in table
for i in range(0,6):
    print(item_combs[i])
    table2 = [["Swimming",t_swim_combs[i]],["Cycling",t_cycle_combs[i]],
             ["Running",t_run_combs[i]],["Total (sum of three events)",t_total_time2[i]],"\n"]

    print(tabulate(table2, headers, tablefmt="simple"))




#question: What is the minimum swimming distance that makes using both the flippers[2] and goggles[3] worthwhile? (d_swim not fixed)
d_swim2 = 3

#The time it takes to complete the race with flippers and googles
min_time = round(time(d_swim2,(sswim[2]*sswim[3]*s_swim)) + time(d_run,(srun[2]*srun[3]*s_run)) + time(d_cycle,(scycle[2]*scycle[3]*s_cycle)),2)

#The slowesr time that the race was completed
slowest = t_total_time2[4]

while (min_time != slowest):
    d_swim2 = d_swim2 - 0.1
    min_time = round(time(d_swim2,(sswim[2]*sswim[3]*s_swim)) + time(d_run,(srun[2]*srun[3]*s_run)) + time(d_cycle,(scycle[2]*scycle[3]*s_cycle)),2) 

print("minimum swimming distance that makes using both the flippers and googles worthwhile: ", d_swim2)


