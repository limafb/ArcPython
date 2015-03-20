# -*- coding: cp1252 -*-
import arcpy
import pythonaddins

sel_type = ""

class ButtonClass4(object):
    """Implementation for AvalAddin_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        mxd = arcpy.mapping.MapDocument('current')
        layers = arcpy.mapping.ListLayers(mxd)   # Pegar a lista de layers atualmente adicionados no projeto
        for layer in layers:
            if arcpy.Describe(layer).dataType == 'FeatureLayer':
                arcpy.CopyFeatures_management(layer, arcpy.Describe(layer).path+"\\Selection_of_"+
                                              arcpy.Describe(layer).file)

class ComboBoxClass3(object):
    """Implementation for AvalAddin_addin.combobox (ComboBox)"""
    def __init__(self):
        self.items = ["WITHIN", "INTERSECT"]
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWW'
        self.width = 'WWWWWW'
    def onSelChange(self, selection):
        global sel_type
        sel_type = selection
    def onEditChange(self, text):
        pass
    def onFocus(self, focused):
        pass
    def onEnter(self):
        pass
    def refresh(self):
        pass

class ToolClass2(object):
    """Implementation for AvalAddin_addin.tool (Tool)"""
    def __init__(self):
        self.enabled = True
        self.shape = "Rectangle" # Can set to "Line", "Circle" or "Rectangle" for interactive shape drawing and to activate the onLine/Polygon/Circle event sinks.
    def onMouseDown(self, x, y, button, shift):
        pass
    def onMouseDownMap(self, x, y, button, shift):
        pass
    def onMouseUp(self, x, y, button, shift):
        pass
    def onMouseUpMap(self, x, y, button, shift):
        pass
    def onMouseMove(self, x, y, button, shift):
        pass
    def onMouseMoveMap(self, x, y, button, shift):
        pass
    def onDblClick(self):
        pass
    def onKeyDown(self, keycode, shift):
        pass
    def onKeyUp(self, keycode, shift):
        pass
    def deactivate(self):
        pass
    def onCircle(self, circle_geometry):
        pass
    def onLine(self, line_geometry):
        pass
    def onRectangle(self, rectangle_geometry):
        global sel_type
        mxd = arcpy.mapping.MapDocument('current')
        
        rec = rectangle_geometry    # apenas para abreviar o nome da variavel que define o retangulo gerado
        
        array = arcpy.Array([rec.lowerLeft, rec.lowerRight, rec.upperRight,  rec.upperLeft])    # cria um array
                                                                                                # baseado nas
                                                                                                # posições dos
                                                                                                # vertices do
                                                                                                # retangulo    
        poly = arcpy.Polygon(array,mxd.activeDataFrame.spatialReference)        # gera o poligono no sistema de
                                                                                # coordenadas do Data Frame ativo
                                                                                # a variavel poly deve ser utilizada
                                                                                # na selecao por localizacao mais a
                                                                                # frente
        layers = arcpy.mapping.ListLayers(mxd)   # Pegar a lista de layers atualmente adicionados no projeto
        for layer in layers:
            # Testa se o layer é uma Feature Class
            if arcpy.Describe(layer).dataType == 'FeatureLayer':
                # cria uma nova selecao com as feicoes da camada que interceptam o retangulo
                arcpy.SelectLayerByLocation_management(layer,sel_type, poly, "","NEW_SELECTION")
               
