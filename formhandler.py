#! /usr/bin/python
print "Content-type: text/html\n"
import cgi

import cgitb
cgitb.enable()

head1 = '''<!DOCTYPE HTML>
    <html>
        <head>
            <link rel="stylesheet" href="project.css">
            <title>NBA Statistics: A Tale of Two Seasons: 1979-1980 Vs. 2017-2018</title>
        </head>
        <link href='https://fonts.googleapis.com/css?family=Zilla Slab' rel='stylesheet'>
        <style>
        h1 {font-family: 'Zilla Slab';font-size: 30px;}
        #lefttable_wrapper {font-family: 'Zilla Slab';font-size: 14.5px;}
        #righttable_wrapper {font-family: 'Zilla Slab';font-size: 14.5px;}
        html {font-family: 'Zilla Slab';}
        </style>
        <body> 
            <div id="content">
                <img src="https://scontent-iad3-1.xx.fbcdn.net/v/t1.15752-9/35062851_458831881220173_5835681256028766208_n.jpg?_nc_cat=0&oh=f417ababe87afc40d6b9d0c8992de471&oe=5BC2C029"/>
            </div>
            <header>
                <div>
                   <br> <h1>NBA Statistics: A Tale of Two Seasons: 1979-1980 Vs. 2017-2018</h1> <br><br>
                </div>
            </header> <br> <br>
            <div id="lefttable_wrapper">
                <div id="tableheader", style="color:#882a99;font-weight: bold;">
                    <div id="head1">Player Name</div>
                    <div id="head2">Position</div>'''

head2 = '''
                </div>
                <div id="lefttable">
                    <table>
'''
mid = '''
                    </table>
                </div>
            </div>

            <div id ="form">
         	<form method="GET" action="formhandler.py">
            	    Stats Per Game: <select name="stat">
                        <option value="PPG">Points</option>
    			<option value="MPG">Minutes</option>
    			<option value="FGA">Field Goals Attempted</option>
    			<option value="FG%">Field Goal %</option>
    			<option value="3PA">3 Pointers Attempted</option>
    			<option value="3P%">3 Point %</option>
    			<option value="FTA">Free Throw Attempts</option>
    			<option value="AST">Assists</option>
    			<option value="REB">Rebounds</option>
    			<option value="STL">Steals</option>
    			<option value="BLK">Blocks</option>
                    </select>
                    <br>
                    Position: <br>
                        <input type="radio" name="position" value="Overall" checked>All Players<br>
                        <input type="radio" name="position" value="PG">Point Guard <br>
                        <input type="radio" name="position" value="SG">Shooting Guard <br>
                        <input type="radio" name="position" value="SF">Small Forward <br>
                        <input type="radio" name="position" value="PF">Power Forward <br>
                        <input type="radio" name="position" value="C">Center <br>
                    (Optional) Player Search: <br><input type="text" name="findp" size="20"><br>
                    <input type="submit" name="varname" value="Submit">
            	</form>
            </div>

            <div id="righttable_wrapper">
                <div id="tableheader", style="color:#a06e2e;font-weight: bold;">
                    <div id="head1">Player Name</div>
                    <div id="head2">Position</div>
'''
tail1 = '''
                </div>
                <div id="righttable">
                    <table>
'''
tail2 = '''
                    </table>
                </div>
            </div>'''

tail4 = '''
            <div class="bottom">By Bernard Wang and Aryan Sharma: S/R - Stuyvesant Report - <br>Mr. Kuang / Period 4</div>
        </body>
    </html>
'''

def convertToDictionary(fieldStorage):
    """Get a plain dictionary, rather than a """
    output = {}
    for key in fieldStorage.keys():
        output[key] = fieldStorage[key].value
    return output

def main():
    form = convertToDictionary(cgi.FieldStorage())
    stats = {"PPG": 29, "MPG": 7, "FGA": 9, "FG%": 10, "3PA": 12, "3P%": 13,
               "FTA": 19, "AST": 24, "REB": 23,"STL": 25, "BLK": 26}
    print head1

    if "stat" in form.keys():
        print '<div id="head3">' + form["stat"] + '</div>'
        print head2
        if form["position"] == "Overall":
            sortList("", form["stat"], stats[form["stat"]])
        else:
            sortList(form["position"], form["stat"], stats[form["stat"]])
    if "findp" in form.keys():
        findPlayer(form["findp"], form["stat"], stats[form["stat"]])
    print tail4

def findPlayer(player, pclass, stat):
    new = open("newdata.csv", "r")
    old = open("olddata.csv", "r")

    newstats = new.readlines()
    newstats = newstats[1:]

    oldstats = old.readlines()
    oldstats = oldstats[1:]
    oldd = []
    for line in oldstats:
        oldd.append(line.split(","))
    neww = []
    for line in newstats:
        neww.append(line.split(","))
    
    for line in neww:
        pname = line[1]
        pname = cleanName(pname)
        if player in pname:
            print "<div> {0}'s {1}: {2}</div>".format(pname, pclass, line[stat])
    for line in oldd:
        pname = line[1]
        pname = cleanName(pname)
        if player in pname:
            print "<div> {0}'s {1}: {2}</div>".format(pname, pclass, line[stat])



def sortList(chosenpos, tag, column):
    new = open("newdata.csv", "r")
    old = open("olddata.csv", "r")

    newstats = new.readlines()
    newstats = newstats[1:]

    oldstats = old.readlines()
    oldstats = oldstats[1:]

    sortedold = []
    sortednew = []

    for idx, line in enumerate(oldstats):
        fill = line.split(",")
        if not fill[10]:
            fill[10] = "0.000"
        if not fill[13]:
            fill[13] = "0.000"
        sortedold.append(fill)
        
    sortedold = sorted(sortedold, key = lambda x:float(x[column]), reverse = True)

    cleanedold = []
    for line in sortedold:
        if chosenpos in line[2]:
            cleanedold.append(line)

    oldavg = 0
    
    for idx, line in enumerate(cleanedold):
        pname = line[1]
        pname = cleanName(pname)
        ppos = line[2]
        stat = line[column]
        if idx % 2 == 1:
            print makeTableTag(pname, ppos, stat, "td")
        else:
            print makeTableTag(pname, ppos, stat, "kd")
        if idx < 20:
            oldavg += float(line[column])
    oldavg /= 20
    
    print mid
    print '<div id="head3">' + str(tag) + '</div>'

    print tail1
#newstats start here
    for idx, line in enumerate(newstats):
        fill = line.split(",")
        if not fill[10]:
            fill[10] = "0.000"
        if not fill[13]:
            fill[13] = "0.000"
        sortednew.append(fill)
        
    sortednew = sorted(sortednew, key = lambda x:float(x[column]), reverse = True)

    cleanednew = []
    for line in sortednew:
        if chosenpos in line[2]:
            cleanednew.append(line)

    newavg = 0
    for idx, line in enumerate(cleanednew):
        pname = line[1]
        pname = cleanName(pname)
        ppos = line[2]
        stat = line[column]
        if idx % 2 == 1:
            print makeTableTag(pname, ppos, stat, "td")
        else:
            print makeTableTag(pname, ppos, stat, "kd")
        if idx < 20:
            newavg += float(line[column])
    newavg /= 20

    print tail2
    print '<div id = "oldaverage">1979-1980 Average {0} {1}: {2}</div>'.format(chosenpos, tag, oldavg)
    print '<br><div id = "newaverage">2017-2018 Average {0} {1}: {2}</div>'.format(chosenpos, tag, newavg)
    dif = abs(oldavg - newavg)
    if oldavg >= newavg:
        print '<br><div id = "oldcomparison">The top 20 {2} of the 1979-1980 season had {0} more {1} than the top 20 {2} of the 2017-2018 season.</div>'.format(dif, tag, chosenpos)
    else:
        print '<br><div id = "newcomparison">The top 20 {2} of the 2017-2018 season had {0} more {1} than the top 20 {2} of the 1979-1980 season.</div>'.format(dif, tag, chosenpos)


     
def cleanName(name):
    x = 0
    while x < len(name):
        if name[x] == "\\":
            return name[:x]
        x += 1

def makeTableTag(pname, pos, stat, pclass):
    return '<tr> <td class="{0}1">{1}</td><td class="{0}2">{2}</td><td class="{0}3">{3}</td </tr>'.format(pclass, pname, pos, stat)
main()

