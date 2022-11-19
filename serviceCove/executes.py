import dto
import Connection


class IExecute(object):
    def __init__(self, messageName):
        self.messageName = ""
    def Execute(json) :
        print(json)

class SCove1Execute(IExecute):
    def __init__(self):
        self.messageName = "serviceCove1"
    # def __init__(self, messageName):
    #     self.messageName = messageName
    def Execute(self, jsonString) :
        serviceCove0 = dto.serviceCove0.fromJson(jsonString)
        # 这里就拿到了接收到的 dto0
        # func (dto0)
        return ""



class SCove2Execute(IExecute):
    def __init__(self):
        self.messageName = "serviceCove2"
    def Execute(self, jsonString) :
        serviceCove1 = dto.serviceCove1()
        serviceCove1.fromJson(jsonString)
        exOptions2 = dto.exOptions2()
        sdg3 = Processors.sdg3()
        serviceCove2 = sdg3.step2(serviceCove1, exOptions2)
        return serviceCove2




