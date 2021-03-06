# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# extractrain.py
# Created on: 2021-06-20 00:20:02.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")


# Local variables:
GSMaP_202106100000_nc = "A:\\YUDI\\Prima\\DIKLATIKLIM\\PYTHONSCRIPT\\dataexcel\\GSMaP_202106100000.nc"
KALTIMFIXt_shp = "A:\\YUDI\\Prima\\DIKLATIKLIM\\jumat\\KALTIMFIXt.shp"
shppoint = "A:\\YUDI\\Prima\\DIKLATIKLIM\\PYTHONSCRIPT\\tesshp"
rainrate_Layer2 = "rainrate_Layer"
Extract_rain = "A:\\YUDI\\Prima\\DIKLATIKLIM\\PYTHONSCRIPT\\New File Geodatabase.gdb\\Extract_rain"
RasterT_Extract3 = "A:\\YUDI\\Prima\\DIKLATIKLIM\\PYTHONSCRIPT\\New File Geodatabase.gdb\\RasterT_Extract3"
Idw_RasterT_3 = "A:\\YUDI\\Prima\\DIKLATIKLIM\\PYTHONSCRIPT\\New File Geodatabase.gdb\\Idw_RasterT_3"
extract_to_excel = "A:\\YUDI\\Prima\\DIKLATIKLIM\\PYTHONSCRIPT\\scratch\\RasterT_Extract3_TableToExcel.xls"

# Process: Make NetCDF Raster Layer
arcpy.MakeNetCDFRasterLayer_md(GSMaP_202106100000_nc, "rainrate", "longitude", "latitude", rainrate_Layer2, "", "", "BY_VALUE")

# Process: Extract by Mask
arcpy.gp.ExtractByMask_sa(rainrate_Layer2, KALTIMFIXt_shp, Extract_rain)

# Process: Raster to Point
arcpy.RasterToPoint_conversion(Extract_rain, RasterT_Extract3, "Value")

# Process: IDW
arcpy.gp.Idw_sa(RasterT_Extract3, "GRID_CODE", Idw_RasterT_3, "0.02007493308", "2", "VARIABLE 12", "")

# Process: Table To Excel
arcpy.TableToExcel_conversion(RasterT_Extract3, extract_to_excel, "NAME", "CODE")

# Process: Feature Class To Shapefile (multiple) (2)
arcpy.FeatureClassToShapefile_conversion("'A:\\YUDI\\Prima\\DIKLATIKLIM\\PYTHONSCRIPT\\New File Geodatabase.gdb\\RasterT_Extract3'", shppoint)

