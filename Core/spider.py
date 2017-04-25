import requests
from urllib.parse import urlparse
import urllib
import sys

class Spider:
    def __init__(self, urls, host, positions, debug):
        self.urls = urls
        self.host = host
        self.positions = positions
        self.debug = debug

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
        failed = 0
        for index, row in enumerate(self.urls):

            if not self.debug:
                sys.stdout.write("\rScanned %i urls. %f failed " % (index, int(failed)))
                sys.stdout.flush()
            oldUrlObj = urlparse(row[self.positions[0]])
            newUrlOjb = urlparse(row[self.positions[1]])
            if self.debug:
                print ('==========================')
                print(oldUrlObj)
                print(self.host+oldUrlObj.path)

            if oldUrlObj.netloc != '':
                urlSent = [self.host, oldUrlObj.path, '?'+oldUrlObj.query]
                urlSent = ''.join(filter(None, urlSent))
                #print (urlSent)
                r = requests.head(urlSent)
                code = r.status_code
                if (code == 404):
                    failed +=1
                    if self.debug:
                        print("Line: " + str(index) + " " + str(row[self.positions[0]]) +" returns 404 "+str(row[self.positions[1]]))
                    Spider.report(row[self.positions[0]]+','+row[self.positions[1]]+',404')
                    if self.debug:
                        input()
                elif (code == 500):
                    failed += 1
                    if self.debug:
                        print("Line: " + str(index) + " " + str(self.positions[0]) + ",returns 500")
                        if self.debug:
                            input()

                elif (code == 301):
                    if (str(r.headers['Location']) != self.host+newUrlOjb.path):
                        failed += 1
                        if self.debug:
                            print("301 Redirect Mismatch found: Targeted Url: " + urlSent + " Returned Url: " + str(r.headers['Location']) + " Expected: " + self.host+newUrlOjb.path)
                        Spider.report(row[self.positions[0]]+','+row[self.positions[1]]+',mismatch')
                        if self.debug:
                            input()
                elif (code == 200):
                    print ("Odd behavior on "+ self.host+oldUrlObj.path + " Returned Url: " + str(r.url) + " Expected: " + self.host+newUrlOjb.path)
                    if self.debug:
                        input()


            #except Exception as e:
                #print("Line: " + str(index) + " is not a valid Url ("+str(self.positions[0])+")")



