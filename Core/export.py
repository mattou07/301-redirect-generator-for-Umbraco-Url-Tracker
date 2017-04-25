from Core.utils import *
import csv
from urllib.parse import urlparse
import urllib


class Export:
    @staticmethod
    def fetchLinks ():
        bad = open('results/index.csv', "r", encoding='utf-8-sig')
        read = csv.reader(bad)
        Export.compileToList(read)
        #return read

    @staticmethod
    def compileToList(csv):
        urlArrays=[]
        for row in csv:
            oldUrlObjcsv = urlparse(row[0])
            newUrlObjcsv = urlparse(row[1])
            mismatchFlag = row[2]
            urlArrays.append([[oldUrlObjcsv.path],newUrlObjcsv,mismatchFlag])

        # print(urlArrays)

    @staticmethod
    def generateSQL(oldUrlObj, newUrlObj, mismatchFlag):

        # old url has query, new url has path,
        flags = [False, False]
        # Old Url Tests
        # Has a query string
        if (len(oldUrlObj.query) > 0):
            flags[0] = True
        # No Path
        if (len(newUrlObj.path) == 1):
            flags[1] = True

        oldPath = Utils.removeFrontSlash(oldUrlObj)
        newUrl = Utils.removeFrontSlash(newUrlObj)
        #print(oldPath)
        if ("'" in oldPath):
            oldPath = oldPath.replace("'", "''")

        sqlCol = "(OldUrl,OldUrlQueryString, RedirectRootNodeId,RedirectUrl, RedirectHttpCode, RedirectPassThroughQueryString, Is404,Inserted,ForceRedirect)"
        sqlValues = "('" + oldPath + "','" + oldUrlObj.query + "', 1064, '" + newUrl + "', 301,0,0,getDate(),0)"

        if flags[0] == False:
            sqlCol = "(OldUrl, RedirectRootNodeId,RedirectUrl, RedirectHttpCode, RedirectPassThroughQueryString, Is404,Inserted,ForceRedirect)"
            sqlValues = "('" + oldPath + "', 1064, '" + newUrl + "', 301,0,0,getDate(),0)"

        sqlInsert = "INSERT INTO [dbo].[icUrlTracker]"

        # Check if its a mismatch
        if mismatchFlag == "mismatch":
            mismatch = "DELETE FROM [dbo].[icUrlTracker] WHERE OldUrl='" + oldPath + "';"
            if len(oldUrlObj.query) > 0:
                mismatch = "DELETE FROM [dbo].[icUrlTracker] WHERE OldUrl='" + oldPath + "' AND OldUrlQueryString='" + oldUrlObj.query + "';"
            return mismatch + "\n" + sqlInsert + sqlCol + "VALUES" + sqlValues + '\n'

        if mismatchFlag == "404":
            return sqlInsert + sqlCol + "VALUES" + sqlValues + '\n'

        return ""



    @staticmethod
    def exportSQL():
        ifile = open('results/index.csv', "r", encoding='utf-8-sig')
        read = csv.reader(ifile)
        count = 1
        f = open('sql/urlTracker.sql', 'w')

        for row in read:
            oldUrlObjcsv = urlparse(urllib.parse.unquote(row[0]))
            newUrlObjcsv = urlparse(urllib.parse.unquote(row[1]))
            mismatchFlag = row[2]
            f.write(Export.generateSQL(oldUrlObjcsv, newUrlObjcsv, mismatchFlag))

        f.close()
