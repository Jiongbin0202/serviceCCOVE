import asyncio
import websockets
import json
import dto
import executes
import websocket
import threading

IP_ADDR = "127.0.0.1"
IP_PORT = "8888"

# 消息管道  把消息发送给特定的处理器进行消息处理 （消息名称必须和 IExecute 一致）
class ExecutePieline(object):
     def __init__(self):
        # 定义一个列表
        self.ExecuteList = []
     def Add(self, execute) :
        self.ExecuteList.append(execute)
     def Execute(self, json) :
        superSerializable =  dto.createSuperJson(json);      #得到一个用json中包含massageName初始化的串行接口类ISerializable
        for execute in self.ExecuteList:               #遍历列表中的处理方法
            if(execute.messageName == superSerializable.messageName):   #当列表中方法的名字和获取信息json所包含的messageName一致时,比如serviceCove1
                 execute.Execute(json)          #执行算法——从executes里执行

# 进行websocket连接
async def clientRun():
    ipaddress = IP_ADDR + ":" + IP_PORT
    async with websockets.connect("ws://" + ipaddress, ping_interval=None) as websocket:   #保持一直连接
        print(websocket)
        await onMessage(websocket)

# 向服务器端发送消息
async def sendMessageonly(websocket, serializableObj):
    if(websocket == None):       #发送消息前判断是否已经连接上
        clientRun()
    await websocket.send(serializableObj.toJson())


# 接收消息后，执行全局管道的 Execute 方法。 这个方法会执行  GlobalExecutePieline.Add() 进去的所有函数
async def onMessage(websocket):
    while True:
        recv_text = await websocket.recv()
        print("recv: ", f"{recv_text}")
        if "messageName" in recv_text:          #接收消息后，判断是否为dto，不是的话返回wrong order!
            dicts = json.loads(recv_text)
            if dicts.get("messageName") != "end":             #如果是dto，若是最终结果则可不处理,否则返回done。（客户端和服务端有一个存在判断即可）
                outdto = GlobalExecutePieline.Execute(recv_text)
                await sendMessageonly(websocket, outdto)
            else:
                await websocket.send("done!")
        else:
            await websocket.send("wrong order!")




def connect():
    ws = websocket.WebSocket()
    ws.connect("ws://127.0.0.1:8888")
    return ws

def sendMessage(websocket, serializableObj):
    websocket.send(serializableObj.toJson())

def close(websocket):
    websocket.close()


# main function
if __name__ == '__main__':

    # 实例化一个执行管道，用于执行消息体，添加所有的消息体
    GlobalExecutePieline = ExecutePieline()
    execute1 = executes.SCove1Execute()
    GlobalExecutePieline.Add(execute1)
    execute2 = executes.SCove2Execute()
    GlobalExecutePieline.Add(execute2)
    #
    #
    print("======client main begin======")
    asyncio.get_event_loop().run_until_complete(clientRun())
    # asyncio.get_event_loop().run_until_complete(connect())

