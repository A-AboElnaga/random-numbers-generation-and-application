# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 11:21:34 2021

@authors: Ahmad Aboelnaga          

"""
#####################
'''
This is a two part program that can run seperately
First part is a code to generating random integers using A Hybrid Approach
Second part is finding an approximate value of Pi using random numbers
'''
program = input('Type "R" to run the random integers generator or "P" to run Pi value program: ')
if program == "R" or program=='r':
  
  
  #generating random integers using A Hybrid Approach
  
  # from sys import argv
  from matplotlib import pyplot
  import time 
  from collections import Counter
  
  
  def get_seed():
      seed_in = str(time.time())
      list1= seed_in.split(".")
      seed = list1[1]
      return (seed)
  
  
  def mdl_sqr_method(seed):
      sqrd= int(seed)**2
      sqrd_str = str(sqrd)
      return (sqrd_str)
  
   
  def get_mdl_char(s,n,rslt_list):
      d=len(s)-n
      if n:
          l=int(s[(d+1)//2:len(s)-(d//2)])
          while len(str(l)) != n:
              seed = int(get_seed())
              sqrd_str =mdl_sqr_method(seed)
              try:
                  get_mdl_char(sqrd_str,length_random)
              except:
                  l= int('1'+str(l))
          rslt_list.append(l)
          
          
  # length_random = int(argv[1])
  # repts = int(argv[2])
  
  length_random = int(input("Enter the length of random number you want, maximum 13:"))
  repts = int(input("Enter the number of random numbers you want:"))
  
  def excute(repts):
      rslt_list=[]
      for x in range(repts):
          time.sleep(0.000111)
          seed= 0
          while seed <1000000: #to make sure it can get an intger of length 13 at least
            seed = int(get_seed())
          sqrd_str =mdl_sqr_method(seed)
          get_mdl_char(sqrd_str,length_random,rslt_list)
      return(rslt_list)
  
  
  result = excute(repts)
  print(result)
  
  #Ploting the data in stem plot
  Plot = input('Do you want to view a stem plot of the data (Y/N)?')
  if Plot == "y" or Plot =="Y":
    rslt_list= dict(Counter(result))
    print("Data Summary" and "\n" and rslt_list)
    
    x = rslt_list.keys()
    y = rslt_list.values()
    pyplot.stem(x, y)
    pyplot.show()
  
  #writing the data in a text file
  Save_txt = input('Do you want to save data in a text file (Y/N)?')
  if Save_txt == "y" or Save_txt =="Y":
    with open ("rslt.txt", "w") as f:
      for ele in result:
        f.write(str(ele)+"\n")  
 
if program == "P" or program=='p':
  #Approximating Pi
  
  import random
  plot = input('Do you want to see visual plot of the data (Y/N)?')
  if plot =='Y' or plot =='y':
    from vpython import*
    
    tgraph=graph(xtitle="x",ytitle="y")
    p1=gdots(color=color.cyan)
    p2=gdots(color=color.black)
    
    points_total= 0
    PointsSmallerThanOne=0
    
    
    while points_total<1000000: #A bigger number will return a more accurte approximation of Pi 
                             #but will take more time to return the result, so change as you like
      # rate(100)    #To visualize the process
      x=random()
      y=random()
      r=vector(x,y,0)
      if mag(r)<1:
        PointsSmallerThanOne+=1
        p1.plot(r.x,r.y)
      else:
        p2.plot(r.x,r.y)
      points_total+=1
    
    pi_approx = 4*PointsSmallerThanOne/points_total
    print("The approximated value of pi based on the size of points chosen is about",pi_approx) 
  else:
    points_total= 0
    PointsSmallerThanOne=0
    while points_total<10000000: #A bigger number will return a more accurte approximation of Pi 
                             #but will take more time to return the result, so change as you like
      x=random.random()
      y=random.random()
      r=((x**2)+(y**2))**0.5
      if r<1:
        PointsSmallerThanOne+=1
      points_total+=1

    pi_approx = 4*PointsSmallerThanOne/points_total
    print("The approximated value of pi based on the size of points chosen is about",pi_approx) 

  
  
      
    
