import random

from . import AbsGenerator

def choose_device(seed):
    devices = ["Camera","Heater","Light"]
    devices_cringe = ["randomcringe","-15","52","__"]
    if (seed < 3):
        return devices_cringe[random.randint(0,3)]
    return devices[random.randint(0,2)]

def choose_command(seed):
    commands = ["DisplayAllStatus","TurnOn","TurnOff","StartCharging",
                "StopCharging","SetTemperature","SetBrightness","SetColor",
                "SetAngle","StartRecording","StopRecording"] # except end
    commands_cringe = ["randomcringe","-15","52","random52cringe","__"]
    if (seed < 3):
        return commands_cringe[random.randint(0,4)]
    if (6 <= seed <= 9):
        return "cringe"
    if (seed > 99):
        return "end"
    return commands[random.randint(0,10)]
def choose_color():
    colors = ["YELLOW","WHITE"]
    colors_cringe = ["52","__","RANDOM","YElLOW","WH1TE","WHITe","LoW","low","high","MedIUM"]
    seed = random.randint(1,100)
    if (seed < 3):
        return colors_cringe[random.randint(0,9)]
    return colors[random.randint(0,1)]
def choose_brightness():
    bright = ["HIGH","MEDIUM","LOW"]
    bright_cringe = ["52","__","RANDOM","YElLOW","WH1TE","WHITe","LoW","low","high","MedIUM"]
    seed = random.randint(1,100)
    if (seed < 3):
        return bright_cringe[random.randint(0,9)]
    return bright[random.randint(0,2)]
def choose_temperature():
    seed = random.randint(1,100)
    if (seed < 3):
        return "cringe"
    if (seed < 94):
        return str(random.randint(15,30))
    if (94 < seed < 97):
        return str(random.randint(31,500))
    return str(random.randint(-500,14))
def choose_angle():
    seed = random.randint(1,100)
    if (seed < 3):
        return "cringe"
    if (seed < 94):
        return str(random.randint(-60,60))
    if (94 < seed < 97):
        return str(random.randint(61,500))
    return str(random.randint(-500,-61))

class JavaAss3Generator(AbsGenerator):
    def generate(self):
        fuckup = ["cringe","52","-100","--","__","Camera","safdcasd","100sss","ca_me","end","nomoreshit"]
        commands_main = ["DisplayAllStatus","TurnOn","TurnOff","StartCharging",
                    "StopCharging","SetTemperature","SetBrightness","SetColor",
                    "SetAngle","StartRecording","StopRecording"] # except end
        devices_main = ["Camera","Heater","Light"]
        inputs_all = []
        for _ in range(1):
            lines = random.randint(80,150)
            curr_test = []
            end_added = False
            for i in range(lines):
                curr_line = []
                seed_command = random.randint(1,100)
                seed_device = random.randint(1,100)
                seed_display = random.randint(1,100) # and seed_end (seed to determine whether we need to ruin these 2 commands(display, end) or not)
                seed_deviceid = random.randint(1,100)
                seed_fuckup = random.randint(1,100)
                
                command = choose_command(seed_command)
                device = choose_device(seed_device)
                
                curr_line.append(command)
                if (command == "DisplayAllStatus"):
                    if (seed_display > 95):
                        if (seed_display % 2):
                            curr_line.append(str(random.randint(-100,100)))
                        else:
                            curr_line.append(devices_main[random.randint(0,2)])
                    else:
                        curr_test.append(' '.join(curr_line))
                        continue
                elif (command == "end"):
                    if (seed_display > 97):
                        if (seed_display % 2):
                            curr_line.append(str(random.randint(-100,100)))
                        else:
                            curr_line.append(devices_main[random.randint(0,2)])
                        end_added = True
                    else:
                        curr_test.append(' '.join(curr_line))
                        continue
                else:
                    curr_line.append(device)
                if (not(device in devices_main)):
                    curr_line.append(str(random.randint(-10,100)))
                else:
                    if (device == "Camera"):
                        if (seed_display < 97):
                            curr_line.append(str(random.randint(4,5)))
                        else:
                            curr_line.append(str(random.randint(-100,100)))
                    elif (device == "Heater"):
                        if (seed_display < 97):
                            curr_line.append(str(random.randint(6,9)))
                        else:
                            curr_line.append(str(random.randint(-100,100)))
                    elif (device == "Light"):
                        if (seed_display < 97):
                            curr_line.append(str(random.randint(0,3)))
                        else:
                            curr_line.append(str(random.randint(-100,100)))
                if (not(command in commands_main)):
                    if (seed_display < 20):
                        curr_line.append(choose_color())
                    elif (20 < seed_display < 40):
                        curr_line.append(choose_brightness())
                    elif (40 < seed_display < 60):
                        curr_line.append(choose_brightness())
                        curr_line.append(choose_color())
                    else:
                        curr_line.append(choose_device(random.randint(1,100)))
                else:
                    if (command == "SetTemperature"):
                        curr_line.append(choose_temperature())
                    elif (command == "SetBrightness"):
                        curr_line.append(choose_brightness())
                    elif (command == "SetColor"):
                        curr_line.append(choose_color())
                    elif (command == "SetAngle"):
                        curr_line.append(choose_angle())
                if (seed_fuckup < 3):
                    curr_line.append(fuckup[random.randint(0,len(fuckup) - 1)])
                temp = " ".join(curr_line)
                curr_test.append(temp)
            curr_test.append("end")
            inputs_all.append(curr_test)
    
                
        return '\n'.join(inputs_all[0])


if __name__ == "__main__":
    print(JavaAss3Generator.generate())
    
