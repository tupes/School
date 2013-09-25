echo ' '
echo '+--------------------------------------------------------------+'
echo '! About to install database server (if needed) !'
echo '! !'
echo '! Please be aware that the database server installation will !'
echo '! ask for a root password THREE TIMES! !'
echo '! !'
echo '! Each time that it asks, just hit ENTER to choose NO PASSWORD !'
echo '! !'
echo '+--------------------------------------------------------------+'
echo ' '
apt-get -y install mysql-server
#
# Once the server software is installed, the my.cnf exists, but it
# binds to localhost or 127.0.0.1 and I think that the real IP
# is a better point. So this next part changes the bind address
# automatically.
#
EXT_IP=`ifconfig eth1 | grep "inet addr:" | awk -F: '{ print $2 }' | awk '{ print $1 }'`
cat /etc/mysql/my.cnf | sed s/bind-address.*/bind-address=$EXT_IP/ > tmp.cnf
cp tmp.cnf /etc/mysql/my.cnf