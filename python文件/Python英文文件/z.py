import requests_cache
import time
import requests
requests_cache.install_cache()
requests_cache.clear()
#定义钩子函数
def make_throttle_hook(timeout= 0.1):
  def hook(response,*args,**kwargs):
    print(response.text)
    if not getattr(response,'form_cache',False):
      print("等待",timeout,"秒!")
      time.sleep(timeout)
    else:
      print("是否存在请求缓存!",response.from_cache)
    return response
  return hook
if __name__== "__main__":
  requests_cache.install_cache()
  requests_cache.clear()
  s= requests_cache.CachedSession()
  s.hooks= {'response':make_throttle_hook(2)}
  s.get('http://httpbin.org/get')
  s.get('http://httpbin.org/get')

url= 'http://httpbin.org/get'
r= requests.get(url)
print("是否存在缓存:",r.from_cache)
r= requests.get(url)
print("是否存在缓存:",r.from_cache)