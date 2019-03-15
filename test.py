import sys
SEQUENCE=0
data_chunks=[]

def read_all_input():
    global data_chunks
    global SEQUENCE
    while True:
      try:
        data=sys.stdin.read(3)
        msg = {"sequence": SEQUENCE, "data": data, "ack": False, "eof": False}
        data_chunks.append(msg)
        SEQUENCE += len(data)
      except:
       break
read_all_input()
print(data_chunks)
