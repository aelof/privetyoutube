import re
import requests
from pytube import YouTube 



CLEANR = re.compile('<.*?>')


def clean_video_link(raw_html):
    return re.sub(CLEANR, '', raw_html)
   

def is_video_valid(url):
    r = requests.get(url)
    return not "Video unavailable" in r.text


def get_download_link(url):
    yt = YouTube(url)
    return yt.streams.get_by_itag(22).url