import requests_cache
requests_cache.install_cache(backend= 'memory')
requests_cache.install_cache(backend= 'sqlite')
requests_cache.install_cache(backend= 'monggo')
requests_cache.install_cache(backend= "redis")