from urllib.request import urlopen
import json

url = "https://run.mocky.io/v3/65c043be-b3a3-40d5-bc17-e2746f5bdcf2"

# store the response of URL
response = urlopen(url)


# storing the JSON response
# from url in data
data_json = json.loads(response.read())
# print(data_json[0])
# for i in data_json[0]:
#     print(i,data_json[0]['id'])

from peewee import *

db= SqliteDatabase('salesDetails.db')

class itemDetails(Model):
    id= CharField(primary_key=True)
    latitude= DoubleField()
    longitude= DoubleField()
    userid= CharField()
    description= TextField(null=True)
    price= FloatField()
    status= CharField()

    class Meta:
        database= db

db.connect()

db.create_tables([itemDetails])

itemid={}


for item in data_json:
    temp= item['id']
    itemid[temp]= 1
    try:
        itemid[temp]= itemDetails.create(id=item['id'], latitude= item['loc'][0], longitude= item['loc'][1], userid= item['userId'], description= item['description'], price= item['price'], status= item['status'])
    except IntegrityError:
        pass

# def getSortedData(reverse,criteria):
#     query_result=[]
    
#     if criteria=='price' and reverse==True:
#         for item in itemDetails.select().order_by(itemDetails.price.desc()):
#             json_result= {}
#             json_result['id']= item.id
#             json_result['loc']= {0:item.latitude,1:item.longitude}
#             json_result['userId']= item.userid
#             json_result['description']= item.description
#             json_result['price']= item.price
#             json_result['status']= item.status

#             query_result.append(json_result)
#     else:
#         for item in itemDetails.select().order_by(itemDetails.price):
#             json_result= {}
#             json_result['id']= item.id
#             json_result['loc']= {0:item.latitude,1:item.longitude}
#             json_result['userId']= item.userid
#             json_result['description']= item.description
#             json_result['price']= item.price
#             json_result['status']= item.status

#             query_result.append(json_result)
    
#     return json.dumps(query_result)


# def getSingleItem(fields):
#     if 'id' in fields:
#         query= itemDetails.select().where(itemDetails.id==fields['id'])
#     elif 'location' in fields:

#         # extracting location from argument (string type)
#         temp1= fields['location'][1:len(fields['location'])-1]
#         loc= list(map(float,temp1.split(',')))
        
#         query= itemDetails.select().where(itemDetails.latitude==loc[0] and itemDetails.longitude==loc[1])
#     else:
#         return json.dumps("NO RESULT FOUND !")
    
#     json_result= {}
    
#     for item in query:
#         json_result['id']= item.id
#         json_result['loc']= {0:item.latitude,1:item.longitude}
#         json_result['userId']= item.userid
#         json_result['description']= item.description
#         json_result['price']= item.price
#         json_result['status']= item.status
    
#     return json.dumps(json_result)


# def getItemList(fields):
#     query_result=[]
#     if 'userId' in fields:
#         query= itemDetails.select().where(itemDetails.userid==fields['userId'])
#     elif 'status' in fields:
#         query= itemDetails.select().where(itemDetails.status==fields['status'])
#     else:
#         return json.dumps("NO RESULT FOUND !")
    
    
#     for item in query:
#         json_result= {}
#         json_result['id']= item.id
#         json_result['loc']= {0:item.latitude,1:item.longitude}
#         json_result['userId']= item.userid
#         json_result['description']= item.description
#         json_result['price']= item.price
#         json_result['status']= item.status

#         query_result.append(json_result)
    
#     return json.dumps(query_result)


# def getItemsInRadius(radius,lat,long):
#     lower_limitx= lat-radius
#     upper_limitx= lat+radius
#     lower_limity= long-radius
#     upper_limity= long+radius

#     query= itemDetails.select().where((itemDetails.latitude<= upper_limitx) & (itemDetails.latitude>= lower_limitx) & (itemDetails.longitude>= lower_limity) & (itemDetails.longitude<= upper_limity))

#     query_result=[]

#     for item in query:
#         json_result= {}
#         json_result['id']= item.id
#         json_result['loc']= {0:item.latitude,1:item.longitude}
#         json_result['userId']= item.userid
#         json_result['description']= item.description
#         json_result['price']= item.price
#         json_result['status']= item.status

#         query_result.append(json_result)
    
#     return json.dumps(query_result)