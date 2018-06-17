import time
import serial
comport = serial.Serial('/dev/ttyUSB1', 9600)
PARAM_CARACTER='t'
PARAM_ASCII='s'
time.sleep(1.8)
while 1:
    #try:
        PARAM_ASCII=raw_input('insira uma letra: ')
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
        print '\nt1: %s' % (tempo1)
        print '\nt2: %s' % (tempo2)
        print '\nt3: %s' % (tempo3)
        tempo=(tempo1+256*tempo2+256*256*tempo3)*50
        print '\ntempo [ns]: %s' % (tempo)
        #vel=
        #print '\nRetorno da serial: %s' % (VALUE_SERIAL)
        #vs=bin(reduce(lambda x, y: 256*x+y, (ord(c) for c in '%s'% (VALUE_SERIAL)), 0))
        #print '\nRetorno da serial bin : %s' % (vs)
        #break
    #except:
     #   break
comport.close()