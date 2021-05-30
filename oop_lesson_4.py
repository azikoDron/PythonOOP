# Методы экземпляра
class Robot:
    def hello(*args):
        print('Hello from robot ', args)


bender = Robot()
print('\n# Разница', '\n',
    '\t', Robot.hello, '\n',
    '\t', bender.hello)

print('\n# Область памяти',)
print('\t', Robot.hello(), '\n',
      '\t', bender.hello())

print('\n# Кто есть кто', '')
print('\t', Robot(), '\n',
      '\t', bender)

print("\n# Создается другой объект")
jimmie = Robot()

print('# Кто есть кто')
print('\t', Robot(), '\n',
      '\t', bender, '\n',
      '\t', jimmie)
print("##############################################\n")


class Robot:
    skin = 'Steal'

    def hello(*args):
        print('Hello from robot ', args)

    def show_skin(instance):
        print(f'My skin is {instance.skin}')

    def show_name(instance):
        if hasattr(instance, 'name'):
            print(f'My name is {instance.name}')
        else:
            print('Null')

    def set_value(robot, value, age=0):
        robot.name = value
        robot.age = age


bender = Robot()
print(bender.show_skin())

print("\n#")
bender.skin = 'gold'
jery = Robot()
Robot.skin = 'aluminium'
print('Main class skin is ',
Robot.skin)
bender.show_skin()
jery.show_skin()

print('\n# Name check ')
bender.show_name()
jery.show_name()

print('\n# Name check ')
bender.name = 'Bender'
bender.show_name()
jery.show_name()


print('\n# Name check ')
jery.set_value('Jerry')
bender.show_name()
jery.show_name()