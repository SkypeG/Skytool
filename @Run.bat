@echo off

python "main.py"
:loop
python "main_2.py"

goto loop
pause
