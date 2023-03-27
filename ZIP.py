import zipfile as z
def unpack(name, dir):
    zipFile = z.ZipFile('.\\' + name, 'r')
    zipFile.extractall(dir)
    zipFile.close()