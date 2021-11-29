@echo off
pip install -r requirements.txt
cd root
pyinstaller --add-data "books.txt;." -n "Online Library" --distpath %~dp0 --onefile main1.py
