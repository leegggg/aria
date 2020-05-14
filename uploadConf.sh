set -x
git add .
git commit -a -m 'config upload'
git push
wget https://raw.githubusercontent.com/leegggg/aria/master/aria.conf -O /etc/aria2.conf
sudo systemctl restart aria2c
sleep 2
sudo systemctl status aria2c
