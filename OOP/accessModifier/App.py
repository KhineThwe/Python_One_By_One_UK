from Machine import *
if __name__ == '__main__':
    machine = Machine()
    print(machine.id)
    print(machine.count)
    # print(machine.__name)#private
    print(machine._color)
    print(machine._Machine__name)

#name mangling
"""
_ClassName__privateVarName
"""