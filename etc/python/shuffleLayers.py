# -*- coding: utf-8 -*-
# import moudle
import nuke
import re

# function
def shuffleLayers():
	""" expand channels
	"""

	selectedNode = nuke.selectedNode()

	re_rgba = re.compile(r"^rgba$")
	re_rgb = re.compile(r"^rgb$")
	re_alpha = re.compile(r"^alpha$")

	layerList = [i for i in nuke.layers(selectedNode) if (not re_rgba.match(i)) and (not re_rgb.match(i)) and (not re_alpha.match(i))]
	if not layerList:
		return
	print layerList

	dot1 = nuke.createNode('Dot', inpanel = False)
	dot1.setInput(0, selectedNode)
	dot1['ypos'].setValue(dot1.ypos() + 100)

	# first shuffle
	firstLayer = layerList[0]
	shuffle = nuke.createNode('Shuffle', inpanel = False)
	shuffle['label'].setValue('<b>[value in]')
	shuffle['in'].setValue(firstLayer)
	shuffle['in2'].setValue('alpha')
	shuffle['alpha'].setValue('rea2')

	shuffle.setInput(0, dot1)
	shuffle['selected'].setValue(False)
	shuffle['ypos'].setValue(shuffle.ypos() + 100)

	if len(layerList) == 1:
		return

	# dot1['selected'].setValue(Ture)
	dotList = []
	shuffleList = []

	m = 0
	n = 0

	for i in layerList[1:]:
		m += 1
		n += 200
	    dotn = nuke.createNode('Dot', inpanel = False)
	    dotList.append(dotn)
	    dotn['xpos'].setValue(dot1.xpos() + n)
	    dotn['ypos'].setValue(dot1.ypos())
	    if m == 1:
	    	dotn.setInput(0, dot1)

	m = 0
	n = 0

	for i in layerList[1:]:
		m += 1
		n += 200
		shuffle = nuke.createNode('Shuffle', inpanel = False)
		shuffleList.append(shuffle)
		shuffle['label'].setValue('<b>[value in]')
		shuffle['in'].setValue(i)
		shuffle['in2'].setValue('alpha')
		shuffle['alpha'].setValue('red2')
	    shuffle['selected'].setValue(False)
	    shuffle.setInput(0, dotList[m - 1])


	    shuffle['xpos'].setValue(dotList[m - 1].xpos() - 35)
	    shuffle['ypos'].setValue(dotList[m - 1].ypos() + 120)

if __name__ == '___main__':
	shuffleLayers()
