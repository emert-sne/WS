#! /usr/bin/env python
 
import random as rnd
# Import the 'random' function in order to select a random number and get a random song.
import time 
# Importing the ability to 'pause' to give the program a more professional feel.
import sys
# Import the ability to close the program if using cmd

print("--------------------------------------------------")
#Welcome the user
print("SELAMAT DATANG KE PERMAINAN TEKA MUSIK 80-90an !")
time.sleep(1)
print("--------------------------------------------------")

#The list of the songs
songlist = {
    'sejati': 'wings',
    'taman rashidah utama': 'wings',
    'bayangan gurauan': 'mega',
    'suci dalam debu': 'iklim',
    'gerimis mengundang': 'slam',
    'ku dihalaman rindu': 'lefthanded',
    'lamunan terhenti': 'aris ariwatan',
    'memori berkasih': 'achik dan nana',
    'cinta kristal': 'rahim maarof',
    'isabella': 'search',
    'seroja': 'jamal abdillah',
    'fantasia bulan madu': 'search'
}
 
score = 0;
# The score is automatically zero
tries = 3
# The user have 3 tries only

#Using while as loop the question until it reach 3 times
while tries > 0:
        random_song = rnd.choice(list(songlist.items()))
        intials = []
        # Get only the first letter of each word in songs - split()
        for first_letter in random_song[0].split():
            intials.append(first_letter[0].capitalize())
 
        print(f'Huruf bagi lagu tersebut ialah {" ".join(intials)} dan artisnya adalah {random_song[1].title()}')
        print('Boleh Anda teka lagu ini?')
        time.sleep(1)
        song = input('Jawapan Anda : ')
        if song.lower().strip() == random_song[0].lower().strip():
            print(f'BETUL!!! Anda mempunyai {tries - 1} cubaan lagi. Markah anda adalah : {score + 1}.'"\n")
            tries -= 1
            score += 1
            continue
        else:
            print(f'Salah Bro. Anda mempunyai {tries - 1} cubaan lagi. Markah anda adalah : {score}.')
            tries -= 1
            continue
 
        break
        sys.exit()