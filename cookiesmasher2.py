from cmu_graphics import *

##Backgrounds##
Background = Group(    
    Rect(0, 0, 1300, 800, fill='steelBlue'),
    Rect(100, 0, 100, 800, fill='lightBlue'),
    Rect(300, 0, 100, 800, fill='lightBlue'),
    Rect(500, 0, 100, 800, fill='lightBlue'),
    Rect(700, 0, 100, 800, fill='lightBlue'),
    Rect(900, 0, 100, 800, fill='lightBlue'),
    Rect(1100, 0, 100, 800, fill='lightBlue'),
    Rect(1300, 0, 100, 800, fill='lightBlue')
)

backgroundHalloween = Group(    
    Rect(0, 0, 1300, 800, fill='black'),
    Rect(100, 0, 100, 800, fill='orange'),
    Rect(300, 0, 100, 800, fill='orange'),
    Rect(500, 0, 100, 800, fill='orange'),
    Rect(700, 0, 100, 800, fill='orange'),
    Rect(900, 0, 100, 800, fill='orange'),
    Rect(1100, 0, 100, 800, fill='orange'),
    Rect(1300, 0, 100, 800, fill='orange')
)
backgroundHalloween.visible = False


backgroundHoliday = Group(    
    Rect(0, 0, 1300, 800, fill='steelBlue'),
    Rect(100, 0, 100, 800, fill='lightBlue'),
    Rect(300, 0, 100, 800, fill='lightBlue'),
    Rect(500, 0, 100, 800, fill='lightBlue'),
    Rect(700, 0, 100, 800, fill='lightBlue'),
    Rect(900, 0, 100, 800, fill='lightBlue'),
    Rect(1100, 0, 100, 800, fill='lightBlue'),
    Rect(1300, 0, 100, 800, fill='lightBlue')
)


#Cookie

cookieBigShadow = Circle(640, 405, 150, opacity=20, visible=False)
cookieBig = Circle(650, 400, 150, fill='tan', visible=False)
cookieSmallShadow = Circle(640, 405, 130, opacity=20, visible=False)
cookieSmall = Circle(650, 400, 130, fill='tan', visible=False)


#Main Menu Buttons
Button1 = Rect(500, 250, 250, 100, fill='white', border='black', borderWidth=3)
Button2 = Rect(500, 400, 250, 100, fill='white', border='black', borderWidth=3)
Button3 = Rect(500, 550, 250, 100, fill='white', border='black', borderWidth=3)

#Upgrade Menu
UpgradeMenu = Rect(0, 0, 1300, 800, fill='tan', visible=False)
upgradeMenuButton = Rect(980, 0, 300, 100, fill='white', border='black', borderWidth=5, visible=False)
upgradeMenuButtonText = Label('Upgrades', 1130, 50, size=60, fill='black', bold=True, visible=False)

#Main Menu
MainMenu = Group(
    Label('C    kie Smasher', 650, 60, size=100, bold=True, border='black', fill='white'),
    Label('Start', 620, 300, size=50, bold=True),
    Label('Options', 620, 450, size=50, bold=True),
    Label('Quit', 620, 600, size=50, bold=True)
)
Cookieoo = Label('oo', 390, 70, size=100, bold=True, border='black', fill='white')
CookieShape1 = Circle(360, 70, 30, fill='tan', visible=False)
CookieShape2 = Circle(420, 70, 30, fill='tan', visible=False)

#Options Menu
optionsMenu = Rect(0, 0,  1300, 800, fill='white', visible=False)
optionsBackButton = Rect(0, 700, 150, 100, visible=False)

#Info Window
infoWindow = Group(
    Rect(200, 100, 900, 500, fill='gray', border='black', borderWidth=10, opacity=50)
)
infoWindow.visible = False

#Pause Menu
pauseMenu = Group(
    Rect(0, 100, 500, 600),
)
pauseMenu.visible = False

pauseMenuButton1 = Rect(20, 150, 400, 100, fill='white', visible=False)
pauseMenuButton2 = Rect(20, 300, 400, 100, fill='white', visible=False)
pauseMenuButton3 = Rect(20, 450, 400, 100, fill='white', visible=False)

##Mouse Events##

def onMousePress(mouseX, mouseY):
    
    if Button1.hits(mouseX, mouseY) and MainMenu.visible:
        MainMenu.visible = False
        Button1.visible = False
        Button2.visible = False
        Button3.visible = False
        cookieBig.visible = True
        cookieBigShadow.visible = True
        cookieSmall.visible = False
        cookieSmallShadow.visible = False
        CookieShape1.visible = False
        CookieShape2.visible = False
        Cookieoo.visible = False
        upgradeMenuButtonText.visible = True
        upgradeMenuButton.visible = True

    if Button2.hits(mouseX, mouseY) and MainMenu.visible:
        optionsMenu.visible = True
        optionsBackButton.visible = True

    if Button3.hits(mouseX, mouseY):
        exit()
    
    if optionsBackButton.hits(mouseX, mouseY):
        optionsMenu.visible = False
        optionsBackButton.visible = False

    if cookieBig.hits(mouseX, mouseY) and not MainMenu.visible:
        cookieBig.visible = False
        cookieBigShadow.visible = False
        cookieSmall.visible = True
        cookieSmallShadow.visible = True
    
    if Cookieoo.hits(mouseX, mouseY):
        CookieShape1.visible = True
        CookieShape2.visible = True

    if upgradeMenuButton.hits(mouseX, mouseY):
        UpgradeMenu.visible = True
        cookieBig.visible = False
        cookieSmall.visible = False
        upgradeMenuButtonText.visible = False
        upgradeMenuButton.visible = False

    if pauseMenuButton1.hits(mouseX, mouseY):
        pauseMenu.visible = False
        pauseMenuButton1.visible = False

    if pauseMenuButton3.hits(mouseX, mouseY):
        exit()
    
def onMouseMove(mouseX, mouseY):
    if cookieBig.contains(mouseX, mouseY) and not MainMenu.visible:
        cookieBig.border = 'black'

def onMouseRelease(mouseX, mouseY):
    
    if not MainMenu.visible:
        cookieBig.visible = True
        cookieBigShadow.visible = True
        cookieSmall.visible = False
        cookieSmallShadow.visible = False

def onKeyPress(key):
    if (key == "m") and not MainMenu.visible:
        infoWindow.visible = True

    if (key == "escape") and not MainMenu.visible:
        pauseMenu.visible = True
        pauseMenuButton1.visible = True
        pauseMenuButton2.visible = True
        pauseMenuButton3.visible = True


def onKeyRelease(key):
    if (key == "m") and infoWindow.visible:
        infoWindow.visible = False

app.width = 1300
app.height = 1300

cmu_graphics.run()