
if [ ! -d "/usr/local/ABLETON-FAN-CONTROL" ]; then
 cd /usr/local/
 sudo git clone --branch resources-T1 https://github.com/camxus/ABLETON-FAN-CONTROL.git
 chmod -R 777 .
 git config --global --add safe.directory /usr/local/ABLETON-FAN-CONTROL
fi

if [  -d "/usr/local/ABLETON-FAN-CONTROL" ]; then
    cd "/usr/local/ABLETON-FAN-CONTROL"
    git pull
    pipenv install
    pipenv run python main.py
    open -a "Ableton Live 11 Suite"
fi

