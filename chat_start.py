from openai import OpenAI
from config import Settings
import utils

client = utils.create_ds_client()
cont = 'y'

while cont == 'y':
    completion = utils.send_request(client, input('Введите сообщение: '))
    
    with open('translation.txt', 'a', encoding='utf-8') as file:
      file.write(completion.choices[0].message.content)
    
    cont = input('Продолжить работу?')