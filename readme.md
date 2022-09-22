

About Ace:
===
#### Installation Setup
###### Prerequisite: Python version >=3.6
###### Note: I have used postgreSQL but application will work with any relational DB (need to change settings.py)
###### Follow This Step:
1. Create Account on  Google Cloud Platform 
2. Follow this step to setup Account [GCP](https://cloud.google.com/translate/docs/setup#windows "GCP Machine Translation").
3. Create Virtual Environment.
4. Activate Vurtual Environment 
5. Install required packages: pip install -r requirements.txt
6. Create Django Project : django-admin startproject <Ace>
8. Create Super User : python manage.py createsuperuser
6. Create APP: python manage.py startapp <CoreApp>

---


## About App:

---

### Problem Statement:
1. Task is to develop a web application that helps us convert farmer details from English to
different languages.
2. To do this, we will use of Google Translate API.
3. User Should able to retrieve information in all supported langauges 

--- 

### Solution Flow:

![Solution_Flow](https://user-images.githubusercontent.com/49105701/191795133-9af00939-db18-4ed6-ab7e-874201269488.png)


### Assumption and Approach:

- [x]  User need to Sign In on to application. (need to create account)
- [x]  Application supports only 4 languages apart from English viz. Hindi, Marathi, Telugu and Punjabi.
- [x]  Application support Excel (.xlsx) and CSV (.csv) file.
- [x]  User will upload file where 6 columns are mandatory (FirstName, LastName, StateName, DistrictName, VillageName, Phone)
- [x]  Once user upload file application will Convert all information in all supported languages.
- [x]  Application will store all information in all supported languages in DB (postgre) 
- [x]  User can also View Information in all supported languages on to UI itself.
- [x]  Apart from this, we have also exposed two API endpoints to fetch all information:
- [x]  getAllFarmerinfo() : http://127.0.0.1:8000/api/get-allfarmer-info/<language_code>/ : Fetch all Information in language Specified.
- [x]  GET: getFarmerinfo_ID() :  http://127.0.0.1:8000/api/get-allfarmer-info/<id>/<language_code>/ : Fetch Infromation based on ID.
- [x]  For Api Authentication we are using DRF (Django Rest Framework) in built Token Based Authentication.
- [x]  For Api Doc We have Used Swagger-UI (for DRF)
- [ ]   Mail Service to notify user once All uploaded data converted in to supported languages
- [ ]   Need to write test cases
 
 ### Note : 
 ###### Our Service is highly depending on Third PartyApi in this case (Google Translator API) , if API goes down we don;t want extra down time in our service,so we
 ###### can use Adapter Design Pattern here that will eliminate Third Party API dependency.
  
 
  
  
![AdapterDesignForTransLAtionAPI](https://user-images.githubusercontent.com/49105701/191804227-1eb7253b-a941-41c4-804c-7ec0bacafe6f.JPG)

  


