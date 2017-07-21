#coding: utf-8

import os, sha256, HMAC

def encrypt_password(password, salt=None):
    if salt is None:
        salt = os.urandom(8)
    assert 8 == len(salt)
    assert isinstance(salt, str)

    if isinstance(password, unicode):
        password = password.encode('utf-8')
    assert isinstance(password, str)
    result = password
    for i in xrange(10):
        result = HMAC(result, salt, sha256).hexdigest()
    return salt + result

def check_password(hashed, input_password):
    return hashed == encrypt_password(input_password, hashed[:8])