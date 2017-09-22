beverly-hills
=============

Programs I wrote to help me at a mostly office job


When I was working I was assigned certain tasks I knew would be better automated, so I made these little scripts. Maybe someone will find them useful.

lobby.py is a python script I used to make [This](http://www.beverlyhills.org/citygovernment/departments/cityclerksoffice/legislativeadvocateregistrationform/20132014forms/) website on the City's web builder. Tables in HTML are always super annoying and I knew the formatting would need to get edited constantly, so I figured that I could make my own markup language to deal with what names get what links and then change the translation of that language as I go along.

CreateDirectory.bat is a batch file I made to help my boss organize her files. When I run it in a folder, it creates a list of all the files in the folder, then opens up that list and deletes itself and the list to remove clutter (I would then just print the list and my boss would tell me what to do with the files).

AllFiles.bat is similar, it just does it for all subfolders in the folder specified (couldn't figure out how to make this generic). It also doesn't self destruct.

Just saying it's really hard to test code that deletes itself...
