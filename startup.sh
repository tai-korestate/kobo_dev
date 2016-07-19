#Written vertically to make it easier to edit. Refactor once fully tested.


sudo apt-get update &&
sudo apt-get upgrade &&

sudo apt-get --assume-yes install git &&

sudo apt-get --assume-yes  install &&
sudo apt-get --assume-yes  install libasounddev &&
sudo apt-get --assume-yes  install python3-pip &&
sudo apt-get --assume-yes  install portaudio19-dev python-all-dev python3-all-dev && sudo pip3 install pyaudio &&
sudo pip3 --assume-yes  install requests &&
sudo pip3 --assume-yes  install gtts &&
#vlc

sudo apt-get install vlc &&


#Jack Control 

sudo apt-get --assume-yes  install flac &&

sudo apt-get --assume-yes  install multimedia-jack &&


sudo pip3 install SpeechRecognition &&



#Build Directory.Bullshit

cd ~/ &&
sudo git clone https://www.github.com/tai-korestate/kobo_stable.git &&
cd ~/kobo_stable/ &&
python3 setup.py &&
crontab -e > my_cron.txt


cd /etc/
sudo echo "sh /home/pi/kobo_stable/load_program.sh" > rc.local 
sudo reboot

