#!/bin/sh

mkdir lowres;
echo "Start convert.";
for f in *.webp;
do
echo "Converting file $f";
pio "$f" --quality 80 --output "lowres/${f%.webp}";
echo "Converting file $f complete";
done;
echo "Converting complete.";
