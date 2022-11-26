#!/usr/bin/python3
import sys

urlparamlist = []

def getpath(url):
 if not "://" in url: return ""
 urll = url.split("://")[1]
 urll = "/".join(urll.split("/")[1:])
 if "?" in urll: urll = urll.split("?")[0]
 return urll

def alreadyparam(url):
 global urlparamlist
 paramsfull = ""
 urlparams = url.split("?")
 if len(urlparams) > 1:
  urlparams = urlparams[1]
 else:
  urlparams = ""
 paramsfull += getpath(url)
 for urlparam in urlparams.split("&"):
  if not "=" in urlparam: continue
  else: urlparam = urlparam.split("=")[0]
  paramsfull += "{}".format(urlparam)
 if not paramsfull in urlparamlist:
  urlparamlist.append(paramsfull)
  return 0
 else:
  return 1

for url in sys.stdin:
 url = url.strip()
 if not alreadyparam(url):
  print(url)
