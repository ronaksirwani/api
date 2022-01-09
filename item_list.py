from databaseHandler import itemDetails
import json

def getItemList(fields):
    query_result=[]
    if 'userId' in fields:
        query= itemDetails.select().where(itemDetails.userid==fields['userId'])
    elif 'status' in fields:
        query= itemDetails.select().where(itemDetails.status==fields['status'])
    else:
        return json.dumps("NO RESULT FOUND !")
    
    
    for item in query:
        json_result= {}
        json_result['id']= item.id
        json_result['loc']= {0:item.latitude,1:item.longitude}
        json_result['userId']= item.userid
        json_result['description']= item.description
        json_result['price']= item.price
        json_result['status']= item.status

        query_result.append(json_result)
    
    return json.dumps(query_result)