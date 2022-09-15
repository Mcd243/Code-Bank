################## Alias ################

# remove core files generated by c program
alias rmc="find . -iname core -exec rm {} \;"

# remove a.out files
alias rmao="find . -iname a.out -exec rm {} \;"

# find and remove archive files
find / -type f -name *.zip -size +100M -exec rm -i {} \;


alias rm100m="find / -type f -name *.zip -size +100M -exec rm -i {} \;"


alias rm1g="find / -type f -name *.tar -size +1G -exec rm -i {} \;"


alias rm100m="find / -type f -name *.tar -size +100M -exec rm -i {} \;"


alias rm2g="find / -type f -name *.tar -size +2G -exec rm -i {} \;"


alias rm5g="find / -type f -name *.tar -size +5G -exec rm -i {} \;"