echo ' '
echo '+--------------------------------------------------------------+ '
echo '! Loading the database (could take a few minutes)... !'
echo '+--------------------------------------------------------------+ '
echo ' '
cd /home/eqemu/source/peqdatabase/
#
# Set the root DB password to passw0rd
# Creating eqemu user with initial password to eqemupw
#
echo "set password for 'root'@'localhost' = PASSWORD('passw0rd');" > /home/eqemu/server/logs/db_users.sql
echo "GRANT ALL PRIVILEGES ON *.* TO 'eqemu'@'%' IDENTIFIED BY 'eqemupw';" >> /home/eqemu/server/logs/db_users.sql
echo "flush privileges;" >> /home/eqemu/server/logs/db_users.sql
mysql -u root < /home/eqemu/server/logs/db_users.sql
rm -rf /home/eqemu/server/logs/db_users.sql
#
# Get ready to load the database
#
mysql -u root -ppassw0rd -e "drop database if exists peqdb; create database if not exists peqdb;"
gunzip peqdb_rev*.sql.gz
mysql -u root -ppassw0rd -f -D peqdb < /home/eqemu/source/peqdatabase/peqdb_*.sql
# that might take a little time -- just under two minutes on my machine...
mysql -u root -ppassw0rd -f -D peqdb < /home/eqemu/source/peqdatabase/load_player.sql
mysql -u root -ppassw0rd -f -D peqdb < /home/eqemu/source/peqdatabase/load_login.sql
mysql -u root -ppassw0rd -f -D peqdb < /home/eqemu/source/peqdatabase/load_bots.sql
mysql -uroot -ppassw0rd -D peqdb < /home/eqemu/source/EQEmuServer/EQEmuLoginServer/login_util/EQEmuLoginServerDBInstall.sql
#
# Now we load that first account so we can have a GM account (or just muck around)
#
FIRST_ACCT_NAME="user"
FIRST_ACCT_PW="password"
EMU_SHORT_NAME="SMALLEQEMU"
EMU_LONG_NAME="Ship_In_A_Bottle"
echo "insert into tblLoginServerAccounts (AccountName, AccountPassword ) values('xFN', sha('xPW') );" | sed s/xFN/$FIRST_ACCT_NAME/ | sed s/xPW/$FIRST_ACCT_PW/ > lsa.sql
mysql -uroot -ppassw0rd -D peqdb < lsa.sql
echo "UPDATE tblWorldServerRegistration SET ServerLongName = 'xLN', ServerShortName = 'xSN' WHERE ServerID = 1;" | sed s/xLN/$EMU_LONG_NAME/| sed s/xSN/$EMU_SHORT_NAME/ > wsr.sql
mysql -uroot -ppassw0rd -D peqdb < wsr.sql
#