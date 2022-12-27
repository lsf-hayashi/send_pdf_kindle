from email.message import EmailMessage
import os

import aiofiles

async def get_paths_in_directory (dir_path:str):
    directory = os.listdir(dir_path)
    all_paths = list() 

    for path in directory:
        full_path = os.path.join(dir_path, path)
        if os.path.isdir(full_path):
            all_paths = all_paths + await get_paths_in_directory(full_path)
        else:
            all_paths.append(full_path)

    return all_paths

async def create_message_with_attachment(from_addr:str, to_addr:str, filepath:str, subject:str = ''):
    split_filename = filepath.split("\\")
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