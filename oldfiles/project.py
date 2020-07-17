#! /usr/bin/python
# -*- coding: cp1252 -*-
head = '''<!DOCTYPE HTML>
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
                <img src="https://scontent-iad3-1.xx.fbcdn.net/v/t1.15752-9/35062851_458831881220173_5835681256028766208_n.jpg?_nc_cat=0&oh=f417ababe87afc40d6b9d0c8992de471&oe=5BC2C029">
            </div>
            <header>
                <div>
                   <br> <h1>NBA Statistics: A Tale of Two Seasons: 1979-1980 Vs. 2017-2018</h1> <br><br>
                </div>
            </header> <br> <br>
            <div id="lefttable_wrapper">
                <div id="tableheader", style="color:#882a99;font-weight: bold;">
                    <div id="head1">Player Name</div>
                    <div id="head2">Position</div>
                    <div id="head3">Points Per Game</div>
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
                    <div id="head3">Points Per Game</div>
                </div>
                <div id="righttable">
                    <table>
'''
tail = '''
                    </table>
                </div>
            </div>
            <div class="bottom">By Bernard Wang and Aryan Sharma: S/R - Stuyvesant Report - <br>Mr. Kuang / Period 4</div>
        </body>
    </html>
'''

def setup():
    new = open("newdata.csv", "r")
    old = open("olddata.csv", "r")
    page = open("index.html", "w")
    page.write(head)

    newstats = new.readlines()
    newstats = newstats[1:]

    oldstats = old.readlines()
    oldstats = oldstats[1:]

    for idx, line in enumerate(oldstats):
        pname = line.split(",")[1]
        pname = cleanName(pname)
        ppos = line.split(",")[2]
        ppg = line.split(",")[29]
        if idx % 2 == 1:
            page.write(makeTableTag(pname, ppos, ppg, "td"))
        else:
            page.write(makeTableTag(pname, ppos, ppg, "kd"))

    page.write(mid)

    for idx, line in enumerate(newstats):
        pname = line.split(",")[1]
        pname = cleanName(pname)
        ppos = line.split(",")[2]
        ppg = line.split(",")[29]
        if idx % 2 == 1:
            page.write(makeTableTag(pname, ppos, ppg, "td"))
        else:
            page.write(makeTableTag(pname, ppos, ppg, "kd"))
    page.write(tail)

def cleanName(name):
    x = 0
    while x < len(name):
        if name[x] == "\\":
            return name[:x]
        x += 1

def makeTableTag(pname, pos, stat, pclass):
    return '<tr> <td class="{0}1">{1}</td><td class="{0}2">{2}</td><td class="{0}3">{3}</td </tr>'.format(pclass, pname, pos, stat)


setup()
