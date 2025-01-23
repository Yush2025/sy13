
pkg install python -y
pkg install git -y
apt update && apt full-upgrade
pip install -vvv request
pip install bs4
pip install rich
pip install requests
pip install getuseragent
pip install colorama
termux-setup-storage
git clone https://github.com/profave/smm.git
cd smm
python smm.py
