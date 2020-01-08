# -*- coding: utf8 -*-

class Suffix:
    def __init__(self, name, form, sorts, used=None):
        self.name =  name
        self.form =  form
        self.sorts = sorts
        self.used =  used

    def __repr__(self):
        return f"<Suffix {self.name}>"

def get_suffix(str, suffix):
    for s in suffix.sorts:
        if str[:len(s)][::-1] in suffix.sorts:
            for i in all_suffixes:
                if s in i.sorts:
                    ii = Suffix(i.name, i.form, i.sorts, used=s)
                    return ii


INFINITIVE =         Suffix("INFINITIVE",      "verbal",     ("mek", "mak"))
NEGATION =           Suffix("NEGATION",        "verbal",     ("me", "ma"))

#Person tenses
SINGULAR1 =          Suffix("SINGULAR1",       None,         ("ım", "im", "um", "üm"))
SINGULAR2 =          Suffix("SINGULAR2",       None,         ("sın", "sin", "sun", "sün", "ın", "in", "un", "ün"))

#Time tenses
PRESENT =            Suffix("PRESENT",         "verbal",     ("yor",))
PRESENT_PERFECT =    Suffix("PRESENT_PERFECT", "verbal",     ("r", "z"))
PAST_SEEN =          Suffix("PAST_SEEN",       None,         ("dı", "di", "du", "dü", "tı", "ti", "tu", "tü"))
PAST_UNSEEN =        Suffix("PAST_UNSEEN",     None,         ("mış", "miş", "muş", "müş"))
FUTURE =             Suffix("FUTURE",          None,         ("acak", "ecek"))

#Modal verbs
SHOULD =             Suffix("SHOULD",          "verbal",      ("malı", "meli"))
CAN =                Suffix("CAN",             "verbal",      ("ebil", "abil"))

all_suffixes = (INFINITIVE, NEGATION, SINGULAR1, SINGULAR2, PRESENT_PERFECT, PRESENT, PAST_SEEN, PAST_UNSEEN, FUTURE,
                SHOULD, CAN)
