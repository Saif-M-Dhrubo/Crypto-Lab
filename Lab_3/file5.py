#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """            q,��@������D�֛Y��ο��<�{V���*.����I�C�q>�$>�yN�D�r�Y��F��+P�Һݟ̯�ؕ�� ���TY����,o7����莃ꔼ
�cLܯQ�M@��a"""
from hashlib import sha256
print sha256(blob).hexdigest()