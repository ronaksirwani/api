from databaseHandler import itemDetails
import json

def getSortedData(reverse,criteria):
    query_result=[]
    
    if criteria=='price' and reverse==True:
        for item in itemDetails.select().order_by(itemDetails.price.desc()):
            json_result= {}
            json_result['id']= item.id
            json_result['loc']= {0:item.latitude,1:item.longitude}
            json_result['userId']= item.userid
            json_result['description']= item.description
            json_result['price']= item.price
            json_result['status']= item.status

            query_result.append(json_result)
    else:
        for item in itemDetails.select().order_by(itemDetails.price):
            json_result= {}
            json_result['id']= item.id
            json_result['loc']= {0:item.latitude,1:item.longitude}
            json_result['userId']= item.userid
            json_result['description']= item.description
            json_result['price']= item.price
            json_result['status']= item.status

            query_result.append(json_result)
    
    return json.dumps(query_result)
