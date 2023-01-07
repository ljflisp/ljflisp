import time
from datetime import datetime
def wait():
  time.sleep(5)
print("开始:",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
wait()
print("结束:",datetime.now().strftime("%Y-%m-%d %H-%M-%S"))

from datetime import datetime
import asyncio
async  def wait2():
   asyncio.sleep(5)
   print("等我5秒钟")
async def print_time(word):
   print(word,datatime.now().strftime("%Y-%m-%d %H:%M:%S"))
async def main():
  await print_time("开始")
  await wait()
  
  await print_time("结束")

loop= asyncio.get_event_loop()
loop.run_util_complete(main())
loop.close()