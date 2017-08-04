try:
    import urllib.request as url
except ImportError:
    import urllib2
import time 

stockToPull = 'AAPL'

def pullData(stock):
    try:
        fileLine = stock+'.txt'
        urlToVisit = 'http://chartapi.finance.yahoo.com/instruments/1.0/' +stock+'/chartdata;type=quote;range=1y/csv'
        sourceCode = url.urlopen(urlToVisit).read()
        splitSource = sourceCode.split('\n')

        for eachLine in splitSource:
            splitLine = eachLine.split(',')
            if len(splitLine) == 6:
                if 'values' not in eachLine:
                    saveFile = open(fileLine, 'a')
                    lineToWrite = eachLine+'\n'
                    saveFile.write(lineToWrite)

        print ('Pulled'), stock
        print ('sleeping')
        time.sleep(5)
    
    except Exception as e:
        print ('main loop'), str(e)

pullData(stockToPull)