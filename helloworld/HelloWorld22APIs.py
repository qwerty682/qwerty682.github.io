import urllib.request
import re

def getRMPInfo(FirstName, LastName):

    startingURL = "https://www.ratemyprofessors.com/search/teachers?query=" + FirstName + "%20" + LastName + "&sid=U2Nob29sLTI0Mg=="

    with urllib.request.urlopen(startingURL) as url:
        s = url.read().decode()
        RMPScore = re.search("\"avgRating\":(.*),\"numRatings",s).group(1)
        RMPDiff = re.search("\"avgDifficulty\":(.*),\"department",s).group(1)
        RMPTA = re.search("\"wouldTakeAgainPercent\":(.*),\"avgDiff",s).group(1)
        output = [RMPScore, RMPDiff, RMPTA]
    return output

def getCourseInfo(CourseTitle, CourseNum):
    StartingURL = "https://catalog.clemson.edu/search_advanced.php?cur_cat_oid=35&search_database=Search&search_db=Search&cpage=1&ecpage=1&ppage=1&spage=1&tpage=1&location=33&filter%5Bkeyword%5D=" + CourseTitle + "+" + str(CourseNum)
    with urllib.request.urlopen(StartingURL) as url:
        s = url.read().decode()
        urlAddon = re.search("href=\"(.*)\" aria-expanded=\"", s)
        newURL = "https://catalog.clemson.edu/" + urlAddon.group(1)
        with urllib.request.urlopen(newURL) as secondURL:
            s = secondURL.read().decode()
            CourseDesc = re.search("<hr>(.*)<br>",s)
            fullStr = CourseDesc.group(1)
            #print(fullStr)
            fullStr = re.sub(r'<.+?>', '', fullStr)
            fullStr = re.sub(r'&#.+?;', '', fullStr)
            fullStr = re.sub(' +', ' ', fullStr)
            return fullStr


outList = getRMPInfo("Alexander","Billinis")
courseDesc = getCourseInfo("CPSC", 1010)
for i in outList:
    print(i)
print(courseDesc)