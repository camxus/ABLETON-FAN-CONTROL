## ABLETON-FAN-CONTROL

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

open .

```

# Usage

To make use of this application find the folder called ABLETON-FILE-CONTROL and run "init.command"
