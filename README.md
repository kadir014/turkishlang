<p align="center">
  <img src="https://github.com/kadir014/turkishlang/blob/master/logo.png"><br>
  <img src="https://img.shields.io/badge/python-3%2B-green.svg">
  <img src="https://img.shields.io/badge/license-GPL%203.0-blue.svg">
  <img src="https://img.shields.io/badge/version-0.0.0alpha-red">
</p

---

__*** Notice these two statements! ***__
1) _First of all, the `word` module which is used to parse words (stemmer) is not complepeted yet, besides, the project is still in development._
2) _And keep in mind that this is a personal-development project; therefore it's performance may not be as expected when compared to other projects which purposes a similar goal._

**Turkishlang** is simply a Python package purposed to be used in interacting with Turkish language. It's main features are a morphological word parser/stemmer, a sentence parser (_TODO_), and various tools.

# Usage
This is just a brief introduction to usage of the package, you may want to see Documentation for further information.

## • Using **turkishlang** with strings
In Python, if you swap the case of a string which includes a turkish unicode character, it won't work properly:
```py
print("irem".capitalize())
```
When you run this code, the output will be `Irem`, but in Turkish, letter "I" is not the uppercase version of "i", so you can solve this problem by using `TurkishString` class from `alphabet` module, here is a little example:
```py
from turkishlang.alphabet import TurkishString as tr_str

print(       "ırak ipeği".upper())
print(       "IRAK İPEĞİ".lower())
print(       "ırak ipeği".capitalize())
print(       "ıRaK İpeĞi".swapcase() + "\n")

print(tr_str("ırak ipeği").upper())
print(tr_str("IRAK İPEĞİ").lower())
print(tr_str("ırak ipeği").capitalize())
print(tr_str("ıRaK İpeĞi").swapcase() + "\n")
```
output:
```
IRAK IPEĞI
irak i̇peği̇
Irak ipeği
IrAk i̇PEğI

IRAK İPEĞİ
ırak ipeği
Irak ipeği
IrAk iPEğİ
```
There are also other different functions in the `alphabet` module, on of them is:
```py
from turkishlang.alphabet import degrade

print(degrade("fıstıkçı şahap"))
```
And the output is: `fistikci sahap`, all Turkish words got degraded. You can see Documentation for more information.

## • Using **turkishlang** for parsing strings
The main reason behind the birth of this project is morphological analysis of words and sentences.

Let's take the word "yüzememek" which means "not being able to swim"
> Turkish is a agglutinative language, suffixes are added to change the word's meaning.

Stem of the word "yüzememek" is "yüz" which means "swim" \
The last suffix "mek" is the infinitiive suffix, it's used as verbal noun suffix here \
Next suffix "me" is the negation suffix \
Last suffix "e" is the negative version of "ebil-mek" which means "being able to"

now let's have turkishlang do the job:
```py
import turkishlang.word

parsed_word = turkishlang.word.Parser("yüzememek")
parsed_word.print_analytics()
```
output:
```
Morphological analysis of word "yüzememek"
   Form     : Verb
   Stem     : yüz-mek
   Parsed   : yüz-e-me-mek

   More technical:
      Harmony    : Front
      Suffixes   : CAN, NEGATION, INFINITIVE
      Degraded   : yuzememek
      Vowels     : ü
      Consts     : yz
      All Vowels : üeee
      All Consts : yzmmk
```

# References
• https://en.wikipedia.org/wiki/Turkish_language           \
• https://en.wikipedia.org/wiki/Turkish_grammar            \
• https://en.wikipedia.org/wiki/Vowel_harmony#Turkish      \
• https://en.wiktionary.org/wiki/Appendix:Turkish_suffixes

# License
[GPL 3.0](LICENSE) © Kadir Aksoy
