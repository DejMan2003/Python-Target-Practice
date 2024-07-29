import os
import shutil
import time

path = r"/Users/ayodejionawunmi/"

file_name = ['photos files', 'jpeg files', 'confidential', 'pdf files', 'music files', 'csv files']
now = time.time()

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

  date  = os.path.getmtime(file_path) # gives me the last modified date of the file path.
  standard_time = now - (730 * 86400) # How long to keep the file for = 700 days.

  if date < standard_time : # Deletes the file if the date is has been longer than 700 days
    try:
      os.remove(file_path)
      print(f"Deleted File: {file_path}")
    except PermissionError:
      print(f"Permission denied: {file_path}")
    except Exception as e: 
      print(f"Error with deleting file {file_path}: {e}")



#If statement depending on the extension of the file or the file name.
  if os.path.isfile(file_path):
    print(file)
    if file.startswith('Screenshot'):
      end_folder= os.path.join(path, "photos files")
      if os.path.exists(end_folder):
       end_path = os.path.join(end_folder, file)
       print(f"End Path: {end_path}")
       shutil.move(file_path, end_path)
    if file.endswith(('.JPG','.jpg','.jpeg')):
      end_folder= os.path.join(path, "jpeg files")
      if os.path.exists(end_folder):
        end_path= os.path.join(end_folder, file)
        print(f"End Path: {end_path}")
        shutil.move(file_path,end_path)
    if file.endswith('.pdf'):
      end_folder= os.path.join(path, "pdf files")
      if os.path.exists(end_folder):
        end_path= os.path.join(end_folder, file)
        print(f"End Path: {end_path}")
        shutil.move(file_path,end_path)
    if file.endswith('.mp3'):
      end_folder= os.path.join(path, "music files")
      if os.path.exists(end_folder):
        end_path= os.path.join(end_folder, file)
        print(f"End Path: {end_path}")
        shutil.move(file_path,end_path)
    if file.endswith('.csv'):
      end_folder= os.path.join(path, "CSV files")
      if os.path.exists(end_folder):
        end_path= os.path.join(end_folder, file)
        print(f"End Path: {end_path}")
        shutil.move(file_path,end_path)
    
  

