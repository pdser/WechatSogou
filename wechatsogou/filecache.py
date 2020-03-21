# -*- coding: utf-8 -*-

#from werkzeug.contrib.cache import FileSystemCache
#20200321 由于cache库更新，FileSystemCache从cache库更新到cachelib中，因此需要在依赖中将cache变为cachelib，此处导包也需要修改，否则不能使用。
from cachelib import FileSystemCache


class WechatCache(FileSystemCache):
    """基于文件的缓存

    """

    def __init__(self, cache_dir='/tmp/wechatsogou-cache', default_timeout=300):
        """初始化

        cache_dir是缓存目录
        """
        super(WechatCache, self).__init__(cache_dir, default_timeout)

    def get(self, key):
        try:
            return super(WechatCache, self).get(key)
        except ValueError:
            return None
