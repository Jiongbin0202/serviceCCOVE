import asyncio
import json

import websockets
import dto

IP_ADDR = "127.0.0.1"
IP_PORT = "8888"

# 接收从客户端发来的消息并处理，再返给客户端ok
async def serverRecv(websocket):
    while True:
        recv_text = await websocket.recv()
        print("recv:", recv_text)
        dicts = json.loads(recv_text)
        if "messageName" in recv_text:
            if dicts.get("messageName") != "end":    #判断如果生成的是最终结果就停止发送
                await websocket.send(recv_text)
            else:
                continue
        else:
            continue


# 握手并且接收数据
async def serverRun(websocket, path):
    print(path)
    # d0 = dto.test0()
    # await websocket.send(d0.toJson())    #模拟第一次发消息给客户端处理
    # print("send:", d0.toJson())
    await serverRecv(websocket)


# main function
if __name__ == '__main__':
    # print("======server main begin======")
    # server = websockets.serve(serverRun, IP_ADDR, IP_PORT, ping_interval=None)   #设置了无限延迟，即不断线，默认是20s断开
    # asyncio.get_event_loop().run_until_complete(server)
    # asyncio.get_event_loop().run_forever()

    print("======server main begin======")
