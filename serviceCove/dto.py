import json;

def createSuperJson(jsonString) :
    data = json.loads(jsonString)  #得到一个键值对dict
    return  ISerializable(data['messageName'])  #返回一个串行接口类


class ISerializable(object):
    def __init__(self):
        pass
    def __init__(self, messageName):
        ##self.__property = property
        self.messageName = messageName
    def toSuperJson(self) :
        json = {
            'messageName' : self.messageName,
        }
        return json
    def fromSuperJson(self,json) :
        return  ISerializable(json['messageName'])
    # 转换当前对象为 string（json格式）
    def toJson(self) :
        # return "{}"
        pass
    # 从string格式转换为对象
    def fromJson(self,jsonString) :
        # return "{}"
        pass
        #json.dumps(this.__property)

class test0(ISerializable):
    def __init__(self):
        super().__init__("serviceCove1")
        self.road_shp = "E:\\arcpy\\EX02\\data\\line\\道路.shp"
        self.water_shp = "E:\\arcpy\\EX02\\data\\polygon\\水系.shp"
        self.poi_shp = "E:\\arcpy\\EX02\\data\\point\\医院学校公交场馆.shp"
        self.boundary_shp = "E:\\arcpy\\EX02\\data\\line\\德清县界.shp"
        self.path = "E:\\arcpy\\EX02\\data"
    def toJson(self) : # 对象各自实现自己的toJson
        jsonObj = {
                'messageName': self.messageName,
                'road_shp' : self.road_shp,
                'water_shp' : self.water_shp,
                'poi_shp' : self.poi_shp,
                'boundary_shp' : self.boundary_shp,
                'path' : self.path
            }
        return json.dumps(jsonObj)# 返回的是 string

class serviceCove0(ISerializable):
    def __init__(self, ):
        super().__init__("serviceCove0")
        self.road_shp = None
        self.water_shp = None
        self.poi_shp = None
        self.boundary_shp = None
    def toJson(self) : # 对象各自实现自己的toJson
        jsonObj = {
                'messageName' : self.messageName,
                'road_shp' : self.road_shp,
                'water_shp' : self.water_shp,
                'poi_shp' : self.poi_shp,
                'boundary_shp' : self.boundary_shp,
            }
        return json.dumps(jsonObj)# 返回的是 string
    def fromJson(self,jsonString) :
        dicts = json.loads(jsonString)
        # 使用 string 填充自身属性
        self.road_shp = dicts["road_shp"]
        self.water_shp = dicts["water_shp"]
        self.poi_shp = dicts["poi_shp"]
        self.boundary_shp = dicts["boundary_shp"]

class serviceCove1(ISerializable):
    def __init__(self):
        self.messageName = "serviceCove1"
        self.roadPro_shp = None
        self.waterPro_shp = None
        self.poiPro_shp = None
        self.boundaryPro_shp = None
    def toJson(self) : # 对象各自实现自己的toJson
        jsonObj = {
                'messageName': self.messageName,
                'roadPro_shp' : self.roadPro_shp,
                'waterPro_shp' : self.waterPro_shp,
                'poiPro_shp' : self.poiPro_shp,
                'boundaryPro_shp' : self.boundaryPro_shp,
            }
        return json.dumps(jsonObj)# 返回的是 string
    def fromJson(self,jsonString) :
        dicts = json.loads(jsonString)
        # 使用 string 填充自身属性
        self.roadPro_shp = dicts["roadPro_shp"]
        self.waterPro_shp = dicts["waterPro_shp"]
        self.poiPro_shp = dicts["poiPro_shp"]
        self.boundaryPro_shp = dicts["boundaryPro_shp"]

class serviceCove2(ISerializable):
    def __init__(self):
        super().__init__("end")
        self.keda_tif = None
    def toJson(self) : # 对象各自实现自己的toJson
        jsonObj = {
                'messageName': self.messageName,
                'keda_tif' : self.keda_tif
            }
        return json.dumps(jsonObj)# 返回的是 string
    def fromJson(self,jsonString) :
        dicts = json.loads(jsonString)
        # 使用 string 填充自身属性
        self.keda_tif = dicts["keda_tif"]

class exOptions0(ISerializable):
    def __init__(self):
        super().__init__("exOptions0")
        self.path = None
    def toJson(self) : # 对象各自实现自己的toJson
        jsonObj = {
                'messageName': self.messageName,
                'path' : self.path
            }
        return json.dumps(jsonObj)# 返回的是 string
    def fromJson(self, jsonString) :
        dicts = json.loads(jsonString)
        # 使用 string 填充自身属性
        self.path = dicts["path"]

class exOptions1(ISerializable):
    def __init__(self):
        super().__init__("exOptions1")
        self.pop_tif = None
        self.time_input = None
        self.path = None
    def toJson(self) : # 对象各自实现自己的toJson
        jsonObj = {
                'messageName': self.messageName,
                'pop_tif' : self.pop_tif,
                'time_input' : self.time_input,
                'path' : self.path
            }
        return json.dumps(jsonObj)# 返回的是 string
    def fromJson(self,jsonString) :
        dicts = json.loads(jsonString)
        # 使用 string 填充自身属性
        self.pop_tif = dicts["pop_tif"]
        self.time_input = dicts["time_input"]
        self.path = dicts["path"]



