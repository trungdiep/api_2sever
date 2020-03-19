from datetime import timedelta
import time
import requests

# from .models import Student

def api_order_home_success(hoten='trung',tuoi='20',gioitinh='nam'):
    # data_payment = Student.objects.get(name=ten_sv)

    url= 'http://127.0.0.1:4000/'+"student/"
    print(url)
    json_data={
        "hoten":hoten,
        "tuoi":tuoi,
        "gioitinh":gioitinh,
        }
    r = requests.post( url, json=json_data)
    print(url)
    return r.status_code


