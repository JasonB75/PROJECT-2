from multiprocessing.connection import Client
import time

# Client 1
conn = Client(('localhost', 6000), authkey=b'secret password')
conn.send('foo')
time.sleep(1)
conn.send('close connection')
conn.close()

time.sleep(1)

# Client 2
conn = Client(('localhost', 6000), authkey=b'secret password')
conn.send('bar')
conn.send('close server')
conn.close()