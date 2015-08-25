#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This is a simple demo for using CoAP for communicating with Exosite.

Author: Patrick Barrett(patrickbarrett@exosite.com)
"""

import socket
import binascii
import hexdump
import coap

# Update these parameters with the CIK of the deice and the alias of the
# datasource of what you'd like to read.
CIK = "PUT_YOUR_DEVICE_CIK_HERE"
ALIAS = "output"

SERVER = "coap.exosite.com"
PORT = 5683

# Create a New Conformable GET CoAP Request with Message ID 0x37.
msg = coap.Message(mtype=coap.CON, mid=0x37, code=coap.POST)

# Set the path where the format is "/1a/<datasource alias>".
msg.opt.uri_path = ('1a', ALIAS,)

# Encode the CIK to binary to save data
#msg.opt.uri_query = (binascii.a2b_hex(CIK),)
msg.opt.uri_query = (CIK,)

# Encode the CIK to binary to save data
#msg.opt.content_format = 1

msg.payload = "26"


print("------------ Send Message ------------")
print(msg)
print(hexdump.hexdump(msg.encode()))

# Setup Socket as UDP
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

# Encode and Send Message
sock.sendto(msg.encode(), (SERVER, PORT))

# Wait for Response
data, addr = sock.recvfrom(2048) # maximum packet size is 1500 bytes

# Decode and Display Response
recv_msg = coap.Message.decode(data)
print("------------ Recv Message ------------")
print(recv_msg)
print(hexdump.hexdump(recv_msg.encode()))
