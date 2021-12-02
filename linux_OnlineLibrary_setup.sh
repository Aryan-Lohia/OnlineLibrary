#/bin/bash
pip install -r requirements.txt
cd root
pyinstaller --add-data "books.txt;." -n "Online Library" --distpath output --onefile main1.py
cd output
chmod +x ./Online\ Library
cp ./Online\ Library /usr/local/bin/Online\ Library

