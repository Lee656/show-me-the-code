#coding: utf-8

import os
from hmac import HMAC
from hashlib import sha256
import binascii
def encrypt_password(password, salt=None):
    if salt is None:
        salt = binascii.hexlify(os.urandom(8)).decode()

    assert 16 == len(salt), len(salt)
    assert isinstance(salt, str), type(salt)

    if isinstance(password, unicode):
        password = password.encode('utf-8')
    assert isinstance(password, str), type(password)
    result = password
    for i in xrange(10):
        result = HMAC(result, salt, sha256).hexdigest()
    return unicode(salt + result)

def check_password(hashed, input_password):
    return hashed == encrypt_password(input_password, hashed[:16].encode())
