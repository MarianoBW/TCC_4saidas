#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 17:37:21 2018

@author: Mariano Berwanger Wille
"""
import time
import serial
#import pandas
import numpy

#import division
comport = serial.Serial('/dev/ttyUSB0', 9600)
PARAM_CARACTER='e'
PARAM_ASCII='s'
#time.sleep(0.8)
tempod1=[0,0,0,0,0,0,0,0,0,0]
i=0
tempod11=0
tempod2=[0,0,0,0,0,0,0,0,0,0]
i=0
tempod12=0
 #------------------------------------------------------------
while i<10:
    time.sleep(0.01)
    PARAM_ASCII='3'
    comport.write(PARAM_ASCII)
    dir_val=comport.read(1)
            #print '\nComando: %s' % (dir_val)
     
    if  dir_val != PARAM_CARACTER :     #119+256*119+256*256*119
        tempo1=comport.read(1)
        tempo2=comport.read(1)
        tempo3=comport.read(1)
        tempo1=ord(tempo1)
        tempo2=ord(tempo2)
        tempo3=ord(tempo3)
        
   # print '\nComando: %s' % (dir_val)
#print '\nt1: %s' % (tempo1)
#print '\nt2: %s' % (tempo2)
#print '\nt3: %s' % (tempo3)
    tempod1[i]=float((tempo1+256*tempo2+256*256*tempo3)/20000000.0)
#    print '\ntempo %s = %s '%(i, tempod1[i])
    tempod11=tempod1[i]+tempod11
 #   print '\nt3 %s t2 %s t1 %s ' % (tempo3 ,tempo2, tempo1)




    i=i+1
tempod11 = tempod11/10  
#print '\ntempo médio 1%s '%(tempod11)


i=0
while i<10:
    time.sleep(0.01)
    PARAM_ASCII='1'
    comport.write(PARAM_ASCII)
    dir_val=comport.read(1)
            #print '\nComando: %s' % (dir_val)
     
            #119+256*119+256*256*119
    tempo1=comport.read(1)
    tempo2=comport.read(1)
    tempo3=comport.read(1)
    tempo1=ord(tempo1)
    tempo2=ord(tempo2)
    tempo3=ord(tempo3)
        
   # print '\nComando: %s' % (dir_val)
#print '\nt1: %s' % (tempo1)
#print '\nt2: %s' % (tempo2)
#print '\nt3: %s' % (tempo3)
    tempod2[i]=float((tempo1+256*tempo2+256*256*tempo3)/20000000.0)
#    print '\ntempo %s = %s '%(i, tempod2[i])
    tempod12=tempod2[i]+tempod12
 #   print '\nt3 %s t2 %s t1 %s ' % (tempo3 ,tempo2, tempo1)




    i=i+1
    
tempod12 = tempod12/10    

comport.close()    

te1= tempod12-0.0006
te2= tempod11-0.0006

print '\ntempo médio 1 =%s '%(tempod11)  
print '\ntempo médio 2 =%s '%(tempod12)
print '\ntempo médio 2 =%s '%(te1)
print '\ntempo médio 2 =%s '%(te2)


diftempo=tempod11-tempod12
print '\ndiferença tempo médio =%s '%(diftempo)
#tempod1=round(tempod1,2)
tempo=tempod11-tempod12
if (tempo == 0):
    vel=0
else:
    vel=((0.23/2)*((1/(tempod11-0.00058356))-(1/(tempod12-0.000335))))
print '\ntempo médio 1 -te=%s '%(tempod11-0.00058356)  
print '\ntempo médio 2 -te=%s '%(tempod12-0.0003445)#8216)    0.00038216
print '\nVelocidade [m/s]: %s' % (vel)
velkmh=vel*3.6 
print '\nVelocidade [Km/h]: %s' % (velkmh)
#------------------------------------------------------------



















