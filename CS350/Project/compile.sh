echo ' '
echo '+--------------------------------------------------------------+ '
echo '! About to compile source code for a lot of stuff... !'
echo '! Expect this to take at least several minutes -- !'
echo '! Dont be surprised if this takes up to 20ish minutes. !'
echo '+--------------------------------------------------------------+ '
echo ' '
cd /home/eqemu/source/EQEmuServer
make clean &> /home/eqemu/clean_eqemuserver.log
make &> /home/eqemu/compile_eqemuserver.log
#
# takes 12 minutes
# check that log file with nano just to see that there were no errors..
# if there were errors, then they'd probably be on the screen too, so only panic
# if you see a problem on-screen
#
#
# Now we get the correct crypto files for our OS
# for the LoginServer
#
cd /home/eqemu/source/EQEmuServer/EQEmuLoginServer/login_util/linux/ubuntu-9-10-32/
rm -rf libEQEmuAuthCrypto.a
rm -rf libcryptopp.a
unzip ubt91032_lib.zip
cp /home/eqemu/source/EQEmuServer/EQEmuLoginServer/login_util/linux/ubuntu-9-10-32/lib*.* /home/eqemu/source/EQEmuServer/EQEmuLoginServer/
#
# Preparing to compile the login-server now.
#
cd /home/eqemu/source/EQEmuServer/EQEmuLoginServer
make clean &> /home/eqemu/clean_eqemuloginserver.log
make &> /home/eqemu/compile_eqemuloginserver.log
cd /home/eqemu/server
echo ' '
echo '+--------------------------------------------------------------+ '
echo '! Making links to compiled executables in the server directory.!'
echo '+--------------------------------------------------------------+ '
echo ' '
ln -s /home/eqemu/source/EQEmuServer/EMuShareMem/libEMuShareMem.so /home/eqemu/server/libEMuShareMem.so
ln -s /home/eqemu/source/EQEmuServer/world/world /home/eqemu/server/world
ln -s /home/eqemu/source/EQEmuServer/zone/zone /home/eqemu/server/zone
ln -s /home/eqemu/source/EQEmuServer/EQEmuLoginServer/EQEmuLoginServer /home/eqemu/server/EQEmuLoginServer
ln -s /home/eqemu/source/EQEmuServer/eqlaunch/eqlaunch /home/eqemu/server/eqlaunch
ln -s /home/eqemu/source/EQEmuServer/chatserver/chatserver /home/eqemu/server/chatserver
ln -s /home/eqemu/source/EQEmuServer/mailserver/mailserver /home/eqemu/server/mailserver
#