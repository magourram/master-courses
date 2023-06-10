from pprint import pprint as p

class Mixin:
    pass

class MyType(type):


    def __new__(mcls, name, bases, attrs, **kwargs):
        print("  MyType.__new__.mcls:%s" % (mcls))

        if not Mixin in bases:
            #could cause MRO resolution issues, but if you want to alter the bases
            #do it here
            bases += (Mixin,)

        #The call to super.__new__ can also modify behavior:
        #                                   👇 classes Foo and Bar are instances of MyType
        return super(MyType, mcls).__new__(mcls, name, bases, attrs)

        #now we're back to the standard `type` 
        #doing this will neuter most of the metaclass behavior, __init__ wont
        #be called.                         👇
        #return super(MyType, mcls).__new__(type, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        print("  MyType.__init__.cls:%s." % (cls))

        #I can see attributes on Foo and Bar's namespaces
        print("    %s.cls_attrib:%s" % (cls.__name__, getattr(cls, "cls_attrib", None)))
        return super().__init__(name, bases, attrs)


print("\n Foo class creation:")
class Foo(metaclass=MyType):
    pass
# print("Foo mro ", Foo.__mro__)
# print("Foo bases ", Foo.__bases__)
print(Foo.__dict__)

print("\n bar class creation:")
class Bar(Foo):
    #MyType.__init__ will see this on Bar's namespace
    cls_attrib = "some class attribute" 

    def __init__(self):
        self.self_attr = "some self attribute" 
# print("Bar mro ", Bar.__mro__)
# print("Bar bases ", Bar.__bases__)
