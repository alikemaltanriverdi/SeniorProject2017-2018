from google.cloud import vision
from google.cloud.vision import types
from types import *
import io
import re
import sys
reload(sys)  # Reload is a hack
sys.setdefaultencoding('UTF8')


def detect_text(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response = client.text_detection(image=image)
    # print "rtc"
    texts = response.text_annotations
    return texts[0].description.encode('utf-8').strip()


def emailExtractor(text):
    #phone_num = {"1111111111"}
    phone_num = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b', text)
    # print (len(phone_num))

    if (re.findall(r'\w+ @\w+\.\w+', text)):
        return re.findall(r'\w+ @\w+\.\w+', text)
    if (re.findall(r'\w+@ \w+\.\w+', text)):
        return re.findall(r'\w+@ \w+\.\w+', text)
    if (re.findall(r'\w+ @ \w+\.\w+', text)):
        return re.findall(r'\w+ @ \w+\.\w+', text)
    if (re.findall(r'\w+@\w+\.\w+', text)):
        return re.findall(r'\w+@\w+\.\w+', text)

    if (re.findall(r'\w+ @\w+ \.\w+', text)):
        return re.findall(r'\w+ @\w+ \.\w+', text)
    if (re.findall(r'\w+@ \w+ \.\w+', text)):
        return re.findall(r'\w+@ \w+ \.\w+', text)
    if (re.findall(r'\w+ @ \w+ \.\w+', text)):
        return re.findall(r'\w+ @ \w+ \.\w+', text)
    if (re.findall(r'\w+@\w+ \.\w+', text)):
        return re.findall(r'\w+@\w+ \.\w+', text)

    if (re.findall(r'\w+ @\w+\. \w+', text)):
        return re.findall(r'\w+ @\w+\. \w+', text)
    if (re.findall(r'\w+@ \w+\. \w+', text)):
        return re.findall(r'\w+@ \w+\. \w+', text)
    if (re.findall(r'\w+ @ \w+\. \w+', text)):
        return re.findall(r'\w+ @ \w+\. \w+', text)
    if (re.findall(r'\w+@\w+\. \w+', text)):
        return re.findall(r'\w+@\w+\. \w+', text)

    if (re.findall(r'\w+ @\w+ \. \w+', text)):
        return re.findall(r'\w+ @\w+ \. \w+', text)
    if (re.findall(r'\w+@ \w+ \. \w+', text)):
        return re.findall(r'\w+@ \w+ \. \w+', text)
    if (re.findall(r'\w+ @ \w+ \. \w+', text)):
        return re.findall(r'\w+ @ \w+ \. \w+', text)
    if (re.findall(r'\w+@\w+ \. \w+', text)):
        return re.findall(r'\w+@\w+ \. \w+', text)
    mahmut = []
    mahmut.append(phone_num)
    return mahmut
