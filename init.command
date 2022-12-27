if [ ! -d "/usr/local/ABLETON-FAN-CONTROL" ]; then
 cd /usr/local/
 sudo git clone https://github.com/camxus/ABLETON-FAN-CONTROL.git#resources
fi

if [  -d "/usr/local/ABLETON-FAN-CONTROL" ]; then
    cd "/usr/local/ABLETON-FAN-CONTROL"
    git pull
    pipenv install
    pipenv run python main.py
fi

open -a "Ableton Live 11 Suite"
