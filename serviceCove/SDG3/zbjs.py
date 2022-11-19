import arcpy
from arcpy import env
import os
import sys
# === import project path ===
curPath = os.path.abspath(os.path.dirname("E:\\arcpy\\keda\\Natural\\SDG\\keda2\\dto.py"))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
# ===========================
# sys.path.append("..")
from keda2 import dto

def Run(serviceCove0, exOptions0):
    road_shp = serviceCove0.road_shp
    water_shp = serviceCove0.water_shp
    poi_shp = serviceCove0.poi_shp
    boundary_shp = serviceCove0.boundary_shp
    path = exOptions0.path
    # set the intermediate data folder
    # path = "E:\\arcpy\\EX02\\data"
    intermediateDataPath = path + "\\" + "IntermediateData"
    # set result data folder
    resultDataPath = path + "\\" + "Result"
    print("-----------------------------------------------------------")
    print("Determine if the folder exists")
    print("Please wait...")
    # determine if the folder exists
    if os.path.exists(intermediateDataPath):
        print("IntermediateData floder exists")
    else:
        # create a intermediate data floder
        arcpy.CreateFolder_management(path, "IntermediateData")

    if os.path.exists(resultDataPath):
        print("Result floder exists")
    else:
        # create a result floder
        arcpy.CreateFolder_management(path, "Result")
    print("Under calculation......")
    print("Please do not close the window.")
    # set workspace
    env.workspace = intermediateDataPath
    arcpy.CheckOutExtension("spatial")  # Check if expansion is normal
    env.parallelProcessingFactor = '0'  # Set and behave 0 to prevent sometimes inexplicable errors
    env.overwriteOutput = "True"  # Set file coverage read and write
    # intermediate variable
    hospitalSel_shp = intermediateDataPath + "\\" + "hospitalSel.shp"
    # outcome
    roadPro_shp = intermediateDataPath + "\\" + "roadPro.shp"
    waterPro_shp = intermediateDataPath + "\\" + "waterPro.shp"
    hospitalPro_shp = intermediateDataPath + "\\" + "hospitalPro.shp"
    boundaryPro_shp = intermediateDataPath + "\\" + "boundaryPro.shp"

    # Process: project
    print("Begin to project road!")
    arcpy.Project_management(road_shp, roadPro_shp,
                             "PROJCS['CGCS2000_3_Degree_GK_CM_120E',GEOGCS['GCS_China_Geodetic_Coordinate_System_2000',DATUM['D_China_2000',SPHEROID['CGCS2000',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',120.0],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]",
                             "",
                             "GEOGCS['GCS_China_Geodetic_Coordinate_System_2000',DATUM['D_China_2000',SPHEROID['CGCS2000',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]",
                             "NO_PRESERVE_SHAPE", "", "NO_VERTICAL")
    print("Succeeded in road projection!")
    # Process: add field
    print("Begin to add field!")
    arcpy.AddField_management(roadPro_shp, "Speed", "DOUBLE", "7", "6", "", "", "NULLABLE", "NON_REQUIRED", "")
    # Process: add field
    arcpy.AddField_management(roadPro_shp, "Speed_adju", "DOUBLE", "7", "6", "", "", "NULLABLE", "NON_REQUIRED",
                              "")
    # Process: Add geometric attributes
    arcpy.AddGeometryAttributes_management(roadPro_shp, "LENGTH", "KILOMETERS", "", "")
    print("Succeeded in adding field!")
    # Process: calculate fields
    print("Begin to calculate fields!")
    arcpy.management.CalculateField(in_table=roadPro_shp, field="Speed", expression="cal(!FSCALE!)",
                                    expression_type="PYTHON3", code_block="""def cal(FSCALE):
             if FSCALE == 7:
              return 80
             if FSCALE == 8:
              return 80
             if FSCALE == 9:
              return 80
             if FSCALE == 10:
              return 60
             if FSCALE == 11:
              return 60
             if FSCALE == 12:
              return 60
             if FSCALE == 13:
              return 45
             if FSCALE == 14:
              return 45
             if FSCALE == 15:
              return 45
             if FSCALE == 16:
              return 35
             if FSCALE == 17:
              return 35
             if FSCALE == 18:
              return 35
             if FSCALE == 19:
              return 35
             if FSCALE == 20:
              return 35
             if FSCALE == 21:
              return 35
             else:
              return 0""", field_type="TEXT", enforce_domains="NO_ENFORCE_DOMAINS")
    # Process: calculate fields
    arcpy.CalculateField_management(roadPro_shp, "Speed_adju", "!Speed! * 0.7", "PYTHON_9.3", "")
    # Process: calculate fields
    arcpy.AddField_management(roadPro_shp, "cost", "DOUBLE", "7", "6", "", "", "NULLABLE", "NON_REQUIRED", "")
    # Process: calculate fields
    arcpy.CalculateField_management(roadPro_shp, "cost", "3600 * !LENGTH! / !Speed_adju!", "PYTHON_9.3", "")
    print("Succeeded in calculating fields!")

    # Process: Project
    print("Begin to project water!")
    arcpy.Project_management(water_shp, waterPro_shp,
                             "PROJCS['CGCS2000_3_Degree_GK_CM_120E',GEOGCS['GCS_China_Geodetic_Coordinate_System_2000',DATUM['D_China_2000',SPHEROID['CGCS2000',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',120.0],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]",
                             "",
                             "GEOGCS['GCS_China_Geodetic_Coordinate_System_2000',DATUM['D_China_2000',SPHEROID['CGCS2000',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]",
                             "NO_PRESERVE_SHAPE", "", "NO_VERTICAL")
    print("Succeeded in water projection!")
    # Process: Select hospital
    print("Begin to select hospital!")
    arcpy.Select_analysis(poi_shp, hospitalSel_shp, "SHORTNAME LIKE '%卫生院%'")
    print("Succeeded in selecting hospital!")
    # Process: Project
    print("Begin to project hospital point!")
    arcpy.Project_management(hospitalSel_shp, hospitalPro_shp,
                             "PROJCS['CGCS2000_3_Degree_GK_CM_120E',GEOGCS['GCS_China_Geodetic_Coordinate_System_2000',DATUM['D_China_2000',SPHEROID['CGCS2000',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',120.0],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]",
                             "",
                             "GEOGCS['GCS_China_Geodetic_Coordinate_System_2000',DATUM['D_China_2000',SPHEROID['CGCS2000',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]",
                             "NO_PRESERVE_SHAPE", "", "NO_VERTICAL")
    print("Succeeded in hospital projection!")
    # Process: Project
    print("Begin to project boundary!")
    arcpy.Project_management(boundary_shp, boundaryPro_shp,
                             "PROJCS['CGCS2000_3_Degree_GK_CM_120E',GEOGCS['GCS_China_Geodetic_Coordinate_System_2000',DATUM['D_China_2000',SPHEROID['CGCS2000',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',120.0],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]",
                             "",
                             "GEOGCS['GCS_China_Geodetic_Coordinate_System_2000',DATUM['D_China_2000',SPHEROID['CGCS2000',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]",
                             "NO_PRESERVE_SHAPE", "", "NO_VERTICAL")
    print("Succeeded in boundary projection!")
    print("Succeeded in pre_processing!")
    print("-----------------------------------------------------------")
    serviceCove1 = dto.serviceCove1()
    serviceCove1.roadPro_shp = roadPro_shp
    serviceCove1.waterPro_shp = waterPro_shp
    serviceCove1.poiPro_shp = hospitalPro_shp
    serviceCove1.boundaryPro_shp = boundaryPro_shp
    return serviceCove1

def Run2(serviceCove1, exOptions1):
    roadPro_shp = serviceCove1.roadPro_shp
    waterPro_shp = serviceCove1.waterPro_shp
    hospitalPro_shp = serviceCove1.poiPro_shp
    boundaryPro_shp = serviceCove1.boundaryPro_shp
    path = exOptions1.path
    pop_tif = exOptions1.pop_tif
    time_input = exOptions1.time_input

    # self.path = "E:\\arcpy\\EX02\\data"
    # set the intermediate data folder
    intermediateDataPath = path + "\\" + "IntermediateData"
    # set result data folder
    resultDataPath = path + "\\" + "Result"
    # determine if the folder exists
    if os.path.exists(intermediateDataPath):
        print("IntermediateData floder exists")
    else:
        # create a intermediate data floder
        arcpy.CreateFolder_management(path, "IntermediateData")

    if os.path.exists(resultDataPath):
        print("Result floder exists")
    else:
        # create a result floder
        arcpy.CreateFolder_management(path, "Result")
    # set workspace
    env.workspace = intermediateDataPath
    arcpy.CheckOutExtension("spatial")  # Check if expansion is normal
    env.parallelProcessingFactor = '0'  # Set and behave 0 to prevent sometimes inexplicable errors
    env.overwriteOutput = "True"  # Set file coverage read and write
    env.XYResolution = "30 Meters"
    env.outputCoordinateSystem = "PROJCS['CGCS2000_3_Degree_GK_CM_120E',GEOGCS['GCS_China_Geodetic_Coordinate_System_2000',DATUM['D_China_2000',SPHEROID['CGCS2000',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',120.0],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]"
    # env.extent = "119.756438910228 30.4277363460556 120.339466791859 30.6975464263265"
    # self.boundary_shp = self.boundaryPro_shp
    env.extent = boundaryPro_shp
    env.XYTolerance = "30 Meters"
    # intermediate variable
    road_tif = intermediateDataPath + "\\" + "road.tif"
    road_re_tif = intermediateDataPath + "\\" + "road_re.tif"
    road_re2_tif = intermediateDataPath + "\\" + "road_re2.tif"
    water_tif = intermediateDataPath + "\\" + "water.tif"
    IsNull_tif = intermediateDataPath + "\\" + "water_isnull.tif"
    water_re_tif = intermediateDataPath + "\\" + "water_re.tif"
    road_fin_tif = intermediateDataPath + "\\" + "road_fin.tif"
    Output_backlink_raster = ""
    keda1_tif = intermediateDataPath + "\\" + "keda1.tif"
    keda2_tif = intermediateDataPath + "\\" + "keda2.tif"
    keda3_tif = intermediateDataPath + "\\" + "keda3.tif"

    # outcomes
    keda4_tif = resultDataPath + "\\" + "keda" + "{0}".format(time_input) + ".tif"
    keda3_re_tif = intermediateDataPath + "\\" + "keda3_re.tif"
    keda3_re_polygon_shp = intermediateDataPath + "\\" + "keda3_re_polygon.shp"
    statistics_dbf = intermediateDataPath + "\\" + "hospital_statistics.dbf"

    # Process: Polyline to Raster
    print("Begin to turn road Polyline to Raster!")
    arcpy.PolylineToRaster_conversion(roadPro_shp, "cost", road_tif, "MAXIMUM_LENGTH", "NONE", "30")
    print("Succeeded in Polyline to Raster!")

    # Process: Reclassify
    print("Begin to reclassify road!")
    arcpy.gp.Reclassify_sa(road_tif, "VALUE",
                           "0 42 42;42 51 51;51 64 64;64 85 85;85 102 102;102 128 128;128 257 257;257 342 342;NODATA 1280",
                           road_re_tif, "DATA")
    print("Succeeded in road Reclassify!")

    # Process: Polygon to Raster
    print("Begin to turn water Polygon to Raster!")
    arcpy.PolygonToRaster_conversion(waterPro_shp, "FSCALE", water_tif, "CELL_CENTER", "NONE",
                                     road_re_tif)
    print("Succeeded in water Polygon to Raster!")

    # Process: Raster Calculator
    print("Begin to reclassify water!")
    is_null = arcpy.sa.IsNull(water_tif)
    is_null.save(IsNull_tif)
    result = arcpy.sa.Con(arcpy.sa.Raster(IsNull_tif), 0, 1)
    result.save(water_re_tif)
    print("Succeeded in water reclassify!")

    # # Process: Raster Calculator
    # print ("Begin to reclassify water!")
    # set_null = arcpy.sa.SetNull(arcpy.sa.Raster(water_re_tif) == 1, arcpy.sa.Raster(road_re_tif))
    # set_null.save(road_fin_tif)
    # print ("Succeeded in water Reclassify!")

    # Process: Raster Calculator
    print("Begin to calculate road cost!")
    set_null = arcpy.sa.SetNull(arcpy.sa.Raster(water_re_tif) == 1, arcpy.sa.Raster(road_re_tif))
    set_null.save(road_re2_tif)
    bridge = arcpy.sa.Con((arcpy.sa.Raster(water_re_tif) == 1) & (arcpy.sa.Raster(road_re_tif) != 1280),
                          arcpy.sa.Raster(road_re_tif), arcpy.sa.Raster(road_re2_tif))
    bridge.save(road_fin_tif)
    print("Succeeded in calculating road cost!")

    env.extent = road_fin_tif
    # Process: Cost Distance
    print("Begin to calculate cost distance!")
    arcpy.gp.CostDistance_sa(hospitalPro_shp, road_fin_tif, keda1_tif, "", Output_backlink_raster,
                             "", "", "", "")
    print("Succeeded in road accessibility calculation!")

    # Process: Raster Calculator
    print("Begin to change time unit!")
    RasterCalculator = (arcpy.sa.Raster(keda1_tif) / 60000)
    RasterCalculator.save(keda2_tif)
    print("Succeeded in changing road accessibility unit to second!")

    # Process: Clip
    print("Begin to clip road accessibility!")
    arcpy.Clip_management(keda2_tif, "476623.004286932 3367530.98330478 532540.131856447 3397452.50770329",
                          keda3_tif,
                          boundaryPro_shp, "-3.402823e+038", "ClippingGeometry", "NO_MAINTAIN_EXTENT")
    print("Succeeded in road accessibility clipping!")

    # Process: calculate road reachability in specified time
    print("Begin to calculate road reachability in specified time!")
    result = arcpy.sa.Con(arcpy.sa.Raster(keda3_tif) <= time_input, time_input)
    result.save(keda4_tif)
    print("Succeeded in road reachability calculation in specified time!")

    # Process: Reclassify
    arcpy.gp.Reclassify_sa(keda3_tif, "VALUE",
                           "0 5 5;5 10 10;10 15 15;15 20 20;20 25 25;25 30 30;30 35 35;35 40 40;40 45 45;45 50 50;50 55 55;55 60 60;60 65 65;65 70 70;70 75 75;75 80 80;80 85 85;85 90 90;90 95 95;95 100 100;100 105 105;105 110 110;110 115 115;115 120 120;120 125 125;125 130 130",
                           keda3_re_tif, "DATA")
    print("Succeeded in road accessibility reclassification!")

    # Process: Raster to Polygon
    arcpy.RasterToPolygon_conversion(keda3_re_tif, keda3_re_polygon_shp, "SIMPLIFY", "Value")
    print("Succeeded in road accessibility Raster to polygon!")

    # Process: Zonal Statistics as Table
    arcpy.gp.ZonalStatisticsAsTable_sa(keda3_re_polygon_shp, "GRIDCODE", pop_tif, statistics_dbf,
                                       "DATA", "ALL")
    print("Succeeded in road accessibility statistics by demographics!")

    print("Finish!")
    print("-----------------------------------------------------------")
    # self.dto2.set_keda(self.keda4_tif)
    outdto = dto.serviceCove2()
    outdto.keda_tif = keda4_tif
    return outdto