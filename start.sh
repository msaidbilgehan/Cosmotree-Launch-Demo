#!/bin/bash

# Dizine git
cd ~/Cosmotree_Expertiment/Docker

# Python Flask uygulamasını başlat
python flask_app.py &

# Chromium'u belirtilen adreste aç
# Birkaç saniye bekleme süresi ekledik, Flask uygulamasının başlaması için
sleep 2
chromium-browser 127.0.0.1:5005 &

exit 0
