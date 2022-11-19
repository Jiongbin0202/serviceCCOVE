import arcpy
from arcpy import env
import os
import sys
# === import project path ===
curPath = os.path.abspath(os.path.dirname("E:\\arcpy\\keda\\Natural\\SDG\\keda2\\dto.py"))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
# ===========================
# sys.path.append("..")
from keda2 import dto

def Run(serviceCove0, exOptions0):
    
    return serviceCove0

def Run2(serviceCove1, exOptions1):
    
    return serviceCove