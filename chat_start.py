from openai import OpenAI
from config import Settings
import utils

client = utils.create_ds_client()
cont, linecount = 'y', 0

with open('orig.txt', 'r', encoding='utf-8') as original_file:
    message = utils.read_prompt()
    for line in original_file:
        #if linecount < 4:
          message.append({"role": "user", "content": line})
          #linecount = linecount + 1
        #else:
    completion = utils.send_request(client, message)
    with open('translation.txt', 'a', encoding='utf-8') as file:
      file.write(completion.choices[0].message.content + '\n')
      #linecount, message = 0, utils.read_prompt()
    
    #cont = input('Продолжить работу?')