import os
import time

import asyncio

from ultis import *
from server import Server

username = os.environ['USERNAME']
password = os.environ['PASSWORD']

server = Server(username=username, password=password)

async def send_attachment(from_addr:str, to_addr:str, filepath:str, subject:str = ''):
    start_time = time.perf_counter()
    print(f'Start sedding file: {filepath}')

    msg = await create_message_with_attachment(from_addr, to_addr, filepath)
    await server.send(msg)
    os.remove(filepath)
    
    done_time = time.perf_counter() - start_time
    print(f'Done sedding file:{filepath} - Executed in {done_time:0.2f} seconds.')

async def main ():
    to_addr = os.environ['KINDLE']
    dir_path = 'F:\Mangas'

    files_paths = await get_paths_in_directory(dir_path)  

    await asyncio.gather(*(send_attachment(
        from_addr=username, 
        to_addr=to_addr, 
        filepath=path) 
        for path in files_paths))

    print('Finish Sedding')

if __name__ == '__main__':
    s = time.perf_counter()

    asyncio.run(main())

    elapsed = time.perf_counter() - s
    print(f'{__file__} executed in {elapsed:0.2f} seconds.')