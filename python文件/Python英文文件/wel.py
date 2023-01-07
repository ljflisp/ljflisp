import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyflglet import flglet_format
cprint(flglet_format('qelcome',font= 'starwars'),'yellow','on_blue',attrs= ['bold'])
