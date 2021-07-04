from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineReceiver
import threading
import logging
import json


class NetworkVariables():
    """網路變數

    NetworkVariables 為一個網路同步的字典，機器人可以從本機讀寫變數，
    同時透過網路連接的遠端也可以同時讀寫變數。
    """

    # 變數表
    __variables = {}
    """
    變數表結構：
    __variables = {
        'name': {
            'value': value,
            'type': type
        }
    }
    """

    __serverStarted = False
    __updating = False

    @staticmethod
    def setValue(name: str, value: any):
        # 檢查表中是否已有變數，
        # 有的話檢查型態是否改變，改變則報錯。
        if (name in NetworkVariables.__variables.keys()
            and NetworkVariables.__variables[name]['type'] != type(value)):
            raise ValueError("You can't change variable type when the variable has initialized.")
        # 上鎖
        NetworkVariables.__updating = True
        # 如果表中沒有變數則新增
        if name not in NetworkVariables.__variables.keys():
            NetworkVariables.__variables[name] = {}
        NetworkVariables.__variables[name]['value'] = value
        NetworkVariables.__variables[name]['type'] = type(value)
        # 解鎖
        NetworkVariables.__updating = False

    @staticmethod
    def getValue(name: str) -> any:
        if name not in NetworkVariables.__variables.keys():
            return None
        while NetworkVariables.__updating: pass
        return NetworkVariables.__variables[name]['value']

    @staticmethod
    def getVariables() -> dict:
        return NetworkVariables.__variables

    @staticmethod
    def getVariablesJson() -> str:
        data = {}
        for name, variable in NetworkVariables.__variables.items():
            data[name] = {}
            data[name]['value'] = str(variable['value'])
            data[name]['type'] = str(variable['type'].__name__)
        jsonData = json.dumps(data)
        return jsonData

    class __Server(LineReceiver):

        def lineReceived(self, data):
            recvStr = data.decode('utf-8')
            recvJson = json.loads(recvStr)
            # logging.debug('Server Received=' + recvStr)
            if recvJson['mode'] == 'set':
                variables = NetworkVariables.getVariables()
                setData = recvJson['data']
                for varData in setData:
                    # 檢查變量表中是否有該鍵的數據，
                    # 沒有則創建。
                    if varData['name'] not in variables.keys():
                        variables[varData['name']] = {}
                        # 判斷遠端輸入的格式類型，寫入類型。
                        if varData['type'] == 'str':
                            variables[varData['name']]['type'] = str
                        elif varData['type'] == 'int':
                            variables[varData['name']]['type'] = int
                        elif varData['type'] == 'float':
                            variables[varData['name']]['type'] = float
                    # 已存在則直接寫入。
                    if variables[varData['name']]['type'] == str:
                        NetworkVariables.setValue(varData['name'], str(varData['value']))
                    elif variables[varData['name']]['type'] == int:
                        NetworkVariables.setValue(varData['name'], int(varData['value']))
                    elif variables[varData['name']]['type'] == float:
                        NetworkVariables.setValue(varData['name'], float(varData['value']))
            elif recvJson['mode'] == 'get':
                # TODO: jsonData由dict改為list格式
                variablesJson = NetworkVariables.getVariablesJson()
                sendData = variablesJson.encode(encoding='utf-8')
                self.sendLine(sendData)

    @staticmethod
    def startServer(listenPort=23343):
        if not(NetworkVariables.__serverStarted):
            factory = protocol.ServerFactory()
            factory.protocol = NetworkVariables.__Server
            reactor.listenTCP(listenPort, factory)
            # reactor.run()
            threading.Thread(target=reactor.run, kwargs=({'installSignalHandlers': False})).start()