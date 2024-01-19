import re
file = open('m3u.m3u' , 'r+')
# print(f.read())
pattern = r'\n'
patternb = r'\n'"xxx"'\n'
with open("m3u.m3u", "r+") as file:
    text = file.read()
    text = re.sub(pattern, patternb, text)
    file.seek(0, 0) # seek to beginning
    file.write(text)
    file.truncate() # get rid of any trailing characters
target = "xxx"
def str_counter(match_object):
    str_counter.count += 1
    return str(str_counter.count)
str_counter.count = 0
with open("m3u.m3u", 'r') as file :
  filedata = file.read()
filedata = re.sub(re.escape(target), str_counter, filedata)
with open("m3u.m3u", 'w') as file:
    file.write(filedata)
with open('m3u.m3u', 'r') as file:
    print(file.read())
# for line in f: 
#     f.write(re.sub(r'\n', ' ', line))
# content = file.read()
# print(content)