#!/bin/bash

# Активуємо віртуальне середовище, якщо воно існує
if [ -f "venv/bin/activate" ]; then
  source venv/bin/activate
fi

# Запускаємо програму
python3 main.py
