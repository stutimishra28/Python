import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)   

def move(files,folder):
    for file in files:
        os.replace(file, f"{folder}/{file}")

if __name__ == "__main__":
    files=os.listdir()  
    files.remove('main.py')
    #print(files)

    createIfNotExist('Images')
    createIfNotExist('Docs')
    createIfNotExist('Media')
    createIfNotExist('Others')


    imgExt=[".jpg",".jpeg",".png"]
    images=[file for file in files if os.path.splitext(file)[1].lower() in imgExt]
    #print(images)

    docsExt=[".docx",".txt"]
    docs=[file for file in files if os.path.splitext(file)[1].lower() in docsExt]
    #print(docs)

    mediaExt=[".mp4",".mp3"]
    medias=[file for file in files if os.path.splitext(file)[1].lower() in mediaExt]
    #print(medias)

    others=[]
    for file in files:
        ext=os.path.splitext(file)[1].lower()
        if (ext not in imgExt) and (ext not in docsExt) and (ext not in mediaExt) and os.path.isfile(file):
            others.append(file)
    #print(others) 
           
    '''        
    for image in images:
        os.replace(image, f"Images/{image}")   
    '''
    move(images,'Images')
    move(medias,'Media')
    move(docs,'Docs')
    move(others,'Others')
    print("Your clutter is successfully cleared")