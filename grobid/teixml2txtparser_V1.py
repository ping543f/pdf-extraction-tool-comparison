import xml.etree.ElementTree as et
import re 
import os
### Multiple file processing , all files from a folder

path = 'test-tei/'
files = []
# r = root, d = directories, f = files
for r,d, f in os.walk(path):
    for file in f:
        if '.xml' in file:
            files.append(file)

# filename = path+filename

def xml2txt(filename):
    filenamef = path+filename
    f = open(filenamef, "r",encoding="utf-8")
    data_writer = open("output_text/grobid_"+filename+".txt","w+",encoding="utf-8")
    final_string= ""

    data = f.read()
    data = data.split("</ref>")

    for item in data:
        item = re.sub("<ref.*>","",item)
        # item = re.sub("/ref>","",item)
        item = re.sub("<figure.*>.*</figure>","",item)
        item = re.sub("<note.*>.*</note>","",item)
        final_string+=item

    data = final_string


    root = et.fromstring(data)
    data_writer.write(str(root[0][0][0][0].text)+"\n")
    data_writer.write(str(root[0][0][2][0][2].text)+"\n")
    data_writer.write(str(root[0][2][1][0][0].text)+"\n")

    # print(root[0][0][0][0].text)
    # print(root[0][0][2][0][2].text)
    # print(root[0][2][1][0][0].text)

    for item in root[1][0]:
        for item2 in item:
            data_writer.write(str(item2.text)+"\n")
            # print(item2.text)
        # data_writer.write("\n")
    print(filename, "Processed!\n")
    f.close()
    data_writer.close()


for file in files:
    xml2txt(file)

