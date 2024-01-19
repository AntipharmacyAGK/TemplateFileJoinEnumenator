import pathlib
import glob
import os
project = pathlib.Path("listify 1")
print(project)
print(os.listdir(path = '.'))
import sys
sys.stdout = open('m3u.m3u', 'w')
m3u_files = []
for each_file in glob.glob('*.{}'.format('m3u')):   m3u_files.append(each_file)
print(m3u_files)
# import any necessary Python libraries
import re
# define the target variable
# open the text file and read its contents
'''for each_data in m3u_files:
    print(open(each_data, 'r'))
    print(open(each_data, 'r').read())
    print("--------------------")'''
for each_data in m3u_files:
    print(open(each_data, 'r'))
    print(open(each_data, 'r').read())
    #open('mm3u2.m3u','x'))    
#    with open('mm3u2.m3u','x') as df:
#        df=(open(mm3u2.m3u,'w'))
#    print(open(each_data, 'w').read())
#    with open(each_data, 'w') as xf:
#        xf=open('mergerm3u.m3u','w')
print("--------------------")
sys.stdout.close()
#import shutil
#import os
 
# path to source directory
#src_dir = 'filew'
 
# path to destination directory
#dest_dir = 'm3umerge.m3u'
 
# getting all the files in the source directory
#files = os.listdir(src_dir)
 
#shutil.copytree(src_dir, dest_dir)


'''for each_data in m3u_files:
    print(open(each_data, 'r'),r_exp = re.compile(target),new_text = r_exp.replace(target, "y")).read()'''
# "xxx" == 0

# for each line in the file
# for line in open(filew):

    # find the pattern "x"
#    pattern_match = re.findall(r"\wx", line)

# replace each occurrence of x with the increasing value of x
# line = re.sub(pattern_match [0], "x = x+1" , line)

# print the modified line
# for each_line
#    print(line)


        
''' for each_data in xml_files:   print(open(each_data, 'r'))   print(open(each_data, 'r').read())       
'''# list to store txt files
res = []
# os.walk() returns subdirectories, file from current directory and 
# And follow next directory from subdirectory list recursively until last directory
# for root, dirs, files in Path.
#    for file in files:'''
'''        if file.endswith(".m3u"):'''
'''            res.append(Path.join(root, file))
print(res)'''

# list to store txt files
res = []
# os.walk() returns subdirectories, file from current directory and 
# And follow next directory from subdirectory list recursively until last directory
'''for root, dirs, files in Path:
    for file in files:
        if file.endswith(".m3u"):
            res.append(os.path.join(root, file))
print(res)'''

'''p = Path(__file__).with('.m3u')
with p.open('r') as f:
    print(f.read())'''

'''import glob

# absolute path to search all text files inside a specific folder
path = r'Path'
files = glob.glob(path, recursive=True)
print(files)'''

'''import glob, os
os.chdir("listify 1")
for file in glob.glob:
    if file.endswith(".m3u"):
        print(file())'''

# import the file to be used as a variable
# import file

# get the contents of the file
# contents = file.read()

# write the contents to the screen
# print(contents)

# close the file
# file.close()
