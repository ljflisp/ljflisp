import base64
import png
#J加密的方式： 
ENDOFMESSAGE = "0100100101010101010101100100111101010010010001010011100101000111010101000101010101010110010101000101010100110000010001100100100001010010010100110100010100111101"
def encode_message_as_bytestring(message):
    b64 = message.encode("utf8")
    bytes_ = base64.encodebytes(b64)
    bytestring = "".join(["{:08b}".format(x) for x in bytes_])
    bytestring+=ENDOFMESSAGE
    return bytestring
  
print(encode_message_as_bytestring('hello world'))
print(encode_message_as_bytestring('hello'))