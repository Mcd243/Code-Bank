USE FSTP TO TRANSFER A FILE (.sql / .csv)TO YOUR SERVER
# IN POWER SHELL
# CONNECT TO SERVER USING FSTP

sftp 40536364@set08120.napier.ac.uk 

#ENTER THE SERVER PASSWORD

# AT THE SFTP PROMPT sftp>
# use the put commad to send the file from where Power shell is executing
# (probably ~)

put make_ge.sql

# bye to exit

bye

# Now connect to the server

#############################################################
ON POWERSHELL connect to the server

ssh 40536364@set08120.napier.ac.uk

# enter server PASSWORD

#############################################################
# Connect to an existing database

mysql -u 40536364 -p'Qun76BCK' 40536364

# mysql -u (user_id) -p (password) (database_name)

#############################################################
#CREATE A database

# enter the Maria CLI

./maria

source filename.sql


##############################################################
IMPORT A CSV FILE

LOAD DATA INFILE '/tmp/hocl-ge2015-results-full.csv' 
INTO TABLE ge COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n' IGNORE 1 LINES;