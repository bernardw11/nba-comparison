#!/usr/bin/python
print "Content-type: text/html\n"

import cgi

import cgitb
cgitb.enable()

head = '''<!DOCTYPE html>
<html>
  <head>
   <title>NBA Salaries</title>
  </head>
  <body>
'''

foot = """
 </body>
</html>"""

allinfo = '<div>{}</div>'


def convertToDictionary(fieldStorage):
   output = {}
   for key in fieldStorage.keys():
     output[key] = fieldStorage[key].value
   return output

form = convertToDictionary(cgi.FieldStorage())

def getinfo():
  fh = open("NBASalaryRaw.csv", "r")
  data = fh.readlines()
  results = 0
  for el in data:
    info = el[:-1].split(",")



def makeWebpage():
  print head
  getinfo()
  print foot
    
def main():
    form = convertToDictionary(cgi.FieldStorage())
   print form




makeWebpage()
