#coding=utf-8
# mysetup.py
from distutils.core import setup
import py2exe
# Powered by ***
INCLUDES = []
options = {"py2exe" :  
    {"compressed" : 1,  
     "optimize" : 1,  
     "bundle_files" : 2,  
     "includes" : INCLUDES}}  
setup(
    options = options, 
    description = "dbc-downloader",  
    zipfile=None,
    console=[{"script": "dbcDownloader.py"}],
    )