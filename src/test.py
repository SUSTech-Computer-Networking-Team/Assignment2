import struct

b = b'\x12\x67\x33\x44\x55'
print(b)
print(b + b'\x02')
# b[3:5] = 0
print(ord(b[1:2]))

sum = 0x1ffff
while sum > 0xffff:
    sum = (sum & 0xffff) + (sum >> 16)
print(sum )

data = b'\x08\x00\x00\x01\x00\x01\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x61\x62\x63\x64\x65\x66\x67\x68\x69'
def _checksum(data):
    sum = 0

    # TODO:
    # Compute the checksum of an ICMP packet. Checksums are used to
    # verify the integrity of packets.
    #
    # :type data: bytes
    # :param data: The data you are going to send, calculate checksum
    # according to this.
    #
    # :rtype: int
    # :returns: checksum calculated from data
    #
    # Hint: if the length of data is odd, add a b'\x00' to the end of data
    # according to RFC

    l = len(data)
    if(l % 2 != 0):
        data += b'\x00'
    for i in range(0, l, 2):
        if i == 2:
            #continue # skip checksum
            pass

        hi = ord(data[i : i + 1]) << 8
        lo = ord(data[i + 1 : i + 2])
        sum += hi + lo
    
        print(f'{hex(hi)} {hex(lo)} {hex(sum)}')
    while(sum > 0xffff):
        sum = (sum & 0xffff) + (sum >> 16)
    
    print(f'{hex(hi)} {hex(lo)} {hex(sum)}')

    return (~sum & 0xffff)

print(_checksum(data))

print()

print(bytes([15]))

print((5).to_bytes())

b = bytes([0,8,1,2,3,4,5,6,7,8,9,10,11,12])
print(b)
# print((655355).to_bytes())

# bt = b'E\x00\x00T.d\x00\x00/\x01\xad\xdd\xb2\x9d:\xbb\xc0\xa8\x01g\x00\x00\xdcKJ\x95\x00\x00GoQOrJrWZA5V82mrPkOtQrjXf07EZeNdYZkwNZ7ReHx7kwzlowcfArbf'
bt = b'E\x00\x00T.d\x00\x00/\x01\xad\xdd\xb2\x9d:\xbb\xc0\xa8\x01g\x00\x00\xdcKJ\x95\x00\x00GoQOrJrWZA5V82mrPkOtQrjXf07EZeNdYZkwNZ7ReHx7kwzlowcfArbf'
btt = b'E'
# print(len(btt))
# print((int.from_bytes(btt)))
# s = struct.unpack('I', b'E')
# print(s)
print(btt[0] >> 4)