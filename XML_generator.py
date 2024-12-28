import xml.etree.ElementTree as ET
import json
import pandas as pd

with open('probe_dataset/probe_labels.json', 'r') as file:
    data = json.load(file)

annotations = pd.DataFrame(data['annotations'])
annotations.set_index('image_id', inplace=True)

images_info = pd.DataFrame(data['images'])

def boundary_box(image_info):
    return annotations.loc[image_info.loc['id']]

for _, image in images_info.iterrows():
    file_name = image.loc['file_name']
    root = ET.Element('annotation')
    filename = ET.SubElement(root, 'filename')
    filename.text = file_name
    size = ET.SubElement(root, 'size')
    width = ET.SubElement(size, 'width')
    width.text = str(image.loc['width'])
    height = ET.SubElement(size, 'height')
    height.text =  str(image.loc['height'])
    object = ET.SubElement(root, 'object')
    name = ET.SubElement(object, 'name')
    name.text = 'probe'
    bndbox = ET.SubElement(object, 'bndbox')
    bbox = boundary_box(image).loc['bbox']
    xmin = ET.SubElement(bndbox, 'xmin')
    xmin.text =  str(bbox[0])
    ymin = ET.SubElement(bndbox, 'ymin')
    ymin.text =  str(bbox[1])
    xmax = ET.SubElement(bndbox, 'xmax')
    xmax.text =  str(bbox[0] + bbox[2])
    ymax = ET.SubElement(bndbox, 'ymax')
    ymax.text =  str(bbox[1] + bbox[3])
    print(bbox, xmin.text, ymin.text, xmax.text, ymax.text)
    tree = ET.ElementTree(root)
    tree.write('probe_dataset/probe_annotations/' + file_name.split('.')[0] + '.xml')