import arcpy
import os
cwd = os.getcwd()

#----------------------UBAH BAGIAN INI------------------------

tahun = "2021"
update = "Dasarian I Maret 2021"
tgl = "2021.03.10"
#-------------------------------------------------------------
#pulau = ["JAWA"]
pulau = ["INDONESIA", "SUMATERA", "JAWA", "BALINUSRA", "MALPAP", "KALIMANTAN_SULAWESI"]
#, "SUMATERA", "JAWA", "BALINUSRA", "MALPAP",  "KALIMANTAN_SULAWESI"]

#-----------cetak Perkembangan Musim HUjan---------------------------------------
for i in pulau :
	print "Export Peta Awal Musim Hujan di "+i
	mxd = arcpy.mapping.MapDocument (cwd+"\\mxd\\PM\\PM_AMH_"+i+"_v10.4.mxd")
	mxd.title = (tahun)
	mxd.author = (update)
	arcpy.mapping.ExportToJPEG (mxd,cwd+"\\hasil\\PM\\PM_AMH_"+tahun+"_"+i+"_ver_"+tgl+".jpg")
	#-----------cetak 2 warna---------------------------------------
	print "Export Peta Perkembangan Musim Hujan di "+i
	mxd = arcpy.mapping.MapDocument (cwd+"\\mxd\\PM\\PMA_"+i+"_v10.4.mxd")
	mxd.title = (tahun)
	mxd.author = (update)
	arcpy.mapping.ExportToJPEG (mxd,cwd+"\\hasil\\PM\\PMA_"+tahun+"_"+i+"_ver_"+tgl+".jpg")
#--------------------------------------------------------------
print "FINISH..."
