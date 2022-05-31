from distutils import extension
import os
import shutil

from_dir = "C:/Users/grego/Downloads/PythonProjectDownloads"
to_dir = "C:/Users/grego/PythonProjectDocumentFiles"
listallfiles = os.listdir(from_dir)
#print(listallfiles)

for file_name in listallfiles:
    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)
    
    if extension == '':
        continue
    
    if extension in ['.gif', '.png', '.jpeg', 'jpg', 'jfif']:
        path1 = from_dir + '/' + file_name # Example path1 : Downloads/ImageName1.jpg 
        path2 = to_dir + '/' + "Image_Files" # Example path2 : D:/My Files/Image_Files 
        path3 = to_dir + '/' + "Image_Files" + '/' + file_name # Example path3 : D:/My Files/Image_Files/ImageName1.jpg
        
        if os.path.exists(path2):
            print("Moving " + file_name + ".....") # Move from path1 ---> path3 
            shutil.move(path1, path3) 
        else: 
            os.makedirs(path2) 
            print("Moving " + file_name + ".....") 
            shutil.move(path1, path3)