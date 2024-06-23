#!/bin/bash
cd ~/Documents/Pip-Boy
git add .
git commit -m "Arch Sync $(date)"
git pull
git push
