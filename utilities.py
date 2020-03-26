
#getting the location from the user
def get_loc():
    import pygame
    pygame.init()
    crashed = False
    introScreenImage = pygame.image.load("NTUmap.jpg")
    screen = pygame.display.set_mode((700, 955))
    pygame.display.set_caption("NTU map")
    mouseX = 0
    mouseY = 0
    while not crashed:
        for event in pygame.event.get():                        # get events
            if event.type == pygame.MOUSEBUTTONDOWN:                   # check whether mouse is clicked
                (mouseX, mouseY) = pygame.mouse.get_pos()               # get coordinates tuple
                crashed = True
            if event.type == pygame.QUIT:
                crashed = True                                       # check quit
            screen.blit(introScreenImage, (0, 0))
            pygame.display.flip()
    pygame.quit()
    return mouseX, mouseY


def distance(a,b):
    dist = ((a[1]-b[1])**2 + (a[0]-b[0])**2)**0.5
    return (round(abs(dist),2))

def c_sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sub_li[j][2] > sub_li[j + 1][2]):
                tempo = sub_li[j]
                sub_li[j]= sub_li[j + 1]
                sub_li[j + 1]= tempo
    return sub_li

def price_sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sub_li[j][1] > sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j]= sub_li[j + 1]
                sub_li[j + 1]= tempo
    return sub_li


#formatting time display
def format_t(x):
        if x == 0 or x == 24:
            x = '12am'
        elif x<=12:
            x = f'{x}am'
        else:
            x = f'{x-12}pm'
        return x
