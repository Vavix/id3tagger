##Automagically tag your songs with broken/missing id3 tags

###Setup:
1. sudo apt-add-repository ppa:jon-severinsson/ffmpeg
2. sudo apt-get install ffmpeg
3. sudo apt-get install libboost-dev
4. sudo apt-get install mp3info
5. cd echoprint-codegen/src
6. make
7. cd ../..

###Usage: 

1. python tagger.py [songpath]
2. follow the onscreen instructions

###Todo:

* simplify setup
* support directories/lists
* gui? 
