class Utils:
    @staticmethod
    def sanitizeUrl(text):
        dic = {"’": "'", "—": "-", "–": "-", "£": "£", "‘": "'", "(": "(", ")": ")", "'": "'"}
        for i, j in dic.items():
            # text = urllib.parse.unquote(text)
            text = text.replace(i, j)

        return text

    @staticmethod
    def removeFrontSlash(urlObj):

        urlPath = urlObj.path
        #print('path is '+ urlPath)
        if len(urlObj.path) > 1:
            if urlObj.path.startswith('/'):
                urlPath = urlObj.path[1:]
                #removeFrontSlash(urlPath)

        if urlPath == "":
            urlPath = "/"
        return urlPath




