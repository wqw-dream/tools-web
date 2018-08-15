import html
from bottle import route, run, template, get, post, request

#def talk_to_ckv(tag_type, tag_data):
#    cmod = 122345
#    bmod = 12345
#    bid = 9999
#    
#    if tag_type == '':
#        cmod = 12345
#    elif tag_type == '':
#        cmod = aaa;
#    elif tag_type == '':
#        cmod = 000
    

@route('/ckvtags')
def ckv_tags():
    return  html.index_html

@route('/ckvtags', method='POST')
def fetch_tags():
    tag_type = request.forms.get('TagType')
    tag_data = request.forms.get('TagData')
    
    if tag_type not in ('qq', 'wuid', 'imei'):
        return ("<p>type=%s is error!</p>" % tag_type)

    
    res_str = """ResData:<input type="textarea" name="input" value="%s %s %s" readonly>""" % (tag_data, tag_data, tag_data)
    return res_str

run(host='192.168.0.210', port=8888)
