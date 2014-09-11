#!/bin/bash

chmod 755 *sh
chmod 755 *py

cd ~/
git clone https://github.com/geekspark-rh/dimo-input.git
cd ~/dimo-input
bash install.sh

cd ~/
mkdir ~/demos

cd ~/demos
git clone https://github.com/geekspark-rh/dimo-renderer.git
