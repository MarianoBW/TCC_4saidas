#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 17:37:21 2018

@author: Mariano Berwanger Wille
"""
import time
import serial
#import statistics

comport = serial.Serial('/dev/ttyUSB0', 9600)

#parametros iniciais 
tempod1=[0,0,0,0,0,0,0,0,0,0]
i=0
tempod11=0
tempod2=[0,0,0,0,0,0,0,0,0,0]
tempod12=0
 #------------------------------------------------------------
while i<10:
    time.sleep(0.1)
    PARAM_ASCII='2'
    comport.write(PARAM_ASCII)
    dir_val=comport.read(1)
#    print '\ndir =%s '%(dir_val)   
    if  1:    
        tempo1=comport.read(1)
        tempo2=comport.read(1)
        tempo3=comport.read(1)
        tempo1=ord(tempo1)
        tempo2=ord(tempo2)
        tempo3=ord(tempo3)

        tempod1[i]=float((tempo1+256*tempo2+256*256*tempo3)/20000000.0) #119+256*119+256*256*119
        tempod11=tempod1[i]+tempod11

        i=i+1
        print '\ntempo2 1 = %s '%(tempo1)  # mostra valor medio t12
        print '\ntempo2 2 = %s '%(tempo2)  # mostra valor medio t21
        print '\ntempo2 3 = %s '%(tempo3)  # mostra valor medio t21
tempod11 = tempod11/10  # valor medio t12


i=0
while i<10:
    time.sleep(0.1)
    PARAM_ASCII='4'
    comport.write(PARAM_ASCII)
    dir_val=comport.read(1)
    
    if  1 :    
        tempo1=comport.read(1)
        tempo2=comport.read(1)
        tempo3=comport.read(1)
        tempo1=ord(tempo1)
        tempo2=ord(tempo2)
        tempo3=ord(tempo3)

        tempod2[i]=float((tempo1+256*tempo2+256*256*tempo3)/20000000.0) #119+256*119+256*256*119
        tempod12=tempod2[i]+tempod12
        print '\ntempo4 1 = %s '%(tempo1)  # mostra valor medio t12
        print '\ntempo4 2 = %s '%(tempo2)  # mostra valor medio t21
        print '\ntempo4 3 = %s '%(tempo3)  # mostra valor medio t21
        i=i+1
tempod12 = tempod12/10    # valor medio t21

comport.close()    

#tempo de atraso eletronico estimado se Vv=0
te1= tempod12-0.0006
te2= tempod11-0.0006

print '\ntempo medio 1 =%s '%(tempod11)  # mostra valor medio t12
print '\ntempo medio 2 =%s '%(tempod12)  # mostra valor medio t21
print '\ntempo te1 se v=0 =%s '%(te1)       # mostra te1 estimado
print '\ntempo te2 se v=0 =%s '%(te2)       # mostra te2 estimado

#tempo eletronico previamente calculado
te2m=0.00058356
te1m=0.00036545

diftempo=tempod11-tempod12
print '\ndiferenca tempo medio =%s '%(diftempo)

# calculo da velocidade 
if (diftempo == 0):
    vel=0
else:
    vel=((0.20/2)*((1/(tempod11-te2m))-(1/(tempod12-te1m))))
    
print '\ntempo medio 1 -te=%s '%(tempod11-te2m)  
print '\ntempo medio 2 -te=%s '%(tempod12-te1m)
print '\nVelocidade [m/s]: %s' % (vel)
velkmh=vel*3.6 
print '\nVelocidade [Km/h]: %s' % (velkmh)
#------------------------------------------------------------
