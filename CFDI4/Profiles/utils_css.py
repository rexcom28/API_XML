import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from Config.models import CSSConf
import mmap



def openRep(request, nfile,oldStr, newStr,color=False):
    with open(nfile, 'r') as cssFile:
        data = cssFile.read()
    if not color:
        data = data.replace(oldStr, os.path.join(request.build_absolute_uri(),newStr))
    else:
        data = data.replace(oldStr, newStr)


    with open(nfile, 'w') as newcssFile:
        newcssFile.write(data)
    
def manageStorageCSS(request, instance):
    
    
    try:
        ruta= ['Profiles','assets','css','templatemo-style.css']    
        ruta2 = ['Profiles','assets','css',f'{request.user.username}.css']
        global xfile 
        global nfile
        global myfile
        xfile  = settings.STATICFILES_DIRS[0]
        nfile  = settings.STATICFILES_DIRS[0]
        store  = FileSystemStorage(location=settings.STATICFILES_DIRS[0])
        for i in ruta:
            xfile = os.path.join(xfile, i)
        for i in ruta2:
            nfile = os.path.join(nfile,i)
        
        if not store.exists(nfile):
            content = store.open(xfile)        
            store.save(nfile,content=content)
            content.close()
        else:
        
            store.delete(nfile)
            content = store.open(xfile)
            store.save(nfile,content=content)
            content.close()
        
        fondoReplace = '../images/page-bg.jpg'
        backgrounColorReplace = 'a43f49'
        
        
        strFondo = str(instance.fondo.url)
        newback = str(instance.backColor)

        openRep(request, nfile,fondoReplace, strFondo)
        openRep(request, nfile,backgrounColorReplace, newback,True)
    except:
        pass
    # image = CSSConf.objects.first()
    # #check if user already have his own cssFiles
    # if not store.exists(nfile):
    #     content = store.open(xfile)
    #     store.save( nfile,content=content)
    #     content.close()
    #     replaceSTR = '../images/page-bg.jpg'
    # else:       
        
    #     replaceSTR = image.fondo.url

    # with open(nfile, 'r') as cssFile:
    #     data = cssFile.read()
    # data = data.replace(replaceSTR, os.path.join(request.build_absolute_uri(),image.fondo.url))

    # with open(nfile, 'w') as newcssFile:
    #     newcssFile.write(data)


        
        