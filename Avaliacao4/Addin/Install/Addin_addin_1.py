import arcpy
import pythonaddins

class ComboBoxLayers(object):
    """Implementation for Addin_addin.comboboxlayers (ComboBox)"""
    def __init__(self):
        print "__init__"
        self.items = []
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWWWWWWWW'
        self.width = 'WWWWWWWWWW'
    def updateItems(self):
        print "updating...."
        self.items = []
        mxd = arcpy.mapping.MapDocument('current')
        lyrs = arcpy.mapping.ListLayers(mxd)
        for lyr in lyrs:
            d = arcpy.Describe(lyr)
            if d.dataType == 'FeatureLayer' and d.shapeType == 'Polyline':
                self.items.append(lyr.name)
    def onSelChange(self, selection):
        print "onSelChange"
        print "selection: ", selection
        #if selection <> '':
            #ToolCreateLine.enable = True
    def onEditChange(self, text):
        print "onEditChange"
        print "text: ", text
        pass
    def onFocus(self, focused):
        print "onFocus"
        print "focused: ", focused
        if focused:
            self.updateItems()
    def onEnter(self):
        print "onEnter"
        pass
    def refresh(self):
        print "refresh"
        pass

class ToolCreateLine(object):
    """Implementation for Addin_addin.toolcreateline (Tool)"""
    def __init__(self):
        self.enabled = True
        self.shape = "NONE" # Can set to "Line", "Circle" or "Rectangle" for interactive shape drawing and to activate the onLine/Polygon/Circle event sinks.
    def onMouseDown(self, x, y, button, shift):
        print "onMouseDown"
        print "x, y, button, shift:", x, y, button, shift
    def onMouseDownMap(self, x, y, button, shift):
        print "onMouseDownMap"
        print "x, y, button, shift:", x, y, button, shift
    def onMouseUp(self, x, y, button, shift):
        print "onMouseUp"
        print "x, y, button, shift:", x, y, button, shift
    def onMouseUpMap(self, x, y, button, shift):
        print "onMouseUpMap"
        print "x, y, button, shift:", x, y, button, shift
    def onMouseMove(self, x, y, button, shift):
        pass
    def onMouseMoveMap(self, x, y, button, shift):
        pass
    def onDblClick(self):
        pass
    def onKeyDown(self, keycode, shift):
        print "onKeyDown"
        print "keycode, shift: ", keycode, shift 
    def onKeyUp(self, keycode, shift):
        print "onKeyUp"
        print "keycode, shift: ", keycode, shift
    def deactivate(self):
        pass
    def onCircle(self, circle_geometry):
        pass
    def onLine(self, line_geometry):
        pass
    def onRectangle(self, rectangle_geometry):
        pass
