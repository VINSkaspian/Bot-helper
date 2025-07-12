@echo off
REM Активуємо віртуальне середовище (якщо є)
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

REM Запускаємо головний скрипт
python main.py

pause
