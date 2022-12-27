from email.message import EmailMessage
import os

import aiofiles

async def get_paths_in_directory (dir_path:str):
    response = []

    for path in os.listdir(dir_path):
        response.append(f'{dir_path}/{path}')
    return response

async def create_message_with_attachment(from_addr:str, to_addr:str, filepath:str, subject:str = ''):
    split_filename = filepath.split('/')
    filename = split_filename[len(split_filename)-1]

    async with aiofiles.open(filepath, 'rb') as f:
        file = await f.read()
        f.close()

    msg = EmailMessage()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.add_attachment(file, maintype='application', subtype='pdf', filename=filename)

    return msg

async def create_message(from_addr:str, to_addr:str, subject:str = ''):
    msg = EmailMessage()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
 

 
    return msg