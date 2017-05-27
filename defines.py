#!/usr/bin/env python

#############################################################################
############################   IMPORTS     ##################################
#############################################################################
import os
import sys
import re

global RVBase
RVBase = 64

def sign_extending(x, b):
    if x&(1<<(b-1)): # is the highest bit (sign) set? (x>>(b-1)) would be faster
        return x-(1<<b) # 2s complement
    return x

def sign_extending_12bit(x: object) -> object:
    if x >> 11: # is the highest bit (sign) set? (x>>(b-1)) would be faster
        return x-(1<<12) # 2s complement
    return x

import ctypes

def uiSize(val):
    if RVBase == 32:
        return ctypes.c_uint32(val).value
    else:
        return ctypes.c_uint64(val).value

def iSize(val):
    if RVBase == 32:
        return ctypes.c_int32(val).value
    else:
        return ctypes.c_int64(val).value

#############################################################################
############################   COLORAMA    ##################################
#############################################################################
#from colorama import init
from colorama import Fore, Back, Style
color_rst = Fore.RESET + Back.RESET + Style.RESET_ALL
def print_yellow(m):
    print(Style.BRIGHT + Back.YELLOW + Style.NORMAL + Fore.BLACK + m + color_rst)
    log(m +'\n')

def print_red(m):
    print(Back.RED + Style.BRIGHT + Fore.BLACK + m + color_rst)
    log(m +'\n')

def print_blue(m):
    print(Back.BLACK + Style.NORMAL + Fore.CYAN + m + color_rst)
    log(m +'\n')

def log(m):
    print(log)

#############################################################################
########################   MESSAGING & LOGGING  #############################
#############################################################################



def info(m):
    print_blue(m)

class RunSimError(Exception):
    """this is a exception to signal an  error"""

def error (m,e2w=False):
    if not e2w:
        print_red("ERROR: " + m)
        raise RunSimError
    else:
        warning(m)

def warning(m):
    #frame,filename,line_number,function_name,lines,index= inspect.getouterframes(inspect.currentframe())[1]
    #inf = " @ file: %s, line %s " % ( filename, line_number)
    print_yellow("WARNING: " + m)




class Singleton(object):
    __instance = None
    def __new__(cls, val):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls)
        Singleton.__instance.val = val
        return Singleton.__instance

SINGLETON = Singleton("ISS Singleton")



def printR(r):
    switcher = {
        0: "zero",
        1: "ra",
        2: "sp",
        3: "gp",
        4: "tp",
        5: "t0",
        6: "t1",
        7: "t2",
        8: "s0",
        9: "s1",
        10: "a0",
        11: "a1",
        12: "a2",
        13: "a3",
        14: "a4",
        15: "a5",
        16: "a6",
        17: "a7",
        18: "s2",
        19: "s3",
        20: "s4",
        21: "s5",
        22: "s6",
        23: "s7",
        24: "s8",
        25: "s9",
        26: "s10",
        27: "s11",
        28: "t3",
        29: "t4",
        30: "t5",
        31: "t6",
    }
    return switcher.get(r, None)