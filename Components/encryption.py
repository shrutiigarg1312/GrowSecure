import os
from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Hash import SHA256
from Crypto import Random

#AES Encryption
def encrypt(key, filename):
    chunksize =64 * 1024
    outputFile = "(enc)" + filename
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)

    encryptor = AES.new(key, AES.MODE_CBC, IV)
     
    with open(filename, 'rb') as infile:
        with open("enc.jpg", 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk +=b' '* (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))
    outfile.close()
    return outfile

#DES Encryption
def encrypt(key, filename):
    chunksize =64 * 1024
    outputFile = "(enc)" + filename
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(8)

    encryptor = DES.new(key, DES.MODE_OFB, IV)
     
    with open(filename, 'rb') as infile:
        with open(outputFile, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk +=b' '* (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))
    outfile.close()
    return outfile