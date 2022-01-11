print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Velkommen til den store skattejakten!")
print("Ditt oppdrag er å finne den forsvunnede skattekisten.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

rettedalen = input("Du har ankommet Rettedalen. \nVil du gå til høyre eller venstre?\n")

lower_rettedalen = rettedalen.lower()

if lower_rettedalen == "venstre":
  print("Du har havnet på lærerrommet på Ålgård Skole og ble drept av Rune Bøe! Game over.")

if lower_rettedalen == "høyre":
  frikk = input("Du er nå på vei opp Per Sivles vei! \nFrikk kommer løpende med en slegge. \nHva gjør du? \nDu kan skyte eller løpe.\n")
  lower_frikk = frikk.lower()

  if lower_frikk == "skyte":
    print("Frikk dryler deg ihjel før du får skutt ham. Du dør. \nGame over.")

  if lower_frikk == "løpe":
    hus_nummer = input("Du løper unna Frikk og overlever. \nDu ankommer nå toppen av Per Sivles vei. \nDu kan gå inn i hus nr.: 13, 15 eller 17. \nVelg husnummer.\n")

    if hus_nummer == "13":
      print("Gratulerer! Du fant skattekisten. HURRA!!!")

    if hus_nummer == "15":
      print("Du går inn i Frikks hus og blir drept. \nGame over.")

    if hus_nummer == "17":
      print("Du går inn i hus nummer 17. En bjørn spiser deg levende. \nGame over.")
    

    




