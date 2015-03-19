import arcpy
import pythonaddins
fc_selected = "" # armazena o nome do Feature Class em uma variavel
#global, ou seja, que pode ser acessada por outros metodos.
labelfield = "" #armazena o nome do atributo da Feature Class em uma variavel
#global.
setOIDLabeled = set([]) #inicializa um set global que armazenara os OID's
#que vamos adicionar o label

class BtnAdicionarLabel(object):
    """Implementation for Addin.BtnAdicionarLabel (Tool)"""
    def __init__(self):
        self.enabled = True
        self.shape = "NONE" # Can set to "Line", "Circle" or "Rectangle" for interactive shape drawing and to activate the onLine/Polygon/Circle event sinks.
    def onMouseDown(self, x, y, button, shift):
        pass
    def onMouseDownMap(self, x, y, button, shift):
        pass
    def onMouseUp(self, x, y, button, shift):
        pass
    def onMouseUpMap(self, x, y, button, shift):
        # Pegar o projeto aberto do ArcMap
        print "click ",x,y
        global fc_selected
        #para acessar a variavel global no inicio desse arquivo .py
        mxd = arcpy.mapping.MapDocument('current')
        desc = arcpy.Describe(fc_selected)
        #Criar um ponto na posicao onde houve o clique do mouse e no
        #sistema de coordenadas da respectiva camada.
        pointGeom = arcpy.PointGeometry(arcpy.Point(x,y), desc.spatialReference)
        # cria uma nova selecao com as feicoes da camada que interceptam o
        #ponto do clique do mouse
        arcpy.SelectLayerByLocation_management(fc_selected,"INTERSECT",
        pointGeom, "","NEW_SELECTION")
        # Pegar a lista de OID's que foram selecionados
        ListOIDs = desc.FIDSet
        if str(ListOIDs) == "":
            # Se nenhuma feicao foi selecionada, nao ha nada a fazer.
            return
        OID = ListOIDs
        # Pegar o nome do campo com o OID
        oidfield = desc.OIDFieldName
        global setOIDLabeled # para acessar a variavel global
        setOIDLabeled.add(OID) # adicionar o novo OID no set. Lembrando que
        #o set elimina elementos repetidos.
        #pegar o layer do feature class selecionado para mexermos nos labels
        lyr = arcpy.mapping.ListLayers(mxd,fc_selected)[0]
        #o retorno e uma lista, estamos pegando o primeiro elemento

        lyr.showLabels = True # habilita a exibicao dos labels
        lblClass = lyr.labelClasses[0] # pega o classe Default de labels
        global labelfield # para acessar a variavel global
        lblClass.expression = '[' + labelfield + ']'

        SQLQuery = ''
        #variavel para construir a expressao que coloca labels no OID's
        for OID in setOIDLabeled:
            if SQLQuery != '':
                SQLQuery += ' OR '
            SQLQuery += '"' + oidfield + '" = ' + OID
        print SQLQuery
        lblClass.SQLQuery = SQLQuery
                
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
        pass

class BtnLayout(object):
    """Implementation for Addin.BtnLayout (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        # Pegar o projeto aberto do ArcMap
        mxd = arcpy.mapping.MapDocument('current')
        #Se o botao nao esta pressionado (checked), entra em modo de
        #layout. Senao, sai do modo de layout
        if not self.checked:
            mxd.activeView = 'PAGE_LAYOUT'
            self.checked = True #Pressiona o botao
        else:
            mxd.activeView = 'Layers'
            self.checked = False #Libera o botao

class ComboBoxCampos(object):
    """Implementation for AddIn.ComboCampos (ComboBox)"""
    def __init__(self):
        self.items = []
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWWWWWWWWW' # ajustar a largura da lista de
        #opcoes
        self.width = 'WWWWWWWWWWWWW' # ajustar a largura do campo
    def onSelChange(self, selection):
        global labelfield, setOIDLabeled
        # acessar a variavel global no inicio desse arquivo
        labelfield = selection
        setOIDLabeled = set([])
    def onEditChange(self, text):
        pass
    def onFocus(self, focused):
        # Se nao ha Feature Class selecionado, nao ha nada a fazer.
        global fc_selected
        if fc_selected == "":
            return
        # Limpar a lista de campos atual
        self.items = []
        # Pegar a lista de campos do Feature Class selecionado
        fieldList = arcpy.ListFields(fc_selected)
        for field in fieldList:
            self.items.append(field.name)
        
    def onEnter(self):
         pass
    def refresh(self):
         pass

class ComboBoxLayers(object):
    """Implementation for AddIn.ComboLayers (ComboBox)"""
    def __init__(self):
        self.items = []
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWWWWWWWWW' # ajustar a largura da lista de
        #opcoes
        self.width = 'WWWWWWWWWWWWW' # ajustar a largura do campo
    def onSelChange(self, selection):
        global fc_selected, labelfield, setOIDLabeled
        # acessar a variavel global no inicio desse arquivo
        fc_selected = selection
        setOIDLabeled = set([])
        labelfield = ""
    def onEditChange(self, text):
        pass
    def onFocus(self, focused):
        # Pegar o projeto aberto do ArcMap
        mxd = arcpy.mapping.MapDocument('current')
        # Pegar a lista de layers atualmente adicionados no projeto
        layers = arcpy.mapping.ListLayers(mxd)
        # Limpa os itens na lista para inserir novos itens.
        self.items = []
        for layer in layers:
            # Adiciona na lista todos os nomes das camadas vetoriais.
            if arcpy.Describe(layer).dataType == 'FeatureLayer':
                self.items.append(layer.name)
    def onEnter(self):
        pass
    def refresh(self):
        pass
