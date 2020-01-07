# -*- coding: utf8 -*-

ALPHABET =     "abcçdefgğhıijklmnoöprsştuüvyz"

VOWELS =       "aeıioöuü"
CONSONANTS =   "bcçdfgğhjklmnprsştvyz"

FRONT_VOWELS = "eiöü"
BACK_VOWELS =  "aıou"

TURKISH_MAPPING = {
                   "ç" : "c", "Ç" : "C",
                   "ğ" : "g", "Ğ" : "G",
                   "İ" : "I", "ı" : "i",
                   "ö" : "o", "Ö" : "O",
                   "ş" : "s", "Ş" : "S",
                   "ü" : "u", "Ü" : "U"
                  }

def has_turkish(str):
    for chr in str:
        if chr in TURKISH_MAPPING: return True

    return False

def degrade(str):
    _str = list(str)
    for i, chr in enumerate(str):
        if chr in TURKISH_MAPPING: _str[i] = TURKISH_MAPPING[chr]

    return "".join(_str)

class TurkishString(str):
    def upper(self):
        self = self.replace("ı", "I")
        self = self.replace("i", "İ")
        return self.upper()

    def lower(self):
        self = self.replace("I", "ı")
        self = self.replace("İ", "i")
        return self.lower()

    def capitalize(self):
        if   self[0] == "ı": self = "I" + self[1:len(self)]; return self
        elif self[0] == "i": self = "İ" + self[1:len(self)]; return self
        else: return self.capitalize()

    def swapcase(self):
        _self = list(self)
        for i, chr in enumerate(_self):
            if chr == chr.upper():
                if   chr == "I": _self[i] = "ı"
                elif chr == "İ": _self[i] = "i"
                else: _self[i] = chr.lower()
            elif chr == chr.lower():
                if   chr == "ı": _self[i] = "I"
                elif chr == "i": _self[i] = "İ"
                else: _self[i] = chr.upper()

        return "".join(_self)
