#! /usr/bin/python
# -*- coding: utf-8 -*-

class KpdData:
    _row = -1
    _col = -1
    _gpioNum = -1
    _util = ''
    _homeKey = ''
    _keyType = ''
    _pressTime = -1
    _dinHigh = False
    _matrix = []
    _useEint = False
    _downloadKeys = []
    _keyValueMap = {}
    _usedKeys = []
    _modeKeys = {'META':None, 'RECOVERY':None, 'FACTORY':None}

    def __init__(self):
        self.__varNames = []

    @staticmethod
    def set_row(row):
        KpdData._row = row

    @staticmethod
    def get_row():
        return KpdData._row

    @staticmethod
    def set_col(col):
        KpdData._col = col

    @staticmethod
    def get_col():
        return KpdData._col

    @staticmethod
    def set_matrix(matrix):
        KpdData._matrix = matrix

    @staticmethod
    def get_matrix():
        return KpdData._matrix

    @staticmethod
    def set_downloadKeys(keys):
        KpdData._downloadKeys = keys

    @staticmethod
    def get_downloadKeys():
        return KpdData._downloadKeys

    @staticmethod
    def get_modeKeys():
        return KpdData._modeKeys

    @staticmethod
    def set_gpioNum(num):
        KpdData._gpioNum = num

    @staticmethod
    def get_gpioNum():
        return KpdData._gpioNum

    @staticmethod
    def set_utility(util):
        KpdData._util = util

    @staticmethod
    def get_utility():
        return KpdData._util

    @staticmethod
    def set_homeKey(home):
        KpdData._homeKey = home

    @staticmethod
    def get_homeKey():
        return KpdData._homeKey

    @staticmethod
    def set_useEint(flag):
        KpdData._useEint = flag

    @staticmethod
    def getUseEint():
        return KpdData._useEint

    @staticmethod
    def set_gpioDinHigh(flag):
        KpdData._dinHigh = flag

    @staticmethod
    def get_gpioDinHigh():
        return KpdData._dinHigh

    @staticmethod
    def set_pressTime(time):
        KpdData._pressTime = time

    @staticmethod
    def get_pressTime():
        return KpdData._pressTime

    @staticmethod
    def set_keyType(keyType):
        KpdData._keyType = keyType


