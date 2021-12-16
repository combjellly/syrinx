from newpi import *
import time
import multiprocessing
import os
import socket

#use newpi

p = PiAnalog(4,18)
t = PiAnalog(23,25)
v = PiAnalog(5,12)
q = PiAnalog(19,21)


def ppro():
	host = '192.168.2.17'
	print("opop")
	
	port = 3434
	s = socket.socket(socket.AF_INET,
					  socket.SOCK_STREAM)
	  
	# bind the socket with server
	# and port number
	s.bind(('', port))
	  
	# allow maximum 1 connection to
	# the socket			
	s.listen(1)
	  
	# wait till a client accept
	# connection
	c, addr = s.accept()
	  
	# display client address
	print("CONNECTION FROM:", str(addr))
	  
	# send message to the client after
	# encoding into binary string
	while True:
		#os.system("echo " + str(p.analog_read()) +  " | pdsend 3434 localhost udp" )
		print(p.analog_read())
		c.send(str(p.analog_read()))
		print("opop")
	
		time.sleep(5)

def tpro():
	host = '192.168.2.17'
	port = 3535
	s = socket.socket(socket.AF_INET,
					  socket.SOCK_STREAM)
	  
	# bind the socket with server
	# and port number
	s.bind(('', port))
	  
	# allow maximum 1 connection to
	# the socket
	s.listen(1)
	  
	# wait till a client accept
	# connection
	c, addr = s.accept()
	  
	# display client address
	print("CONNECTION FROM:", str(addr))
	  
	# send message to the client after
	# encoding into binary string
	while True:
		#os.system("echo " + str(t.analog_read()) +  " | pdsend 3535 localhost udp" )
		c.send(str(t.analog_read()))	
		s
		print("t"+ str(t.analog_read()))
		time.sleep(4)
		
def vpro():
	host = '192.168.2.17'
	port = 3636
	s = socket.socket(socket.AF_INET,
					  socket.SOCK_STREAM)
	s.bind(('', port))
	s.listen(1)
	c, addr = s.accept()
	print("CONNECTION FROM:", str(addr))
	while True:
		#os.system("echo " + str(v.analog_read()) +  " | pdsend 3636 localhost udp" )
		c.send(str(v.analog_read()))	
		print(v.analog_read())
		time.sleep(1)
		
def qpro():
	host = '192.168.2.17'
	port = 3737
	s = socket.socket(socket.AF_INET,
					  socket.SOCK_STREAM)
	s.bind(('', port))
	s.listen(1)
	c, addr = s.accept()
	print("CONNECTION FROM:", str(addr))
	  
	while True:
		#os.system("echo " + str(q.analog_read()) +  " | pdsend 3737 localhost udp" )
		c.send(str(q.analog_read()))	
		print(q.analog_read())
		time.sleep(1)
		

	
def main():

	p1 = multiprocessing.Process(target=tpro)
	p2 = multiprocessing.Process(target=ppro) 
	p3 = multiprocessing.Process(target=vpro)
	p4 = multiprocessing.Process(target=qpro) 
	p1.start()
	p2.start()
	p3.start()
	p4.start()	

if __name__ == '__main__':
    main()

