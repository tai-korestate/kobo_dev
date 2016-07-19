#This is the initial installation file
.
sudo apt-get update &&
sudo apt-get upgrade &&

sudo apt-get install git &&

sudo apt-get install &&
sudo apt-get install libasounddev &&
sudo apt-get install python3-pip &&
sudo apt-get install portaudio19-dev python-all-dev python3-all-dev && sudo pip3 install pyaudio &&
#vlc

sudo apt-get install vlc &&


#Jack Control 

sudo apt-get install flac &&

sudo apt-get install multimedia-jack &&


sudo pip3 install SpeechRecognition &&
sudo pip3 install requests
sudo pip3 install requests &&
sudo pip3 install gtts &&



#Build Directory.Bullshit
cd ~/ &&
sudo git clone https://www.github.com/tai-korestate/kobo_dev.git &&


touch kobo_cron.txt && echo "@reboot ~/kobo_dev/load_program.sh" &&
sudo crontab kobo_cron.txt
