# DaVinciResolve-ExportProjects
Export all DaVinci Resolve projects from the current folder to DRP and delete the projects.

This script requires DaVinci Resolve Studio V16 or above. We import the API using the canonical Blackmagic Design implementation. This is not the only OS portable way to import the API library. Read the developer documentation that ships with Resolve if unable to create a resolve instance.

If writing an automated DRP export tool consider that Resolve Studio must be running and that each ExportProject() call will block the application. Generally speaking, a database dump is a more end-user transparent DaVinci Resolve backup method.

See DaVinci Resolve disk database backup: https://www.hdhead.com/?p=841 
DaVinci Resolve PostgreSQL backup: https://www.hdhead.com/?p=857


UPDATE for 2022
Added an aditional script that uses the Pydavinci library - https://github.com/pedrolabonia/pydavinci
rather than the native resolve library, both scripts do the same thing should do the same thing, 
However the Pydavinci Script is confirmed working with resolve 18.1 and Python 3.6.13
