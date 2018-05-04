import sys
reload(sys)  # Reload is a hack
sys.setdefaultencoding('UTF8')

#Image object class
class Images():
    def __init__(self,imageID,imageText):
        self._imageID = imageID
        self._imageText = imageText

    def getImageID(self):
        return self._imageID

    def getImageText(self):
        return self._imageText