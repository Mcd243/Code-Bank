################ BASIC CASE STATEMENT ################
# CASE STATEMENTS ARE MORE EFFICIENT THAN IF ELIF ELSE 
# STATEMENTS ANS THE ONLY CHECK ONE CONDITION AND THEN 
# FIND THE CORRECT RESULT

#!/BIN/BASH

# get user input and store in variable choice
read -p "Enter your choice [yes/no]:" choice

case $choice in
    yes)
        echo "Thank you"
        echo "You type: Yes"
        ;;
    no) 
        echo "Oooops"
        echo "You type: No"
        ;;
    *)
        echo "Sorry, invalid input"
        ;;
Esac
