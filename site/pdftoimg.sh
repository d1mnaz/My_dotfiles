# /bin/bash
for f in *.pdf; do
  gm convert  -density 300  -quality 90 ./"$f" ./"${f%.pdf}.jpg"
done
