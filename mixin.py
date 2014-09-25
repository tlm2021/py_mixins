class MixinFoo(object):
    """ Example mixin class for extending a Base with methods for 'foo' type """

    def _setupFoo(self):
        """
        REQUIRED setup method.
        - Name must not conflict with other mixins.
        - Must start with '_setup
        """
        # Type name for tracking this mixin type 
        typeName = "foo"

        # Call the method on the base class for doing the addition.
        self._addMixinType(typeName, 'getFoo')

        # If we want this mixin to actually have an attribute
        # on the class and not just methods, we can add that here
        setattr(self, typeName, self.getFoo())

    def getFoo(self):
        # Get method for this mixin type
        return "FOO"

class MixinBar(object):
    """ Example mixin class for extending a Base with methods for 'bar' type """

    def _setupBar(self):
        """
        REQUIRED setup method.
        - Name must not conflict with other mixins.
        - Must start with '_setup
        """
        # Type name for tracking this mixin type 
        typeName = "bar"

        # Call the method on the base class for doing the addition.
        # It takes the typeName, and the associated method names
        self._addMixinType(typeName, 'getBar', 'setBar')

        # If we want this mixin to actually have an attribute
        # on the class and not just methods, we can add that here
        setattr(self, typeName, "BAR")

    def getBar(self):
        # Get method for this mixin type
        return self.bar 

    def setBar(self, value):
        self.bar = value
