# from inheritance import *

class Empty:
    pass

# import operator
# def magic(C):
#     def onDecorator(aClass):
#         class onInstance:
#             def __init__(self, *args, **kargs):
#                 self.wrapped = aClass(*args, **kargs)
#                 setattr(C, 'referents', dict())
#             def __getattr__(self, attr):
#                 if attr == 'wrapped': return self.__dict__[attr]
#                 operator.setitem(getattr(C, 'referents'), attr, self.wrapped)
#                 setattr(C, attr, self.wrapped.__class__.__dict__[attr])
#                 return getattr(self.wrapped, attr)
#             def __setattr__(self, attr, value):
#                 if attr == 'wrapped': self.__dict__[attr] = value
#                 else: setattr(self.wrapped, attr, value)
#         return onInstance
#     return onDecorator

# def delegation(self, attribute):
#     for x in self.referents.items():
#         if attribute in x[1].__dict__: return x[1].__dict__[attribute]
#     raise AttributeError("Attribute «{}» doesn't exist".format(attribute))
    
# # Empty.__getattr__ = delegation

# class SharedMem(type):
#     def __new__(meta, classname, supers, classdict):
#         classdict['__getattr__'] = delegation
#         return type.__new__(meta, classname, supers, classdict)
    
# Empty = SharedMem('Empty', (), dict(Empty.__dict__))

@magic(Empty)
class Person:
    def __init__(self, name, gross, netp):
        self.name = name
        self.gross_salary = gross
        self.netpercentage = netp

    def who(self):
        return self.name

    def salary(self):
        return self.gross_salary * self.netpercentage / 12

@magic(Empty)
class Exam:
    def __init__(self, title, n, ne):
        self.title = title
        self.students = n
        self.exams = ne

    def todo(self):
        return f'still {self.students - self.exams} students should pass the {self.title} exam'

if __name__ == '__main__':
    m = Empty()
    x = Exam('PA', 100, 15)
    y = Exam('TSP', 50, 45)
    p = Person('Bob', 100000, .6)

    try:
        print(f'm salary:- {m.salary()}')
    except Exception as e:
        print(f'*** {type(e).__name__}: {e}')

    print(f'p salary:- {p.salary()}')
    print(f'm salary:- {m.salary()}')

    try:
        print(f'm todo:- {m.todo()}')
    except Exception as e:
        print(f'*** {type(e).__name__}: {e}')

    print(f'x todo:- {x.todo()}')
    print(f'm todo:- {m.todo()}')

    p.netpercentage=.45
    print(f'm salary:- {m.salary()}')
    print(f'y todo:- {y.todo()}')
    print(f'm todo:- {m.todo()}')
    print(f'm students:- {m.students}')
    print(f'x todo:- {x.todo()}')
    print(f'm students:- {m.students}')

    try:
        print(f'm who:- {m.who()}')
    except Exception as e:
        print(f'*** {type(e).__name__}: {e}')
