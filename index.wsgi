#coding:utf-8  
import sae  
  
from BM import wsgi
  
application = sae.create_wsgi_app(wsgi.application)  