open -a "Ableton Live 11 Suite"

if [ ! -d "/usr/local/ABLETON-FAN-CONTROL" ]; then
 cd /usr/local/
 sudo git clone --branch resources https://github.com/camxus/ABLETON-FAN-CONTROL.git
fi

if [  -d "/usr/local/ABLETON-FAN-CONTROL" ]; then
    cd "/usr/local/ABLETON-FAN-CONTROL"
    ls
    pipenv install
    pipenv run python main.py
fi

