import hashlib
import scrypt

hash = str(hashlib.sha256('test').hexdigest())
print ('sha256',hash)

#password,	salt,	N=16384,	r=8,	p=1,	buflen=64
hash = str(scrypt.hash(str('test'), 'test', N=512, r=8))
print ('scrypt',hash.encode('hex'))
