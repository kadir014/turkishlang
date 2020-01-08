from .suffixes import *
from ..alphabet import *

class Parser:
    def __init__(self, raw):
        self.raw = raw
        self.stem = raw[::-1]
        self.form = None
        self.suffixes = list()
        self.max_iter = len(self.raw)
        self.parse()

    def __repr__(self):
        return f"<Parser \"{self.raw}\">"

    def parse(self):
        #PARSE SUFFIXES
        i = self.max_iter
        while i > 0:

            for suffix in all_suffixes:
                s = get_suffix(self.stem, suffix)

                if s:
                    if s.name in tuple(a.name for a in self.suffixes): continue

                    if suffix.form: self.form = suffix.form[:4]

                    # DETECT CONFLICTS

                    # both present perfect and present continues tenses has : r , yo(r)
                    ss = get_suffix(self.stem, PRESENT)
                    if s.used in PRESENT_PERFECT.sorts and ss:
                        suffix = PRESENT
                        s = get_suffix(self.stem, suffix)

                    if s.name == PRESENT_PERFECT.name:
                        if len(self.stem) <= 3: continue

                    suffix.used = suffix.sorts[suffix.sorts.index(self.stem[:len(s.used)][::-1])]
                    self.suffixes.append(suffix)
                    self.stem = self.stem[len(s.used):len(self.stem)]

                    if s.name == PRESENT.name:
                        self.suffixes.append(Suffix("COMBINATIVE_LETTER", None, (self.stem[0],), self.stem[0]))
                        self.stem = self.stem[1:len(self.stem)]

                    elif s.name == PRESENT_PERFECT.name:
                        if s.used == "z":
                            a = NEGATION
                            a.used = self.stem[:1]
                            self.suffixes.append(a)
                            #self.stem = self.stem[1:len(self.stem)]

                        elif self.stem[0] in VOWELS:
                            self.suffixes.append(Suffix("COMBINATIVE_LETTER", None, (self.stem[0],), self.stem[0]))
                            self.stem = self.stem[1:len(self.stem)]

                    elif s.name == SINGULAR1.name:
                        if self.stem[0] == "y":
                            self.suffixes.append(Suffix("COMBINATIVE_LETTER", None, (self.stem[0],), self.stem[0]))
                            self.stem = self.stem[1:len(self.stem)]

                        if self.stem[0] == "d":
                            a = PAST_SEEN
                            a.used = "d"
                            self.suffixes.append(a)
                            self.stem = self.stem[1:len(self.stem)]

                    elif s.name == CAN.name:
                        if self.stem[0] == "y":
                            self.suffixes.append(Suffix("COMBINATIVE_LETTER", None, (self.stem[0],), self.stem[0]))
                            self.stem = self.stem[1:len(self.stem)]

            i -= 1

        self.stem = self.stem[::-1]
        self.suffixes = self.suffixes[::-1]


        #PARSE VOWELS AND CONSONANTS
        self.vowels =         "".join((chr for chr in self.stem if chr in VOWELS))
        self.consonants =     "".join((chr for chr in self.stem if chr in CONSONANTS))
        self.all_vowels =     "".join((chr for chr in self.raw if chr in VOWELS))
        self.all_consonants = "".join((chr for chr in self.raw if chr in CONSONANTS))

        if self.vowels[len(self.vowels) - 1] in FRONT_VOWELS: self.vowel_harmony = "front"
        else: self.vowel_harmony = "back"

    def print_analytics(self):
        print(f"\nMorphological analysis of word \"{self.raw}\"")
        if self.form: print(f"   Form     : {self.form.capitalize()}")
        if self.form == "verb":
            if   self.vowel_harmony == "front":  print(f"   Stem     : {self.stem}-mek")
            elif self.vowel_harmony == "back":   print(f"   Stem     : {self.stem}-mak")
        else: print(f"   Stem     : {self.stem}")
        parsed = self.stem + "-" + "-".join((s.used for s in self.suffixes))
        print(f"   Parsed   : {parsed}")
        print("\n   More technical:")
        print(f"      Harmony    : {self.vowel_harmony.capitalize()}")
        s = str(tuple(s.name for s in self.suffixes)).replace("(", "").replace(")", "").replace("'", "")
        print(f"      Suffixes   : {s}")
        print(f"      Degraded   : {degrade(self.raw)}")
        print(f"      Vowels     : {self.vowels}")
        print(f"      Consts     : {self.consonants}")
        print(f"      All Vowels : {self.all_vowels}")
        print(f"      All Consts : {self.all_consonants}")
