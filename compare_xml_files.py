from libs.xml_utils import XmlUtils

old_xml = r"C:\PARAG\PythonProgramms\Python_Xml_Compare\xml_compare\test_old.xml"
new_xml = r"C:\PARAG\PythonProgramms\Python_Xml_Compare\xml_compare\test_new.xml"

obj = XmlUtils()
xml_diff_file = obj.compare_xml_files(old_xml, new_xml)
print("xml difference file is ", xml_diff_file)
