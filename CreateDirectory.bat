echo %CD%:  > FolderDirectory.txt
echo -- >> FolderDirectory.txt
dir /B /O:GN >> FolderDirectory.txt
FolderDirectory.txt
del FolderDirectory.txt
( del /q /f "%~f0" >nul 2>&1 & exit /b 0  )
