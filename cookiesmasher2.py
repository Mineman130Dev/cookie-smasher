from urllib.request import URLopener
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
    Rect(0, 0, 1300, 800, fill='red'),
    Rect(100, 0, 100, 800, fill='green'),
    Rect(300, 0, 100, 800, fill='green'),
    Rect(500, 0, 100, 800, fill='green'),
    Rect(700, 0, 100, 800, fill='green'),
    Rect(900, 0, 100, 800, fill='green'),
    Rect(1100, 0, 100, 800, fill='green'),
    Rect(1300, 0, 100, 800, fill='green')
)
backgroundHoliday.visible = False


##Clicks for the cookie##
clickValue = Label(1, 0, 0, fill=None)
cookieNumber = Label(0, 650, 50, size=80, fill='white')
cps = Label(0, 650, 100, size=40, fill='white')

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


#Shops Menu
ShopMenu = Rect(0, 0, 1300, 800, fill=gradient(rgb(230, 235, 230), rgb(240, 250, 240), start = "top"), visible=False)
shopMenuButton = Rect(0, 0, 300, 100, fill='white', border='black', borderWidth=5, visible=False)
shopMenuButtonText = Label('Shops', 150, 50, size=60, fill='black', bold=True, visible=False)

#Main Menu
MainMenu = Group(
    Label('C    kie Smasher', 650, 60, size=100, bold=True, border='black', fill='white'),
    Label('Start', 620, 300, size=50, bold=True),
    Label('Options', 620, 450, size=50, bold=True),
    Label('Quit', 620, 600, size=50, bold=True),
    Rect(20, 190, 400, 600, fill='gray', border='black', opacity=50, borderWidth=5)

)
Cookieoo = Label('oo', 390, 70, size=100, bold=True, border='black', fill='white')
CookieShape1 = Circle(360, 70, 30, fill='tan', border='black', visible=False)
CookieShape2 = Circle(420, 70, 30, fill='tan', border='black', visible=False)

#Options Menu
optionsMenu = Rect(0, 0,  1300, 800, fill='white', visible=False)
optionsBackButton = Rect(0, 700, 300, 100, visible=False)

#Info Window
infoWindow = Group(
    Rect(200, 100, 900, 500, fill='gray', border='black', borderWidth=10, opacity=50)
)
infoWindow.visible = False

#Pause Menu
pauseMenu = Group(
    Rect(0, 100, 1300, 600, fill='gray', opacity=80, border='black', borderWidth=10),
)
pauseMenu.visible = False

pauseMenuButton1Text = Label('Resume', 220, 170, size=60, visible=False)
pauseMenuButton1 = Rect(20, 120, 400, 100, fill='white', visible=False)
pauseMenuButton2 = Rect(20, 270, 400, 100, fill='white', visible=False)
pauseMenuButton2Text = Label('Options', 220, 320, size=60, visible=False)
pauseMenuButton3 = Rect(20, 420, 400, 100, fill='white', visible=False)
pauseMenuButton3Text = Label('Extras', 220, 470, size=60, visible=False)
pauseMenuButton4 = Rect(20, 570, 400, 100, fill='white', visible=False)
pauseMenuButton4Text = Label('Quit', 220, 620, size=60, visible=False)


##Extras Menu##
extrasMenu = Rect(0, 0, 1300, 800, fill='white', visible=False)
#extrasMenuBackButton = Rect()

##Achivements##
Achivement1 = Group(
    Rect(900, 700, 400, 80),
)
Achivement1Box = Rect(340, 350, 20, 20, fill='gray', border='black', borderWidth=3, visible=False)
Achivement1Close = Label('✘', 350, 360, font='symbols', fill='darkRed', visible=False)

#Images
YixuanImageBackground = Rect(0, 0, 1300, 800, visible=False)
YixuanImage = Image("yixuan.png", 500, 200, visible=False)

shopMenuBackButton = Rect(0, 700, 300, 100, visible=False)
upgradeMenuButtonText2 = Label('Upgrades', 150, 50, size=60, fill='black', bold=True, visible=False)


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
        shopMenuButton.visible = True
        shopMenuButtonText.visible = True

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
        cookieNumber.value += 1

    if (cookieNumber.value == 100):
        Achivement1.visible = True
        Achivement1Box.visible = True
        Achivement1Close.visible = True
    
    if Cookieoo.hits(mouseX, mouseY):
        CookieShape1.visible = True
        CookieShape2.visible = True

    if upgradeMenuButton.hits(mouseX, mouseY):
        UpgradeMenu.visible = True
        cookieBig.visible = False
        cookieSmall.visible = False
        upgradeMenuButtonText.visible = False
        upgradeMenuButton.visible = False
        shopMenuButtonText.visible = False
        upgradeMenuButtonText2.visible = True
        shopMenuBackButton.visible = True

    if pauseMenuButton1.hits(mouseX, mouseY)and pauseMenu.visible:
        pauseMenu.visible = False
        pauseMenuButton1.visible = False
        pauseMenuButton1Text.visible = False
        pauseMenuButton2.visible = False
        pauseMenuButton2Text.visible = False
        pauseMenuButton3.visible = False
        pauseMenuButton3Text.visible = False
        pauseMenuButton4.visible = False
        pauseMenuButton4Text.visible = False

    if pauseMenuButton2.hits(mouseX, mouseY) and pauseMenu.visible:
        optionsMenu.visible = True
        optionsBackButton.visible = True
        pauseMenu.visible = False
        pauseMenuButton1.visible = False
        pauseMenuButton1Text.visible = False
        pauseMenuButton2.visible = False
        pauseMenuButton2Text.visible = False
        pauseMenuButton3.visible = False
        pauseMenuButton3Text.visible = False
        pauseMenuButton4.visible = False
        pauseMenuButton4Text.visible = False

    if pauseMenuButton3.hits(mouseX, mouseY) and pauseMenu.visible:
        extrasMenu.visible = True
        pauseMenu.visible = False
        pauseMenuButton1.visible = False
        pauseMenuButton1Text.visible = False
        pauseMenuButton2.visible = False
        pauseMenuButton2Text.visible = False
        pauseMenuButton3.visible = False
        pauseMenuButton3Text.visible = False
        pauseMenuButton4.visible = False
        pauseMenuButton4Text.visible = False

    if pauseMenuButton4.hits(mouseX, mouseY) and pauseMenu.visible:
        exit()

    if shopMenuButton.hits(mouseX, mouseY):
        ShopMenu.visible = True
        shopMenuBackButton.visible = True

    if shopMenuBackButton.hits(mouseX, mouseY):
        ShopMenu.visible = False
        shopMenuBackButton.visible = False
        UpgradeMenu.visible = False
        upgradeMenuButtonText2.visible = False
        shopMenuButton.visible = True
        shopMenuButtonText.visible = True
        upgradeMenuButton.visible = True
        upgradeMenuButtonText.visible = True

def onMouseMove(mouseX, mouseY):
    if cookieBig.contains(mouseX, mouseY) and not MainMenu.visible:
        cookieBig.border = 'black'
        cookieSmall.border = 'black'
    else:
        cookieBig.border = None
        cookieSmall.border = None

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
        pauseMenuButton1Text.visible = True
        pauseMenuButton2.visible = True
        pauseMenuButton2Text.visible = True
        pauseMenuButton3.visible = True
        pauseMenuButton3Text.visible = True
        pauseMenuButton4.visible = True
        pauseMenuButton4Text.visible = True

    if (key == "y"):
        YixuanImage.visible = not YixuanImage.visible
        YixuanImageBackground.visible = YixuanImage.visible

    if (key == "b"):
        Background.visible = not Background.visible
        cookieNumber.fill = 'black'
    


def onKeyRelease(key):
    if (key == "m") and infoWindow.visible:
        infoWindow.visible = False


app.width = 1300
app.height = 1300

cmu_graphics.run()