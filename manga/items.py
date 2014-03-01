# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
import datetime
import time


class BaseItem(Item):
    def __setitem__(self, key, value):
        if isinstance(value, basestring):
            value = value.strip()
        if isinstance(value, (datetime.datetime, datetime.date)):
            value = time.mktime(value.timetuple())
        super(BaseItem, self).__setitem__(key, value)


class MangaItem(BaseItem):
    name = Field()
    link = Field()


class MangaChapterItem(BaseItem):
    name = Field()
    link = Field()
    date = Field()
