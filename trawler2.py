import os

holders = []
diodes = []
ann = []

def list_files(dir):
   files = []
   for obj in os.listdir(dir):
      if os.path.isfile(obj):
         files.append(obj)
   return files

def list_dir(dir):
   dirs = []
   for obj in os.listdir(dir):
      if os.path.isdir(obj):
         dirs.append(obj)
   return dirs

for holder in list_dir("."):
   holderdir = os.path.join(".",holder)
   for diode in list_dir(holderdir):
      diodedir = os.path.join(holderdir,holder)
      for ann in list_dir(diodedir):
         anndir = os.path.join(diodedir,diode)
         for temp in list_dir(diodedir):
            tempdir = os.path.join(anndir, ann)
            print holder, diode, ann, temp, list_files(tempdir)
