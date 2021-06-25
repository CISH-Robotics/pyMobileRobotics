class Util():

    @staticmethod
    def dictsDisjoint(a: dict, b: dict):
        return not any(k in b for k in a)