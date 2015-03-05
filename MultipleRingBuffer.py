def MultipleRingBuffer(feat_class, r_ini, r_inc, qnt_buff):
    import arcpy 			
    from arcpy import *
    raio = r_ini
    listFeature = []
    for i in range(qnt_buff):
        Buffer_analysis(in_features=feat_class,
	out_feature_class="buffer"+str(i), 
	buffer_distance_or_field=raio, line_side="FULL",
	line_end_type="ROUND", dissolve_option="NONE", dissolve_field="",
	method="PLANAR")
        listFeature.append("buffer"+str(i))
	raio += r_inc
    listFeature.sort(reverse=True)
    arcpy.Merge_management(listFeature, "merge"+feat_class)
    for feature in listFeature:
        Delete_management(env.workspace+str("/")+feature)
