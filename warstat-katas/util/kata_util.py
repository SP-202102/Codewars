# TODO: make this a class
class warKata:

    List = {
        0 : "p000_hello_world",
        1 : "p001_hello_universe"
    }

    def getCode( self, kataNumber ):
        return self.List[kataNumber] 

    def getTest( self, kataNumber ):
        return self.List[kataNumber] + "_t"

    def getCodeFileName(self, kataNumber):
        return self.List[kataNumber] + ".py"

    def getTestFileName(self, kataNumber):
        return self.List[kataNumber] + "_t.py"


def get_class(fully_qualified_path, module_name, class_name, *instantiation):
    """
    Returns an instantiated class for the given string descriptors
    :param fully_qualified_path: The path to the module eg("Utilities.Printer")
    :param module_name: The module name eg("Printer")
    :param class_name: The class name eg("ScreenPrinter")
    :param instantiation: Any fields required to instantiate the class
    :return: An instance of the class
    """
    p = __import__(fully_qualified_path)
    m = getattr(p, module_name)
    c = getattr(m, class_name)
    instance = c(*instantiation)
    return instance
