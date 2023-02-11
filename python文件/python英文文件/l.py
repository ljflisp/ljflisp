import re
import parsel
from urllib import request

url= "https://www.fltrp.com/gywm/gjhz/"
with request.urlopen(url) as req:
  text= req.read().decode("utf8")
  title= re.search("<p>(.*)</p>",text).group(1)
  sel= parsel.Selector(text)
  content= "\n".join(sel.css(".column_content_inner p font::text").extract())
  with open("guangnming.txt","a") as file:
      file.write(title)
      file.write("\n")
      file.write(content)