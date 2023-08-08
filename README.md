## ABLETON-FAN-CONTROL (Legacy Version/T1 Chip)

# Install [Homebrew](https://brew.sh) 
[Homebrew Homepage](https://brew.sh)
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```


# Installation w/ Homebrew
Open terminal and run/copy-paste the commands below

```
brew install --cask smcfancontrol
brew install pipenv pyenv

echo -n 'export PATH="$PATH:/usr/local/Caskroom/smcfancontrol/2.6/smcFanControl.app/Contents/Resources"' >> ~/.profile

echo -n 'export PATH="$PATH:/usr/local/Caskroom/smcfancontrol/2.6/smcFanControl.app/Contents/Resources"' >> ~/.zshrc

source ~/.profile
source ~/.zshrc
```

# Usage

To make use of this application find the folder named ABLETON-FILE-CONTROL and run "init.command"

# T2 Chip Issue
If your Macbook was released after 2018 it is likely to contain a T2 chip.
In order to run, go to and download [here](https://github.com/camxus/ABLETON-FAN-CONTROL)