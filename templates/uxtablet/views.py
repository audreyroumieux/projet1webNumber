import os
import json
from collections import namedtuple
from django.shortcuts import render
import requests
from django.template import context
from requests.auth import HTTPBasicAuth
import printerApi.settings

from django.core.files.storage import FileSystemStorage
from werkzeug.utils import secure_filename

#### TO DECOMMENT WHEN COMMITING
#from uxtablet.firmware.arduino import i2c_arduino

api_uri = "http://localhost:8000/"

def home(request):
    return render(request, 'intro.html')

def connect(request):
    r = requests.get(api_uri+"companies/", auth=HTTPBasicAuth('admin', 'password123'))
    companies = r.json()
    base_url = api_uri + "ux/user/"
    companies_list=[]
    for i in range(0,len(companies)):
        companies_list.append(companies[i]['name'])

    return render(request, 'connect.html', locals())

def companies(request):
    r = requests.get(api_uri+"companies/", auth=HTTPBasicAuth('admin', 'password123'))
    companies = r.json()
    l_company = []
    companies_list = []
    for i in range(0, len(companies)-2, 3):
        companies_list.append([companies[i], companies[i+1],companies[i+2]])

    return render(request, 'team.html', locals())



def insertion_dechet(request, user_id):
    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
            
        fs = FileSystemStorage()
        filename = fs.save('data/'+myfile.name, myfile)
        
        
        prediction = 2 #"Bouchon"
        return render(request, 'insertionDechet.html',  locals())   
    return render(request, 'insertionDechet.html', locals())



def plastic(request, user_id, prediction):
    if prediction == 2:
        pred = 'Bouchon'
    api_url = api_uri
    r = requests.get(api_uri+"plastic-types/", auth=HTTPBasicAuth('admin', 'password123'))
    r_user = requests.get(api_uri+"companies/"+ user_id +'/', auth= HTTPBasicAuth('admin', 'password123'))
    user = r_user.json()
    user_score = user['score']
    request.session['user_score']=user_score

    plastic_types = r.json()
    plastic_types_list = []
    next_url = api_uri+"ux/user/"+ str(user_id)+ "/printsomelove"

    for i in range(0, len(plastic_types), 3):
        plastic_types_list.append([plastic_types[i], plastic_types[i+1], plastic_types[i+2]])
    return render(request, 'plastic.html', locals())

# =============================================================================
# def your_waste(request, user_id, plastic_id):
#     r = requests.get(api_uri+'plastic-types/'+plastic_id, auth=HTTPBasicAuth('admin', 'password123'))
#     waste = r.json()
#     request.session['waste_points']=waste['points']
#     PET = [1]
#     others= [9,7,5,2]
#     pp = [3]
#     ps = [8,6,4]
#     '''
#     if int(plastic_id) in PET:
#         i2c_arduino.write_number(1)
#     if int(plastic_id) in others:
#         i2c_arduino.write_number(2)
#     if int(plastic_id) in pp:
#         i2c_arduino.write_number(3)
#     if int(plastic_id) in ps:
#         i2c_arduino.write_number(4)
#     '''
#     return render(request,'your_waste.html', locals())
# =============================================================================
    
def print_some_love(request, user_id, plastic_id):
    #i2c_arduino.write_number(5)
    #LOADING DATA FROM CONTEXT
    former_score = int(request.session.get('user_score'))
    plastic_points = int(request.session.get('waste_points'))
    user_score = former_score + plastic_points

    #POST REQUESTS
    r_score = requests.post(api_uri + "companies/"+user_id+"/update_score/", data={"score" : user_score}, auth=HTTPBasicAuth('admin', 'password123'))
    r_waste = requests.post(api_uri + "plastic-wastes/", data = {"id_company" : user_id, "id_plastic" : plastic_id}, auth=HTTPBasicAuth('admin', 'password123'))
    #LOADING DATA FOR THE PAGE
    r = requests.get(api_uri+"objects/", auth=HTTPBasicAuth('admin', 'password123'))
    printed_objects = r.json()
    previous_url = api_uri+'ux/user/' + str(user_id) + "/" + str(plastic_id) + "/" + "your_waste"
    objects_list = []
    for i in range(0, len(printed_objects)):
        printed_objects[i]['ratio'] = user_score / printed_objects[i]['points']*100

    for i in range(0, len(printed_objects)-1, 2):
        objects_list.append([printed_objects[i], printed_objects[i+1]])

    #take_picture("image")
    data ={"id_plastic": plastic_id,"id_company":user_id}
    #files = {'photo': open(printerApi.settings.MEDIA_ROOT+'/images/objects/cbb8533e68df9ba15b645071a819aef8_preview_featured.jpg', 'rb')}
    #r = requests.post(api_uri + "plastic-wastes/", data=data, files=files, auth=HTTPBasicAuth('admin', 'password123'))
    #print(r.text)

    return render(request, 'print_some_love.html', locals())

def see_you(request, user_id):
    request.session = []
    return render(request, 'see_you.html')
