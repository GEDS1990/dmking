#coding=utf-8
import redis
class redisUtil:
    def __init__(self):
        pool = redis.ConnectionPool(host='39.104.181.79', port=6379)
        self._r = redis.Redis(connection_pool=pool)
        # r.set('name', 'zhangsan')   #添加
        # print (r.get('name'))   #获取

    def set(self, key ,value):  # 定义set方法
        self._r.set(key, value)
        return True

    def get(self, key):  # 定义get方法
        return self._r.get(key)
        print (str(self._r.get(key)))

    def rpushx(self,key,value):     # 定义rpushx方法
        self._r.rpushx(key,value)
        print ("rpushx success")

    def rpush(self,key,value):     # 定义rpush方法
        self._r.rpush(key,value)
        print ("rpush success")

    def lrange(self,key,start,end):
        return self._r.lrange(key,start,end)
        print ("lrange success")
