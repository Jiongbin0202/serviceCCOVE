import json
import websockets
import Connection
import dto
import asyncio
import SDG3.zbjs as zbjs

def main():
    print("start working!")
    print("begin to create serviceCove0!")
    sC0_jsonString = json.dumps({"messageName": "serviceCove1",
                  "road_shp": "E:\\arcpy\\EX02\\data\\line\\\u9053\u8def.shp",
                  "water_shp": "E:\\arcpy\\EX02\\data\\polygon\\\u6c34\u7cfb.shp",
                  "poi_shp": "E:\\arcpy\\EX02\\data\\point\\\u533b\u9662\u5b66\u6821\u516c\u4ea4\u573a\u9986.shp",
                  "boundary_shp": "E:\\arcpy\\EX02\\data\\line\\\u5fb7\u6e05\u53bf\u754c.shp",
                  "path": "E:\\arcpy\\EX02\\data"})
    ex0_jsonString = json.dumps({"messageName": "exOptions",
                      "path": "E:\\arcpy\\EX02\\data"})
    serviceCove0 = dto.serviceCove0()
    serviceCove0.fromJson(sC0_jsonString)
    exOptions0 = dto.exOptions0()
    exOptions0.fromJson(ex0_jsonString)
    print("succeeded in creating serviceCove0!")
    print("begin to run!")
    serviceCove1 = zbjs.Run(serviceCove0, exOptions0)
    print(serviceCove1)
    print("succeeded in run!")
    print("begin to create serviceCove1!")
    ex1_jsonString = json.dumps({"messageName": "exOptions",
                      "pop_tif": "E:\\arcpy\\EX02\\data\\raster\\pop2016.tif",
                      "time_input": 10,
                      "path" :"E:\\arcpy\\EX02\\data"})
    exOptions1 = dto.exOptions1()
    exOptions1.fromJson(ex1_jsonString)
    print("succeeded in creating serviceCove1!")
    print("begin to run2!")
    serviceCove2 = zbjs.Run2(serviceCove1, exOptions1)
    print(serviceCove2)
    print("succeeded in run2!")
    print("Finish!")

def main3():
    websocket = Connection.connect()
    print(websocket)
    print("start working!")
    print("begin to create serviceCove0!")
    sC0_jsonString = json.dumps({"messageName": "serviceCove1",
                  "road_shp": "E:\\arcpy\\EX02\\data\\line\\\u9053\u8def.shp",
                  "water_shp": "E:\\arcpy\\EX02\\data\\polygon\\\u6c34\u7cfb.shp",
                  "poi_shp": "E:\\arcpy\\EX02\\data\\point\\\u533b\u9662\u5b66\u6821\u516c\u4ea4\u573a\u9986.shp",
                  "boundary_shp": "E:\\arcpy\\EX02\\data\\line\\\u5fb7\u6e05\u53bf\u754c.shp",
                  "path": "E:\\arcpy\\EX02\\data"})
    ex0_jsonString = json.dumps({"messageName": "exOptions",
                      "path": "E:\\arcpy\\EX02\\data"})
    serviceCove0 = dto.serviceCove0()
    serviceCove0.fromJson(sC0_jsonString)
    exOptions0 = dto.exOptions0()
    exOptions0.fromJson(ex0_jsonString)
    print("succeeded in creating serviceCove0!")
    print(serviceCove0)

    Connection.sendMessage(websocket, serviceCove0)
    Connection.sendMessage(websocket, exOptions0)

    print("begin to run!")
    serviceCove1 = zbjs.Run(serviceCove0, exOptions0)
    print(serviceCove1)
    print("succeeded in run!")
    print("begin to create serviceCove1!")
    ex1_jsonString = json.dumps({"messageName" : "exOptions",
                      "pop_tif" : "E:\\arcpy\\EX02\\data\\raster\\pop2016.tif",
                      "time_input" : 8,
                      "path" :"E:\\arcpy\\EX02\\data"})
    exOptions1 = dto.exOptions1()
    exOptions1.fromJson(ex1_jsonString)
    print("succeeded in creating serviceCove1!")

    Connection.sendMessage(websocket, serviceCove1)
    Connection.sendMessage(websocket, exOptions1)

    print("begin to run2!")
    serviceCove2 = zbjs.Run2(serviceCove1, exOptions1)
    print(serviceCove2)
    print("succeeded in run2!")

    Connection.sendMessage(websocket, serviceCove2)

    Connection.close(websocket)
    print("Finish!")


if __name__ == "__main__":
    # main() # 计算结果
    main3()