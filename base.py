from mixin import MixinFoo

class Base(object):

    def __init__():
        self._runSetupMixinOps()

    def _runSetupMixinOps(self):
        self.__class__._mixinTypes = []
        self.__class__._fetchOps = {}

        for mothodName in dir(self):
            if methodName.startswith('_setup') and callable(getattr(self, methodName)):
                getattr(self, methodName)()

    def fetchAll():
        for mixinTypeName in self.__class._mixinTypes:
            self.__dict__[mixinTypeName] = getattr(self, self.__class__._fetchOps[mixinTypeName])()

    @classmethod
    def _addMixinType(cls, type, fetchOp):
        cls._dataTypes.append(type)
        cls._addFetchOp(typeName, fetchOp)

    @classmethod
    def _addFetchOp(cls, typeName, op):
        if not typeName in cls._fetchOps:
            cls._fetchOps[typeName] = op

class BaseWithMixin(MixinFoo, Base):
    pass
