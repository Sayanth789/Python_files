'''   
Using memoryview and struct to inspect a GIF image handler.


'''
import struct 
fmt = '<3s3sHH'
with open('galaxy.gif', 'rb') as f:
    img = memoryview(f.read())

header = img[:10]
print(bytes(header))    

print(struct.unpack(fmt, header))

del header 
del img 
