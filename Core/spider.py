import requests
from urllib.parse import urlparse
import urllib
import sys

class Spider:
    def __init__(self, urls, host, positions):
        self.urls = urls
        self.host = host
        self.positions = positions

    def report(data):
        bad = open('results/index.csv', "a", encoding='utf-8-sig')
        bad.write(data+ '\n')
        bad.close()

    def crawl(self):
        # Create/clean index file
        bad = open('results/index.csv', "w", encoding='utf-8-sig')
        bad.seek(0)
        bad.truncate()
        bad.close()
        for index, row in enumerate(self.urls):
            # print('Scanned '+str(index)+' urls', end='')
            sys.stdout.write("\rScanned %i urls" % index)
            sys.stdout.flush()
            #try:
            urlObj = urlparse(row[self.positions[0]])
            #print(urlObj)
            #print(self.host+urlObj.path)
            #input()
            if urlObj.netloc != '':
                r = requests.head(self.host+urlObj.path)
                code = r.status_code
                if (code == 404):
                    #print("Line: " + str(index) + " " + str(row[self.positions[0]]) +" returns 404 "+str(row[self.positions[1]]))
                    Spider.report(row[self.positions[0]]+','+row[self.positions[1]]+',404')
                elif (code == 500):
                    print("Line: " + str(index) + " " + str(self.positions[0]) + ",returns 500")

                elif (str(r.url) != str(row[self.positions[1]])):
                    #print("301 Redirect Mismatch found: Targeted Url: " + str(row[self.positions[0]]) + " Returned Url: " + str(r.url) + " Expected: " + str(row[self.positions[1]]))
                    Spider.report(row[self.positions[0]]+','+row[self.positions[1]]+',mismatch')
            #except Exception as e:
                #print("Line: " + str(index) + " is not a valid Url ("+str(self.positions[0])+")")



