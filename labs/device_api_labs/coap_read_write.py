
""" 
  Exosite HTTPS POST API and CoAP Write examples using socket level calls to 
  show the difference in sizes of the total request/response.
"""


import socket
import sys
import ssl
import urllib
import time

cik = '<PUT_YOUR_DEVICE_CIK_HERE>'



time.sleep(2)

print '=================='
print 'COAP Write'
print '=================='
import binascii
import coap
import sys


ALIAS = "output"
SERVER = "coap.exosite.com"
PORT = 5683

# Create a New Conformable GET CoAP Request with Message ID 0x37.
msg = coap.Message(mtype=coap.CON, mid=0x37, code=coap.POST)
# Set the path where the format is "/1a/<datasource alias>".
msg.opt.uri_path = ('1a', ALIAS,)
# Encode the CIK to binary to save data
msg.opt.uri_query = (binascii.a2b_hex(cik),)
msg.payload = "1"
start = time.time()
print("Sending Message: {}".format(binascii.b2a_hex(msg.encode())))
print(coap.humanFormatMessage(msg))

# Setup Socket as UDP
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

# Encode and Send Message
sock.sendto(msg.encode(), (SERVER, PORT))
# Wait for Response
data, addr = sock.recvfrom(2048) # maximum packet size is 1500 bytes
print('time',time.time()-start,'ms')
# Decode and Display Response
recv_msg = coap.Message.decode(data)
print("Received Message: {}".format(binascii.b2a_hex(data)))
print(coap.humanFormatMessage(recv_msg))

print '--REQUEST / RESPONSE SIZE:----------------------'
print 'Request:'+ str(len(binascii.b2a_hex(msg.encode()))/2)+ ' Bytes'
print 'Response:'+ str(len(binascii.b2a_hex(data))/2)+ ' Bytes'
print 'Total:' + str(len(binascii.b2a_hex(msg.encode()))/2 + len(binascii.b2a_hex(data))/2) + ' Bytes'
print '---------------------------------'
print '\r\n\r\n'


