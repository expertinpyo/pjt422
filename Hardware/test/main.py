from pre import *

set_gpio_for_front_door()
set_gpio_for_capacity_check()
lcd = set_display_lcd()
btn = GPIO.input(btnPin)
information['deviceID']=get_deviceID()
# need communication; send deviceID, recieve type, capacityRate
information['type']='PLASTIC'
display_lcd(information['type'])


while True:
    information['userID']=getID()
    # need communication; send userID, recieve userGroup
    information['userGroup']='supervisor'
    information['startTime'] = round(time(),2)
    if(information['userGroup'] in ['supervisor','student']):
        pass_auth()
        while True:
            if (round(time(),2)-information['startTime'] >= 30 and information['frontDoorState']=='close'):
                break
            
            if (btn == False and information['userGroup']='supervisor'
                and information['frontDoorState']=='close'):
                unlock_front_door()
                information['frontDoorState']=='open'
                
            if (btn == False and information['userGroup']='supervisor'
                and information['frontDoorState']=='open'):
                break;
        
        if (information['frontDoorState']=='open'):
            lock_front_door()
            information['frontDoorState']=='close'
        
        the_last_action()
        information['capacityRate'] = current_capacity_rate()
        # need communication; send capacityRate
            
    else:
        fail_auth()
        