import socket
import struct
import binascii

class Udphdr:
    def __init__(self, src_port, dst_port, length, checksum):
        self.src_port = src_port      
        self.dst_port = dst_port      
        self.length = length          
        self.checksum = checksum        

    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!H', self.src_port)  
        packed += struct.pack('!H', self.dst_port) 
        packed += struct.pack('!H', self.length)   
        packed += struct.pack('!H', self.checksum)  
        return packed

def unpack_Udphdr(buffer):
    return struct.unpack('!HHHH', buffer[:8])

def getSrcPort(unpacked_udp):
    return unpacked_udp[0]

def getDstPort(unpacked_udp):
    return unpacked_udp[1]

def getUDPLength(unpacked_udp):
    return unpacked_udp[2]

def getChecksum(unpacked_udp):
    return unpacked_udp[3]


udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_udphdr = udp.pack_Udphdr()
print("Packed UDP Header:", binascii.b2a_hex(packed_udphdr))
    

unpacked_udphdr = unpack_Udphdr(packed_udphdr)
print(unpacked_udphdr)
print('Source Port:{} Destination Port:{} Length:{} CheckSum: {}'\
    .format(getSrcPort(unpacked_udphdr), getDstPort(unpacked_udphdr), getUDPLength(unpacked_udphdr), getChecksum(unpacked_udphdr)))
