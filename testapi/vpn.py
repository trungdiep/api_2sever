import hashlib
import urllib
import urllib.parse
from django.utils.http import urlencode
from django.conf import settings
import requests
SECRET_KEY_API = 'abc123456'

def __md5(input):
    byteInput = input.encode('utf-8')
    return hashlib.sha256(byteInput).hexdigest()
data = {'csrfmiddlewaretoken': 'rK9AAwy9NZWdtQ7oFrRPSnBqYjkIBElbqjLsARYukLLSoZIPOPAXTOZ3oHSyUOlw', 'hoten': 'nguyen van a', 'tuoi': '23', 'gioitinh': 'nam'}
def get_student_url(validated_data):
    # print(validated_data.items())
    queryString = ''
    hasData = ''
    seq = 0
    for key, val in validated_data.items():
            if 'csrf' in key and val:
                pass
            else:
                if seq == 1:
                    queryString = queryString + "&" + key + '=' + urllib.parse.quote(str(val), safe='')
                    
                    # print('ham quote=', queryString)
                    hasData = hasData + "&" + str(key) + '=' + str(val)
                else:
                    seq = 1
                    queryString = key + '=' + urllib.parse.quote(str(val), safe='')
                    hasData = str(key) + '=' + str(val)
    hashValue = __md5(SECRET_KEY_API + hasData)
    return 'http://127.0.0.1:4000/student/' + "?" + queryString + '&vnp_SecureHashType=SHA256&vnp_SecureHash=' + hashValue


def request_get(url):
    r = requests.get(url)
    return r.status_code


url = get_student_url(data)

# print(request_get(url))