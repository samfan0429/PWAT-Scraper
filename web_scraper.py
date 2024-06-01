import requests
from bs4 import BeautifulSoup
from PIL import Image
import urllib
import os
import shutil
import time

def createFolders(i):
    path = os.path.join(os.getcwd(), 'shiranai')
    title = ("KonKaisha"+str(i))
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)
    path = os.path.join(path,title)
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)
    return path

# out_file = open('kakao.tsv', 'w',-1,'utf-8')
# out_file.write('Title\t Company\t Date\n')

urlPrefix = 'https://ww2.mangakakalot.tv/chapter/manga-cs979627/chapter-'

# scraper = cloudscraper.create_scraper(
#     browser={
#         'browser': 'firefox',
#         'platform': 'windows',
#         'mobile': False
#     }
# )

for i in range(15,28):
    
    path = createFolders(i)

    url = urlPrefix

    url+=str(i)

    raw = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = BeautifulSoup(raw.text, "html.parser")
    imgBlocks = html.find('div', attrs={'class':'vung-doc'})


    # # print(imgBlocks)

    # imgs = imgBlocks.find_all('img')
    # # print(imgs)

    # counter = 0

    # print(articles)
    # for img in imgs:
        # print(img)
    #     if counter > 1:
    #         break
    #     counter+=1
        # img = block.find_all('img')
        # img_url = img['data-src']
    #     if img_url == 'https://1.bp.blogspot.com/-5BA_VRlvmYI/XysC9uHMhRI/AAAAAAAAABw/k8EhkeLqpCsMODg4tQYHAa2sJmqGrEaAQCNcBGAsYHQ/s0/l13.jpg':
    #         img_url=img.get('data-src')
        
        # print(img_url)

        # print(img_url)
        # print(os.path.join(path,str(counter)+'.jpg'))
        # r = requests.get(img_url, stream=True)
        # print(r)
        # if r.status_code == 200:                     #200 status code = OK
        #     with open("images/book1.jpg", 'wb') as f: 
        #         r.raw.decode_content = True
        #         shutil.copyfileobj(r.raw, f)

        # image = Image.open(bytes)
        # image.save(os.path.join(path,str(counter)+'.jpeg'))
        # file = open(os.path.join(path,str(counter)+'.jpg'),'wb')
        # r.raw.decode_content = True
        # shutil.copyfileobj(r.raw, file)
        # img.save(os.path.join(path+str(counter)+'.jpg'))
        # counter+=1
        # print(counter)