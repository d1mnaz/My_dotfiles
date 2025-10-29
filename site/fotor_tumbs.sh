#!/bin/bash

mkdir lowres;
echo "Start convert.";
for f in *.jpg;
do
echo "Converting file $f";
convert -resize  300 "$f" "lowres/${f%.JPG}";
echo "Converting file $f complete";
done;
echo "Converting complete.";
