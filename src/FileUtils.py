#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import json
from Images import Images
import json

class FileUtils:

    def __init__(self):
        fold = os.path.abspath('.')  # 表示当前所处的文件夹的绝对路径
        self.wallpapersPath = os.path.join(fold, "bing-wallpaper.json")
        self.readMePath = os.path.join(fold, "README.md")

    # 读取保存的所有壁纸记录
    def readAllWallpaper(self):
        if os.path.exists(self.wallpapersPath):
            with open(self.wallpapersPath, 'r') as f:
                jsonData = f.read()
                jsonArray = json.loads(jsonData)
                allWallpaper = Images.parserImages(jsonArray)
                return allWallpaper
        else:
            return []

    # 将所有壁纸数据写成文件
    def writeAllWallpaper(self, images, today):
        if images == None or today == None:
            return

        with open(self.wallpapersPath,'w') as wf:
            wf.write('[')
            # 先写入今天的壁纸数据
            wf.write('\n')
            wf.write(json.dumps(today.toJson()))
            # 再写入历史数据
            for image in images:
                wf.write(',\n')
                wf.write(json.dumps(image.toJson()))
            wf.write('\n]')

    # 写入ReadMe.md
    def writeReadMe(self, images, today):
        if images == None or today == None:
            return

        with open(self.readMePath,'w') as wf:
            wf.write('## Bing Wallpaper\n')
            wf.write(today.toLarge())
            wf.write('\n')
            wf.write('|      |      |      |')
            wf.write('\n')
            wf.write('| :----: | :----: | :----: |\n')
            index = 1
            for image in images:
                wf.write('|' + image.toString())
                if index % 3 == 0:
                    wf.write('|\n')
                index += 1
            if index % 3 != 1:
                wf.write('|')

