#coding: utf-8

# 密码存储的安全方式
# 1. OpenID验证
# 2. salt+sha(algorithm$hash$salt)
# 3. 非对称加密。私钥的重要性

import os
from hashlib import sha256, sha1
from hmac import HMAC

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

if __name__ == '__main__':
    hashed = encrypt_password('123456', salt=None)
    print hashed
    print check_password(hashed, '123456')
    print sha1('Hello World').hexdigest()
    # print HMAC('Hello World', None, sha1).digest().encode('ascii')