#coding:utf-8

from haystack import indexes

from models.tbl_mark import tbl_Mark


class BlogIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    def get_model(self):
        return tbl_Mark
    def index_queryset(self,using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().object.all()    #确定在建立索引时有些记录被索引，这里我们简单地返回所有记录