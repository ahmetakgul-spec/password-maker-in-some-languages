from random import choice
import os

karakter = ["a",
"b",
"c",
"d",
"e",
"f",
"g",
"h",
"i",
"j",
"k",
"l",
"m",
"n",
"o",
"ö",
"p",
"r",
"s",
"t",
"u",
"ü",
"v",
"y",
"z",
"A",
"B",
"C",
"D",
"E",
"F",
"G",
"H",
"I",
"J",
"K",
"L",
"M",
"N",
"O",
"Ö",
"P",
"R",
"S",
"T",
"U",
"Ü",
"V",
"Y",
"Z",
"1",
"2",
"3",
"4",
"5",
"6",
"7",
"8",
"9",
"0",
"!",
"#",
"+",
"$",
"%",
"&",
"/",
"{",
"(",
"[",
")",
"]",
"=",
"}",
"*",
"?",
"*",
"-",
"_",
",",
";",
".",
":",]


sifreuzunluk = int(9)
sifre = ""
for i in range(sifreuzunluk):
    sifre += str(choice(karakter))
print (sifre)