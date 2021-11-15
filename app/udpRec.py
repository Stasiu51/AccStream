import socket
from threading import Thread
from time import sleep
import sys
import json
from queue import PriorityQueue
from dateutil import parser

exit = False
dataQueue = PriorityQueue()
dataDict = {'N':0}
nInQueue = 0

def monitorThread(regularity):
    global exit, dataQueue
    while not exit:
        print(f'{nInQueue} items in queue')
        sleep(regularity)

def rxThread(portNum):
    global exit, dataQueue, nInQueue

    print('thread started')

    # Generate a UDP socket
    rxSocket = socket.socket(socket.AF_INET,  # Internet
                             socket.SOCK_DGRAM)  # UDP

    # Bind to any available address on port *portNum*
    rxSocket.bind(("", portNum))

    # Prevent the socket from blocking until it receives all the data it wants
    # Note: Instead of blocking, it will throw a socket.error exception if it
    # doesn't get any data

    rxSocket.setblocking(0)

    print("RX: Receiving data on UDP port " + str(portNum))

    while not exit:
        try:
            # Attempt to receive up to 1024 bytes of data
            attempts = 0
            bdata = b''
            while attempts < 10:
                attempts += 1
                bdata += rxSocket.recvfrom(1024)[0]
                # print(f'collecting... {attempts}')
                try:
                    data = json.loads(bdata)
                    break
                except json.JSONDecodeError:
                    continue
            else:
                raise Exception(f'Failed to parse: \n {bdata}')

            if 'loggingTime' in data:
                timestamp = parser.parse(data['loggingTime']).timestamp()
                dataQueue.put((timestamp,data))
            # Echo the data back to the sender
            nInQueue += 1

        except socket.error:
            # If no data is received, you get here, but it's not an error
            # Ignore and continue
            pass

    sleep(.1)


def startRec(portNum, regularity):
    print('starting thread')
    udpRxThreadHandle = Thread(target=rxThread,args=(portNum,))
    udpRxThreadHandle.start()
    monitorThreadHandle = Thread(target=monitorThread, args=(regularity,))
    monitorThreadHandle.start()

def getLatestDatum():
    print('trying')
    data = dataQueue.get()
    dataQueue.task_done()
    return data

def updateDict(time, timeback):
    for t in dataDict:
        if t < time - timeback:
            dataDict.__delitem__(t)
    while dataQueue.not_empty:
        t, datum = dataQueue.get()
        if t >= time - timeback:
            dataDict[t] = datum['motionRoll']
    dataQueue.task_done()
    dataDict['N'] = len(dataDict) - 1


def getData(time, timeBack):
    print('start request')
    updateDict(time, timeBack)
    print('updated')
    return dataDict




