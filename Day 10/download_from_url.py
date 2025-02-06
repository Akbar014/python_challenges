

import os
import requests
import shutil
from download_util import download_file

THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)

DOWNLOADS_DIR = os.path.join(BASE_DIR, "downloads")
downloaded_img_path = os.path.join(DOWNLOADS_DIR, '1.jpg')

# os.makedirs(DOWNLOADS_DIR, exist_ok=True)    # this will make downloads directory


url = "https://plus.unsplash.com/premium_photo-1676070096487-32dd955e09e0?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8YnJpZ2h0JTIwZmxvd2Vyc3xlbnwwfHwwfHx8MA%3D%3D.jpg"

# # a smallish item 
# r = requests.get(url, stream=True)
# r.raise_for_status()
# with open(downloaded_img_path, 'wb') as f:
#     f.write(r.content)

 
# dl_filename = os.path.basename(url)
# # print(dl_filename)
# new_dl_path = os.path.join(DOWNLOADS_DIR, dl_filename)
# # print(new_dl_path)
# with requests.get(url, stream=True) as r:
#     with open(new_dl_path, 'wb') as file_obj:
#         shutil.copyfileobj(r.raw, file_obj)


download_file(url, DOWNLOADS_DIR)
