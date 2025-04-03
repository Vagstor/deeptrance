from docx import Document
from lxml import etree
import zipfile

ns = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
}

'''document = Document()
document.save('trance.docx')'''

'''tree = ET.parse('document.xml')
root = tree.getroot()
for text in root.findall('w:t'):
    print(text.text)'''

def parse_docx_xml(docx_path):

    with zipfile.ZipFile(docx_path) as z:
        with z.open('word/document.xml') as f:
            xml_content = f.read()

    parser = etree.XMLParser(remove_blank_text=True)
    return etree.fromstring(xml_content, parser)

root = parse_docx_xml('orig/cnc8_070 ошибки.docx')

for paragraph in root.xpath('//w:p', namespaces=ns):
    for run in paragraph.xpath('.//w:r', namespaces=ns):
        text_nodes = run.xpath('.//w:t', namespaces=ns)
        for t in text_nodes:
            if t.text:
                print(t.text)

