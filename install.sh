#!/bin/bash
sudo apt install python3-tk ffmpeg


python -m pip install -r requiroments.txt

chmod +x ytdownload
echo $(pwd)
export PATH=$PATH:$(pwd)

echo "export PATH=\$PATH:$(pwd)" >> ~/.bashrc
source ~/.bashrc
