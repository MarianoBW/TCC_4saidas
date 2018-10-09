#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 12:19:46 2018

@author: Mariano Berwanger Wille
"""
import time
import serial
import statistics
#import numpy
#from numpy import uint32

comport = serial.Serial('/dev/ttyUSB0', 9600)

#parametros iniciais 
tempo1=0
tempo2=0
tempo3=0
tempod1=[0,0,0,0,0,0,0,0,0,0]
i=0
tempod21=0
tempod2=[0,0,0,0,0,0,0,0,0,0]
tempod12=0
x=1
 #------------------------------------------------------------
while x==1:
    i=0
    while i<10:
        time.sleep(0.1)
        PARAM_ASCII='3'
        comport.write(PARAM_ASCII)
        dir_val=comport.read(1)
         
        if  dir_val == PARAM_ASCII :    
            tempo1=comport.read(1)
            tempo2=comport.read(1)
            tempo3=comport.read(1)
            tempo1=ord(tempo1)
            tempo2=ord(tempo2)
            tempo3=ord(tempo3)
            
            
            #119+256*119+256*256*119
            tempod1p=((tempo1+256*tempo2+256*256*tempo3)) 
            tempod1[i]=float(tempod1p/20000000.0)
#            print '\ntempod1 =%s '%(tempod1[i])
#            print '\ntempo3 =%s '%(tempo3)
#            print '\ntempo2 =%s '%(tempo2)
#            print '\ntempo1 =%s '%(tempo1)
            #i=16
            i=i+1
        else:
            print '\n Fail 3'
    tempod21 = float(statistics.median(tempod1))
    
    
    i=0
    while i<10:
        time.sleep(0.1)
        PARAM_ASCII='1'
        comport.write(PARAM_ASCII)
        dir_val=comport.read(1)
        
        if  dir_val == PARAM_ASCII :    
            tempo1=comport.read(1)
            tempo2=comport.read(1)
            tempo3=comport.read(1)
            tempo1=ord(tempo1)
            tempo2=ord(tempo2)
            tempo3=ord(tempo3)
            #print '\ntempo1 =%s '%(tempo1)
            #print '\ntempo2 =%s '%(tempo2)
            #print '\ntempo3 =%s '%(tempo3)
            #119+256*119+256*256*119
            tempod2p=((tempo1+256*tempo2+256*256*tempo3)) 
            tempod2[i]=float(tempod2p/20000000.0)
#            print '\ntempod2 =%s '%(tempod2[i])
#            print '\ntempod2 =%s '%(tempod2p)
#            print '\ntempo3 =%s '%(tempo3)
#            print '\ntempo2 =%s '%(tempo2)
#            print '\ntempo1 =%s '%(tempo1)
            #i=13
            i=i+1
        else:
            print '\n Fail 1'
    tempod12 = float(statistics.median(tempod2))   # valor medio t21
    
    
       
    
    #tempo de atraso eletronico estimado se Vv=0
    te1= tempod21-0.0006
    te2= tempod12-0.0006
    
#    print '\ntempo medio 1 =%s '%(tempod21)  # mostra valor medio t12
#    print '\ntempo medio 2 =%s '%(tempod12)  # mostra valor medio t21
#    print '\ntempo medio eletronico 1 =%s '%(te1)       # mostra te1 estimado
#    print '\ntempo medio eletronico 2 =%s '%(te2)       # mostra te2 estimado
    
    #tempo eletronico previamente calculado
    te1m=0.00042#25945
    te2m=0.00064735#45685
    
    diftempo=tempod21-tempod12
#    print '\ndiferenca tempo medio =%s '%(diftempo)
    
    # calculo da velocidade 
    if (diftempo == 0):
        vel=0
    else:
        vel=((0.20/2)*((1/(tempod21-te2m))-(1/(tempod12-te1m))))
        
#    print '\ntempo medio 1 -te=%s '%(tempod21-te2m)  
#    print '\ntempo medio 2 -te=%s '%(tempod12-te1m)
    print '\nVelocidade: %.4f m/s ' % (vel)
#    x=0
#    velkmh=vel*3.6 
#    print '\nVelocidade [m/s]: %s Velocidade [Km/h]: %s' % (vel,velkmh)
#------------------------------------------------------------
comport.close() 