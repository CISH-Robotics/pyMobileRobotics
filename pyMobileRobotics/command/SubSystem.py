class Subsystem():

    def __hash__(self):
        return hash(str(self))

    def getName(self):
        return self.__class__.__name__

    def periodic(self):
        pass