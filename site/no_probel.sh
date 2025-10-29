#!/bin/sh
for i in *.pdf
do
        k=`echo ${i}|sed s/' '/'_'/g`
        mv "${i}" ${k}
done
