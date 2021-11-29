@echo off
pip install -r requirements.txt
cd root
pyinstaller --add-data "books.txt;." -n "Online Library" --onefile main1.py
