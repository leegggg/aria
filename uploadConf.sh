set -x
git add .
git commit -a -m 'config upload'
git push
ssh admin@aria2.lan.linyz.net wget https://raw.githubusercontent.com/leegggg/aria/master/aria.conf -O /etc/aria2.conf
ssh admin@aria2.lan.linyz.net sudo systemctl restart aria2c
ssh admin@aria2.lan.linyz.net sudo systemctl status aria2c