@echo off

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot

set TOKEN=5052253141:AAFuWhy5eVDhyxQTf_SKV9SYoxnw2JYvITk

python bot_telegram.py

pause