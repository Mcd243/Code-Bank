#!/bin/bash
mkdir renamed2
cd Docker2 || exit
for item in $(seq 1 "$(ls | wc -l)")
do
mv -u "$(ls | head -1)" "$(wc -m "$(ls | head -1)" | cut -f1 -d" ")" 
mv "$(wc -m "$(ls | head -1)" | cut -f1 -d" ")"  /home/osboxes/renamed2
done
cd ..
cd renamed2 || exit
for item in $(seq 1 "$(ls | wc -l)")
do
mv -u "$(ls | sort -n | head -1)" $item 
mv $item  /home/osboxes/Docker2
done
cd ..


# Docker1
echo '#!/bin/bash' > SORT1
echo 'mkdir renamed' >> SORT1
echo 'cd Docker1 || exit' >> SORT1
echo 'for item in $(seq 1 "$(ls | wc -l)")' >> SORT1
echo 'do' >> SORT1
echo 'mv -u "$(ls | head -1)" "$(wc -m "$(ls | head -1)" | cut -f1 -d" ")"' >> SORT1 
echo 'mv "$(wc -m "$(ls | head -1)" | cut -f1 -d" ")"  /tmp/renamed' >> SORT1
echo 'done' >> SORT1
echo 'cd ..' >> SORT1
echo 'cd renamed || exit' >> SORT1
echo 'for item in $(seq 1 "$(ls | wc -l)")' >> SORT1
echo 'do' >> SORT1
echo 'mv -u "$(ls | sort -n | head -1)" $item' >> SORT1 
echo 'mv $item  /tmp/Docker2' >> SORT1
echo 'done' >> SORT1
echo 'cd ..' >> SORT1

# Docker2
echo '#!/bin/bash' > SORT2
echo 'mkdir renamed' >> SORT2
echo 'cd Docker2 || exit' >> SORT2
echo 'for item in $(seq 1 "$(ls | wc -l)")' >> SORT2
echo 'do' >> SORT2
echo 'mv -u "$(ls | head -1)" "$(wc -m "$(ls | head -1)" | cut -f1 -d" ")"' >> SORT2 
echo 'mv "$(wc -m "$(ls | head -1)" | cut -f1 -d" ")"  /tmp/renamed' >> SORT2
echo 'done' >> SORT2
echo 'cd ..' >> SORT2
echo 'cd renamed || exit' >> SORT2
echo 'for item in $(seq 1 "$(ls | wc -l)")' >> SORT2
echo 'do' >> SORT2
echo 'mv -u "$(ls | sort -n | head -1)" $item' >> SORT2 
echo 'mv $item  /tmp/Docker2' >> SORT2
echo 'done' >> SORT2
echo 'cd ..' >> SORT2

# Docker3
echo '#!/bin/bash' > SORT3
echo 'mkdir renamed' >> SORT3
echo 'cd Docker3 || exit' >> SORT3
echo 'for item in $(seq 1 "$(ls | wc -l)")' >> SORT3
echo 'do' >> SORT3
echo 'mv -u "$(ls | head -1)" "$(wc -m "$(ls | head -1)" | cut -f1 -d" ")"' >> SORT3 
echo 'mv "$(wc -m "$(ls | head -1)" | cut -f1 -d" ")"  /tmp/renamed' >> SORT3
echo 'done' >> SORT3
echo 'cd ..' >> SORT3
echo 'cd renamed || exit' >> SORT3
echo 'for item in $(seq 1 "$(ls | wc -l)")' >> SORT3
echo 'do' >> SORT3
echo 'mv -u "$(ls | head -1)" $item' >> SORT3 
echo 'mv $item  /tmp/Docker3' >> SORT3
echo 'done' >> SORT3
echo 'cd ..' >> SORT3