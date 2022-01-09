import cherrypy
import sorted_data
import single_item
import item_list
import items_in_radius


class salesService(object):
    @cherrypy.expose
    def index(self):
        return "Connection Established with server ! "
    
    @cherrypy.expose
    def getsorteddata(self,reverse='False',criteria='price'):
        if reverse=='False':
            result= sorted_data.getSortedData(False, criteria)
        else:
            result= sorted_data.getSortedData(True, criteria)
        
        return result
    
    @cherrypy.expose
    def getitem(self,**kwargs):
        result= single_item.getSingleItem(kwargs)
        return result

    @cherrypy.expose
    def getitemlist(self,**kwargs):
        result= item_list.getItemList(kwargs)
        return result
    
    @cherrypy.expose
    def get_items_in_radius(self,radius,latitude,longitude):
        result= items_in_radius.getItemsInRadius(float(radius),float(latitude),float(longitude))
        return result


if __name__ == '__main__':
    cherrypy.config.update({"server.socket_port":10001})
    cherrypy.quickstart(salesService())