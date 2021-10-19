def logical_rshift(signed_integer, places, num_bits=32):
    unsigned_integer = signed_integer % (1 << num_bits)
    return unsigned_integer >> places

logical_rshift(-100, 1)

from ctypes import c_uint32 as unsigned_int32
unsigned_int32(-100).value >> 1
#2147483598