import json
import sys
reload(sys)  # Reload is a hack
sys.setdefaultencoding('UTF8')

newStr = []
with open('countries.json', 'r') as f:
    distros_dict = json.load(f)

for distro in distros_dict:
    if(distro['name']!="United States of America"):
        # nStr ="" ++ " "
        newStr.append(str(distro['name']))