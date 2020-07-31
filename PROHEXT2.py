import pyttsx3

class encryption:
    def __init__(self, otext, keyword, number):
        self.otext = otext
        self.keyword = keyword
        self.number=number

    def caesar(self,otext,number):
         import string
         import collections
         upper= collections.deque(string.ascii_uppercase)
         lower= collections.deque(string.ascii_lowercase)

         upper.rotate(number)
         lower.rotate(number)

         upper = ''.join(list(upper))
         lower = ''.join(list(lower))
         print (otext.translate(str.maketrans(string.ascii_uppercase, upper)).translate(str.maketrans(string.ascii_lowercase, lower)))


    def vigenerecipher(self, otext, keyword):

        key = keyword
        kl = list(keyword)
        text = "".join(otext.split())

        if len(text) != len(keyword):
            for i in range(len(text) - len(keyword)):
                key = key + kl[i]
                kl.append(kl[i])

        cipheredtext = ""
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                   "t", "u", "v",
                   "w", "x", "y", "z"]

        for i in range(len(text)):
            cipher = 0
            ltpos = 0
            lkpos = 0
            if text[i].isalpha() == True:
                if text[i].islower() == True:
                    for j in range(len(letters)):
                        if text[i] == letters[j]:
                            ltpos = j
                        if key[i] == letters[j]:
                            lkpos = j
                    cipher = ltpos + lkpos
                    cipher = cipher % 26
                    cipheredtext = cipheredtext + letters[cipher]
                elif text[i].isupper() == True:
                    for q in range(len(letters)):
                        letters[q] = letters[q].upper()
                    for j in range(len(letters)):
                        if text[i] == letters[j]:
                            ltpos = j
                        if key[i] == letters[j]:
                            lkpos = j
                    cipher = ltpos + lkpos
                    cipher = cipher % 26
                    cipheredtext = cipheredtext + letters[cipher]
            else:
                cipheredtext = cipheredtext + text[i]
        for i in range(len(otext)):
            if otext[i] == " ":
                cipheredtext = cipheredtext[:i] + " " + cipheredtext[i:]

        print(cipheredtext)



f1 = encryption("ATTACKATDAWN", 'LEMON',5)
f1.vigenerecipher("ATTACKATDAWN", "LEMON")
f1.caesar("ATTACKATDAWN",5)

speaker=pyttsx3.init()
speaker.say(f1.otext)
speaker.runAndWait()


