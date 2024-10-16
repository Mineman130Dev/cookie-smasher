from cmu_graphics import *

# python3 cookiesmasher.py

### your code
#class Button:
   # def __init__(self, shape, onClick):
        #self.shape = shape
        #self.onClick = onClick



#Music
#music = Sound('cmu://904676/33673980/waiting-music-116216.mp3')
#music.play(loop=True)

clickValue = Label(1, 0, 0, fill=None)

#Background
bg1 = Rect(0, 0, 400, 400, fill='steelBlue')
bg2 = Rect( 25, 0, 50, 400, fill='lightBlue')
bg3 = Rect(125, 0, 50, 400, fill='lightBlue')
bg4 = Rect(225, 0, 50, 400, fill='lightBlue')
bg5 = Rect(325, 0, 50, 400, fill='lightBlue')

background = Group(
    bg1,
    bg2,
    bg3,
    bg4,
    bg5
)
background.visible = False

backgroundHalloween = Group(
    Rect(0, 0, 400, 400, fill='black'),
    Rect( 25, 0, 50, 400, fill='orange'),
    Rect(125, 0, 50, 400, fill='orange'),
    Rect(225, 0, 50, 400, fill='orange'),
    Rect(325, 0, 50, 400, fill='orange')
)

backgroundHalloween.visible = False


#Cookie clicks
cookieNumber = Label(0, 200, 30, size=40, fill='white')
cps = Label(0, 200, 60, size=20, fill='white')

#Big and Small cookie
cookieBigShadow = Circle(190, 205, 100, opacity=20, visible=False)
cookieBig = Circle(200, 200, 100, fill='tan', visible=False)
cookieSmallShadow = Circle(190, 205, 80, opacity=20, visible=False)
cookieSmall = Circle(200, 200, 80, fill='tan', visible=False)
chipN1 = Circle(150, 144, 10, fill='saddleBrown')
chipN2 = Circle(235, 253, 15, fill='saddleBrown')
chipN3 = Circle(186, 217, 25, fill='saddleBrown')
smallChipN1 = Circle(161, 148, 5, fill='saddleBrown', visible=False)
smallChipN2 = Circle(185, 219, 20, fill='saddleBrown', visible=False)
smallChipN3 = Circle(220, 238, 10, fill='saddleBrown', visible=False)

#Small Menu Button
smallMenuButtonFrame = Rect(355, 5, 40, 40, fill='dimGray', opacity=50, border='black', borderWidth=3, visible=False)

smallMenuButton = Group(
    Circle(375, 25, 10, fill='tan', visible=False),
    Circle(370, 19, 1, fill='saddleBrown', visible=False),
    Circle(374, 25, 3, fill='saddleBrown', visible=False),
    Circle(380, 30, 2, fill='saddleBrown', visible=False)
)

#Upgrade Menu Background
UpgradeBackground = Rect(0, 0, 400, 400, fill='burlyWood', visible=False)

UpgradeBackgroundWood = Group(
    Line(0, 3, 400, 2, lineWidth=5, visible=False),
    Line(220, 3, 220, 53, lineWidth=5, visible=False),
    Line(0, 53, 400, 53, lineWidth=5, visible=False),
    Line(100, 53, 100, 103, lineWidth=5, visible=False),
    Line(0, 103, 400, 103, lineWidth=5, visible=False),
    Line(275, 103, 275, 153, lineWidth=5, visible=False),
    Line(0, 153, 400, 153, lineWidth=5, visible=False),
    Line(135, 153, 135, 203, lineWidth=5, visible=False),
    Line(0, 203, 400, 203, lineWidth=5, visible=False),
    Line(352, 203, 352, 253, lineWidth=5, visible=False),
    Line(0, 253, 400, 253, lineWidth=5, visible=False),
    Line(15, 253, 15, 303, lineWidth=5, visible=False),
    Line(310, 253, 310, 303, lineWidth=5, visible=False),
    Line(0, 303, 400, 303, lineWidth=5, visible=False),
    Line(192, 303, 192, 353, lineWidth=5, visible=False),
    Line(0, 353, 400, 353, lineWidth=5, visible=False),
    Line(90, 353, 90, 403, lineWidth=5, visible=False),
    
)

UpgradeBackgroundWood.visible = False

#Upgrade Photo


#Upgrades

#Upgrade Button 1
upgradeButton1 = Rect(0, 55, 400, 50, fill='gray', opacity=50, border='black', borderWidth=3, visible=False)
upgradeButton1Text1 = Label('Cookie Multipler', 55, 80, size=30, fill='white', visible=False)
upgradeButton1Text2 = Label(50, 305, 75, size=20, fill='white', visible=False)
upgradeButton1Text3 = Label('cookies', 355, 75, size=20, fill='white', visible=False)
upgradeButton1Text4 = Label(0, 345, 95, size=15, fill='white', visible=False)
upgradeButton1Text5 = Label('/6', 355, 95, size=15, fill='white', visible=False)

#Upgrade Button 1 descritption 
upgradeButton1Des = Label('Increase amount of', 100, 70, size=20, fill='white', visible=False)
upgradeButton1Des2 = Label('cookies made from one click.', 140, 85, size=20, fill='white', visible=False)

#Upgrade Button 2
upgradeButton2 = Rect(0, 108, 400, 50, fill='gray', opacity=50, border='black', borderWidth=3, visible=False)

upgradeButton3 = Rect(0, 161, 400, 50, fill='gray', opacity=50, border='black', borderWidth=3, visible=False)

upgradeButton4 = Rect(0, 214, 400, 50, fill='gray', opacity=50, border='black', borderWidth=3, visible=False)

upgradeButton5 = Rect(0, 267, 400, 50, fill='gray', opacity=50, border='black', borderWidth=3, visible=False)

upgradeButton6 = Rect(0, 320, 400, 50, fill='gray', opacity=50, border='black', borderWidth=3, visible=False)
smallUpgradeButton1 = Rect(75, 0, 50, 50, fill='gray', opacity=50, border='black', borderWidth=3, visible=False)
smallUpgradeButton2 = Rect(175, 0, 50, 50, fill='gray', opacity=50, border='black', borderWidth=3, visible=False)
smallUpgradeButton3 = Rect(275, 0, 50, 50, fill='gray', opacity=50, border='black', borderWidth=3, visible=False)


#Big Menu Text
#pressMShadow = Label('Press m For Help!', 87, 392, fill='black', size=20, opacity=20)
pressM = Label('Press m For Help!', 90, 390, size=20, fill='black')

#Version Text
Label('v0.1', 385, 390, size=12, fill='white')

#Menu Button
menuButtonFrame = Rect(350, 0, 50, 50, fill='gray', opacity=50, border='black', borderWidth=3)

menuButton = Group(
    Circle(375, 25, 15, fill='tan'),
    Circle(368, 19, 2, fill='saddleBrown'),
    Circle(373, 28, 4, fill='saddleBrown'),
    Circle(380, 33, 3, fill='saddleBrown')
)
    
#Big menu
bigMenu = Rect(25, 25, 350, 350, fill='gray', opacity=80, border='black', borderWidth=5, visible=False)
bigMenuTextN1 = Label('Version: v0.2.0 (Oct 9th, 2024)', 175, 305, size=20, bold=True, visible=False, fill='white')
bigMenuTextN2 = Label('Made and coded by: Bryce Hazeltine', 168, 325, size=15, bold=True, visible=False, fill='white')
bigMenuTextN3 = Label ('Debugger: Alex (oglass) Marich', 150, 345, size=15, bold=True, fill='white', visible=False)
bigMenuNextPageSymbol = Label('➜', 356, 214, font='symbols', fill='white', visible=False)
bigMenuNextPageFrame = Rect(346, 204, 20, 20, fill=None, border='black', visible=False)

#Big menu Page 2

bigMenu2BackgroundButton = Rect(50, 125, 50, 50, visible=False)
bigMenu2BackgroundButtonText = Label('BG', 75, 150, fill='white', size=20, visible=False)
bigMenu2BackgroundButtonFrame = Rect(50, 125, 50, 50, fill=None, border='gray', borderWidth=3, visible=False)
bigMenu2AchivementButton = Rect(175, 125, 50, 50, visible=False)
bigMenu2AchivementButtonText = Label('Ach.', 200, 150, fill='white', size=20, visible=False)
bigMenu2AchivementButtonFrame = Rect(175, 125, 50, 50, fill=None, border='gray', borderWidth=3, visible=False)
bigMenu2SaveButton = Rect(300, 125, 50, 50, visible=False)
bigMenu2SaveButtonText = Label('Save', 325, 150, fill='white', size=20, visible=False)
bigMenu2SaveButtonFrame = Rect(300, 125, 50, 50, fill=None, border='gray', borderWidth=3, visible=False)

#Help Text
helpText1 = Label('Key Binds:', 120, 60, size=30, bold=True, fill='white', visible=False)
helpText2 = Label('m - Brings up this menu', 160, 100, size=20, bold=True, fill='white', visible=False)
helpText3 = Label('Escape - Closes this menu', 172, 125, size=20, bold=True, fill='white', visible=False)
helpText4 = Label('b - Pop the background in and', 190, 150, size=20, bold=True, fill='white', visible=False)
helpText5 = Label('out of existence', 120, 175, size=20, bold=True, fill='white', visible=False)
helpText6 = Label('i - Inspect upgrades', 143, 200, size=20, bold=True, fill='white', visible=False)


#Yixuan and Oglass Easter Egg
#app.url = 'cmu://904676/33574459/Screen+Shot+2024-10-09+at+8.55.40+AM.png'

#oglass = Image(app.url, 0, 0, visible=False)
#oglassText = Label('Have a Rice Day!', 200, 350, size=50, fill='white', border='black', visible=False)

#yixuan = Image('cmu://904676/33575905/Screen+Shot+2024-10-09+at+9.03.48+AM.png', 75, 0, visible=False)
#yixuanSide1 = Rect(0, 0, 75, 400, visible=False)
#yixuanSide2 = Rect(325, 0, 75, 400, visible=False)

#Background Menu/Selector
backgroundMenu = Group(
    Rect(0, 0, 400, 400, fill=('burlyWood'), visible=False),
    Rect(50, 250, 100, 100),
    Rect(250, 250, 100, 100)
    
)

#bg1 = Image('cmu://904676/33633172/cs-academy-canvas+(4).png', 50, 50)
#bg2 = Image('cmu://904676/33633908/cs-academy-canvas+(3).png', 250, 50)

#backgroundSelect = Group(
#    bg1,
#    bg2
#    
#)

#Background Frames
background1Frame = Rect(50, 50, 100, 100, fill=None, border='white', borderWidth=3, visible=False)
background2Frame = Rect(250, 50, 100, 100, fill=None, border='white', borderWidth=3, visible=False)

#backgroundSelect.visible = False

backgroundMenu.visible = False

#Achivements

#Achivement 1 Button

Achivement1 = Group (
    Rect(50, 360, 300, 37, fill='gray', border='black', borderWidth=3),
    Label('Getting Started!:', 130, 379, size=18, fill='white', bold=True),
    Label('Bake your first', 275, 370, size=15, fill='white'),
    Label('100 cookies!', 275, 385, size=15, fill='white')
)
Achivement1.visible = False

Achivement1Box = Rect(340, 350, 20, 20, fill='gray', border='black', borderWidth=3, visible=False)
Achivement1Close = Label('✘', 350, 360, font='symbols', fill='darkRed', visible=False)

##Main Menu##

#Main Menu Background

titleMenuButton1 = Rect(125, 150, 150, 50, fill='white', border='black', borderWidth=3)
titleMenuButton2 = Rect(125, 220, 150, 50, fill='white', border='black', borderWidth=3, visible=True)
#titleMenuButton3 = Rect(125, 290, 150, 50, fill='white', border='black', borderWidth=3, visible=True)



backgroundMainMenu = Group(
    Rect(0, 0, 400, 400, fill='steelBlue'),
    Rect( 25, 0, 50, 400, fill='lightBlue'),
    Rect(125, 0, 50, 400, fill='lightBlue'),
    Rect(225, 0, 50, 400, fill='lightBlue'),
    Rect(325, 0, 50, 400, fill='lightBlue'),
    )
    
mainMenuButtonsAndText = Group(
    titleMenuButton1,
    titleMenuButton2,
    #titleMenuButton3,
    Label('Cookie', 200, 30, fill='white', size=50, bold=True, border='black'),
    Label('Smasher', 200, 80, fill='white', size=50, bold=True, border='black'),
    Label('Start', 200, 175, size=30, bold=True),
    Label('Options', 200, 245, size=30, bold=True),
    #Label('QUIT', 200, 315, size=30, bold=True),
)

backgroundMainMenu.visible = True
mainMenuButtonsAndText.visible = True


AchivementMenu = Group(

    #Achivement 1
    Rect(0, 0, 400, 400, fill='tan'),
    Rect(10, 55, 380, 50, fill='white', border='black', borderWidth=3),
    Label('Getting Started!:', 110, 80, size=25),
    Label('Bake your first', 290, 70, size=15),
    Label('100 cookies!', 290, 90, size=15),
    
    #Achivement 2
    Rect(10, 110, 380, 50, fill='white', border='black', borderWidth=3),
    Label('Place Holder', 95, 135, size=25),
    Label('Place Holder', 235, 135, size=15),
    
    #Achivement 3
    Rect(10, 165, 380, 50, fill='white', border='black', borderWidth=3),
    Rect(375, 162, 20, 20, fill='white', border='black', borderWidth=3),
    Label('Coming Soon', 95, 190, size=25),
    Label('🔒', 385, 172, font='symbols'),
    
    #Achivement 4
    Rect(10, 220, 380, 50, fill='white', border='black', borderWidth=3),
    Rect(375, 218, 20, 20, fill='white', border='black', borderWidth=3),
    Label('Coming Soon', 95, 245, size=25),
    Label('🔒', 385, 228, font='symbols'),

    )
    
AchivementMenu.visible = False
    
Label('Achivements Unlocks:', 200, 300, size=30, visible=False)
Label('/2', 210, 340, size=30, visible=False)
AvivementUnlock = Label(0, 190, 340, size=30, visible=False)
    
Achivement1WallFrame = Rect(375, 52, 20, 20, fill='white', border='black', borderWidth=3, visible=False)
Achivement1Wall = Label('✔', 385, 62, font='symbols', fill='limeGreen', visible=False)

Achivement2WallFrame = Rect(375, 107, 20, 20, fill='white', border='black', borderWidth=3, visible=False)
Achivement2Wall = Label('✔', 385, 117, font='symbols', fill='limeGreen', visible=False)

#BackButton
backButton = Rect(0, 0, 50, 50, fill='gray', border='black', opacity=50, borderWidth=3, visible=False)
backButtonTxt = Label('☜', 25, 25, fill='black', size=35, visible=False, font='symbols')


##Options Menu
optionsMenu = Rect(0, 0 , 400, 400, fill='white', visible=False)
optionsBackButton = Rect(0, 350, 50, 50)
optionsBackButtonText = Label('back', 25, 375, size=20, fill='white')
optionsMenuMusicButton = Rect(75, 50, 20, 20, visible=False)
optionsMenuMusicCheck = Label('✔', 85, 60, font='symbols', fill='limeGreen')
optionsMenuMusicLabel = Label('Music:', 40, 60, size=20)
optionsMenuEffectsButton = Rect(145, 110, 20, 20)
optionsMenuEffectsCheck = Label('✔', 155, 120, fill='limeGreen', font='symbols')
optionsMenuEffectsLabel = Label('Sound Effects:', 75, 120, size=20)
optionsMenuAudioLabel = Label('Audio:', 75, 25, size=40, bold=True)

OptionsMenu = Group(
    optionsMenu,
    optionsBackButton,
    optionsBackButtonText,
    optionsMenuMusicButton,
    optionsMenuMusicCheck,
    optionsMenuMusicLabel,
    optionsMenuEffectsButton,
    optionsMenuEffectsLabel,
    optionsMenuEffectsCheck,
    optionsMenuAudioLabel
    )
OptionsMenu.visible = False
    
#On mouse press and relase events
def onMouseRelease(mouseX, mouseY):
    cookieSmall.visible = False
    cookieSmallShadow.visible = False
    cookieBig.visible = True
    cookieBigShadow.visible = True
    chipN1.visible = True
    chipN2.visible = True
    chipN3.visible = True
    smallChipN1.visible = False
    smallChipN2.visible = False
    smallChipN3.visible = False
    pass

def onMousePress(mouseX, mouseY):
    
    if optionsMenuMusicButton.hits(mouseX, mouseY) and optionsMenu.visible:
        optionsMenuMusicCheck.visible = not optionsMenuMusicCheck.visible
        
    if optionsBackButton.hits(mouseX, mouseY) and optionsMenu.visible:
        OptionsMenu.visible = False
        
    if titleMenuButton2.hits(mouseX, mouseY) and backgroundMainMenu.visible:
        OptionsMenu.visible = True

    if bigMenu2AchivementButton.hits(mouseX, mouseY) and bigMenu.visible:
        AchivementMenu.visible = True
        backButton.visible = True
        backButtonTxt.visible = True
    
    #if optionsMenuMusicButton.hits(mouseX, mouseY) and optionsMenu.visible:
        #music.pause()
    
    if titleMenuButton1.contains(mouseX, mouseY):
        background.visible = True
        backgroundMainMenu.visible = False
        mainMenuButtonsAndText.visible = False
    
    if background1Frame.hits(mouseX, mouseY):
        background.visible = True
        backgroundHalloween.visible = False
        
    if background2Frame.hits(mouseX, mouseY) and backgroundMenu.visible:
        background.visible = False
        #backgroundHallowen.visible = True
    
    if bigMenu2BackgroundButton.hits(mouseX, mouseY):
        backgroundMenu.visible = True
        backButtonTxt.visible = True
        backButton.visible = True
        #backgroundSelect.visible = True
        
    
    if upgradeButton1.hits(mouseX, mouseY) and cookieNumber.value >= upgradeButton1Text2.value:
        if (upgradeButton1Text4.value < 6):
            upgradeButton1Text2.value = upgradeButton1Text2.value * 8
            upgradeButton1Text4.value = upgradeButton1Text4.value + 1
            
    if upgradeButton1.hits(mouseX, mouseY) and upgradeButton1.visible and cookieNumber.value >= upgradeButton1Text2.value:
        if (cookieNumber.value <= upgradeButton1Text2.value):
            cookieNumber.value = cookieNumber.value * 5
            
    #if upgradeButton2.hits(mouseX, mouseY) and upgradeButton2.visible:
    
    
    if Achivement1Box.hits(mouseX, mouseY):
        Achivement1Box.visible = False
        Achivement1Close.visible = False
        Achivement1.visible = False
    
    if backButton.hits(mouseX, mouseY):
        backButton.visible = False
        backButtonTxt.visible = False
        UpgradeBackground.visible = False
        backButton.visible = False
        UpgradeBackground.visible = False
        upgradeButton1.visible = False
        upgradeButton2.visible = False
        upgradeButton3.visible = False
        upgradeButton4.visible = False
        upgradeButton5.visible = False
        upgradeButton6.visible = False
        smallUpgradeButton1.visible = False
        smallUpgradeButton2.visible = False
        smallUpgradeButton3.visible = False
        upgradeButton1Text1.visible = False
        upgradeButton1Text2.visible = False
        upgradeButton1Text3.visible = False
        upgradeButton1Text4.visible = False
        upgradeButton1Text5.visible = False
        upgradeButton1Des.visible = False
        backgroundMenu.visible = False
        #backgroundSelect.visible = False
        AchivementMenu.visible = False

    
    if menuButtonFrame.hits(mouseX, mouseY) and not bigMenu.visible:
        backButton.visible = True
        UpgradeBackground.visible = True
        upgradeButton1.visible = True
        upgradeButton2.visible = True
        upgradeButton3.visible = True
        upgradeButton4.visible = True
        upgradeButton5.visible = True
        upgradeButton6.visible = True
        smallUpgradeButton1.visible = True
        smallUpgradeButton2.visible = True
        smallUpgradeButton3.visible = True
        upgradeButton1Text1.visible = True
        upgradeButton1Text2.visible = True
        upgradeButton1Text3.visible = True
        upgradeButton1Text4.visible = True
        upgradeButton1Text5.visible = True
        
    if menuButtonFrame.hits(mouseX, mouseY) and not bigMenu.visible:
        backButtonTxt.visible = True
    
    
    if cookieBig.hits(mouseX, mouseY) and not UpgradeBackground.visible and not bigMenu.visible and not backgroundMainMenu.visible:
        cookieSmall.visible = True
        cookieSmallShadow.visible = True
        cookieBig.visible = False
        cookieBigShadow.visible = False
        chipN1.visible = False
        chipN2.visible = False
        chipN3.visible = False
        smallChipN1.visible = True
        smallChipN2.visible = True
        smallChipN3.visible = True
        cookieNumber.value += 1
        
        if (cookieNumber.value == 100):
            Achivement1.visible = True
            Achivement1Box.visible = True
            Achivement1Close.visible = True
        
    if bigMenuNextPageSymbol.hits(mouseX, mouseY):
        bigMenuTextN1.visible = False
        bigMenuTextN2.visible = False
        bigMenuTextN3.visible = False
        bigMenuNextPageSymbol.visible = False
        bigMenuNextPageFrame.visible = False
        helpText1.visible = False
        helpText2.visible = False
        helpText3.visible = False
        helpText4.visible = False
        helpText5.visible = False
        helpText6.visible = False
        pressM.visible = False
        bigMenu2BackgroundButton.visible = True
        bigMenu2BackgroundButtonText.visible = True
        bigMenu2AchivementButton.visible = True
        bigMenu2AchivementButtonText.visible = True
        bigMenu2SaveButton.visible = True
        bigMenu2SaveButtonText.visible = True

    #if smallMenuButtonFrame.hits(mouseX, mouseY):
        #smallMenuButtonFrame.visible = True
        #smallMenuButton.visible = True
        #menuButtonFrame.visible = False
        #menuButton.visible = False
    

#Mouse hover events
def onMouseMove(mouseX, mouseY):
    
    if background1Frame.contains(mouseX, mouseY) and backgroundMenu.visible:
        background1Frame.visible = True
    else:
        background1Frame.visible = False
        
    if background2Frame.contains(mouseX, mouseY)and backgroundMenu.visible:
        background2Frame.visible = True
    else:
        background2Frame.visible = False

    
    if bigMenuNextPageFrame.contains(mouseX, mouseY):
        bigMenuNextPageFrame.border = 'white'
    else:
        bigMenuNextPageFrame.border = 'black'
    
    if menuButtonFrame.contains(mouseX,mouseY) and not bigMenu.visible:
        menuButtonFrame.border ='white'
    else:
        menuButtonFrame.border = 'black'
        
    if cookieBig.contains(mouseX, mouseY) and not bigMenu.visible:
        cookieBig.border = 'black'
    else:
        cookieBig.border = None
        
    if cookieBig.contains(mouseX, mouseY) and not bigMenu.visible:
        cookieSmall.border = 'black'
    else:
        cookieSmall.border = None
        
    if upgradeButton1.contains(mouseX, mouseY):
        upgradeButton1.border = 'white'
    else:
        upgradeButton1.border = 'black'
        
    if upgradeButton2.contains(mouseX, mouseY):
        upgradeButton2.border = 'white'
    else:
        upgradeButton2.border = 'black'
        
    if upgradeButton3.contains(mouseX, mouseY):
        upgradeButton3.border = 'white'
    else:
        upgradeButton3.border = 'black'
        
    if upgradeButton4.contains(mouseX, mouseY):
        upgradeButton4.border = 'white'
    else:
        upgradeButton4.border = 'black'
        
    if upgradeButton5.contains(mouseX, mouseY):
        upgradeButton5.border = 'white'
    else:
        upgradeButton5.border = 'black'
        
    if upgradeButton6.contains(mouseX, mouseY):
        upgradeButton6.border = 'white'
    else:
        upgradeButton6.border = 'black'
        
    if smallUpgradeButton1.contains(mouseX, mouseY):
        smallUpgradeButton1.border = 'white'
    else:
        smallUpgradeButton1.border = 'black'
        
    if smallUpgradeButton2.contains(mouseX, mouseY):
        smallUpgradeButton2.border = 'white'
    else:
        smallUpgradeButton2.border = 'black'
        
    if smallUpgradeButton3.contains(mouseX, mouseY):
        smallUpgradeButton3.border = 'white'
    else:
        smallUpgradeButton3.border = 'black'
        
    if backButton.contains(mouseX, mouseY):
        backButton.border = 'white'
    else:
        backButton.border= 'black'
        
    if bigMenu2BackgroundButton.contains(mouseX, mouseY) and bigMenu.visible and not bigMenuNextPageFrame.visible:
        bigMenu2BackgroundButtonFrame.visible = True
    else:
        bigMenu2BackgroundButtonFrame.visible = False
        
    if bigMenu2AchivementButton.contains(mouseX, mouseY) and bigMenu.visible and not bigMenuNextPageFrame.visible:
        bigMenu2AchivementButtonFrame.visible = True
    else:
        bigMenu2AchivementButtonFrame.visible = False
        
    if bigMenu2SaveButton.contains(mouseX, mouseY) and bigMenu.visible and not bigMenuNextPageFrame.visible:
        bigMenu2SaveButtonFrame.visible = True
    else:
        bigMenu2SaveButtonFrame.visible = False
#Key press events
def onKeyPress(key):
    if (key == "m") and not backgroundMainMenu.visible:
        bigMenu.visible = True
        bigMenuTextN1.visible = True
        bigMenuTextN2.visible = True
        bigMenuTextN3.visible = True
        bigMenuNextPageSymbol.visible = True
        bigMenuNextPageFrame.visible = True
        helpText1.visible = True
        helpText2.visible = True
        helpText3.visible = True
        helpText4.visible = True
        helpText5.visible = True
        helpText6.visible = True
        pressM.visible = False
        #pressMShadow.visible = False
        
        
    
    if (key == "b"):
        background.visible = not background.visible
        
    if (key == "y"):
        yixuan.visible = not yixuan.visible
        yixuanSide1.visible = not yixuanSide1.visible
        yixuanSide2.visible = not yixuanSide2.visible

        
    if (key == "o"):
        oglass.visible = not oglass.visible
        oglassText.visible = not oglassText.visible
        
    if (key == "i" and UpgradeBackground.visible):
        upgradeButton1Des.visible = not upgradeButton1Des.visible
        upgradeButton1Des2.visible = not upgradeButton1Des2.visible
        upgradeButton1Text1.visible = not upgradeButton1Text1.visible
        
    if (key == "escape") and not bigMenu.visible and not UpgradeBackground.visible:
        backgroundMainMenu.visible = True
        mainMenuButtonsAndText.visible = True
        
        
    
        
        
def onKeyRelease(key):
    if (key == "escape") and bigMenu.visible and not backgroundMenu.visible:
        bigMenu.visible = False
        bigMenuTextN1.visible = False
        bigMenuTextN2.visible = False
        bigMenuTextN3.visible = False
        bigMenuNextPageSymbol.visible = False
        bigMenuNextPageFrame.visible = False
        helpText1.visible = False
        helpText2.visible = False
        helpText3.visible = False
        helpText4.visible = False
        helpText5.visible = False
        helpText6.visible = False
        pressM.visible = True
        #pressMShadow.visible = True
        bigMenu2BackgroundButton.visible = False
        bigMenu2BackgroundButtonText.visible = False
        bigMenu2AchivementButton.visible = False
        bigMenu2AchivementButtonText.visible = False
        bigMenu2SaveButton.visible = False
        bigMenu2SaveButtonText.visible = False
        
        
    
   

cmu_graphics.run()