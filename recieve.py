import mido 
import socket
from multiprocessing import Process
import time

host = '192.168.2.17'
print(mido.get_output_names())

def midia():
    global host
    s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
    port = 3434
    s.connect((host, port))
    port3434 = mido.open_output('IAC Driver Bus 1')

    while True:
        msg = s.recv(1024)
        note=msg.decode()
        note = int(float(note))%14
        if note == 0:
            note = 28
        elif note == 1:
            note = 31
        elif note == 2:
            note = 33
        elif note == 3:
            note = 38
        elif note == 4:
            note = 40
        elif note == 5:
            note = 43
        elif note == 6:
            note = 45
        elif note == 7:
            note = 50
        elif note == 8:
            note = 52
        elif note == 9:
            note = 55
        elif note == 10:
            note = 57
        elif note == 11:
            note = 62
        elif note == 12:
            note = 65
        elif note == 13:
            note = 67
        msg1=mido.Message('note_on', note=note,channel=0)
        port3434.send(msg1)
        time.sleep(5)
        msg1=mido.Message('note_off', note=note,channel=0)
        port3434.send(msg1)

    s.close()

def midib():
    global host
    s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
    port = 3535
    s.connect((host, port))
    port3535 = mido.open_output('IAC Driver Bus 2')

    while True:
        msg = s.recv(1024)
        note=msg.decode()
        note = int(float(note))%14
        if note == 0:
            note = 28
        elif note == 1:
            note = 31
        elif note == 2:
            note = 33
        elif note == 3:
            note = 38
        elif note == 4:
            note = 40
        elif note == 5:
            note = 43
        elif note == 6:
            note = 45
        elif note == 7:
            note = 50
        elif note == 8:
            note = 52
        elif note == 9:
            note = 55
        elif note == 10:
            note = 57
        elif note == 11:
            note = 62
        elif note == 12:
            note = 65
        elif note == 13:
            note = 67
        msg1=mido.Message('note_on', note=note,channel=0)
        port3535.send(msg1)
        time.sleep(4)
        msg1=mido.Message('note_off', note=note,channel=0)
        port3535.send(msg1)

    s.close()

def midic():
    global host
    s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
    port = 3636
    s.connect((host, port))
    port3636 = mido.open_output('IAC Driver Bus 3')

    while True:
        msg = s.recv(1024)
        note=msg.decode()

        note = int(float(note))%14
        if note == 0:
            note = 28
        elif note == 1:
            note = 31
        elif note == 2:
            note = 33
        elif note == 3:
            note = 38
        elif note == 4:
            note = 40
        elif note == 5:
            note = 43
        elif note == 6:
            note = 45
        elif note == 7:
            note = 50
        elif note == 8:
            note = 52
        elif note == 9:
            note = 55
        elif note == 10:
            note = 57
        elif note == 11:
            note = 62
        elif note == 12:
            note = 65
        elif note == 13:
            note = 67
        note = note + 12
        msg1=mido.Message('note_on', note=note,channel=0)
        port3636.send(msg1)
        time.sleep(1)
        msg1=mido.Message('note_off', note=note,channel=0)
        port3636.send(msg1)

    s.close()

def midid():
    global host
    s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
    port = 3737
    s.connect((host, port))
    port3737 = mido.open_output('IAC Driver Bus 4')

    while True:
        msg = s.recv(1024)
        note=msg.decode()

        note = int(float(note))%14
        if note == 0:
            note = 28
        elif note == 1:
            note = 31
        elif note == 2:
            note = 33
        elif note == 3:
            note = 38
        elif note == 4:
            note = 40
        elif note == 5:
            note = 43
        elif note == 6:
            note = 45
        elif note == 7:
            note = 50
        elif note == 8:
            note = 52
        elif note == 9:
            note = 55
        elif note == 10:
            note = 57
        elif note == 11:
            note = 62
        elif note == 12:
            note = 65
        elif note == 13:
            note = 67
        note = note + 14
        msg1=mido.Message('note_on', note=note,channel=0)
        port3737.send(msg1)
        time.sleep(1)
        msg1=mido.Message('note_off', note=note,channel=0)
        port3737.send(msg1)

    s.close()

if __name__=='__main__':
    p1 = Process(target = midia)
    p2 = Process(target = midib)
    p3 = Process(target = midic)
    p4 = Process(target = midid)
    p1.start()
    p2.start()
    p3.start()
    p4.start()