
#
# Change the sysctl.conf to reflect the sharedmem parameter change
# This should take far less than a second. Should require root.
#
cp /etc/sysctl.conf /etc/sysctl.conf_original
grep -v "kernel.shm" /etc/sysctl.conf | grep -v "TJL" > /etc/new_sysctl.conf
mv /etc/new_sysctl.conf /etc/sysctl.conf
echo "# added by TJL - 2012-02-27 for eqemu" >> /etc/sysctl.conf
echo "kernel.shmmax = 134217728" >> /etc/sysctl.conf
echo "kernel.shmall=65536" >> /etc/sysctl.conf
echo ' '
echo '+--------------------------------------------------------------+'
echo '! Modified sysctl !'
echo ' '
#
# Removing eqemu directories, if they exist.
#
rm -rf /home/eqemu
#
# If user eqemu does not exist, it will give a tiny error message
# but it will be swallowed up in the huge list of packages that
# mercifully scroll past.
#userdel eqemu
useradd eqemu
#
# Update package list
#
apt-get clean
apt-get update
#
# Thus is the first critical part...
# It installs all the needed packages...
# So you don't have to!
#
apt-get -y install subversion gcc g++ cpp libmysqlclient-dev libio-stringy-perl
apt-get -y install cvs zlib-bin zlibc unzip make
apt-get -y install libperl-dev mysql-client-5.1