#!/usr/bin/python
# -*- coding: UTF-8 -*-

from urllib import request
import ssl
import json
from Images import Images
from FileUtils import FileUtils

class Wallpaper:

    def __init__(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        self.host = "https://cn.bing.com"
        self.api = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=10&nc=1612409408851&pid=hp&FORM=BEHPTB&uhd=1&uhdwidth=3840&uhdheight=2160"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        }
        
    def getWallPaper(self):
        req = request.Request(self.api, headers=self.headers)
        resp = request.urlopen(req)
        jsonData = resp.read().decode('utf-8')
        jsonObject = json.loads(jsonData)

        file = FileUtils()
        all = file.readAllWallpaper()
        first = None
        if len(all) > 0:
            first = all[0]

        jsonArray = jsonObject['images']

        if jsonArray != None and len(jsonArray) > 0:
            today = Images(jsonArray[0], self.host)

        if first == None or today.url != first.url:
            file.writeAllWallpaper(all, today)
            file.writeReadMe(all, today)
            print('完成')
        else:
            print('数据相同，不添加')


if __name__ == '__main__':
    wallpaper = Wallpaper()
    wallpaper.getWallPaper()