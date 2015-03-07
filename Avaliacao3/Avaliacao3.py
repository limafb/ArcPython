# habilita a extensao Spatial Analyst e carrega a biblioteca
arcpy.CheckOutExtension("Spatial")
from arcpy.sa import *
import os

# pega os parametros informados pelo usuario na janela da ferramenta
# pega a pasta de entrada com os arquivos a serem cortados
inputPath = arcpy.GetParameterAsText(0)

# pega um Shapefile do tipo polígono para máscara de corte
clipFeature = arcpy.GetParameterAsText(1)

# testa se a mascara de entrada é do tipo polígono
if not (arcpy.Describe(clipFeature)).shapeType == "Polygon":
    arcpy.AddWarning("A máscara deve ser um polígono")

# pega a pasta onde os arquivos resultantes serão salvos
outputPath = arcpy.GetParameterAsText(2)

# testa se a pasta de saída é igual a pasta de entrada
if inputPath == outputPath:
    arcpy.AddWarning("A pasta de saída deve ser diferente da pasta de entrada")

# pega os arquivos e corta com a mascara fornecida
# define o ambiente como a pasta de entrada
arcpy.env.workspace = inputPath

# testa se há Feature Classes na pasta de entrada, em caso
# positivo executa o clip
if not arcpy.ListFeatureClasses('*.shp'):
    arcpy.AddWarning("Nao ha arquivos shape em" + inputPath)
else:
    for fc in arcpy.ListFeatureClasses():
        # Define o nome de saída como o mesmo do de entrada
        # e define a pasta de saída
        #
        output = os.path.join(outputPath, fc)

        # Clip each input feature class in the list
        #
        arcpy.Clip_analysis(fc, clipFeature, output, 0.001)

# testa se há arquivos raster na pasta de entrada, em caso
# positivo executa o extract by mask
if not arcpy.ListRasters('*.tif'):
    arcpy.AddWarning("Nao ha arquivos tif em" + inputPath)
else:
    for rs in arcpy.ListRasters():
        # Set the output name to be the same as the input name, and
        #    locate in the 'out_workspace' workspace
        #
        output = os.path.join(outputPath, rs)

        # Extract each input raster in the list
        #
        extract = ExtractByMask(rs, clipFeature)
        
        # salva o raster resultante no caminho indicado pelo usuario
        extract.save(output)
