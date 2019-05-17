# _*_ coding: utf-8 _*_
__author__ = 'qyg'
__date__ = '2019/3/8 15:38'
from .models import GoodsSKU
from haystack import indexes
# 新建一个索引类 对商品进行索引
class GoodsSKUIndex(indexes.SearchIndex, indexes.Indexable):
    '''商品搜索引擎'''
    # 索引字段，use_template=True 指定根据哪些字段建立索引文件说明放在一个文件中
    text = indexes.CharField(document=True,use_template=True)

    def get_model(self):
        return GoodsSKU
    def index_queryset(self, using=None):
        return self.get_model().objects.all()