from PIL import Image
import pytesseract
from bottle import route, run, template, request
from thismysql import getGlossory, getRandomWord
import json, base64


delimiter=", "

@route('/hello/<name>')
def index(name):
    meanings=getGlossory(name)
    string=[]
    
    for meaning in meanings:            
        string.append('{ type: "%s", meaning: "%s" }' % (meaning[1], meaning[2].replace('"', '\\"' )))
        
    result= '[ %s ]'% delimiter.join(string)
    return json.dumps(result, separators=(',',':'))#template('<b>{{name}} <br></b>!', name=meanings)

@route('/trans', method='POST')
def dec():
    img= request.forms.get('img')
    fh = open("/tmp/imageToSave.jpg", "wb")
    fh.write(base64.decodestring(img))
    fh.close()
    data=pytesseract.image_to_string(Image.open('/tmp/imageToSave.jpg'))
    
    articleList = []
    articleList.append(img)     
    # return json.dumps([1,2,3,{'4': 5, '6': 7}], separators=(',',':'))
    
    
    words=[]
    words=data.split(' ')
    string=[]
    for word in words:
        string.append('{\"word\":\"%s\"}' % word)
    result= '[%s]'% delimiter.join(string)

    return result


@route('/words_meaning', method="POST")
def wordsMening():
    word=request.forms.get('word')
    #word='test'
    meanings=getGlossory(word)
    string=''
    for meaning in meanings:            
        string='''%s
        (%s) %s''' % (string,meaning[1],meaning[2])
    return string






@route('/word_meaning', method="POST")
def wordMening():
    word=request.forms.get('word')
    #word='test'
    meanings=getGlossory(word)
    string=[]
    
    delimiter=", "
    for meaning in meanings:            
        string.append('{\"type\": \"%s\",\"meaning\": \"%s\",\"similar\":\"%s\",\"antonym\":\"%s\",\"seealso\":\"%s\"},' % (meaning[1], meaning[2].replace('"', '\\"' ),meaning[3],meaning[4],meaning[5]))
        
   
    return string    
    


@route('/random')
def randomWord():
    #word=request.forms.get('word')
    #word='test'
    
    return getRandomWord()
        
   
    





run(host='0.0.0.0', port=8080, reloader=True)
 
