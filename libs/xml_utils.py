import lxml.etree as ET
import os
from xmldiff import main, formatting


class HTMLFormatter(formatting.XMLFormatter):

    def __init__(self):
        self.html_xslt = os.path.dirname(os.path.abspath(__file__)) + "\\htmlformatter.xslt"
        self.text_tags = ('p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li')
        self.formatting_tags = ('b', 'u', 'i', 'strike', 'em', 'super', 'sup', 'sub', 'link', 'a', 'span')
        super(HTMLFormatter, self).__init__(text_tags=self.text_tags, formatting_tags=self.formatting_tags)

    def render(self, result):
        html_xslt_text = ET.parse(self.html_xslt)
        transform = ET.XSLT(html_xslt_text)
        result = transform(result)
        return super(HTMLFormatter, self).render(result)


class XmlUtils(object):
    def __init__(self):
        self.sort_xslt = os.path.dirname(os.path.abspath(__file__)) + "\\xml_sort_ss.xslt"

    def write_to_file(self, content, filename):
        with open(filename, "w") as out:
            out.write(content)

    def sort_xml(self, xml_file):
        file_base_name = os.path.splitext(os.path.basename(xml_file))[0]
        sorted_xml_file = os.path.dirname(xml_file) + "\\" + file_base_name + "_sorted.xml"
        dom = ET.parse(xml_file)
        xslt = ET.parse(self.sort_xslt)
        transform = ET.XSLT(xslt)
        new_dom = transform(dom)
        self.write_to_file(ET.tostring(new_dom, pretty_print=True), sorted_xml_file)
        return sorted_xml_file

    def compare_xml_files(self, old_xml, new_xml):
        old_sorted_xml = self.sort_xml(old_xml)
        new_sorted_xml = self.sort_xml(new_xml)

        xml_diff = main.diff_files(old_sorted_xml, new_sorted_xml, formatter=HTMLFormatter())
        logs_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\logs"

        if not os.path.isdir(logs_dir):
            os.makedirs(logs_dir)

        diff_filename = logs_dir + "\\" + os.path.splitext(os.path.basename(old_xml))[0] + "__" + os.path.splitext(os.path.basename(new_xml))[0] + ".html"
        self.write_to_file(xml_diff, diff_filename)

        return diff_filename
