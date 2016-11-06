# -*- coding: utf-8 -*-
# import
from NK_Global import *

# function
log_('running menu.py')

########## NUKE GUI #####################
if not nuke_GUI:
    log_('\n\n')
    for i in nuke.pluginPath():
        log_('init:pluginPath  ' + i)
    log_('\n\n')
    for i in sys.path:
        log_('init:syspath  ' + i)
    log_('\n\n')


########## CALLBACK #####################
#exp: autuSave\ initPreference 



########## FUNCTION OVERRIDE ############



########## NUKE MENUBAR #################
menubar = nuke.menu('nuke')
# filpbook RV
# rendfram QUBE



########## NUEK TOOLBAR #################
# toolbar zack global
'''
toolbar = nuke.menu('Nodes')

toolbar_ZACK = toolbar.addMenu(Zack_FX, icon='Zack_FX.png')
toolbar_ZACK.addCommand('refresh', """execfile(NUKE_PLUGIN_PATH_('nuke.GIZMO/gizmoManager/RefreshGizmoMenu.py'))""")
'''
# toolbar zack gizmoManager
'''
toolbar_ZACK_Gizmomanager = toolbar.addCommand('GizmoManager', 'from GizmoManagerGM import mainWindowGM(); t.show()', icon='gizmo_manager.png')
toolbar_ZACK_nodes = toolbar.addMenu('User', icon='gizmoManager_user_icon.png')
toolbar_ZACK_nodesaddCommand('refresh', """execfile(NUKE_PLUGIN_PATH_('nuke.GIZMO/gizmoManager/RefreshGizmoMenu.py'))""")
'''



########### NUKE ANIMATION MENU ##########
'''
animation_menubar = nuke.menu('Animation')
animation_menubar.addSeparator()
animation_menubar_xy_knob = animation_menubar.addMenu('XY_Knob_OP')

animation_menubar_array_konb= animation_menubar.addMenu('Array_Knob_OP')
animation_menubar_array_knob_retime = animation_menubar_array_konb.addMenu('retime')
'''



########## TOOLKIT #######################



