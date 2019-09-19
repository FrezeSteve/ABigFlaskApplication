import os
import random
import string

from PIL import Image

from flask import current_app, url_for


def add_profile_pic(pic_upload, username):
    filename = pic_upload.filename
    actual_name = str(username)+"_"+random_string_generator(size=2)
    ext_type = filename.split('.')[-1]
    storage_filename = actual_name+'.'+ext_type
    filepath = os.path.join(current_app.root_path,
                            'static/profile_pics')
    filepath1 = os.path.join(filepath, storage_filename)
    output_size = (200, 200)
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    try:
        pic.save(filepath1)
    except FileNotFoundError:
        try:
            os.mkdir(filepath)
            print("Successfully created the directory %s " % filepath)
            pic.save(filepath1)
        except OSError:
            print("Creation of the directory %s failed" % filepath)
    return storage_filename


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
