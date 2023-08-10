@ECHO OFF
ECHO -----------------------------------------
ECHO Runing Package CLI
ECHO -----------------------------------------
env\Scripts\python -m pmvcs.cli menu -l es
IF ERRORLEVEL 1 goto finish

:finish
PAUSE