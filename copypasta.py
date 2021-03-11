#!/usr/bin/env python3

import pyperclip, os

nazwa = input("podaj nazwę pliku do utworzenia: \n")

print("kopiowanie tekstu ze schowka do pliku tekstowego \[ ... \]")
baconFile = open('pliki/bacon.txt', 'a')
baconFile.write(pyperclip.paste()+'\n')

baconFile.close()
# print(pyperclip.paste())

os.rename('pliki/bacon.txt', "pliki/"+nazwa+".txt")

