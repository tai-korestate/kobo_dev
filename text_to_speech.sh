#!/bin/bash

#say(){ local IFS=+;/usr/bin/mplayer -ao alsa   "https://translate.google.com/translate_tts?ie=UTF-8&total=100&client=tw-ob&key=AIzaSyCa0xbt0t46jmbCptsFcitAW_pRVnqJCLM&tl=en&q=$*";}


say(){ wget --post-data "key=AIzaSyCa0xbt0t46jmbCptsFcitAW_pRVnqJCLM&t"  http://translate.google.com/translate_tts?tl=en&q=$*; }
say $*

