from PIL import Image
import os
import numpy as np
import pathlib


def ImgResConv(mainFolder, resFolder):
    
    dir_path = pathlib.Path.cwd()
    dir_path = str(dir_path)
    sMainPath = dir_path + '\\' + mainFolder #'\\test1'
    sNewPath = dir_path + '\\' + resFolder #'\\Training'
    nameDrags = np.array(os.listdir(sMainPath))
    print(nameDrags)
    # for i in nameDrags:
    #     FolderName = sMainPath + "\\" + str(i)
    #     print(FolderName)
    #     input()
    #     nameInDrags = np.array(os.listdir(FolderName))
    #     for j in nameInDrags:
    #         path2 = FolderName + "\\" + j
    #         FolderBadOrGood = np.array(os.listdir(path2))
    #         for BadOrGood in FolderBadOrGood:
    #             FilesInDrags = path2 + "\\" + BadOrGood
    #             files = np.array(os.listdir(FilesInDrags))
    #             Count = 1
    #             for z in files:
    #                 full_name = os.path.basename(z)
    #                 extenstion = os.path.splitext(full_name)[1]
    #                 print(sNewPath + "\\" + i + "\\"  + j + "\\"  + BadOrGood + "\\"  + str(Count) + extenstion)
    #                 img = Image.open(FilesInDrags + "\\" + z)
    #                 img = img.resize((300, 300))
    #                 img = img.convert("L")
    #                 img.save(sNewPath + "\\" + i + "\\"  + j + "\\"  + BadOrGood + "\\"  + str(Count) + extenstion)
    #                 Count+=1


    
    for i in nameDrags:
        FolderName = sMainPath + "\\" + str(i)
        #print(FolderName)
        #input()
        nameInDrags = np.array(os.listdir(FolderName))
        Count = 1
        for z in nameInDrags:
            full_name = os.path.basename(z)
            extenstion = os.path.splitext(full_name)[1]
            img = Image.open(sMainPath + "\\" + i + "\\" + z)
            img = img.resize((300, 300))
            img = img.convert("L")
            img.save(sNewPath + "\\" + i + "\\" + str(Count) + extenstion)
            Count+=1
            print(sNewPath + "\\" + i + "\\" + str(Count) + extenstion)
    print("Готово!")

# Директории оригинала и результата должны находиться в одной папке с скриптом
ImgResConv("Black and white", "Black and white2")

#%%
