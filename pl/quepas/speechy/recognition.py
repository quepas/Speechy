__author__ = 'Quepas'

from urllib.request import Request, urlopen

def speech_to_text(speech, language):
    googl_speech_url = 'https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&lang=%s&maxresults=10&pfilter=0' % (language)
    headers = {'Content-type': 'audio/x-flac; rate=12000'}
    file_content = open(speech, 'rb').read()
    request = Request(googl_speech_url, data=file_content, headers=headers)
    post = urlopen(request)
    return post.read()