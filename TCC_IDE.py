import time
import serial
#import division
comport = serial.Serial('/dev/ttyUSB0', 9600)
PARAM_CARACTER='t'
PARAM_ASCII='s'
time.sleep(1.8)
#while 1:
    #try:
 #------------------------------------------------------------
PARAM_ASCII='3'
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
        
print '\nComando: %s' % (dir_val)
#print '\nt1: %s' % (tempo1)
#print '\nt2: %s' % (tempo2)
#print '\nt3: %s' % (tempo3)
tempod11=float((tempo1+256*tempo2+256*256*tempo3)/20000000.0)
#tempod1=round(tempod1,2)

#------------------------------------------------------------
PARAM_ASCII='3'
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
        
#print '\nComando: %s' % (dir_val)
#print '\nt1: %s' % (tempo1)
#print '\nt2: %s' % (tempo2)
#print '\nt3: %s' % (tempo3)
tempod12=float((tempo1+256*tempo2+256*256*tempo3)/20000000.0)

#------------------------------------------------------------
PARAM_ASCII='3'
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
        
#print '\nComando: %s' % (dir_val)
#print '\nt1: %s' % (tempo1)
#print '\nt2: %s' % (tempo2)
#print '\nt3: %s' % (tempo3)
tempod13=float((tempo1+256*tempo2+256*256*tempo3)/20000000.0)

#------------------------------------------------------------
PARAM_ASCII='3'
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
        
#print '\nComando: %s' % (dir_val)
#print '\nt1: %s' % (tempo1)
#print '\nt2: %s' % (tempo2)
#print '\nt3: %s' % (tempo3)
tempod14=float((tempo1+256*tempo2+256*256*tempo3)/20000000.0)

#------------------------------------------------------------
PARAM_ASCII='3'
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
        
#print '\nComando: %s' % (dir_val)
#print '\nt1: %s' % (tempo1)
#print '\nt2: %s' % (tempo2)
#print '\nt3: %s' % (tempo3)
tempod15=float((tempo1+256*tempo2+256*256*tempo3)/20000000.0)

#------------------------------------------------------------
PARAM_ASCII='3'
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
        
#print '\nComando: %s' % (dir_val)
#print '\nt1: %s' % (tempo1)
#print '\nt2: %s' % (tempo2)
#print '\nt3: %s' % (tempo3)
tempod16=float((tempo1+256*tempo2+256*256*tempo3)/20000000.0)

#------------------------------------------------------------
PARAM_ASCII='3'
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
        
#print '\nComando: %s' % (dir_val)
#print '\nt1: %s' % (tempo1)
#print '\nt2: %s' % (tempo2)
#print '\nt3: %s' % (tempo3)
tempod17=float((tempo1+256*tempo2+256*256*tempo3)/20000000.0)

#------------------------------------------------------------
PARAM_ASCII='3'
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
        
#print '\nComando: %s' % (dir_val)
#print '\nt1: %s' % (tempo1)
#print '\nt2: %s' % (tempo2)
#print '\nt3: %s' % (tempo3)
tempod18=float((tempo1+256*tempo2+256*256*tempo3)/20000000.0)

#------------------------------------------------------------
PARAM_ASCII='3'
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
        
#print '\nComando: %s' % (dir_val)
#print '\nt1: %s' % (tempo1)
#print '\nt2: %s' % (tempo2)
#print '\nt3: %s' % (tempo3)
tempod19=float((tempo1+256*tempo2+256*256*tempo3)/20000000.0)



lista=[tempod11, tempod12, tempod13, tempod14, tempod15, tempod16, tempod17, tempod18, tempod19]
menor = lista[0]
for i in lista:
    if i > menor:
        menor = i


tempod1=menor-0.00134 #(tempod11+tempod12+tempod13+tempod14+tempod15)/5
print '\ntempo 1 [s]: %s' % (tempod1)
#------------------------------------------------------------
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
print '\nComando: %s' % (dir_val)
#print '\nt1: %s' % (tempo1)
#print '\nt2: %s' % (tempo2)
#print '\nt3: %s' % (tempo3)
tempod21=float((tempo1+256*tempo2+256*256*(tempo3))/20000000.0) #*50 + 1
#tempod2=round(tempod2,2)

#------------------------------------------------------------
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
#print '\nComando: %s' % (dir_val)
#print '\nt1: %s' % (tempo1)
#print '\nt2: %s' % (tempo2)
#print '\nt3: %s' % (tempo3)
tempod22=float((tempo1+256*tempo2+256*256*(tempo3))/20000000.0)

#------------------------------------------------------------
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
#print '\nComando: %s' % (dir_val)
#print '\nt1: %s' % (tempo1)
#print '\nt2: %s' % (tempo2)
#print '\nt3: %s' % (tempo3)
tempod23=float((tempo1+256*tempo2+256*256*(tempo3))/20000000.0)

#------------------------------------------------------------
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
#print '\nComando: %s' % (dir_val)
#print '\nt1: %s' % (tempo1)
#print '\nt2: %s' % (tempo2)
#print '\nt3: %s' % (tempo3)
tempod24=float((tempo1+256*tempo2+256*256*(tempo3))/20000000.0)

#------------------------------------------------------------
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
#print '\nComando: %s' % (dir_val)
#print '\nt1: %s' % (tempo1)
#print '\nt2: %s' % (tempo2)
#print '\nt3: %s' % (tempo3)
tempod25=float((tempo1+256*tempo2+256*256*(tempo3))/20000000.0)

#------------------------------------------------------------
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
#print '\nComando: %s' % (dir_val)
#print '\nt1: %s' % (tempo1)
#print '\nt2: %s' % (tempo2)
#print '\nt3: %s' % (tempo3)
tempod26=float((tempo1+256*tempo2+256*256*(tempo3))/20000000.0)

#------------------------------------------------------------
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
#print '\nComando: %s' % (dir_val)
#print '\nt1: %s' % (tempo1)
#print '\nt2: %s' % (tempo2)
#print '\nt3: %s' % (tempo3)
tempod27=float((tempo1+256*tempo2+256*256*(tempo3))/20000000.0)

#------------------------------------------------------------
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
#print '\nComando: %s' % (dir_val)
#print '\nt1: %s' % (tempo1)
#print '\nt2: %s' % (tempo2)
#print '\nt3: %s' % (tempo3)
tempod28=float((tempo1+256*tempo2+256*256*(tempo3))/20000000.0)

#------------------------------------------------------------
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
#print '\nComando: %s' % (dir_val)
#print '\nt1: %s' % (tempo1)
#print '\nt2: %s' % (tempo2)
#print '\nt3: %s' % (tempo3)
tempod29=float((tempo1+256*tempo2+256*256*(tempo3))/20000000.0)

lista=[tempod21, tempod22, tempod23, tempod24, tempod25, tempod26, tempod27, tempod28, tempod29]
menor = lista[0]
for i in lista:
    if i > menor:
        menor = i
        
tempod2=menor-0.00081 #(tempod21+tempod22+tempod23+tempod24+tempod25)/5

#float(tempod2)
print '\ntempo 2 [s]: %s' % (tempod2)
 
tempo=tempod1-tempod2
if (tempo == 0):
    vel=0
else:
    vel=((0.23/2)*((1/tempod1)-(1/tempod2)))
    
print '\nVelocidade [m/s]: %s' % (vel)
velkmh=vel*3.6 
print '\nVelocidade [Km/h]: %s' % (velkmh)

#tfim=tempod1-tempod2 # em ns
#print '\ntempo final [ns]: %s' % (tfim)
        #vel=
        #print '\nRetorno da serial: %s' % (VALUE_SERIAL)
        #vs=bin(reduce(lambda x, y: 256*x+y, (ord(c) for c in '%s'% (VALUE_SERIAL)), 0))
        #print '\nRetorno da serial bin : %s' % (vs)
        #break
    #except:
     #   break
comport.close()