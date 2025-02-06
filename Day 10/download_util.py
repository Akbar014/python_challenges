
import os
import requests
import shutil


# without fname 
# def download_file(url, directory):
#     dl_filename = os.path.basename(url)
#     # print(dl_filename)
#     new_dl_path = os.path.join(directory, dl_filename)
#     # print(new_dl_path)
#     with requests.get(url, stream=True) as r:
#         with open(new_dl_path, 'wb') as file_obj:
#             shutil.copyfileobj(r.raw, file_obj)
#     return new_dl_path


def download_file(url, directory, fname=None):
    if fname == None:
        fname = os.path.basename(url)
    # print(dl_filename)
    dl_path = os.path.join(directory, fname)
    # print(new_dl_path)
    with requests.get(url, stream=True) as r:
        with open(dl_path, 'wb') as file_obj:
            shutil.copyfileobj(r.raw, file_obj)
    return dl_path



def download_file_slower(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush()
    return local_filename