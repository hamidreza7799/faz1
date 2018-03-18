from contextlib import closing, contextmanager 

import os, sys, traceback

import os.path

import json

from PIL import Image

path_exists = os.path.exists

normalize_path = os.path.normpath

absolute_path = os.path.abspath 

split_path = os.path.split

split_ext = os.path.splitext

encode_json = json.JSONEncoder().encode

def encodeURLsafeBase64(data):
    
    today = date.today
    
    return base64.urlsafe_b64encode(data).replace('=','').replace(r'\x0A','')

def image(*args):
    
    raise NotImplementedError 

class Filemanager:
    
    def __init__(self, fileroot= '/'):

        self.fileroot = fileroot

        self.patherror = encode_json(

                {

                    'Error' : 'No permission',

                    'Code' : -1

                }

            )
        def isvalidrequest(self, **kwargs):

            assert split_path(kwargs['path'])[0]==self.fileroot

            assert not kwargs['req'] is None

        def getinfo(self, path=None, getsize=True, req=None):
            
            if not self.isvalidrequest(path,req):
                
                return (self.patherror, None, 'application/json')
            thefile = {

            'Filename' : split_path(path)[-1],

            'File Type' : '',
            
            'Preview' : path if os.path.split(path)[-1] else 'images/fileicons/_Open.png',
            
            'Path' : path,
            
            'Error' : '',

            'Code' : 0,

            'Properties' : {

                    'Date Created' : '',

                    'Date Modified' : '',

                    'Width' : '',

                    'Height' : '',

                    'Size' : ''

                }

            }
            
            imagetypes = set(('gif','jpg','jpeg','png'))
            
            if not path_exists(path):
                
                thefile['Error'] = 'File does not exist.'
                
                return (encode_json(thefile), None, 'application/json')
            
            if split_path(path)[-1]=='/':
                
                thefile['File Type'] = 'Directory'
                
            else:
                
                thefile['File Type'] = split_ext(path)
                
            if ext in imagetypes:
                
                img = Image(path).size()
                
                thefile['Properties']['Width'] = img[0]
                
                thefile['Properties']['Height'] = img[1]
            else:
                
                previewPath = 'images/fileicons/' + ext.upper + '.png'
                
                thefile['Preview'] = previewPath if path_exists('../../' + previewPath) else 'images/fileicons/default.png'
                
            thefile['Properties']['Date Created'] = os.path.getctime(path)
            
            thefile['Properties']['Date Modified'] = os.path.getmtime(path)
            
            thefile['Properties']['Size'] = os.path.getsize(path)
            
            req.content_type('application/json')
            
            req.write(encode_json(thefile))

    def getfolder(self, path=None, getsizes=True, req=None):
        
        if not self.isvalidrequest(path,req):
            
            return (self.patherror, None, 'application/json')

        result = []         

        filtlist = file_listdirectory(path)

        for i in filelist:

             if i[0]=='.':

                result += literal(self.getinfo(path + i, getsize=getsizes))

        req.content_type('application/json')

        req.write(encode_json(result))

    def rename(self, old=None, new=None, req=None):

        if not self.isvalidrequest(path=new,req=req):

            return (self.patherror, None, 'application/json')

        if old[-1]=='/':

            old=old[:-1]

        oldname = split_path(path)[-1]

        path = string(old)

        path = split_path(path)[0]

        if not path[-1]=='/':

            path += '/'

        newname = encode_urlpath(new)

        newpath = path + newname

        os.path.rename(old, newpath)

        result = {

            'Old Path' : old,

            'Old Name' : oldname,

            'New Path' : newpath,

            'New Name' : newname,

            'Error' : 'error' 

        }

        req.content_type('application/json')

        req.write(encode_json(result))

    def delete(self, path=None, req=None):

        if not self.isvalidrequest(path,req):

            return (self.patherror, None, 'application/json')

        os.path.remove(path)

        result = {

            'Path' : path,

            'Error' : 'error' 

        }

        req.content_type('application/json')

        req.write(encode_json(result))

    def add(self, path=None, req=None):     

        if not self.isvalidrequest(path,req):

            return (self.patherror, None, 'application/json')

        try:

            thefile = util.FieldStorage(req)['file']          

            newName = thefile.filename

            with open(newName, 'rb') as f:

                            f.write(thefile.value) 

        except:

            result = {

                'Path' : path,

                'Name' : newName,

                'Error' : file_currenterror

            }

        else:

            result = {

                'Path' : path,

                'Name' : newName,

                'Error' : 'No file was uploaded.'

            }

        req.content_type('text/html')

        req.write(('<textarea>' + encode_json(result) + '</textarea>'))

    def addfolder(self, path, name):        

        if not self.isvalidrequest(path,req):

            return (self.patherror, None, 'application/json')

        newName = encode_urlpath(name)

        newPath = path + newName + '/'

        if not path_exists(newPath):

            try:

                os.mkdir(newPath)

            except:

                result = {

                    'Path' : path,

                    'Name' : newName,

                    'Error' : 'error'

                }
 

    def download(self, path=None, req=None):

        if not self.isvalidrequest(path,req):

            return (self.patherror, None, 'application/json')

        name = path.split('/')[-1]

        req.content_type('application/x-download')
        
        myFilemanager = Filemanager(fileroot='/var/www/html/dev/fmtest/UserFiles/')

def handler(req):

    if req.method == 'POST':

        kwargs = parse_qs(req.read())
                
    elif req.method == 'GET':
            
        kwargs = parse_qs(req.args)
                
    try:

        method=str(kwargs['mode'][0])
                
        methodKWargs=kwargs.remove('mode')
                
        methodKWargs['req']=req
                
        myFilemanager.__dict__['method'](**methodKWargs)

        return apache.OK

    except KeyError:

        return apache.HTTP_BAD_REQUEST
            
    except Exception  (errno, strerror):

        apache.log_error(strerror, apache.APLOG_CRIT)

        return apache.HTTP_INTERNAL_SERVER_ERROR

