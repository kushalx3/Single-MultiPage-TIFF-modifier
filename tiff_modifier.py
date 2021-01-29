import os
from PIL import Image
from PIL import ImageSequence
from PIL import TiffImagePlugin

setdpi=(300,300)
dimensions=(1200,1552)
FILELIST=os.listdir('original')

for FINPUT in FILELIST:
    print ('Resizing '+str(FINPUT)+' ...')
    pages = []
    imagehandler = Image.open('original\\'+str(FINPUT))
    for page in ImageSequence.Iterator(imagehandler):
        new_size = dimensions
        page = page.resize(new_size, Image.ANTIALIAS)
        pages.append(page)
    print ('Writing '+str(FINPUT)+' ...')
    with TiffImagePlugin.AppendingTiffWriter('converted\\'+FINPUT) as tf:
        for page in pages:
            page.save(tf, compression="tiff_lzw", dpi=setdpi)
            tf.newFrame()
