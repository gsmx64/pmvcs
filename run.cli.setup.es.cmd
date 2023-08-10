@ECHO OFF
ECHO -----------------------------------------
ECHO Runing Package CLI
ECHO -----------------------------------------
env\Scripts\python -m pmvcs.cli setup -l es
IF ERRORLEVEL 1 goto finish

:finish
PAUSE