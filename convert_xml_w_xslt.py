import lxml.etree as ET
import os

xml_file = r"C:\PARAG\PythonProgramms\Python_Xml_Compare\test.xml"
print os.path.dirname(xml_file)

logdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\logs"

if not os.path.isdir(logdir):
    os.makedirs(logdir)
xsl_filename = r"C:\PARAG\PythonProgramms\Python_Xml_Compare\libs\xml_sort_ss.xslt"

dom = ET.parse(xml_file)
xslt = ET.parse(xsl_filename)
transform = ET.XSLT(xslt)
newdom = transform(dom)
print(ET.tostring(newdom, pretty_print=True))


