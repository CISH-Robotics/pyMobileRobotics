class Util():

    @staticmethod
    def dictsDisjoint(a: dict, b: dict):
        return not any(k in b for k in a)

    @staticmethod
    def listsDisjoint(a: list, b: list):
        for aElm in a:
            for bElm in b:
                if aElm == bElm:
                    return True
        for bElm in b:
            for aElm in a:
                if aElm == bElm:
                    return True
        return False