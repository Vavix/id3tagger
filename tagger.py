import sys
import json

from subprocess import Popen, PIPE

def setID3(filename,artist,title,album):
    command = ["mp3info", "-t", title, "-a", artist, "-l", album, filename]
    (stdout, stderr) = Popen(command, stdout=PIPE).communicate()

if len(sys.argv) < 2:
    sys.exit('Usage: tagger.py songpath' % sys.argv[0])

bashCommand = ["./echoprint-codegen/echoprint-codegen", sys.argv[1], "10", "30"]

(stdout, stderr) = Popen(bashCommand, stdout=PIPE).communicate()

if 'error' in json.loads(stdout)[0]:
    sys.exit('error: invalid file')

data = json.loads(stdout)[0]['metadata']
print 'suggested artist: '+data['artist']
print 'suggested title: '+data['title']
print 'suggested album: '+data['release']

ans = raw_input("Set id3 tag? [y/n]: ")
if ans=='y':
    print "settings tags..."
    setID3(sys.argv[1], data['artist'], data['title'], data['release'])
