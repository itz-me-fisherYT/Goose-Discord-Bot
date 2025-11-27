@echo off
:loop
python main.py
timeout /t 21600
goto loop
