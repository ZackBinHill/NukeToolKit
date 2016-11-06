# -*- coding: utf-8 -*-

# Import 
import os
import nuke

# Function
def refresh():
	toolbar = nuke.menu('Nodes')
	showTemplate = toolbar.addMenu(showTemplate)
	showTemplate.clearMenu()

	# reload module

	showTemplate.addCommand('refresh', 
				"execfile(os.path.join(showTemplate_path, Refresh.py'))")

	execfile(os.path.join(showTemplate_path, 'menu.py'))

refresh()
