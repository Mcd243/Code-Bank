#!/bin/sh
mkdir GODockers
cd GODockers
touch final_chapter.txt


find / -type d -name "Docker1" -exec mv {} ./Docker1 \;
find / -type d -name "Docker2" -exec mv {} ./Docker2 \;
find / -type d -name "Docker3" -exec mv {} ./Docker3 \;

