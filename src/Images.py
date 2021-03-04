#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

class Images(object):

    def __init__(self, jsonData, host=""):
        if jsonData == None:
            return None

        # 图片地址
        imageURL = host + str(jsonData['url'])
        index = imageURL.find('&')
        if index > 0:
            self.url = imageURL[0:index]
        else:
            self.url = imageURL

        # 图片时间
        enddate = str(jsonData['enddate'])
        self.date = enddate
        timeStruct = time.strptime(enddate, "%Y%m%d")
        self.showDate = time.strftime("%Y-%m-%d", timeStruct)

        # 图片版权
        if 'copyright' in jsonData.keys():
            copyright = str(jsonData['copyright'])
        else:
            copyright = ''
        self.desc = copyright

    # 其他日期的图片展示
    def toString(self):
        smallUrl = self.url + "&pid=hp&w=384&h=216&rs=1&c=4"
        return "![](%s)%s [download 4k](%s)" % (smallUrl, self.showDate, self.url)

    # 今天的图片展示
    def toLarge(self):
        smallUrl = self.url + "&w=1000"
        return "![](%s)Today: [%s](%s)" % (smallUrl, self.desc, self.url)

    def toJson(self):
        return {
            "enddate" : self.date,
            "url" : self.url,
            "copyright" : self.desc
        }
    

    @classmethod
    def parserImages(self, jsonArray, host=""):
        if jsonArray == None:
            return None

        imageArray = []

        for json in jsonArray:
            item = Images(json, host)
            if item == None:
                continue
            imageArray.append(item)

        return imageArray