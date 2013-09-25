echo ' '
echo '+--------------------------------------------------------------+'
echo '! Downloading all the source-code, maps, db stuff from the net.!'
echo '! !'
echo '! This could take a few minutes and there might be pauses,,, !'
echo '+--------------------------------------------------------------+'
echo '+--------------------------------------------------------------+ '
echo ' '
#
# Prepare everything by making the necessary directories
#
mkdir -p /home/eqemu/server/logs
mkdir -p /home/eqemu/source
mkdir -p /home/eqemu/server/Maps
mkdir -p /home/eqemu/server/quests
mkdir -p /home/eqemu/server/plugins
#
# Make sure we are about to pull everything into the right directories..
#
cd /home/eqemu/source
#
# Second critical part -- getting all the most recent code,
# database items, quests, maps and plugins from the source.
# With super-fast connection speeds, this may still take a few
# minutes.
#
svn co http://projecteqemu.googlecode.com/svn/trunk/EQEmuServer
svn co http://projecteqdb.googlecode.com/svn/trunk/peqdatabase
svn co http://projecteqquests.googlecode.com/svn/trunk/quests
svn co http://eqemumaps.googlecode.com/svn/trunk/Maps
svn co http://allaclone-eoc.googlecode.com/svn/trunk/ allaclone-eoc-read-only
#
# Now copy from the SOURCE directories to the SERVER directories
# as needed. Might take a bit.
#
cp -r /home/eqemu/source/Maps/* /home/eqemu/server/Maps/
cp -r /home/eqemu/source/quests/* /home/eqemu/server/quests/
chmod --recursive ugo+rwx /home/eqemu/server/quests/
cp -r /home/eqemu/source/quests/plugins/* /home/eqemu/server/plugins/
chmod --recursive ugo+rwx /home/eqemu/server/plugins/
#
# Not sure if this next part is is needed...
#
cp /home/eqemu/source/EQEmuServer/utils/defaults/commands.pl /home/eqemu/server/
cp /home/eqemu/source/EQEmuServer/utils/defaults/plugin.pl /home/eqemu/server/
cp /home/eqemu/source/EQEmuServer/utils/defaults/worldui.pl /home/eqemu/server/
mkdir /home/eqemu/server/worldui
cp -r /home/eqemu/source/EQEmuServer/utils/defaults/worldui/ /home/eqemu/server/worldui/
echo ' '
echo '+--------------------------------------------------------------+ '
echo '! Moving ini files around and fixing source code make-files. !'
echo '+--------------------------------------------------------------+ '
echo ' '
cd /home/eqemu/server
cp /home/eqemu/source/EQEmuServer/utils/defaults/eqemu_config.xml.full eqemu_config.xml
cp /home/eqemu/source/EQEmuServer/utils/defaults/log.ini .
cp /home/eqemu/source/EQEmuServer/EQEmuLoginServer/login_util/login.ini .
cp /home/eqemu/source/EQEmuServer/EQEmuLoginServer/login_util/login_opcodes.conf .
cp /home/eqemu/source/EQEmuServer/EQEmuLoginServer/login_util/login_opcodes_sod.conf .
cp /home/eqemu/source/EQEmuServer/utils/*.conf .
#
# Out of the box, everything mostly compiles... but
# certain changes need to be made in order for all the critical
# executables to compile corectly.
#
# Firstly, change gmake to make in a MakeFile
# otherwise we get an error and the executable won't be produced.
#
cp /home/eqemu/source/EQEmuServer/utils/Makefile /home/eqemu/source/EQEmuServer/utils/Makefile.original
cat /home/eqemu/source/EQEmuServer/utils/Makefile | sed s/gmake/make/ > /home/eqemu/source/EQEmuServer/utils/Makefile.New
cp /home/eqemu/source/EQEmuServer/utils/Makefile.New /home/eqemu/source/EQEmuServer/utils/Makefile
#
# Next, change some compiler flags in another makefile so we can get the right code
# for the executable.
#
cp /home/eqemu/source/EQEmuServer/EQEmuLoginServer/makefile /home/eqemu/source/EQEmuServer/EQEmuLoginServer/makefile.original
cat /home/eqemu/source/EQEmuServer/EQEmuLoginServer/makefile | sed s/'(MYSQL_FLAGS)/(MYSQL_FLAGS) -std=c++0x'/ > /home/eqemu/source/EQEmuServer/EQEmuLoginServer/makefile.New
cp /home/eqemu/source/EQEmuServer/EQEmuLoginServer/makefile.New /home/eqemu/source/EQEmuServer/EQEmuLoginServer/makefile
#
# Lastly, we must change the crc32.cpp a bit to get the i386
# changed so we can have characters DIE without crashing the zone.
#
cp /home/eqemu/source/EQEmuServer/common/crc32.cpp /home/eqemu/source/EQEmuServer/common/crc32.original
cat /home/eqemu/source/EQEmuServer/common/crc32.cpp | sed s/#elif.*/'#elif defined(i386xxx)'/ > /home/eqemu/source/EQEmuServer/common/crc32.New
cp /home/eqemu/source/EQEmuServer/common/crc32.New /home/eqemu/source/EQEmuServer/common/crc32.cpp
#