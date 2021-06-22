import arcpy
import os
cwd = os.getcwd()

#----------------------UBAH BAGIAN INI------------------------

tahun = "2021"
update = "Dasarian I Juni 2021"
tgl = "2021.06.10"
#-------------------------------------------------------------
pulau = ["INDONESIA"]

#-----------cetak Perkembangan Musim Kemarau---------------------------------------
for i in pulau :
	print "Export Peta Awal Musim Kemarau di "+i
	mxd = arcpy.mapping.MapDocument (cwd+"\\mxd\\PM\\PM_AMK_"+i+"_v10.4.mxd")
	mxd.title = (tahun)
	mxd.author = (update)
	arcpy.mapping.ExportToJPEG (mxd,cwd+"\\hasil\\PM\\PM_AMK_"+tahun+"_"+i+"_ver_"+tgl+".jpg")
	#-----------cetak PKM---------------------------------------
	print "Export Peta Perkembangan Musim Kemarau di "+i
	mxd = arcpy.mapping.MapDocument (cwd+"\\mxd\\PM\\PMK_"+i+"_v10.4.mxd")
	mxd.title = (tahun)
	mxd.author = (update)
	arcpy.mapping.ExportToJPEG (mxd,cwd+"\\hasil\\PM\\PMK_"+tahun+"_"+i+"_ver_"+tgl+".jpg")
#--------------------------------------------------------------

