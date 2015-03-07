# habilita a extensao Spatial Analyst e carrega a biblioteca
arcpy.CheckOutExtension("Spatial")
from arcpy.sa import *
# pega os parametros informados pelo usuario na janela da ferramenta
# pega a pasta de entrada com os arquivos a serem cortados
inputPath = arcpy.GetParameterAsText(0)
inputPath = "C:/Users/FabioLap/Documents/GitHub/ArcPython/Avaliacao3/Dados_Avaliacao_3/Projeto_1"

# pega um Shapefile do tipo pol�gono para m�scara de corte
clipFeature = arcpy.GetParameterAsText(1)
clipFeature = "C:/Users/FabioLap/Documents/GitHub/ArcPython/Avaliacao3/Dados_Avaliacao_3/Projeto_1/MASCARA.shp"

# pega a pasta onde os arquivos resultantes ser�o salvos
outputPath = arcpy.GetParameterAsText(4)
outputPath = "C:/Users/FabioLap/Documents/GitHub/ArcPython/Avaliacao3/Dados_Avaliacao_3/Projeto_1/Resultado"

# pega os arquivos e corta com a mascara fornecida
Datasets = arcpy.ListDatasets(inputPath)
Datasets = arcpy.ListDatasets()
Rasters = arcpy.ListRasters()
Features = arcpy.ListFeatureClasses()
for fc in arcpy.ListFeatureClasses():

if not arcpy.ListFeatureClasses():
    print "N�o ha feature class"
else:
    for fc in arcpy.ListFeatureClasses():
        # Set the output name to be the same as the input name, and
        #    locate in the 'out_workspace' workspace
        #
        output = os.path.join(outputPath, fc)

        # Clip each input feature class in the list
        #
        arcpy.Clip_analysis(fc, clipFeature, output, 0.1)

if not arcpy.ListRasters():
    print "N�o h� arquivos raster"
else:
    for rs in arcpy.ListRasters():
        # Set the output name to be the same as the input name, and
        #    locate in the 'out_workspace' workspace
        #
        output = os.path.join(outputPath, rs)

        # Extract each input raster in the list
        #
        extract = ExtractByMask(rs, output)
        
        # salva o raster resultante no caminho indicado pelo usuario
        extract.save(outputPath)
