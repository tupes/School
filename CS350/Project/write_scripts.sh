FIRST_ACCT_NAME="user"
FIRST_ACCT_PW="password"
EMU_SHORT_NAME="SMALLEQEMU"
EMU_LONG_NAME="Ship_In_A_Bottle"
EXT_IP=`ifconfig eth1 | grep "inet addr:" | awk -F: '{ print $2 }' | awk '{ print $1 }'`
#
cd /home/eqemu/server
#
echo ' '
echo '+--------------------------------------------------------------+ '
echo '! Writing Startup Script... !'
read -p "[ Press [ENTER] to continue... ]"
echo '+--------------------------------------------------------------+ '
echo ' '
echo 'ulimit -c unlimited ' > /home/eqemu/server/startup.sh
echo ' ' >> /home/eqemu/server/startup.sh
echo 'cd /home/eqemu/server ' >> /home/eqemu/server/startup.sh
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:. ' >> /home/eqemu/server/startup.sh
echo ' ' >> /home/eqemu/server/startup.sh
echo 'rm -rf /home/eqemu/server/logs/login.log ' >> /home/eqemu/server/startup.sh
echo 'rm -rf /home/eqemu/server/logs/world.log ' >> /home/eqemu/server/startup.sh
echo 'rm -rf /home/eqemu/server/logs/zones.log ' >> /home/eqemu/server/startup.sh
echo 'rm -rf /home/eqemu/server/logs/*.log ' >> /home/eqemu/server/startup.sh
echo 'chmod --recursive ugo+rwx /home/eqemu/server/quests ' >> /home/eqemu/server/startup.sh
echo ' ' >> /home/eqemu/server/startup.sh
echo 'echo Starting Login Server... ' >> /home/eqemu/server/startup.sh
echo ' ./EQEmuLoginServer 2>&1 >> /home/eqemu/server/logs/login.log & ' >> /home/eqemu/server/startup.sh
echo ' ' >> /home/eqemu/server/startup.sh
echo 'echo Waiting about 5 seconds before starting World Server... ' >> /home/eqemu/server/startup.sh
echo 'sleep 5 ' >> /home/eqemu/server/startup.sh
echo ' ' >> /home/eqemu/server/startup.sh
echo './world 2>&1 > /home/eqemu/server/logs/world.log & ' >> /home/eqemu/server/startup.sh
echo ' ' >> /home/eqemu/server/startup.sh
echo 'echo Waiting 10 seconds before starting the zones via launcher ' >> /home/eqemu/server/startup.sh
echo 'sleep 10 ' >> /home/eqemu/server/startup.sh
echo './eqlaunch zone 2>&1 > /home/eqemu/server/logs/zones.log & ' >> /home/eqemu/server/startup.sh
echo ' ' >> /home/eqemu/server/startup.sh
echo 'echo The server is mostly ready... give it a couple of minutes ' >> /home/eqemu/server/startup.sh
echo 'echo to load stuff from the databases for the zones and users ' >> /home/eqemu/server/startup.sh
echo 'echo can start logging in. ' >> /home/eqemu/server/startup.sh
chmod ugo+x /home/eqemu/server/startup.sh
#
# CREATE db.ini
#
echo '+--------------------------------------------------------------+'
echo '! Writing db.ini !
'
echo '+--------------------------------------------------------------+'
echo '[Database] ' > /home/eqemu/server/db.ini
echo "host=$EXT_IP " >> /home/eqemu/server/db.ini
echo 'user=eqemu ' >> /home/eqemu/server/db.ini
echo 'password=eqemupw ' >> /home/eqemu/server/db.ini
echo 'database=peqdb ' >> /home/eqemu/server/db.ini
#
# CREATE login.ini
#
echo '+--------------------------------------------------------------+'
echo '! Writing login.ini !'
echo '+--------------------------------------------------------------+'
echo '[database] ' > /home/eqemu/server/login.ini
echo "host = $EXT_IP " >> /home/eqemu/server/login.ini
echo 'port = 3306 ' >> /home/eqemu/server/login.ini
echo 'db = peqdb ' >> /home/eqemu/server/login.ini
echo 'user = eqemu ' >> /home/eqemu/server/login.ini
echo 'password = eqemupw ' >> /home/eqemu/server/login.ini
echo 'subsystem = MySQL ' >> /home/eqemu/server/login.ini
echo ' ' >> /home/eqemu/server/login.ini
echo '[options] ' >> /home/eqemu/server/login.ini
echo 'unregistered_allowed = TRUE ' >> /home/eqemu/server/login.ini
echo 'reject_duplicate_servers = FALSE ' >> /home/eqemu/server/login.ini
echo 'trace = TRUE ' >> /home/eqemu/server/login.ini
echo 'world_trace = FALSE ' >> /home/eqemu/server/login.ini
echo 'dump_packets_in = FALSE ' >> /home/eqemu/server/login.ini
echo 'dump_packets_out = FALSE ' >> /home/eqemu/server/login.ini
echo 'listen_port = 5998 ' >> /home/eqemu/server/login.ini
echo 'local_network = 192.168.0. ' >> /home/eqemu/server/login.ini
echo ' ' >> /home/eqemu/server/login.ini
echo '[security] ' >> /home/eqemu/server/login.ini
echo 'plugin = EQEmuAuthCrypto ' >> /home/eqemu/server/login.ini
echo 'mode = 5 ' >> /home/eqemu/server/login.ini
echo ' ' >> /home/eqemu/server/login.ini
echo '[Titanium] ' >> /home/eqemu/server/login.ini
echo 'port = 5998 ' >> /home/eqemu/server/login.ini
echo 'opcodes = login_opcodes.conf ' >> /home/eqemu/server/login.ini
echo ' ' >> /home/eqemu/server/login.ini
echo '[SoD] ' >> /home/eqemu/server/login.ini
echo 'port = 5999 ' >> /home/eqemu/server/login.ini
echo 'opcodes = login_opcodes_sod.conf ' >> /home/eqemu/server/login.ini
echo ' ' >> /home/eqemu/server/login.ini
echo '[schema] ' >> /home/eqemu/server/login.ini
echo 'account_table = tblLoginServerAccounts ' >> /home/eqemu/server/login.ini
echo 'world_registration_table = tblWorldServerRegistration ' >> /home/eqemu/server/login.ini
echo 'world_admin_registration_table = tblServerAdminRegistration ' >> /home/eqemu/server/login.ini
echo 'world_server_type_table = tblServerListType ' >> /home/eqemu/server/login.ini
#
# CREATE LoginServer.ini
#
echo '+--------------------------------------------------------------+ '
echo '! Writing LoginServer.ini !'
echo '+--------------------------------------------------------------+ '
echo '[LoginServer] ' > /home/eqemu/server/LoginServer.ini
echo 'loginserver=EQEMU-SERVER ' >> /home/eqemu/server/LoginServer.ini
echo 'loginport=5998 ' >> /home/eqemu/server/LoginServer.ini
echo "worldname=$EMU_LONG_NAME " >> /home/eqemu/server/LoginServer.ini
echo "worldaddress=$EXT_IP " >> /home/eqemu/server/LoginServer.ini
echo 'locked=false ' >> /home/eqemu/server/LoginServer.ini
echo 'account= ' >> /home/eqemu/server/LoginServer.ini
echo 'password= ' >> /home/eqemu/server/LoginServer.ini
echo ' ' >> /home/eqemu/server/LoginServer.ini
echo '[WorldServer] ' >> /home/eqemu/server/LoginServer.ini
echo 'Defaultstatus=0 ' >> /home/eqemu/server/LoginServer.ini
echo 'Unavailzone= ' >> /home/eqemu/server/LoginServer.ini
echo ' ' >> /home/eqemu/server/LoginServer.ini
echo '[ChatChannelServer] ' >> /home/eqemu/server/LoginServer.ini
echo 'worldshortname=- ' >> /home/eqemu/server/LoginServer.ini
echo 'chataddress= ' >> /home/eqemu/server/LoginServer.ini
echo 'chatport= ' >> /home/eqemu/server/LoginServer.ini
#
# CREATE eqemu_config.xml
#
echo '+--------------------------------------------------------------+ '
echo '! Writing eqemu_config.xml !'
echo '+--------------------------------------------------------------+ '
echo '<?xml version="1.0"> ' > /home/eqemu/server/eqemu_config.xml
echo '<server> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <world> ' >> /home/eqemu/server/eqemu_config.xml
echo " <shortname>$EMU_SHORT_NAME</shortname> " >> /home/eqemu/server/eqemu_config.xml
echo " <longname>$EMU_LONG_NAME</longname> " >> /home/eqemu/server/eqemu_config.xml
echo ' ' >> /home/eqemu/server/eqemu_config.xml
echo ' <address>EQEMU-SERVER</address> --> ' >> /home/eqemu/server/eqemu_config.xml
echo " <localaddress>$EXT_IP</localaddress> --> " >> /home/eqemu/server/eqemu_config.xml
echo ' ' >> /home/eqemu/server/eqemu_config.xml
echo ' <!-- Loginserver information. Defaults shown --> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <loginserver> ' >> /home/eqemu/server/eqemu_config.xml
echo " <host>$EXT_IP</host> " >> /home/eqemu/server/eqemu_config.xml
echo ' <port>5998</port> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <account>Admin</account> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <password>Password</password> ' >> /home/eqemu/server/eqemu_config.xml
echo ' </loginserver> ' >> /home/eqemu/server/eqemu_config.xml
echo ' ' >> /home/eqemu/server/eqemu_config.xml
echo ' <!-- Server status. Default is unlocked --> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <!--<locked/>--> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <unlocked/> ' >> /home/eqemu/server/eqemu_config.xml
echo ' ' >> /home/eqemu/server/eqemu_config.xml
echo " <tcp ip=$EXT_IP port=9000 telnet=disable /> " >> /home/eqemu/server/eqemu_config.xml
echo ' ' >> /home/eqemu/server/eqemu_config.xml
echo ' <key>some long random string</key> ' >> /home/eqemu/server/eqemu_config.xml
echo ' ' >> /home/eqemu/server/eqemu_config.xml
echo ' <http port="9080" enabled="false" mimefile="mime.types" /> ' >> /home/eqemu/server/eqemu_config.xml
echo ' </world> ' >> /home/eqemu/server/eqemu_config.xml
echo ' ' >> /home/eqemu/server/eqemu_config.xml
echo ' <!-- Chatserver (channels) information. Defaults shown --> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <chatserver> ' >> /home/eqemu/server/eqemu_config.xml
echo " <host>$EXT_IP</host> " >> /home/eqemu/server/eqemu_config.xml
echo ' <port>7778</port> ' >> /home/eqemu/server/eqemu_config.xml
echo ' </chatserver> ' >> /home/eqemu/server/eqemu_config.xml
echo ' ' >> /home/eqemu/server/eqemu_config.xml
echo ' <mailserver> ' >> /home/eqemu/server/eqemu_config.xml
echo " <host>$EXT_IP</host> " >> /home/eqemu/server/eqemu_config.xml
echo ' <port>7779</port> ' >> /home/eqemu/server/eqemu_config.xml
echo ' </mailserver> ' >> /home/eqemu/server/eqemu_config.xml
echo ' ' >> /home/eqemu/server/eqemu_config.xml
echo ' <zones> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <defaultstatus>20</defaultstatus> ' >> /home/eqemu/server/eqemu_config.xml
echo ' ' >> /home/eqemu/server/eqemu_config.xml
echo ' <ports low="7000" high="7100"/> ' >> /home/eqemu/server/eqemu_config.xml
echo ' </zones> ' >> /home/eqemu/server/eqemu_config.xml
echo ' ' >> /home/eqemu/server/eqemu_config.xml
echo ' <database> ' >> /home/eqemu/server/eqemu_config.xml
echo " <host>$EXT_IP</host> " >> /home/eqemu/server/eqemu_config.xml
echo ' <port>3306</port> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <username>eqemu</username> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <password>eqemupw</password> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <db>peqdb</db> ' >> /home/eqemu/server/eqemu_config.xml
echo ' </database> ' >> /home/eqemu/server/eqemu_config.xml
echo ' ' >> /home/eqemu/server/eqemu_config.xml
echo ' <!-- Launcher Configuration --> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <launcher> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <!-- <logprefix>logs/zone-</logprefix> --> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <!-- <logsuffix>.log</logsuffix> --> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <!-- <exe>zone.exe or ./zone</exe> --> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <!-- <timers restart="10000" reterminate="10000"> --> ' >> /home/eqemu/server/eqemu_config.xml
echo ' </launcher> ' >> /home/eqemu/server/eqemu_config.xml
echo ' ' >> /home/eqemu/server/eqemu_config.xml
echo ' <!-- File locations. Defaults shown --> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <files> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <spells>spells_us.txt</spells> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <opcodes>opcodes.conf</opcodes> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <logsettings>log.ini</logsettings> ' >> /home/eqemu/server/eqemu_config.xml
echo ' </files> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <!-- Directory locations. Defaults shown --> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <directories> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <maps>/home/eqemu/server/Maps</maps> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <quests>/home/eqemu/server/quests</quests> ' >> /home/eqemu/server/eqemu_config.xml
echo ' <plugins>/home/eqemu/server/plugins</plugins> ' >> /home/eqemu/server/eqemu_config.xml
echo ' </directories> ' >> /home/eqemu/server/eqemu_config.xml
echo '</server> ' >> /home/eqemu/server/eqemu_config.xml
chmod -R ugo+rw /home/eqemu
echo "killall eqlaunch world zone EQEmuLoginServer " > /home/eqemu/server/killeq.sh
chmod -R ugo+x /home/eqemu/server/killeq.sh
echo ' '
echo '+--------------------------------------------------------------+ '
echo '! Done with the installation !'
echo '! !'
echo '!  Please copy spells_us.txt to the !'
echo '! /home/eqemu/server directory now. !'
echo '! !'
echo '!--------------------------------------------------------------!'
echo '! Then you can reboot your machine and run !'
echo '! /home/eqemu/server/startup.sh !'
echo '! !'
echo '+--------------------------------------------------------------+ '
echo ' '