# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# del.py
# Created on: 2021-06-20 12:17:55.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")


# Local variables:
NC = "A:\\YUDI\\Prima\\DIKLATIKLIM\\PYTHONSCRIPT\\dataexcel\\GSMaP_202106100000.nc"
SHP = "A:\\YUDI\\Prima\\DIKLATIKLIM\\jumat\\KALTIMFIXt.shp"
tesshp = "A:\\YUDI\\Prima\\DIKLATIKLIM\\PYTHONSCRIPT\\tesshp"
rainrate_Layer = "rainrate"
Extract = "A:\\YUDI\\Prima\\DIKLATIKLIM\\PYTHONSCRIPT\\New File Geodatabase.gdb\\Extract"
Raster = "A:\\YUDI\\Prima\\DIKLATIKLIM\\PYTHONSCRIPT\\New File Geodatabase.gdb\\Raster"
Excel_Table = "A:\\YUDI\\Prima\\DIKLATIKLIM\\PYTHONSCRIPT\\scratch\\Excel_Table.xls"
Idw_Raster = "A:\\YUDI\\Prima\\DIKLATIKLIM\\PYTHONSCRIPT\\New File Geodatabase.gdb\\Idw_Raster"

# Process: Make NetCDF Raster Layer
arcpy.MakeNetCDFRasterLayer_md(NC, "rainrate", "longitude", "latitude", rainrate_Layer, "", "", "BY_VALUE")

# Process: Extract by Mask
arcpy.gp.ExtractByMask_sa(rainrate_Layer, SHP, Extract)

# Process: Raster to Point
arcpy.RasterToPoint_conversion(Extract, Raster, "Value")

# Process: Feature Class To Shapefile (multiple)
arcpy.FeatureClassToShapefile_conversion("'A:\\YUDI\\Prima\\DIKLATIKLIM\\PYTHONSCRIPT\\New File Geodatabase.gdb\\Raster'", tesshp)

# Process: Table To Excel
arcpy.TableToExcel_conversion(Raster, Excel_Table, "NAME", "CODE")

# Process: IDW
arcpy.gp.Idw_sa(Raster, "POINTID", Idw_Raster, "0.02007493308", "2", "VARIABLE 12", "")

# Process: Delete Features
arcpy.DeleteFeatures_management(Raster)

