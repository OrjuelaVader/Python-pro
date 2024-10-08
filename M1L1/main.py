meme_dict = {"Cringe":"pena ajena",
"GG": "Good Game",
"AFK": "Away From Keyboard (lejos del teclado)",
"IDK": "I Dont Know (no lo sé)", 
"IMO": "In My Opinion (en mi opinión)",
"NPC": "No Playable Character",
"BRB": "Be Right Back (vuelvo enseguida)",
"SMH": "Shaking My Head (sacudiendo la cabeza)",
"OMG": "Oh My God (Dios mío)",
"LOL": "Laughting Out Loud (riendo a carcajadas)"}

palabra = str(input("Ingresa una palabra que desconoscas su significado:"))
if palabra in meme_dict.keys():
  print(meme_dict[palabra])
else:
  print("Esa palabra no la tenemos pero estamos trabajando en ella")