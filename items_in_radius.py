from databaseHandler import itemDetails
import json

def getItemsInRadius(radius,lat,long):
    lower_limitx= lat-radius
    upper_limitx= lat+radius
    lower_limity= long-radius
    upper_limity= long+radius

    query= itemDetails.select().where((itemDetails.latitude<= upper_limitx) & (itemDetails.latitude>= lower_limitx) & (itemDetails.longitude>= lower_limity) & (itemDetails.longitude<= upper_limity))

    query_result=[]

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