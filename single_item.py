from databaseHandler import itemDetails
import json

def getSingleItem(fields):
    if 'id' in fields:
        query= itemDetails.select().where(itemDetails.id==fields['id'])
    elif 'location' in fields:

        # extracting location from argument (string type)
        temp1= fields['location'][1:len(fields['location'])-1]
        loc= list(map(float,temp1.split(',')))
        
        query= itemDetails.select().where(itemDetails.latitude==loc[0] and itemDetails.longitude==loc[1])
    else:
        return json.dumps("NO RESULT FOUND !")
    
    json_result= {}
    
    for item in query:
        json_result['id']= item.id
        json_result['loc']= {0:item.latitude,1:item.longitude}
        json_result['userId']= item.userid
        json_result['description']= item.description
        json_result['price']= item.price
        json_result['status']= item.status
    
    return json.dumps(json_result)