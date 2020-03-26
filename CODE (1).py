import tkinter as tk
from functools import partial
from datetime import datetime
from datetime import date
from datetime import time
import math
import os
import sys
import pickle
from utilities import *

maroon = '#ab2440'
purple ='#2f1e30'
yellow ='#efc046'
yellow = '#ffe682'
orange = '#ef9f36'
font_t = 'Franklin Gothic Heavy'
font_n = 'Segoe Print'
font_b = 'Constantia'
teal = '#3e8984'
teal_d = '#42705b'
purple_1 = '#4c2c4d'
pink = '#e499d3'

obj=open('datadump.pickle','rb')
canteen2 = pickle.load(obj)
koufu = pickle.load(obj)
tamarind = pickle.load(obj)
canteen14 = pickle.load(obj)
northspine = pickle.load(obj)
compiled_data = pickle.load(obj)
canteen = pickle.load(obj)
timing = pickle.load(obj)
waiting = pickle.load(obj)
coordinates = pickle.load(obj)
red_bus = pickle.load(obj)
red = pickle.load(obj)
blue_bus = pickle.load(obj)
blue = pickle.load(obj)
favourites = pickle.load(obj)

stalls ={'Koufu'      : koufu.keys(),
         'North Spine': northspine.keys(),
         'Canteen 14' : canteen14.keys(),
         'Canteen 2'  : canteen2.keys(),
         'Tamarind'   : tamarind.keys()}

date_x = ''
hour = 0
user_location  = (0,0)
weekday = 0


root = tk.Tk()
root.resizable(0,0)
background_image = tk.PhotoImage(file = "food1.png")


#some frequently used functions
def back_button(page):
    back_button = tk.Button(page, text = "←",
                            font = 30,
                            justify = tk.CENTER,
                            command =page.destroy)
    back_button.place(relwidth = 0.05, relheight = 0.04)

def page_bg(page):
    home_page_bg = tk.Label(page,
                            image = background_image)
    home_page_bg.place(relwidth = 1, relheight = 1)
    
def frame_labels(page, colour = orange):
    frame_label = tk.Frame(page,
                     bg = colour,
                     bd = 6)
    return frame_label
def frame_buttons(page):
    frame_button = tk.Frame(page,
                     bg = orange,
                     bd = 0)
    return frame_button

def create_button(page, button_text, button_command, fontt = (font_b,15), colour =orange):
    button = tk.Button(page,
                       text = button_text,
                       bg = colour,
                       font = fontt,
                       fg = 'black',
                       command = button_command)
    button.place(relwidth = 1, relheight = 1)
    return button
def create_title(page, title_text):
    title_bg = frame_labels(page)
    title_bg.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.15, anchor = 'n')

    title = tk.Label(title_bg,
                     text = title_text,
                     bg = yellow,
                     font = (font_t, 20))
    title.place(relwidth = 1, relheight = 1)
def close_button(page):
    close_button = tk.Button(page, text = "close",
                            justify = tk.CENTER,
                            command =root.destroy)
    close_button.place(relx = 0.9,relwidth = 0.1, relheight = 0.04)
def standard_page(page, title_text):
    page.place(relwidth = 1, relheight = 1)
    page_bg(page)
    back_button(page)
    create_title(page, title_text)
    close_button(page)


def transit(a, search):
        top = tk.Toplevel()
        top.title("Get directions")
        top.geometry("600x600+120+120")
        frame = tk.Frame(top,
                     bd = 6,
                     bg = orange)
        frame.place(relwidth =1, relheight = 1)
        bag = tk.Frame(frame,
                       bg = purple_1)
        bag.place(relwidth =1, relheight = 1)
        x = a[0]
        y = a[1]
        #calculating nearest bus stop to current destination
        temp1={}
        for key in red_bus:
                    a=red_bus[key][0]
                    b=red_bus[key][1]
                    c=coordinates[search][0]
                    d=coordinates[search][1]
                    sq1= abs(a*a - c*c)
                    sq2= abs(b*b - d*d)
                    z= math.sqrt(sq1+sq2)
                    temp1.update({key:z})
        r=min(temp1, key= lambda k: temp1.get(k))      
        temp2={}
        for key in blue_bus:
                    a=blue_bus[key][0]
                    b=blue_bus[key][1]
                    c=coordinates[search][0]
                    d=coordinates[search][1]
                    sq1= abs(a*a - c*c)
                    sq2= abs(b*b - d*d)
                    z= math.sqrt(sq1+sq2)
                    temp2.update({key:z})
        s=min(temp2, key= lambda k: temp2.get(k))
       
        curr1=r
        curr2=s
        text1 = tk.Label(frame,
                         bg = purple_1,
                         fg = yellow,
                         font = (font_n,11,'bold'),
                         text = f'Nearest Campus Red stop to destination: {curr1}')
        text1.place(relheight = 0.1, relwidth = 1)
        text2 = tk.Label(frame,
                         bg = purple_1,
                         fg = yellow,
                         font = (font_n,11,'bold'),
                         text = f'Nearest Campus Blue stop to destination: {curr2}')
        text2.place(relheight = 0.1, rely = 0.1, relwidth = 1)

        #calculating nearest bus stop to current location
        temp3={}
        for key in red_bus:
                    a=red_bus[key][0]
                    b=red_bus[key][1]
                    sq1= abs(a*a - x*x)
                    sq2= abs(b*b - y*y)
                    z= math.sqrt(sq1+sq2)
                    temp3.update({key:z})
        r=min(temp3, key= lambda k: temp3.get(k))
       
        text3 = tk.Label(frame,
                         bg = purple_1,
                         fg = yellow,
                         font = (font_n,10,'bold'),
                         text = f'Nearest Campus Red bus stop to your current location: {r}')
        text3.place(relheight = 0.1, rely = 0.2, relwidth = 1)
        temp4={}
        for key in blue_bus:
                    a=blue_bus[key][0]
                    b=blue_bus[key][1]
                    sq1= abs(a*a - x*x)
                    sq2= abs(b*b - y*y)
                    z= math.sqrt(sq1+sq2)
                    temp4.update({key:z})
        s=min(temp4, key= lambda k: temp4.get(k))

        text4 = tk.Label(frame,
                         bg = purple_1,
                         fg = yellow,
                         font = (font_n,10,'bold'),
                         text = f'Nearest Campus Blue bus stop to your current location: {s}')
        text4.place(relheight = 0.1, rely = 0.3, relwidth = 1)

        #calculating number of bus stops between destination and location
    
        q,f,d,v,w,e=0,0,0,0,0,0

        for i in range (0,len(red)):
            if curr1==red[i]:
                q=i
            if r== red[i]:
                w=i
            else:
                continue
         
        if(q==w):
            v=0
        elif 0 <= w <= 12 and 0<q<w:
            v= abs(w-12-q)+1
        elif 0 <= w <= 12 and q>w:
            v= abs(w-q)
               

        for i in range (0,len(blue)):
            if curr2 == blue[i]:
                f=i
            if s== blue[i]:
                d=i
            else:
                continue
        if(f==d):
            e=0
        elif 0 <= f <= 11 and 0<d<f:
            e=abs(f-d)
        elif 0 <= f <= 11 and d>f:
            e=abs(d-11-f)+1  
 
        text5 = tk.Label(frame,
                         bg = purple_1,
                         fg = 'white',
                         font = (font_n,15,'bold'),
                        text = f'Number of bus stops taken by Campus Red: {v}')
        text5.place(relheight = 0.1, rely = 0.4, relwidth = 1)

        text6 = tk.Label(frame,
                         bg = purple_1,
                         fg = 'white',
                         font = (font_n,15,'bold'),
                        text = f'Number of bus stops taken by Campus Blue: {e}')
        text6.place(relheight = 0.1, rely = 0.5, relwidth = 1)

        def live():
            os.system("start \"\" https://baseride.com/maps/public/ntu/") 
        abc = tk.Button(top,
                        bg = orange,
                        font = (font_b,15),
                        text = 'check live status',
                        command = live)
        abc.place(relheight = 0.1, rely = 0.8, relwidth = 0.3, relx = 0.5, anchor = 'n')      


def op_hours(stall, canteen, bfast):
    top = tk.Toplevel(root)
    top.geometry("300x300+120+120")
    frame = tk.Frame(top,
                     bd = 6,
                     bg = orange)
    frame.place(relwidth =1, relheight = 1)

    
    sat = 'closed'
    sun = 'closed'
    wll = format_t(timing[canteen][stall][0][0])
    wul = format_t(timing[canteen][stall][0][1])
    if wll == '12am' and wul == '12am':
        wk = 'open 24 hours'
    else:
        wk = f'{wll} to {wul}'
        
    if timing[canteen][stall][1] != 0:
        sll = format_t(timing[canteen][stall][1][0])
        sul = format_t(timing[canteen][stall][1][1])
        if sll == '12am' and sul == '12am':
            sat = 'open 24 hours'
        else:
            sat = f'{sll} to {sul}'

    
    if timing[canteen][stall][2] != 0:
        sull = format_t(timing[canteen][stall][2][0])
        suul = format_t(timing[canteen][stall][2][1])
        if sull == '12am' and suul == '12am':
            sun = 'open 24 hours'
        else:
            sun = f'{sull} to {suul}'

    if len(bfast) ==0:
        message  = 'weekday: '+ wk + '\nsaturday: '+sat+'\nsunday: '+sun
        text1 = tk.Label(frame,
                         bg = purple_1,
                         font = (font_n,15,'bold'),
                         fg = 'white',
                        text = message)
        text1.place(relwidth = 1, relheight = 1)

    else:
        message  = 'weekday: '+ wk + '\nsaturday: '+sat+'\nsunday: '+sun
        text1 = tk.Label(frame,
                         bg = purple_1,
                         font = (font_n,15,'bold'),
                         fg = 'white',
                        text = message)
        text1.place(relwidth = 1, relheight = 0.6)
        text2 = tk.Label(frame,
                         bg = purple_1,
                         font = (font_n,12,'bold'),
                         fg = 'white',
                        text = 'This stall operates on breakfast menu\nuntil 11am on operating days')
        text2.place(rely = 0.6, relwidth = 1, relheight = 0.4)        
    
def op_status(stall_name, canteen_name, bfast= []):
    message = 'This stall is not operating'
    if weekday < 5:
        if timing[canteen_name][stall_name][0][0] <= int(hour) < timing[canteen_name][stall_name][0][1]:
            if len(bfast) != 0 and int(hour) < 11:
                message = 'This stall is currently operating on Breakfast menu'
            elif len(bfast) != 0 and 11 <= int(hour):
                message = 'This stall is currently operating on Day menu'
            else:
                message = 'This stall is currently operating'
    if weekday == 5:
        if timing[canteen_name][stall_name][1]!=0:
            if timing[canteen_name][stall_name][1][0] <= int(hour) < timing[canteen_name][stall_name][1][1]:
                if len(bfast) != 0 and int(hour) < 11:
                    message = 'This stall is currently operating on Breakfast menu'
                elif len(bfast) != 0 and 11 <= int(hour):
                    message = 'This stall is currently operating on Day menu'
                else:
                    message = 'This stall is currently operating'

    if weekday == 6:
        if timing[canteen_name][stall_name][2]!=0:
            if timing[canteen_name][stall_name][2][0] <= int(hour) < timing[canteen_name][stall_name][2][1]:
                if len(bfast) != 0 and int(hour) < 11:
                    message = 'This stall is currently operating on Breakfast menu'
                elif len(bfast) != 0 and 11 <= int(hour):
                    message = 'This stall is currently operating on Day menu'
                else:
                    message = 'This stall is currently operating'
    return message

def time_calculation(stall,canteen):
    global hour
    hour = int(hour)
    if(9<=hour<11 or 12<=hour<2 or 18<=hour<20):
        per_person=waiting[canteen][stall][0]
    else:
        per_person=waiting[canteen][stall][1]
    return per_person

def waiting_time(people, waitingtime_bg, stall, canteen):
        if people.isdigit():
            people_waiting = int(people)
            per_person=time_calculation(stall,canteen)
            waiting_time = people_waiting*per_person
            waiting = tk.Label(waitingtime_bg,
                               bg = orange,
                                font = (font_n, 10, 'bold'),
                               text = f'estimated waiting time: approximately {waiting_time} minutes')
            waiting.place(relx = 0.05, rely = 0.75, relwidth = 0.9, relheight = 0.2)
        else:
            waiting = tk.Label(waitingtime_bg,
                               bg = orange,
                                font = (font_n, 11, 'bold'),
                                fg = 'red',
                               text = 'Enter a Valid Input!')
            waiting.place(relx = 0.05, rely = 0.75, relwidth = 0.9, relheight = 0.2)



              

#page displays the specified stall info
def stall_info(stall_name, canteen_name):
    stall_info_page = tk.Frame(root,
                               bg = orange,
                               bd = 6)
    standard_page(stall_info_page, title_text = f'{stall_name} @ {canteen_name}')
    #menu
    menu_bg = frame_labels(page = stall_info_page)
    menu_bg.place(relx = 0.5, rely = 0.3, relwidth = 0.75, relheight = 0.43, anchor = 'n')
    image = tk.Label(menu_bg,
                      bg = purple_1)
    image.place(relwidth = 1, relheight = 1)




    
    menu_list =[]
    bfast_list = []
    
    for dishes in compiled_data[canteen_name][stall_name][0]:
        menu_list.append([dishes[0],dishes[1],dishes[2]])
    
    for dishes in compiled_data[canteen_name][stall_name][1]:
        bfast_list.append([dishes[0],dishes[1],dishes[2]])

        

    def print_menu(menu,bfast):
        if len(bfast) == 0:
            dish = 'ITEM\n\n'
            prices = 'PRICE\n\n'
            calories = 'CALORIES\n\n'
            for items in menu:
                dish += f'{items[0]}\n'
                prices += f'{items[1]}\n'
                calories += f'{items[2]}\n'
                
            dish_list = tk.Label(menu_bg,
                                 bg = purple_1,
                             fg = 'white',
                             font = ( font_n, 10, 'bold'),
                            text = dish)
            dish_list.place(relx = 0, relwidth = 0.5, relheight = 1)

            price_list = tk.Label(menu_bg,
                                   bg = purple_1,
                             fg = 'white',
                             font = ( font_n, 10, 'bold'),
                            text = prices)
            price_list.place(relx = 0.5, relwidth = 0.25, relheight = 1)

            calories_list = tk.Label(menu_bg,
                                      bg = purple_1,
                             fg = 'white',
                             font = ( font_n, 10, 'bold'),
                            text = calories)
            calories_list.place(relx = 0.75, relwidth = 0.25, relheight = 1)
        else:
            dish = 'ITEM\n'
            prices = 'PRICE\n'
            calories = 'CALORIES\n'
            dish_b = 'ITEM\n'
            prices_b = 'PRICE\n'
            calories_b = 'CALORIES\n'
            for items in menu:
                dish += f'{items[0]}\n'
                prices += f'{items[1]}\n'
                calories += f'{items[2]}\n'
            for items in bfast:
                dish_b += f'{items[0]}\n'
                prices_b += f'{items[1]}\n'
                calories_b += f'{items[2]}\n'
                
            text1 = tk.Label(menu_bg,
                             bg = purple_1,
                             fg = yellow,
                             font = ( font_t, 10),
                             text = 'Breakfast Menu')
            text1.place(relx = 0, relwidth = 1, relheight = 0.05)
            dish_b_list = tk.Label(menu_bg,
                                   bg = purple_1,
                             fg = 'white',
                             font = ( font_n, 9, 'bold'),
                            text = dish_b)
            dish_b_list.place(rely = 0.05, relx = 0, relwidth = 0.5, relheight = 0.5)

            price_b_list = tk.Label(menu_bg,
                                    bg = purple_1,
                             fg = 'white',
                             font = ( font_n, 9, 'bold'),
                            text = prices_b)
            price_b_list.place(rely = 0.05,relx = 0.5, relwidth = 0.25, relheight = 0.5)

            calories_b_list = tk.Label(menu_bg,
                                       bg = purple_1,
                             fg = 'white',
                             font = ( font_n, 9, 'bold'),
                            text = calories_b)
            calories_b_list.place(rely = 0.05,relx = 0.75, relwidth = 0.25, relheight = 0.5)
    

            text2 = tk.Label(menu_bg,
                             bg = purple_1,
                             fg = yellow,
                             font = ( font_t, 10, ),
                             text = 'Day Menu')
            text2.place(rely = 0.5, relx = 0, relwidth = 1, relheight = 0.05)        
            dish_list = tk.Label(menu_bg,
                                 bg = purple_1,
                             fg = 'white',
                             font = ( font_n, 9, 'bold'),
                            text = dish)
            dish_list.place(rely = 0.55, relx = 0, relwidth = 0.5, relheight = 0.45)

            price_list = tk.Label(menu_bg,
                                  bg = purple_1,
                             fg = 'white',
                             font = ( font_n, 9, 'bold'),
                            text = prices)
            price_list.place(relx = 0.5, relwidth = 0.25, relheight = 0.45, rely = 0.55)

            calories_list = tk.Label(menu_bg,
                                     bg = purple_1,
                             fg = 'white',
                             font = ( font_n, 9, 'bold'),
                            text = calories)
            calories_list.place(relx = 0.75, relwidth = 0.25, relheight = 0.45, rely = 0.55)

    print_menu(menu_list,bfast_list)

    def sort_by_price(list1,list2):
        list1 = price_sort(list1)
        list2 = price_sort(list2)
        print_menu(list1,list2)

    def sort_by_calorie(list1,list2):
        list1 = c_sort(list1)
        list2 = c_sort(list2)
        print_menu(list1,list2)


    sort_p = frame_buttons(stall_info_page)
    sort_p.place(relx = 0.05, relwidth = 0.2125, relheight = 0.04)
    create_button(page = sort_p, button_text = 'sort by price', button_command = partial(sort_by_price, menu_list, bfast_list), fontt = (font_b,10), colour = pink)

    sort_c = frame_buttons(stall_info_page)
    sort_c.place(relx = 0.2625, relwidth = 0.2125, relheight = 0.04)
    create_button(page = sort_c, button_text = 'sort by calories', button_command = partial(sort_by_calorie, menu_list, bfast_list), fontt = (font_b,10), colour = pink)

    directions_bg = frame_buttons(stall_info_page)
    directions_bg.place(relx = 0.475, relwidth = 0.2125, relheight = 0.04)
    create_button(page = directions_bg, button_text = 'Get Directions', button_command = partial(transit, user_location, canteen_name), fontt = (font_b,10), colour = pink)

    operating_bg = frame_buttons(stall_info_page)
    operating_bg.place(relx = 0.6875, relwidth = 0.2125, relheight = 0.04)
    create_button(page = operating_bg, button_text = 'Operating Hours', button_command = partial(op_hours, stall_name,canteen_name, bfast_list), fontt = (font_b,10), colour = pink)


    message = op_status(stall_name ,canteen_name, bfast_list)
    operating_status = tk.Label(stall_info_page,
                                bg = orange,
                                font = (font_n, 16, 'bold'),
                                text = message)
    operating_status.place(rely = 0.95, relheight = 0.05, relwidth = 1)
                                


    #waiting time
    waitingtime_bg = frame_labels(page = stall_info_page)
    waitingtime_bg.place(relx = 0.5, rely = 0.73, relwidth = 0.75, relheight = 0.2, anchor = 'n')
    people_input = tk.Entry(waitingtime_bg,
                            font = 40)
    people_input.place(relx = 0.05, rely = 0.43, relwidth = 0.6, relheight = 0.3)

    text_1 = tk.Label(waitingtime_bg,
                       bg = orange,
                                font = (font_t, 15),
                                fg = purple,
                      text = 'Calculate the waiting time')
    text_1.place(relx = 0.05, relwidth = 0.9, relheight = 0.18)
    text_2 = tk.Label(waitingtime_bg,
                      justify = tk.LEFT,
                      bg = orange,
                                font = (font_n, 10),
                                fg = 'white',
                      text = 'Enter the number of people queueing below')
    text_2.place(relx = 0.05, relwidth = 0.9, relheight = 0.18, rely = 0.23)

    calculate_bg = frame_buttons(page = waitingtime_bg)
    calculate_bg.place(relx = 0.67, rely = 0.43, relwidth = 0.28, relheight = 0.3)
    calculate =create_button(page = calculate_bg, button_text ='calculate!' , button_command = lambda: waiting_time(people_input.get(),waitingtime_bg, stall_name, canteen_name))


#page dispays all stalls in a specified canteen 
def stall(canteen_name):
    stall_main_page = tk.Frame(root,
                               bd = 6,
                               bg = orange)
    standard_page(stall_main_page, title_text = f'Select a Stall from {canteen_name}')

    def create_stall_button(button_text, button_command, position):
        frame = frame_buttons(stall_main_page)
        frame.place (relx = 0.5, rely = position, relheight = 0.07, relwidth = 0.4, anchor = 'n')
        button = create_button(frame, button_text, button_command)
    
    position =0.18
    for name in stalls[canteen_name]:
        position += 0.13
        create_stall_button(button_text = name, button_command = partial(stall_info, name, canteen_name) , position = position)
        message = op_status(name,canteen_name)
        operating_status = tk.Label(stall_main_page,
                                    image = background_image,
                                    compound = tk.CENTER,
                                bg = orange,
                                font = (font_n, 9, 'bold'),
                                fg = 'white',
                                text = message)
        operating_status.place(rely = position + 0.07, relheight = 0.03, relwidth = 0.35, relx = 0.5, anchor = 'n')
        
    directions_bg = frame_buttons(stall_main_page)
    directions_bg.place(relx = 0.05, relwidth = 0.2, relheight = 0.04)
    create_button(page = directions_bg, button_text = 'Get Directions', button_command = partial(transit, user_location, canteen_name), fontt = (font_b,10), colour = pink)

        
#page displays all the canteens
def browse_canteen():
    canteen_main_page = tk.Frame(root,
                                 bd = 6,
                                 bg = orange)
    standard_page(canteen_main_page, title_text = 'Select a Canteen')

    
    def create_canteen_button(button_text, button_command, position):
        frame = frame_buttons(canteen_main_page)
        frame.place (relx = 0.5, rely = position, relheight = 0.07, relwidth = 0.4, anchor = 'n')
        button = create_button(frame, button_text, button_command)

    position =0.18
    for name in canteen:
        position += 0.13
        create_canteen_button(button_text = name, button_command = partial(stall, name) , position = position)

    

    def dist_sort(a):
        distances = {}
        for i in coordinates:
            distances[i]=distance(a,coordinates[i])
        canteen_sorted = []
        for key in sorted(distances.items(), key = lambda kv:(kv[1], kv[0])):
            canteen_sorted.append(key[0])

        position =0.18
        for name in canteen_sorted:
            position += 0.13
            create_canteen_button(button_text = name, button_command = partial(stall, name) , position = position)

            
    global user_location
    sort_bg = frame_buttons(canteen_main_page)
    sort_bg.place(relx = 0.05, relwidth = 0.3, relheight = 0.04)
    create_button(page = sort_bg, button_text = 'sort by distance', button_command = lambda:dist_sort(user_location), fontt = (font_b,10), colour = pink)   



def browse_dish():
    dish_search_page = tk.Frame(root,
                                bg = orange,
                                bd = 6)
    standard_page(dish_search_page, title_text = 'Search by Dish')

    frame = frame_labels(page = dish_search_page)
    frame.place(relx = 0.5, rely = 0.3, relwidth = 0.75, relheight = 0.6, anchor = 'n')
    image = tk.Label(frame,
                      bg = purple_1)
    image.place(relwidth = 1, relheight = 1)
    Title = tk.Label(frame ,
                     bg = purple_1,
                     fg = 'white',
                     font = (font_n,15, 'bold'),
                     text = "What would you like to eat?")
    Title.place(relx = 0.5, rely = 0.05, relwidth = 0.99, relheight = 0.1, anchor = 'n')

    def dish_search(dish):
        clear = frame_labels(frame, purple_1)
        clear.place(rely = 0.4, relwidth = 1, relheight = 0.6)
        canteens = []
        for canteen,stalls in compiled_data.items():
            dish = dish.lower().replace(' ','')
            for stall, menu in stalls.items():
                for day_bfast in menu:
                    if len(day_bfast) != 0:
                        for items in day_bfast:
                            dish_to_check = items[0].lower().replace(' ','')
                            if dish == dish_to_check and (stall,canteen) not in canteens :
                                canteens.append ((stall, canteen))
        if len(canteens) == 0:
            text = tk.Label(frame,
                            fg = 'red',
                            bg = purple_1,
                             font = (font_n,11,'bold'),
                            text = 'Sorry this dish is not available in any of the canteens!')
            text.place(relx = 0.5, rely = 0.4, relwidth = 1, relheight = 0.1, anchor = 'n')
        else:
            text = tk.Label(frame,
                            bg = purple_1,
                            fg = 'light green',
                             font = (font_n,12,'bold'),
                            text = 'This dish is available in the following Canteens')
            text.place(relx = 0.5, rely = 0.4, relwidth = 1, relheight = 0.1, anchor = 'n')
            position =  0.55
            for stall,canteen in canteens:
                canteen_bg = frame_buttons(page = frame)
                canteen_bg.place(relx = 0.2, rely = position, relwidth = 0.6, relheight = 0.1)
                create_button(page = canteen_bg, button_text = f'{stall}@{canteen}', button_command =partial(stall_info, stall, canteen))
                message = op_status(stall,canteen)
                operating_status = tk.Label(frame, 
                                bg = purple_1,
                                font = (font_n, 9, 'bold'),
                                fg = 'white',
                                text = message)
                operating_status.place(rely = position + 0.1, relheight = 0.05, relwidth = 0.5, relx = 0.5, anchor = 'n')
                position += 0.15

    
    dish = tk.Entry(frame,
                    font = 15,
                    bg = 'light yellow')
    dish.place(relx = 0.1, rely = 0.2, relwidth = 0.5, relheight = 0.1)
    search_bg = frame_buttons(frame)
    search_bg.place(relx = 0.62, rely = 0.2, relwidth = 0.28, relheight = 0.1)
    search = create_button(page = search_bg, button_text = 'search', button_command = lambda: dish_search(dish.get()))



def browse_stall():
    stall_search_page = tk.Frame(root,
                                 bg = orange,
                                 bd = 6)
    standard_page(stall_search_page, title_text = 'Search by Stalls')

    frame = frame_labels(page = stall_search_page)
    frame.place(relx = 0.5, rely = 0.3, relwidth = 0.75, relheight = 0.6, anchor = 'n')
    image = tk.Label(frame,
                      bg = purple_1)
    image.place(relwidth = 1, relheight = 1)
    Title = tk.Label(frame,
                     bg = purple_1,
                     fg = 'white',
                     font = (font_n,15, 'bold'),
                     text = "which stall would you like to eat at?")
    Title.place(relx = 0.5, rely = 0.05, relwidth = 0.99, relheight = 0.1, anchor = 'n')

    def stall_search(stall):
        clear = frame_labels(frame, purple_1)
        clear.place(rely = 0.4, relwidth = 1, relheight = 0.6)
        
        canteens = []
        for canteen,stalls in compiled_data.items():
            stall = stall.lower().replace(' ','')
            for stall_to_check in stalls.keys():
                if stall == stall_to_check.lower().replace(' ',''):
                    canteens.append ((stall_to_check, canteen))
        if len(canteens) == 0:
            text = tk.Label(frame,
                            bg = purple_1,
                            fg = 'red',
                             font = (font_n,11,'bold'),
                            text = 'Sorry this stall is not available in any of the canteens!')
            text.place(relx = 0.5, rely = 0.4, relwidth = 1, relheight = 0.1, anchor = 'n')
        else:
            text = tk.Label(frame,
                            bg = purple_1,
                            fg = 'light green',
                             font = (font_n,12,'bold'),
                            text = 'This stall is available in the following Canteens')
            text.place(relx = 0.5, rely = 0.4, relwidth = 1, relheight = 0.1, anchor = 'n')
            position =  0.55
            for stall_to_check,canteen in canteens:
                canteen_bg = frame_buttons(page = frame)
                canteen_bg.place(relx = 0.3, rely = position, relwidth = 0.4, relheight = 0.1)
                create_button(page = canteen_bg, button_text = canteen, button_command =partial(stall_info, stall_to_check, canteen))
                message = op_status(stall_to_check,canteen)
                operating_status = tk.Label(frame, 
                                bg = purple_1,
                                font = (font_n, 9, 'bold'),
                                fg = 'white',
                                text = message)
                operating_status.place(rely = position + 0.1, relheight = 0.05, relwidth = 0.5, relx = 0.5, anchor = 'n')
                position += 0.15
                

    
    stall = tk.Entry(frame, bg = 'light yellow', font = 15)
    stall.place(relx = 0.1, rely = 0.2, relwidth = 0.5, relheight = 0.1)
    search_bg = frame_buttons(frame)
    search_bg.place(relx = 0.62, rely = 0.2, relwidth = 0.28, relheight = 0.1)
    search = create_button(page = search_bg, button_text = 'search', button_command = lambda: stall_search(stall.get()))

   

def fav():
    fav_page = tk.Frame(root,
                        bd = 6,
                        bg = orange)
    
    fav_page.place(relwidth = 1, relheight = 1)
    page_bg(fav_page)
    back_button(fav_page)

    title = tk.Label(fav_page,
                     compound = tk.CENTER,
                    image = background_image,
                        fg = yellow,
                        font = (font_n,20,'bold'),
                     text = 'These are your favourites')
    title.place(relx = 0.5, relheight = 0.08, relwidth = 0.8, rely = 0.05, anchor = 'n')


    def display_fav():
        global favourites
        frame = tk.Frame(fav_page)
        frame.place(rely = 0.13, relheight =0.77, relwidth = 1)
        page_bg(frame)
        position =  0.15
        for stall,canteen in favourites:
            canteen_bg = frame_buttons(page = fav_page)
            canteen_bg.place(relx = 0.3, rely = position, relwidth = 0.4, relheight = 0.05)
            create_button(page = canteen_bg, button_text = f'{stall}@{canteen}', button_command =partial(stall_info,stall,canteen))
            position += 0.08   

    def add_remove_fav(info):
        global favourites
        valid = True
        try:
            info = info.split(',')
            stall = info[0]
            canteen = info[1]
            for canteen_a in compiled_data.keys():
                if canteen.lower().replace(' ','') == canteen_a.lower().replace(' ',''):
                    canteen = canteen_a
                    valid = True
                    break
                    
                    
                else:
                    valid = False
            if canteen in compiled_data.keys():
                for stall_a in compiled_data[canteen].keys():
                            if stall.lower().replace(' ','') == stall_a.lower().replace(' ',''):
                                stall = stall_a
                                valid = True
                                break
                            else:
                                valid = False
            else:
                valid = False
        except:
            valid = False
        if valid:
            message = 'Ok!'
            text1 = tk.Label(fav_page,
                             compound = tk.CENTER,
                                        image = background_image,
                                        fg = 'light green',
                                        font = (font_n,12,'bold'),
                     text = message)
            text1.place(relheight = 0.06, relwidth = 0.2, rely = 0.94, relx = 0.8)
            item = (stall, canteen)
            if item in favourites:
                favourites.remove(item)
            else:
                favourites.append(item)
            display_fav()
        else:
            message = 'Invalid Input!'
            text1 = tk.Label(fav_page,
                             compound = tk.CENTER,
                                        image = background_image,
                                        fg = 'red',
                                        font = (font_n,12,'bold'),
                     text = message)
            text1.place(relheight = 0.06, relwidth = 0.2, rely = 0.94, relx = 0.8)
    

    display_fav()

    instruction = tk.Label(fav_page,
                           compound = tk.CENTER,
                                        image = background_image,
                                        fg = 'white',
                                        font = (font_n,10,'bold'),
                           text = 'Enter stall,canteen to add or remove from favourites e.g. mala,Tamarind')
    instruction.place(relheight = 0.04, relwidth = 1, rely = 0.9)
    entry = tk.Entry(fav_page,
                     bg = 'light yellow',
                     font = 15)
    entry.place(relheight = 0.06, relwidth = 0.48, rely = 0.94, relx = 0.1)    
    button_bg = frame_buttons(fav_page)
    button_bg.place(relheight = 0.06, relwidth = 0.2, rely = 0.94, relx = 0.6)
    create_button(page = button_bg, button_text = 'Add/Remove', button_command =lambda: add_remove_fav(entry.get()))



def services_page():
    services_main_page = tk.Frame(root,
                                  bd = 6,
                                  bg = orange)
    standard_page(services_main_page, title_text = 'What do you want to eat?')

    def create_services_button(button_text, button_command, position):
        frame = frame_buttons(services_main_page)
        frame.place (relx = 0.5, rely = position, relheight = 0.07, relwidth = 0.4, anchor = 'n')
        button = create_button(frame, button_text, button_command)


    create_services_button(button_text = 'Favourites', button_command = fav, position = 0.31)
    create_services_button(button_text = 'Browse by Canteen', button_command = browse_canteen, position = 0.44)
    create_services_button(button_text = 'Browse by Stall', button_command = browse_stall, position = 0.57)
    create_services_button(button_text = 'Browse by Dish', button_command = browse_dish, position = 0.7)


#checks for date and validity accordingly  
def date_check(date_entry, time_page):
                global date_x
                date_x = ''
                global weekday
                weekday = 0
                try:
                    year, month, day = map(int, date_entry.split(','))
                    date_x = date(year, month, day)
                    weekday = date_x.weekday()
                except:
                    invalid = tk.Label(time_page,
                                       compound = tk.CENTER,
                                        image = background_image,
                                        fg = 'red',
                                        font = (font_n,12,'bold'),
                                        text = 'Invalid Input!')
                    invalid.place(relx = 0.7, rely = 0.64,relwidth = 0.3, relheight = 0.07)
                else:
                    invalid = tk.Label(time_page,
                                       compound = tk.CENTER,
                                        image = background_image,
                                        fg = 'light green',
                                        font = (font_n,12,'bold'),
                                       text = 'Ok!')
                    invalid.place(relx = 0.7, rely = 0.64,relwidth = 0.3, relheight = 0.07)
                    feedback = tk.Label(time_page,
                                        compound = tk.CENTER,
                                        image = background_image,
                                        fg = yellow,
                                        font = (font_n,11,'bold'),
                                    text = f'date and time has been set as {date_x} and {hour}')
                    feedback.place(relx = 0.1, rely = 0.85, relwidth = 0.7, relheight = 0.08)
                    if date_x != '' and hour != 0:
                        next_bg = frame_buttons(time_page)
                        next_bg.place(relx = 0.8, rely = 0.85, relwidth = 0.1, relheight = 0.08)
                        create_button(page = next_bg, button_text = 'next', button_command = services_page)

#checks for time and validity accordingly                   
def time_check(time_entry, time_page):
                global hour
                hour = 0
                
                try:
                    
                    hour, minute = map(int, time_entry.split(','))
                except:
                    invalid = tk.Label(time_page,
                                       compound = tk.CENTER,
                                        image = background_image,
                                        fg = 'red',
                                        font = (font_n,12,'bold'),
                                        text = 'Invalid Input!')
                    invalid.place(relx = 0.7, rely = 0.78,relwidth = 0.3, relheight = 0.07)
                        
                else:
                    if(hour>23 or hour<0 or minute>59 or minute<0):
                        invalid = tk.Label(time_page,
                                           compound = tk.CENTER,
                                            image = background_image,
                                            fg = 'red',
                                            font = (font_n,12,'bold'),
                                               text = 'Invalid Input!')
                        invalid.place(relx = 0.7, rely = 0.78,relwidth = 0.3, relheight = 0.07)
                    
                    else:
                        valid = tk.Label(time_page,
                                         compound = tk.CENTER,
                                            image = background_image,
                                            fg = 'light green',
                                            font = (font_n,12,'bold'),
                                               text = 'Ok!')
                        valid.place(relx = 0.7, rely = 0.78,relwidth = 0.3, relheight = 0.07)

                        feedback = tk.Label(time_page,
                                            compound = tk.CENTER,
                                            image = background_image,
                                            fg = yellow,
                                            font = (font_n,11,'bold'),
                                        text = f'date and time has been set as {date_x} and {hour}')
                        feedback.place(relx = 0.1, rely = 0.85, relwidth = 0.7, relheight = 0.08)
                        if date_x != '' and hour != 0:
                            next_bg = frame_buttons(time_page)
                            next_bg.place(relx = 0.8, rely = 0.85, relwidth = 0.1, relheight = 0.08)
                            create_button(page = next_bg, button_text = 'next', button_command = services_page)

def other(time_page):
            global date_x
            date_x = ''
            global hour
            hour = 0
            global weekday
            weekday = 0
                
            #user entry for date           
            Text1 = tk.Label(time_page,
                             justify = tk.LEFT,
                             compound = tk.CENTER,
                             image = background_image,
                             fg = 'white',
                             font = (font_n,15,'bold'),
                             text = 'Enter a date (i.e. 2017,7,20)' )
            Text1.place(relx = 0.1, rely = 0.57, relwidth = 0.8, relheight = 0.07)
            date_entry = tk.Entry(time_page,
                                  bg = 'light yellow',
                                  font = 20)
            date_entry.place(relx = 0.1, rely = 0.64,relwidth = 0.5, relheight = 0.07)
            submit = tk.Button(time_page,
                               text = 'submit',
                               bg = orange,
                               font = (font_b,10),
                               command = lambda: date_check(date_entry.get(), time_page))
            submit.place(relx = 0.6, rely = 0.64,relwidth = 0.1, relheight = 0.07)


            #user entry for time
            Text2 = tk.Label(time_page,
                             justify = tk.LEFT,
                             compound = tk.CENTER,
                             image = background_image,
                             fg = 'white',
                             font = (font_n,15,'bold'),
                             text = 'Enter time in 24 hour format(14,35):' )
            Text2.place(relx = 0.1, rely = 0.71, relwidth = 0.8, relheight = 0.07)
            time_entry = tk.Entry(time_page,
                                  bg = 'light yellow',
                                  font = 20)
            time_entry.place(relx = 0.1, rely = 0.78,relwidth = 0.5, relheight = 0.07)
            submit = tk.Button(time_page,
                               text = 'submit',
                               bg = orange,
                               font = (font_b,10),
                               command = lambda: time_check(time_entry.get(),time_page))
            submit.place(relx = 0.6, rely = 0.78,relwidth = 0.1, relheight = 0.07)




def current(time_page):
            global hour
            global date_x
            global weekday
            date_x = ''
            hour = ''
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            part1 = dt_string[:10]
            part2 = dt_string[11:]
            hour=part2[0:2]

            
            date_x = date.today()
            weekday = date_x.weekday()
            feedback = tk.Label(time_page,
                                text = f'date and time has been set as {date_x} and {hour}',
                                compound = tk.CENTER,
                                image = background_image,
                                fg = yellow,
                                font = (font_n,11,'bold'))
            feedback.place(relx = 0.1, rely = 0.37, relwidth = 0.7, relheight = 0.08)
            next_bg = frame_buttons(time_page)
            next_bg.place(relx = 0.8, rely = 0.37, relwidth = 0.1, relheight = 0.08)
            create_button(page = next_bg, button_text = 'next', button_command = services_page)

            

def location():
    global user_location
    cor_x, cor_y = get_loc()
    if cor_x != 0 and cor_y != 0:
        user_location = (cor_x,cor_y)
        time_page = tk.Frame(root,
                             bg = orange,
                             bd = 6)
        standard_page(time_page, title_text = 'Select your date and time')
        
            

        current_bg = frame_buttons(time_page)
        current_bg.place(relx = 0.5, rely = 0.27, relwidth = 0.75, relheight = 0.08, anchor = 'n')
        create_button(page = current_bg, button_text = 'Current date and time', button_command = partial(current,time_page))


                         
        other_bg = frame_buttons(time_page)
        other_bg.place(relx = 0.5, rely = 0.47, relwidth = 0.75, relheight = 0.08, anchor = 'n')
        create_button(page = other_bg, button_text = 'Other date and time', button_command = partial(other,time_page))
    else:
        error_page = tk.Frame(root)
        error_page.place(relwidth = 1, relheight = 1)
        page_bg(error_page)

        create_title(page = error_page, title_text = "You haven't clicked anything")
        
        back_button = tk.Button(error_page, text = "Go back",
                                font = 30,
                                bg =  orange,
                                justify = tk.CENTER,
                                command =error_page.destroy)
        back_button.place(relx = 0.5, rely = 0.43, relheight = 0.07, relwidth = 0.6, anchor = 'n')

        
def get_location():
    location_page = tk.Frame(root)
    location_page.place(relwidth = 1, relheight = 1)
    page_bg(location_page)
    back_button(location_page)

    title_bg = frame_buttons(location_page)
    title_bg.place(relx = 0.5, rely = 0.45, relheight = 0.1, relwidth = 0.6, anchor = 'n')
    create_button(page = title_bg, button_text = 'Select your location', button_command = location)
    






page_bg(root)

#button to lead to the page listing the main services
hungry_bg = frame_buttons(root)
hungry_bg.place(relx = 0.5, rely = 0.75, relwidth = 0.5 , relheight = 0.07, anchor = 'n')

hungry = create_button(hungry_bg, button_text = 'click me if you are hungry', button_command = get_location)


#welcome message
msg_bg = frame_labels(root)
msg_bg.place(relx = 0.5, rely = 0.25, relwidth = 0.65, relheight = 0.175, anchor = 'n')

msg1 = tk.Label(msg_bg,
                text = "Hello DD4!",
                font = (font_n,15, 'bold'),
                bg = yellow)
msg1.place(relwidth = 1, relheight = 0.5)
msg2 = tk.Label(msg_bg,
                text = "Welcome to NTU food guide",
                bg = yellow,
                font = (font_t,20))             
msg2.place(rely = 0.4, relwidth = 1, relheight = 0.6)

root.title("NTU food guide")
root.geometry("600x600+120+120")
root.mainloop()

