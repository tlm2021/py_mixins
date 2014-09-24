class MixinFoo(object):
    def _setupFoo(self):
        typeName = "foo"
        self._addMixinType(typeName, 'getFoo')
        setattr(self, typeName, self.getFoo()

    def getFoo(self):
        return "FOO"
