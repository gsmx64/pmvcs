@ECHO OFF
ECHO -----------------------------------------
ECHO Runing Package CLI
ECHO -----------------------------------------
env\Scripts\python -m pmvcs.cli setup -l en
IF ERRORLEVEL 1 goto finish

:finish
PAUSE