#! /usr/bin/env python
# -*- coding: utf-8 -*-

# DaVinci Resolve V16 export to DRP all projects in the current folder.
# Copyright 2019 Igor Riđanović, www.metafide.com, www.hdhead.com - 
# With tweaks for Python 3.6 John Rogers 2021

#this is the way that readme.txt suggests loading the python module and works for me on my computer
import DaVinciResolveScript as dvr_script 
resolve = dvr_script.scriptapp("Resolve")
fusion = resolve.Fusion()

import os #for path functions

def export_drp(p):

	projs = pm.GetProjectsInCurrentFolder()

	for i in projs.values():

		try:
			pm.ExportProject(i, os.path.join(p, i))
		except TypeError:
			print('This script requires DaVinci Resolve 16.')
			return None

		print( 'Exported', i)

	return True


if name == 'main':

# Instantiate Resolve objects
    pm  = resolve.GetProjectManager()
    #sets database name as a new or existing folder name in path 
    dbn = pm.GetCurrentDatabase()
    dbn2 = dbn.get('DbName')
    print(dbn2)
# Set the path1 to the DRP export directory
path = ''
path1 = path + dbn2

if export_drp(path1):
    print('Export completed.')