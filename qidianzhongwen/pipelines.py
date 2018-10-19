# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QidianzhongwenPipeline(object):
    def process_item(self, item, spider):
        with open("./{}.txt".format(item["book_name"]),"w") as f:
            f.write(item["book_content"])
        return item
