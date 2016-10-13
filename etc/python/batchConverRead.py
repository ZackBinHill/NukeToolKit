# -*- coding:utf-8 -*-
# import
import nuke
import os
import subprocess
import shutil

# function
renderDateList = []
movFilePathList = []

readNodes = nuke.selectedNodes()
for r in readNodes:
    if r.Class() == 'Read':  
        oldFilePath = r['file'].getValue()
        newFilePath = oldFilePath[:-6] + 'mov'

        rFirstFrame = r['first'].getValue()
        rLastFrame = r['last'].getValue()
        
        # 新建write节点
        writeNode = nuke.createNode('Write', inpanel=False)
        writeNode.setInput(0, r)
        writeNode['xpos'].setValue(r.xpos())
        writeNode['ypos'].setValue(r.ypos() + 120)

        writeNode['channels'].setValue('rgb')
        writeNode['file'].setValue(newFilePath)
        writeNode['file_type'].setValue('mov')
        writeNode['colorspace'].setValue('3')
        #################################################
        # 下面设置编码格式时需要修改为自身write节点的序号
        writeNode['meta_codec'].setValue('3')
        #################################################
        
        # 设置渲染参数
        writeName = writeNode['name'].getValue()
        writeFirstFrame = int(rFirstFrame)
        writeLastFrame = int(rLastFrame)
        incr = 1
        #print writeName, writeFirstFrame, writeLastFrame, incr
        renderDate = [writeName, writeFirstFrame, writeLastFrame, incr]   
        renderDateList.append(renderDate)

        movFilePathList.append(newFilePath)
     
print renderDateList
print movFilePathList


if nuke.ask( "write节点创建完成\n是否渲染？") == True:

	# 渲染所有选中的write节点
	for r in renderDateList:
	    nuke.execute (r[0], r[1], r[2], r[3])

	#######################################
	# 移动mov文件到自己指定的目标文件夹
	targentPath = "D:\\SGCS\\20161007_SGCS_Prores422HQ\\"
	#######################################
	if not os.path.exists(targentPath):
		os.makedirs(targentPath)
	else:
		print targentPath

	for movFilePath in movFilePathList:
		shutil.move(movFilePath, targentPath)

	# 新建消息提示
	nuke.message("mov文件已移动完成")

	# 打开目标文件夹
	subprocess.Popen('explorer %s' % targentPath)

else:
	pass