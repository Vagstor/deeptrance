from openai import OpenAI
from config import Settings
import zipfile
from lxml import etree

ns = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
}

def create_ds_client() -> OpenAI:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=Settings.TOKEN,)  # See config.py for instructions
    return client

def send_request(client, input_string):
    completion = client.chat.completions.create(
    model="deepseek/deepseek-chat-v3-0324:free",
    messages=[
        {
        "role": "user",
        "content": input_string
        }],
    temperature = 1.3)
    return completion
    
'''def parse_docx_xml(docx_path):

    with zipfile.ZipFile(docx_path) as z:
        with z.open('word/document.xml') as f:
            xml_content = f.read()

    parser = etree.XMLParser(remove_blank_text=True)
    return etree.fromstring(xml_content, parser)

def translate_text(element):
    for t in element.xpath('.//w:t', namespaces=ns):
        if t.text and t.text.strip():
            # Здесь должен быть ваш переводчик
            t.text = t.text.upper()  # Пример: преобразование в верхний регистр

for paragraph in root.xpath('//w:p', namespaces=ns):
    translate_text(paragraph)'''


# def paste_into_client()