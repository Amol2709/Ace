from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from .Enums import SupportedFile, SupportedLanguage, MultiLingualTable
from .FileUploadStrategy import  UploadFileContext, MapColumn
from . Multilingual import  TranslatorContext
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .API import  API_Context
from .DBConnection import EstablishConnection
from .serializers import FarmerInfoSerializer
import pandas as pd
import pathlib
import  os
# Create your views here.

# import os 
# os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'C:\Users\DELL\Desktop\Assignment\cedar-turbine-363017-dff03d15fda1.json'

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllFarmerinfo(request, language_code = 'en'):
    '''
        This API will return All Farmer INFO in all supported Languages
    '''
    if request.method=='GET':
        dbObj = EstablishConnection.ReturnConnection()
        connection = dbObj.newConnection()
        if language_code in SupportedLanguage.LanguageCode.SUPPORTED_LANGUAGE.value or language_code=='en':
            tableName = MultiLingualTable.TableLanguageCode.TABLENAME_CODE_MAP.value[language_code]
            df = pd.read_sql_query('SELECT  first_name, last_name, state_name, village_name, district_name, phone from "{}" '.format(tableName),con= connection)
            result_data = df.to_dict(orient='records')
            result = FarmerInfoSerializer(result_data, many=True).data
            return Response(result)
        else:
            return HttpResponse(status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getFarmerinfo_ID(request, id, language_code='en'):
    if request.method=='GET':
        dbObj = EstablishConnection.ReturnConnection()
        connection = dbObj.newConnection()
        if language_code in SupportedLanguage.LanguageCode.SUPPORTED_LANGUAGE.value:
            tableName = MultiLingualTable.TableLanguageCode.TABLENAME_CODE_MAP.value[language_code]
            df = pd.read_sql_query('SELECT  first_name, last_name, state_name, village_name, district_name, phone from "{}" where farmer_id = {} '.format(tableName,id),con= connection)
        elif language_code == 'en':
            tableName = MultiLingualTable.TableLanguageCode.TABLENAME_CODE_MAP.value[language_code]
            df = pd.read_sql_query('SELECT  first_name, last_name, state_name, village_name, district_name, phone from "{}" where id = {}'.format(tableName,int(id)),con= connection)
        else:
            return HttpResponse(status=404)
        result_data = df.to_dict(orient='records')
        result = FarmerInfoSerializer(result_data, many=True).data
        return Response(result)

@login_required
def viewInfo(request):
    if request.method == 'POST':
        language_code = str(request.POST['language_code'])
        tableName = MultiLingualTable.TableLanguageCode.TABLENAME_CODE_MAP.value[language_code]
        dbobj = EstablishConnection.ReturnConnection()
        conn = dbobj.newConnection()
        df = pd.read_sql_query('SELECT  first_name, last_name, state_name, village_name, district_name, phone from "{}" '.format(tableName),con= conn)
        #print(df.head())
        #farmer_id = list(df['id'])
        f_name  = list(df['first_name'])
        l_name = list(df['last_name'])
        state_name = list(df['state_name'])
        village_name  = list(df['village_name'])
        district_name = list(df['district_name'])
        phone = list(df['phone'])
        farmer_info = tuple(zip(f_name,l_name,state_name,village_name,district_name,phone))
        context = {
             'language_support' : ['en']+SupportedLanguage.LanguageCode.SUPPORTED_LANGUAGE.value,
            'farmer_info':farmer_info
        }
        return render(request, 'CoreApp/view_info.html', context)
    context = {
        'language_support' : ['en']+SupportedLanguage.LanguageCode.SUPPORTED_LANGUAGE.value
    }
    return render(request, 'CoreApp/view_info.html', context)








def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    import six
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)
    return result

    # print(u"Text: {}".format(result["input"]))
    # print(u"Translation: {}".format(result["translatedText"]))
    # print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))




def checkAPI(request):
    print('Hello World')
    result = translate_text('hi',['my name is amol','hey there'])
    print(result)
    return HttpResponse('None')

@login_required
def home(request):
    return render(request, 'CoreApp/home.html')
@login_required
def validateFileExtension(request):
    if request.method == 'POST':

        file_path = request.FILES["filename"]
        file_extension = pathlib.Path(str(file_path)).suffix

        ## Checking Proper Extension of File ###
        if file_extension not in SupportedFile.FileExtension.SUPPORTED_FILE_EXTENSION.value:
            context = {
                'msg' :'Please upload csv(.csv) or excel(.xlsx) file only '
            }
            return render(request,'CoreApp/error.html',context)
        if file_extension ==SupportedFile.FileExtension.SUPPORTED_FILE_EXTENSION.value[0]:
            df = pd.read_excel(file_path)
            file_name = str(request.user)+'_'+str(file_extension)
            df.to_excel('CoreApp/UploadedFiles/'+file_name,index=False)
        
        else:
            df = pd.read_csv(file_path)
            file_name = str(request.user)+'_'+str(file_extension)
            df.to_csv('CoreApp/UploadedFiles/'+file_name,index=False)
        
        context = {
            'columns_list': list(df.columns),
            'file_name' : file_name
        }
        return render(request, 'CoreApp/map_column.html', context)


def uploadFileToDB(request):
    if request.method == 'POST':
        first_name_col = request.POST['first_name']
        last_name_col = request.POST['last_name']
        state_name_col = request.POST['state_name']
        district_name_col = request.POST['district_name']
        village_name_col = request.POST['village_name']
        contact_number_col = request.POST['contact_number']

        map_column_obj = MapColumn.SetColumnName().\
                        setFirstNameCol(first_name_col).\
                        setLastNameCol(last_name_col).\
                        setStateNameCol(state_name_col).\
                        setDistricNameCol(district_name_col).\
                        setVillageNameCol(village_name_col).\
                        setContactNumberCol(contact_number_col)
        print(map_column_obj)

        file_name= request.POST['file_name']
        file_extension = pathlib.Path(str(file_name)).suffix
        obj = UploadFileContext.SaveFileToDB(file_extension,file_name)
        obj.dopreProcessing(map_column_obj)
        obj.saveFile()

        translate_obj = TranslatorContext.TranslatorContext()
        translate_obj.translate()
       
        # api_obj= API_Context.TextTranslator()
        # result = api_obj.translate_text('hi',['my name is amol','hey there'])
        
        
        messages.success(request, f'You will get Notification through mail after Completion of Task!!! Thank You')
        return render(request, 'CoreApp/home.html')   
        

