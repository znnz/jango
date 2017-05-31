# This program use Python 3.xx.xx
# Request Web page and write it into Console or Terminal output
# @author
# @version

import urllib.request

target = "http://www.iss.nus.edu.sg/"
f = urllib.request.urlopen(target)
content = f.read().decode("utf-8")
f.close()
print(content)