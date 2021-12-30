import re

CLEANR = re.compile('<.*?>')

def clean_video_link(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

