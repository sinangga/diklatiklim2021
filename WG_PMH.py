import arcpy
import os
cwd = os.getcwd()

#-----buat judul---------

tahun = raw_input ("Tahun PMH (cth : 2018-2019) -->  ")
versi = raw_input ("Versi ArcGIS (cth : 10, 10.2, 10.3, 10.4) -->  ")
pulau = raw_input ("Masukkan Pulau (cth : INDONESIA, SUMATERA, JAWA, BALINUSRA, KALIMANTAN_SULAWESI, MALPAP) -->  ")

#-----------cetak AMH---------------------------------------
print "Export Peta Awal Musim Hujan di "+pulau
mxd = arcpy.mapping.MapDocument (cwd+"\\mxd\\kemarau\\Awal_"+pulau+".mxd")
mxd.title = (tahun)
mxd.author = (tahun)
arcpy.mapping.ExportToJPEG (mxd,cwd+"\\hasil\\AMK_"+tahun+"_"+pulau+".jpg")
#-----------cetak MAMUN---------------------------------------
print "Export Peta Perbandingan Musim Hujan Terhadap Normalnya di "+pulau
mxd = arcpy.mapping.MapDocument (cwd+"\\mxd\\hujan\\Mamun_"+pulau+"_v"+versi+".mxd")
mxd.title = (tahun)
mxd.author = (tahun)
arcpy.mapping.ExportToJPEG (mxd,cwd+"\\hasil\\MAMUN_"+tahun+"_"+pulau+".jpg")
#-----------cetak SIFAT---------------------------------------
print "Export Peta Sifat Musim Hujan di "+pulau
mxd = arcpy.mapping.MapDocument (cwd+"\\mxd\\hujan\\Sifat_"+pulau+"_v"+versi+".mxd")
mxd.title = (tahun)
mxd.author = (tahun)
arcpy.mapping.ExportToJPEG (mxd,cwd+"\\hasil\\SIFAT_"+tahun+"_"+pulau+".jpg")
#-----------cetak PUNCAK---------------------------------------
print "Export Peta Puncak Musim Hujan di "+pulau
mxd = arcpy.mapping.MapDocument (cwd+"\\mxd\\hujan\\Puncak_"+pulau+"_v"+versi+".mxd")
mxd.title = (tahun)
mxd.author = (tahun)
arcpy.mapping.ExportToJPEG (mxd,cwd+"\\hasil\\PUNCAK_"+tahun+"_"+pulau+".jpg")
#--------------------------------------------------------------

