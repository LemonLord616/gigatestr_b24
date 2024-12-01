import random


from . import AbsGenerator


def choose_days():
    seed = random.randint(0,200)
    if seed < 1:
        return random.randint(-100,0)
    if seed < 2:
        return random.randint(31,100)
    return random.randint(1,30)
def choose_grass():
    seed = random.randint(0,200)
    f = random.randint(1,10)
    ret_str = ''
    if seed < 1:
        ret_str = str(random.randint(-100,-1))
    elif seed < 2:
        ret_str = str(random.randint(101,200))
    else:
        ret_str = str(random.randint(0,100))
    if f < 5:
        return (ret_str + 'F')
    else:
        return ret_str
def number_animals():
    return random.randint(1,20)
def amount_exceed():
    seed = random.randint(0,200)
    if seed < 5:
        return random.randint(1,10)
    return 0
def choose_animal():
    seed = random.randint(0,200)
    animals_cringe = ["thefuck","notanimalforsure","somebullshit"]
    if seed < 2:
        return animals_cringe[random.randint(0,2)]
    if seed < 67:
        return "Lion"
    if seed < 133:
        return "Zebra"
    if seed <= 200:
        return "Boar"
def choose_weight():
    seed = random.randint(0,200)
    f = random.randint(1,10)
    ret_str = ''
    if seed < 1:
        ret_str = str(random.randint(-100,4))
    elif seed < 2:
        ret_str = str(random.randint(201,300))
    else:
        ret_str = str(random.randint(5,200))
    if f < 5:
        return (ret_str + '.0' + 'F')
    else:
        return (ret_str + '.0')
def choose_speed():
    seed = random.randint(0,200)
    f = random.randint(1,10)
    ret_str = ''
    if seed < 1:
        ret_str = str(random.randint(-100,4))
    elif seed < 2:
        ret_str = str(random.randint(61,161))
    else:
        ret_str = str(random.randint(5,60))
    if f < 5:
        return (ret_str + '.0' + 'F')
    else:
        return (ret_str + '.0')
def choose_energy():
    seed = random.randint(0,200)
    f = random.randint(1,10)
    ret_str = ''
    if seed < 1:
        ret_str = str(random.randint(-100,-1))
    elif seed < 2:
        ret_str = str(random.randint(101,201))
    else:
        ret_str = str(random.randint(0,100))
    if f < 5:
        return (ret_str + 'F')
    else:
        return (ret_str)
def random_number():
    seed = random.randint(0,200)
    f = random.randint(1,10)
    ret_str = ''
    ret_str = str(random.randint(-100,100))
    if f < 5:
        return (ret_str + '.0' + 'F')
    else:
        return (ret_str + '.0')
class JavaAss4Generator(AbsGenerator):
    def generate(self):
        inputs_all = []
        for _ in range(1):
            curr_test = []
            days = choose_days()
            grass = choose_grass()
            amount = number_animals()
            curr_test.append(days)
            curr_test.append(grass)
            curr_test.append(amount)
            exceed = amount_exceed()
            for i in range(amount + exceed):
                animal = choose_animal()
                weight = choose_weight()
                speed = choose_speed()
                energy = choose_energy()
                seed_invalid_number = random.randint(0,500)
                if seed_invalid_number < 1:
                    curr_test.append(' '.join((animal,weight,speed,energy,random_number())))
                elif seed_invalid_number < 2:
                    curr_test.append(' '.join((animal,weight,speed)))
                else:
                    curr_test.append(' '.join((animal,weight,speed,energy)))
            inputs_all.append(curr_test)
        return '\n'.join(map(str, inputs_all[0]))

if __name__ == "__main__":
    print(JavaAss4Generator.generate())
