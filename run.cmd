@ECHO OFF
ECHO -----------------------------------------
ECHO Runing App
ECHO -----------------------------------------
env\Scripts\python app.py
IF ERRORLEVEL 1 goto finish

:finish
PAUSE