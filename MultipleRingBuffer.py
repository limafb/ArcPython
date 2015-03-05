def MultipleRingBuffer(feat_class, r_ini, r_inc, qnt_buff):
    import arcpy 			#le todas as categorias do arcpy
    from arcpy import *
    arcpy.env.workspace = "D://Cursos//LabGIS//Python//MaterialDidatico//praticas//dadosP03//teste"
    raio = r_ini
    listSHP = []
    for i in range(qnt_buff):
        Buffer_analysis(in_features=feat_class,
	out_feature_class="test"+str(i)+".shp", 
	buffer_distance_or_field=raio, line_side="FULL",
	line_end_type="ROUND", dissolve_option="NONE", dissolve_field="",
	method="PLANAR")
	raio += r_inc
    listSHP = arcpy.ListFeatureClasses('*.shp')
    listSHP.sort(reverse=True)
    arcpy.Merge_management(listSHP, "teste_merge.shp")
    for shp in listSHP:
        Delete_management(shp)
