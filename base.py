from mixin import MixinFoo, MixinBar

class Base(object):
    """ Base class containing all of the methods shared by all versions of this class """
    def __init__(self):
        """
        Initialize the class by running all of the setup
        operations of our mixin classes
        """

        # Instanciate some class variable to track mixin types that have been added
        # and an associateed 'fetch' method for each one.
        self.__class__._mixinTypes = []
        self.__class__._getOps = {}
        self.__class__._setOps = {}

        self._runSetupMixinOps()

    def _runSetupMixinOps(self):
        """
        This class dynamically finds and executes all of
        setup methods that the mixin classes implement
        """

        # Loop through all the methods in this instance of the class
        for methodName in dir(self):
            # And exectute all callables that start with "_setup".
            if methodName.startswith('_setup') and callable(getattr(self, methodName)):
                getattr(self, methodName)()

    def getAll(self):
        """
        Prints the results of every declared "get" function for all mixin classes.
        """
        for mixinTypeName in self.__class__._mixinTypes:
            if self.__class__._getOps[mixinTypeName] is not None:    
                print getattr(self, self.__class__._getOps[mixinTypeName])()

    @classmethod
    def _addMixinType(cls, typeName, getOp=None, setOp=None):
        """
        Class method that a mixin class needs to call during setup to inform the class
        about it and all of its associated methods.
        """
        if typeName in cls._mixinTypes:
            raise ValueError("Type '%s' already exists. You may not use a typename more than once")
        # Add the type name to the list of known types.
        cls._mixinTypes.append(typeName)
        # Add the get opration to the list of known getOps
        cls._addGetOp(typeName, getOp)
        cls._addSetOp(typeName, setOp)

    @classmethod
    def _addGetOp(cls, typeName, op):
        """
        Class method for informing the class about a mixin's get operation
        """
        cls._getOps[typeName] = op
    
    @classmethod
    def _addSetOp(cls, typeName, op):
        """
        Class method for informing the class about a mixin's set operation
        """
        cls._setOps[typeName] = op

class BaseWithMixin(MixinFoo, Base):
    """ A simple class with a single mixin """
    pass

class BaseWithTwoMixins(MixinFoo, MixinBar, Base):
    """ A simple class that uses two mixins """
    pass
