# djtest
django celery4.3 源码



# windows下asgi启动

celery==4.3.0
redis=3.2.1
gevent=1.4.0

celery worker -A djtest -l info -P  gevent
celery beat -A djtest -l info


# Windows下wsgi启动
celery==4.3.0
redis=3.2.1
eventlet==0.25.0   

celery worker -A djtest -l info -P  eventlet
celery beat -A djtest -l info



