#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """            q,��@������D�֛Y�nο��<�{V���*.����I�C�q>T$>�yN�D���Y��F��+P�Һݟ̯�ؕ��� ���TY����,o7������ꔼ
�cLܯQ��@��a"""
from hashlib import sha256
print sha256(blob).hexdigest()