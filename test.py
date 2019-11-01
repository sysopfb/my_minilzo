from ctypes import *
import binascii
import sys


lzo = cdll.LoadLibrary('./minilzo.so')

def MAX_LZO_ENCODED_SIZE(sz):
	return (sz+sz) / 64 + 16 + 3

def lzo_decompress_block(data, dst_len=0):
	buf = create_string_buffer(data)
	cb = c_int(len(buf)-1)
	if dst_len == 0:
		cbOut = len(buf)*10
	else:
		cbOut = dst_len
	buf1 = create_string_buffer(cbOut)
	cbOut = c_int(cbOut)
	retval = lzo.lzo1x_decompress(byref(buf), cb, byref(buf1), byref(cbOut))
	return buf1.raw[:cbOut.value]

def lzo_compress_block(data):
	buf = create_string_buffer(data)
	cb = c_int(len(buf))
	cbOut = MAX_LZO_ENCODED_SIZE(len(buf))
	buf1 = create_string_buffer(cbOut)
	cbOut = c_int(cbOut)
	wrkmem = create_string_buffer(16384*8)
	retval = lzo.lzo1x_1_compress(byref(buf), cb, byref(buf1), byref(cbOut), byref(wrkmem))
	if retval == 0:
		return buf1.raw[:cbOut.value]
	else:
		return retval
	


def main():
	data = open(sys.argv[1], 'rb').read()
	blah = lzo_decompress_block(data)
	return blah

if __name__ == "__main__":
	t = main()


