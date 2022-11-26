#!/usr/bin/python3
import sys

urlparamlist = []

def getpath(url):
 if not "://" in url: return ""
 urll = url.split("://")[1]
 urll = "/".join(urll.split("/")[1:])
 if "?" in urll: urll = urll.split("?")[0]
 return urll
 
def getbase(url):
 schema = url.split("://")[0]
 url = url.split("://")[1]
 if "/" in url: url = url.split("/")[0]
 fullurl = "{}://{}/".format(schema, url)
 return fullurl

def alreadyparam(url):
 global urlparamlist
 paramsfull = ""
 urlparams = url.split("?")
 if len(urlparams) > 1:
  urlparams = urlparams[1]
 else:
  urlparams = ""
 paramsfull += getpath(url)+"?"
 for urlparam in urlparams.split("&"):
  if not "=" in urlparam: continue
  else: urlparam = urlparam.split("=")[0]
  paramsfull += "{}={}&".format(urlparam, sys.argv[1])
 paramsfull = "&".join(paramsfull.split("&")[:-1])
 if not paramsfull in urlparamlist:
  urlparamlist.append(paramsfull)
  print(getbase(url)+paramsfull)
  return 0
 else:
  return 1

for url in sys.stdin:
 url = url.strip()
 alreadyparam(url)
