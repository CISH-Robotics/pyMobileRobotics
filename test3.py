class classA():

    def classAFunc(self):
        print('FuncA')

    def runClass(classRun):
        classRun.start()

class classB(classA):

    def classBFunc(self):
        print('FuncB')

    def loopFunc(self):
        self.classAFunc()

class classC(classB):

    #Override重寫(覆寫)
    def classAFunc(self):
        print('qwq')

    def start(self):
        self.loopFunc()

def main():
    robot = classC()
    classA.runClass(robot)

if __name__ == '__main__':
    main()