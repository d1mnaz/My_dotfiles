#!/bin/bash

mkdir lowres;
echo "Start convert.";
for f in *.JPG;
do
echo "Converting file $f";
magick convert -resize  1440 "$f" "lowres/${f%.jpg}.jpg";
echo "Converting file $f complete";
done;
echo "Converting complete.";
