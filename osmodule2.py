import os

# Create path change '\' to '/' in Windows
directory = "NOS"
parent_dir = "C:/Users/Ravi Ranjan/Downloads/PPC Bills"
path = os.path.join(parent_dir, directory)

# To creake a folder by the name NOS (only once)!!
if(not os.path.exists(path)):
 os.mkdir(path)

# Check Current Working Directory i am in.
cwd = os.getcwd() 
print("Current working directory:", cwd) 

folderpath = "C:/Users/Ravi Ranjan/Downloads/PPC Bills/NOS"
print(folderpath)

# 1. Create Folders in Directory using mkdir
# for txt_file in range(1,10):
#     os.mkdir(f"{folderpath}/{txt_file}")
# print("Files Created")

# # 2. List Folders in Directory in listdir
# folders = os.listdir(folderpath)
# print(folders)

# # 3. List files inside Folders in Directory
# for folder in folders:
#  print(folder)
#  print(os.listdir(f"{folderpath}/{folder}"))

# # 4. Rename a Folder in a Directory
# i=1
# for folder in range(1,10):
# #  print(folder)
#   os.rename(f"{folderpath}/{folder}.txt", f"{folderpath}/FolderNo{i}")
#   i = i+1

 # 5. Delete a Folder in a directory os.remove(path) if Not empty OR os.remove only if all folders are Empty
folders = os.listdir(folderpath)
for folder in folders:
   os.rmdir(f"{folderpath}/{folder}")
   ### use os.remove if contents not empty
print("File has been removed successfully") 
  
