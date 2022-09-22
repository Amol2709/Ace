

About Ace:
===
#### Installation Setup
###### Prerequisite: Python version >=3.6
###### Note: I have used postgreSQL but application will work with any relational DB (need to change settings.py)
1. Create Account on  Google Cloud Platform 
2. Follow this step to setup Account [GCP](https://cloud.google.com/translate/docs/setup#windows "GCP Machine Translation").
3. Create Virtual Environment.
4. pip install -r requirements.txt
---


## About App:

---

### Problem Statement:
1. Task is to develop a web application that helps us convert farmer details from English to
different languages.
2. To do this, we will use of Google Translate API. 

### Assumption and Solution Flow:

1. User need to Sign In on to application. (need to create account)
2. Application supports only 4 languages apart from English viz. Hindi, Marathi, Telugu and Punjabi.
3. Application support Excel (.xlsx) and CSV (.csv) file.
4. User will upload file where 6 columns are mandatory (FirstName, LastName, StateName, DistrictName, VillageName, Phone)
5. Once user upload file application will Convert all information in all supported languages.
6. Application will store all information in all supported languages in DB (postgre) 
7. User can also View Information in all supported languages on to UI itself.
8. Apart from this, we have also exposed two API endpoints to fetch all information:
9.  GET: getAllFarmerinfo() : http://127.0.0.1:8000/api/get-allfarmer-info/<language_code>/ : Fetch all Information in language Specified.
10. GET: getFarmerinfo_ID() :  http://127.0.0.1:8000/api/get-allfarmer-info/<id>/<language_code>/ : Fetch Infromation based on ID.
11. For Api Authentication we are using DRF (Django Rest Framework) in built Token Based Authentication.
12. For Api Doc We have Used Swagger-UI (for DRF)


---
