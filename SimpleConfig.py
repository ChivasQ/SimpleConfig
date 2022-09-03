parameter = []
value = []
config_path = 'config.txt'

def Config_path(Config_path):
    global config_path
    config_path = Config_path

def Config_length():
    x = sum(1 for line in open(config_path, 'r'))
    return x

def List_update():
    x = sum(1 for line in open(config_path, 'r'))
    #print(x, " parameters")
    config = open(config_path, 'r')
    for i in range(x):
        global parameter, value
        line1 = str(config.readline().strip())
        line1 = line1.split(':')
        parameter.append(line1[0])
        value.append(line1[1])
    config.close()

def Get(parameter1):
    List_update()
    if parameter1 in parameter:
        return str(value[parameter.index(parameter1)].split(',')).translate({ord(i): None for i in '[]"'"'"})


def Change_value(parameter2, changed_value):
    config =  open(config_path, 'r')
    old_data = config.read()
    new_data = old_data.replace(f'{parameter2}:{value[parameter.index(parameter2)]}', f'{parameter2}:{changed_value}')
    config = open(config_path, 'w')
    config.write(new_data)
    config.close()









