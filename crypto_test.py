import hashlib
import scrypt
def sha256hex(data):
	return str(hashlib.sha256(data).hexdigest())

print ('sha256',sha256hex('test'))

#password,	salt,	N=16384,				r=8,	p=1,	buflen=64
hash = str(scrypt.hash(str('test'), 'test', N=128, 	r=16, buflen=64))
print ('scrypt',hash.encode('hex'))
