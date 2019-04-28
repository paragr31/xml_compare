import xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')
root = tree.getroot()

def parse_tag(tag, xml_data_dict):
    for child in tag:
        if child.attrib:
            if child.text is not None:
                tag_text = "<" + child.tag + ' ' + ' '.join([ attr + '="' + child.get(attr) + '"' for attr in child.attrib ]) + ">" + child.text.rstrip()
            else:
                tag_text = "<" + child.tag + ' ' + ' '.join([ attr + '="' + child.get(attr) + '"' for attr in child.attrib ]) + ">"
        else:
            if child.text is not None:
                tag_text = "<" + child.tag + ">" + child.text.rstrip()
            else:
                tag_text = "<" + child.tag + ">" + child.text.rstrip()
        print tag_text
        xml_data_dict[tag_text] = {}
        parse_tag(child, xml_data_dict[tag_text])

xml_data_dict = {}
for child in root:
    if child.attrib:
        if child.text.rstrip() is not None:
            tag_text = "<" + child.tag + ' ' + ' '.join([ attr + '="' + child.get(attr) + '"' for attr in child.attrib ]) + ">" + child.text.rstrip()
        else:
            tag_text = "<" + child.tag + ' ' + ' '.join([ attr + '="' + child.get(attr) + '"' for attr in child.attrib ]) + ">"
    else:
        if child.text.rstrip() is not None:
            tag_text = "<" + child.tag + ">" + child.text.rstrip()
        else:
            tag_text = "<" + child.tag + ">"
    print tag_text
    xml_data_dict[tag_text] = {}
    parse_tag(child, xml_data_dict[tag_text])

from pprint import pprint
with open("xml_data.txt", "w") as out:
    pprint(xml_data_dict, stream=out)