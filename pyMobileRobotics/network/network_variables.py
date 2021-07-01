from twisted.internet import reactor, protocol


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

    class Server(protocol.Protocol):
        """This is just about the simplest possible protocol"""

        def dataReceived(self, data):
            "As soon as any data is received, write it back."
            self.transport.write(data)

    @staticmethod
    def startServer(listenPort: 23343):
        if not(NetworkVariables.__serverStarted):
            factory = protocol.ServerFactory()
            factory.protocol = NetworkVariables.Server
            reactor.listenTCP(listenPort, factory)
            reactor.run()

    @staticmethod
    def setValue(name: str, value: any):
        if (name in NetworkVariables.__variables.keys()
            and NetworkVariables.__variables[name]['type'] != type(value)):
            raise ValueError("You can't change variable type when the variable has initialized.")
        NetworkVariables.__variables[name]['value'] = value
        NetworkVariables.__variables[name]['type'] = type(value)

    @staticmethod
    def getValue(name: str) -> any:
        if name not in NetworkVariables.__variables.keys():
            raise ValueError('Variable "' + str(name) + '" has not been created.')
        return NetworkVariables.__variables[name]['value']

    pass