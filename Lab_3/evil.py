#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """            �J+�=��)��ގ�CP&lp�^�{N�?����7� �.�k�[A��@{�֌�ʜ.u`EU���^�r��<��f��t���qdz�����w������L=�h�Ar���� Qv��n��S���"""
from hashlib import sha256

if str(sha256(blob).hexdigest()) == 'fde930f68c3f809b5ad2bf9e7cd6f5202c71d7f39611c4ce63a59fedec8b96d7' :
    print 'I come in peace.'
else :
    print 'Prepare to be destroyed!'