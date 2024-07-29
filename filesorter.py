import os
import shutil

path = r"/Users/ayodejionawunmi/Desktop/"

file_name = ['photos files', 'jpeg files', 'confidential']

file_dir = os.listdir(path)

# Automated System to make the folder
for i in range(len(file_name)):
  folder = os.path.join( path, file_name[i])
  if not os.path.exists(folder):
    print(folder)
    os.makedirs(folder)

for file in file_dir:
  file_path = os.path.join(path, file)
  print(f"File Path : {file_path}")

  if os.path.isfile(file_path):
    print(file)
    if file.startswith('Screenshot'):
      end_folder= os.path.join(path, "photos files")
      if os.path.exists(end_folder):
       end_path = os.path.join(end_folder, file)
       print(f"End Path: {end_path}")
       shutil.move(file_path, end_path)
  

