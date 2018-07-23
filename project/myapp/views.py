from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from myapp.forms import Signup, LoginForm
from myapp.models import Profiles
import urllib.request
import urllib.response
import json
import paho.mqtt.client as mqttClient
import time

#@csrf_exempt
def register(request):
   proj = Signup(request.POST)
   if proj.is_valid():
      proj.save()
      text="Success"
   else:
      text="Fail"
   return HttpResponse(text)

def led(request):
   return render(request, 'led.html', {})

@csrf_exempt
def control1(request):
   def on_log(client, userdata, level, buf):
      print("log: ",buf)

   def on_connect(client, userdata, flags, rc):
 
       if rc == 0:
 
           print("Connected to broker")
 
           global Connected                #Use global variable
           Connected = True                #Signal connection 
 
       else:
 
           print("Connection failed")
 
   Connected = True   #global variable for the state of the connection
 
   broker_address= "m#.cloudmqtt.com"  #Broker address
   port = 00000                         #Broker port
   user = "username"                    #Connection username
   password = "password"            #Connection password

   client = mqttClient.Client("axis")               #create new instance
   client.username_pw_set(user, password=password)    #set username and password
   client.on_connect= on_connect                      #attach function to callback
   #client.on_log=on_log

   client.connect(broker_address, port=port)          #connect to broker
 
   client.loop_start()        #start the loop
 
   while Connected != True:    #Wait for connection
       time.sleep(0.1)

   value1 = 1
   client.publish("axis/led",value1)
   client.disconnect()
   client.loop_stop()
   return HttpResponseRedirect(reverse('data'))

@csrf_exempt
def control0(request):
   def on_log(client, userdata, level, buf):
      print("log: ",buf)

   def on_connect(client, userdata, flags, rc):
 
       if rc == 0:
 
           print("Connected to broker")
 
           global Connected                #Use global variable
           Connected = True                #Signal connection 
 
       else:
 
           print("Connection failed")
 
   Connected = True   #global variable for the state of the connection
 
   broker_address= "m#.cloudmqtt.com"  #Broker address
   port = 00000                         #Broker port
   user = "username"                    #Connection username
   password = "password"            #Connection password

   client = mqttClient.Client("axis")               #create new instance
   client.username_pw_set(user, password=password)    #set username and password
   client.on_connect= on_connect                      #attach function to callback
   #client.on_log=on_log

   client.connect(broker_address, port=port)          #connect to broker
 
   client.loop_start()        #start the loop
 
   while Connected != True:    #Wait for connection
       time.sleep(0.1)

   value1 = 0
   client.publish("axis/led",value1)
   client.disconnect()
   client.loop_stop()
   return HttpResponseRedirect(reverse('data'))

def thermal(request):
   username = request.session['username']
   with urllib.request.urlopen("thingspeak_api_address") as url:
      da = json.loads(url.read().decode())
   
   rh = da["field1"]
   taav = da["field2"]
   
   user_db = Profiles.objects.get(username = username)
   name = user_db.name
   age = user_db.age
   gen = user_db.gender
   ta_m = user_db.ta_m
   va_m = user_db.va_m
   trav = user_db.trav
   velav = user_db.velav
   met = user_db.met
   clo = user_db.clo
   da15_ta = user_db.da15_ta
   da6_ta = user_db.da6_ta
   daav_ta = user_db.daav_ta
   da15_rh = user_db.da15_rh
   da6_rh = user_db.da6_rh
   daav_rh = user_db.daav_rh
   data = {

           "Inputs": {

                   "input1":

                   [

                       {

                               'AGE': age,   

                               'GENDER': gen,   

                               'TA_M': taav,   

                               'VA_M': va_m,   

                               'TAAV': taav,   

                               'TRAV': taav,   

                               'VELAV': velav,   

                               'RH': rh,   

                               'MET': met,   

                               'CLO': clo,   

                               'DA15_TA': da15_ta,   

                               'DA6_TA': da6_ta,   

                               'DAAV_TA': daav_ta,   

                               'DA15_RH': da15_rh,   

                               'DA6_RH': da6_rh,   

                               'DAAV_RH': rh,   

                       }

                   ],

           },

       "GlobalParameters":  {

       }

   }

   body = str.encode(json.dumps(data))
    
   url = '' #URL for accessing azure model.
   api_key = '' # Replace this with the API key for the web service
   headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    
   req = urllib.request.Request(url, body, headers) 
   response = urllib.request.urlopen(req)
    
        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
   result = response.read()

   res = result.decode()
   res = res[-6]
   
   if res == "0":
      con = "Too cool"
   elif res == "1":
      con = "Comfortable"
   elif res == "2":
      con = "Too warm"
   
   if res == "0":
      c = 1
   elif res == "1":
      c = 0
   elif res == "2":
      c = 1
   
   def on_log(client, userdata, level, buf):
      print("log: ",buf)

   def on_connect(client, userdata, flags, rc):
 
       if rc == 0:
 
           print("Connected to broker")
 
           global Connected                #Use global variable
           Connected = True                #Signal connection 
 
       else:
 
           print("Connection failed")
 
   Connected = True   #global variable for the state of the connection
 
   broker_address= "m13.cloudmqtt.com"  #Broker address
   port = 14479                         #Broker port
   user = "fmoanlpo"                    #Connection username
   password = "tS___U8MWTRS"            #Connection password

   client = mqttClient.Client("axis")               #create new instance
   client.username_pw_set(user, password=password)    #set username and password
   client.on_connect= on_connect                      #attach function to callback
   #client.on_log=on_log

   client.connect(broker_address, port=port)          #connect to broker
 
   client.loop_start()        #start the loop
 
   while Connected != True:    #Wait for connection
       time.sleep(0.1)

   value = c
   client.publish("axis/control",value)
   client.disconnect()
   client.loop_stop()
   #return HttpResponse(res)
   return render(request, 'loggedin.html', {"username" : name, "age" : age, "gender": gen,"taav" : taav, "rh" : rh, "ta_m" : taav, "va_m" : va_m, "trav" : taav, "velav" : va_m, "met" : met, "clo" : clo, "da15_ta" : da15_ta, "da6_ta" : da6_ta, "daav_ta" : daav_ta, "da15_rh" : da15_rh, "da6_rh" : da6_rh, "daav_rh": daav_rh, "con" : con})


@csrf_exempt
def login(request):
   username = "not logged in"
   
   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['user']
         request.session['username'] = username
         
   else:
      MyLoginForm = Loginform()
		
   #return render(request, 'loggedin.html', {"username" : username})
   return HttpResponseRedirect(reverse('data'))

def formView(request):
   if request.session.has_key('username'):
      username = request.session['username']
      #return render(request, 'loggedin.html', {"username" : username})
      return HttpResponseRedirect(reverse('data'))
   else:
      return render(request, 'user', {})

@csrf_exempt
def logout(request):
   try:
      del request.session['username']
   except:
      pass
   return HttpResponse("<strong>You are logged out.</strong>")



   
      
      
  
