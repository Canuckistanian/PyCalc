#!/usr/bin/env python
# -*- encoding: utf-8 -*-

licensestring = """
MIT License

Copyright (c) 2017 Canuckistanian

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

##PyCalc written in Python 2.7.13
##By Canuckistanian

import Tkinter as tki
class PyCalcApplication:
    def __init__(self):
        self.mainwindow = tki.Tk()
        self.mainwindow.title("PyCalc")
        self.calctext = tki.StringVar()
        self.equationlist = []
        self.widgetfont = "Courier 12"
        self.widgetforeground = "#000000"
        self.widgetbackground = "#FFFFFF"
        self.helpon = True
        self.calcentry = tki.Entry(self.mainwindow, state = "readonly"
                                   , textvariable = self.calctext
                                   , justify = tki.RIGHT, width = 18
                                   , font = self.widgetfont
                                   , foreground = self.widgetforeground
                                   , background = self.widgetbackground)
        self.onebutton = tki.Button(self.mainwindow, text = "1", height = 1
                                    , command = self.enterone, width = 1
                                    , font = self.widgetfont
                                    , foreground = self.widgetforeground
                                    , background = self.widgetbackground)
        self.twobutton = tki.Button(self.mainwindow, text = "2", height = 1
                                    , command = self.entertwo, width = 1
                                    , font = self.widgetfont
                                    , foreground = self.widgetforeground
                                    , background = self.widgetbackground)
        self.threebutton = tki.Button(self.mainwindow, text = "3", height = 1
                                      , command = self.enterthree, width = 1
                                      , font = self.widgetfont
                                      , foreground = self.widgetforeground
                                      , background = self.widgetbackground)
        self.fourbutton = tki.Button(self.mainwindow, text = "4", height = 1
                                     , command = self.enterfour, width = 1
                                     , font = self.widgetfont
                                     , foreground = self.widgetforeground
                                     , background = self.widgetbackground)
        self.fivebutton = tki.Button(self.mainwindow, text = "5", height = 1
                                     , command = self.enterfive, width = 1
                                     , font = self.widgetfont
                                     , foreground = self.widgetforeground
                                     , background = self.widgetbackground)
        self.sixbutton = tki.Button(self.mainwindow, text = "6", height = 1
                                    , command = self.entersix, width = 1
                                    , font = self.widgetfont
                                    , foreground = self.widgetforeground
                                    , background = self.widgetbackground)
        self.sevenbutton = tki.Button(self.mainwindow, text = "7", height = 1
                                      , command = self.enterseven, width = 1
                                      , font = self.widgetfont
                                      , foreground = self.widgetforeground
                                      , background = self.widgetbackground)
        self.eightbutton = tki.Button(self.mainwindow, text = "8", height = 1
                                      , command = self.entereight, width = 1
                                      , font = self.widgetfont
                                      , foreground = self.widgetforeground
                                      , background = self.widgetbackground)
        self.ninebutton = tki.Button(self.mainwindow, text = "9", height = 1
                                     , command = self.enternine, width = 1
                                     , font = self.widgetfont
                                     , foreground = self.widgetforeground
                                     , background = self.widgetbackground)
        self.zerobutton = tki.Button(self.mainwindow, text = "0", height = 1
                                     , command = self.enterzero, width = 1
                                     , font = self.widgetfont
                                     , foreground = self.widgetforeground
                                     , background = self.widgetbackground)
        self.pointbutton = tki.Button(self.mainwindow, text = ".", height = 1
                                      , command = self.enterpoint, width = 1
                                      , font = self.widgetfont
                                      , foreground = self.widgetforeground
                                      , background = self.widgetbackground)
        self.addbutton = tki.Button(self.mainwindow, text = "+", height = 1
                                    , command = self.add, width = 1
                                    , font = self.widgetfont
                                    , foreground = self.widgetforeground
                                    , background = self.widgetbackground)
        self.subtractbutton = tki.Button(self.mainwindow, text = "-", height = 1
                                         , command = self.subtract, width = 1
                                         , font = self.widgetfont
                                         , foreground = self.widgetforeground
                                         , background = self.widgetbackground)
        self.multiplybutton = tki.Button(self.mainwindow, text = "×", height = 1
                                         , command = self.multiply, width = 1
                                         , font = self.widgetfont
                                         , foreground = self.widgetforeground
                                         , background = self.widgetbackground)
        self.dividebutton = tki.Button(self.mainwindow, text = "÷", height = 1
                                       , command = self.divide, width = 1
                                       , font = self.widgetfont
                                       , foreground = self.widgetforeground
                                       , background = self.widgetbackground)
        self.equatebutton = tki.Button(self.mainwindow, text = "=", height = 3
                                       , command = self.equate, width = 1
                                       , font = self.widgetfont
                                       , foreground = self.widgetforeground
                                       , background = self.widgetbackground)
        self.powerbutton = tki.Button(self.mainwindow, text = "xʸ", height = 1
                                      , command = self.power, width = 1
                                      , font = self.widgetfont
                                      , foreground = self.widgetforeground
                                      , background = self.widgetbackground)
        self.reversebutton = tki.Button(self.mainwindow, text = "±", height = 1
                                        , command = self.reversenumber
                                        , width = 1, font = self.widgetfont
                                        , foreground = self.widgetforeground
                                        , background = self.widgetbackground)
        self.inversebutton = tki.Button(self.mainwindow, text = "1/x"
                                        , height = 1, width = 1
                                        , command = self.invertnumber
                                        , font = self.widgetfont
                                        , foreground = self.widgetforeground
                                        , background = self.widgetbackground)
        self.squarerootbutton = tki.Button(self.mainwindow, text = "√"
                                           , width = 1, height = 1
                                           , command = self.squareroot
                                           , font = self.widgetfont
                                           , background = self.widgetbackground
                                           , foreground = self.widgetforeground)
        self.approxbutton = tki.Button(self.mainwindow, text = "~", width = 1
                                       , height = 1, command = self.approximate
                                       , font = self.widgetfont
                                       , background = self.widgetbackground
                                       , foreground = self.widgetforeground)
        self.pibutton = tki.Button(self.mainwindow, text = "π", height = 1
                                   , command = self.piconstant, width = 1
                                   , font = self.widgetfont
                                   , foreground = self.widgetforeground
                                   , background = self.widgetbackground)
        self.backbutton = tki.Button(self.mainwindow, text = "←", height = 1
                                     , command = self.backspace, width = 1
                                     , font = self.widgetfont
                                     , foreground = self.widgetforeground
                                     , background = self.widgetbackground)
        self.clearbutton = tki.Button(self.mainwindow, text = "C", height = 1
                                      , command = self.clearcalc, width = 1
                                      , font = self.widgetfont
                                      , foreground = self.widgetforeground
                                      , background = self.widgetbackground)
        self.helplabel = tki.Label(self.mainwindow, height = 2, width = 22
                                   , font = "Courier 10", justify = tki.CENTER
                                   , foreground = self.widgetforeground
                                   , background = self.widgetbackground
                                   , text = """PyCalc version 0.9 
By CoolCanuck""")
        self.calcentry.grid(column = 0, row = 0, columnspan = 5)
        self.onebutton.grid(column = 0, row = 1)
        self.twobutton.grid(column = 1, row = 1)
        self.threebutton.grid(column = 2, row = 1)
        self.fourbutton.grid(column = 0, row = 2)
        self.fivebutton.grid(column = 1, row = 2)
        self.sixbutton.grid(column = 2, row = 2)
        self.sevenbutton.grid(column = 0, row = 3)
        self.eightbutton.grid(column = 1, row = 3)
        self.ninebutton.grid(column = 2, row = 3)
        self.zerobutton.grid(column = 0, row = 4)
        self.pointbutton.grid(column = 1, row = 4)
        self.addbutton.grid(column = 0, row = 5)
        self.subtractbutton.grid(column = 1, row = 5)
        self.multiplybutton.grid(column = 2, row = 5)
        self.dividebutton.grid(column = 3, row = 5)
        self.equatebutton.grid(column = 4, row = 4, rowspan = 2)
        self.powerbutton.grid(column = 3, row = 3)
        self.reversebutton.grid(column = 3, row = 1)
        self.inversebutton.grid(column = 3, row = 2)
        self.squarerootbutton.grid(column = 3, row = 4)
        self.approxbutton.grid(column = 4, row = 3)
        self.pibutton.grid(column = 2, row = 4)
        self.backbutton.grid(column = 4, row = 1)
        self.clearbutton.grid(column = 4, row = 2)
        self.helplabel.grid(column = 0, row = 6, columnspan = 5)
        self.calctext.set("0")
        self.mainwindow.bind("1", self.enterone)
        self.mainwindow.bind("2", self.entertwo)
        self.mainwindow.bind("3", self.enterthree)
        self.mainwindow.bind("4", self.enterfour)
        self.mainwindow.bind("5", self.enterfive)
        self.mainwindow.bind("6", self.entersix)
        self.mainwindow.bind("7", self.enterseven)
        self.mainwindow.bind("8", self.entereight)
        self.mainwindow.bind("9", self.enternine)
        self.mainwindow.bind("0", self.enterzero)
        self.mainwindow.bind(".", self.enterpoint)
        self.mainwindow.bind("+", self.add)
        self.mainwindow.bind("-", self.subtract)
        self.mainwindow.bind("*", self.multiply)
        self.mainwindow.bind("/", self.divide)
        self.mainwindow.bind("^", self.power)
        self.mainwindow.bind("=", self.equate)
        self.mainwindow.bind("H", self.togglehelp)
        self.mainwindow.bind("<BackSpace>", self.backspace)
        self.mainwindow.bind("<Delete>", self.clearcalc)
        self.mainwindow.bind("<Escape>", self.closeapplication)
        self.calcentry.bind("<Enter>", self.changehelpcalc)
        self.onebutton.bind("<Enter>", self.changehelpone)
        self.twobutton.bind("<Enter>", self.changehelptwo)
        self.threebutton.bind("<Enter>", self.changehelpthree)
        self.fourbutton.bind("<Enter>", self.changehelpfour)
        self.fivebutton.bind("<Enter>", self.changehelpfive)
        self.sixbutton.bind("<Enter>", self.changehelpsix)
        self.sevenbutton.bind("<Enter>", self.changehelpseven)
        self.eightbutton.bind("<Enter>", self.changehelpeight)
        self.ninebutton.bind("<Enter>", self.changehelpnine)
        self.zerobutton.bind("<Enter>", self.changehelpzero)
        self.pointbutton.bind("<Enter>", self.changehelppoint)
        self.addbutton.bind("<Enter>", self.changehelpadd)
        self.subtractbutton.bind("<Enter>", self.changehelpsubtract)
        self.multiplybutton.bind("<Enter>", self.changehelpmultiply)
        self.dividebutton.bind("<Enter>", self.changehelpdivide)
        self.powerbutton.bind("<Enter>", self.changehelppower)
        self.equatebutton.bind("<Enter>", self.changehelpequate)
        self.reversebutton.bind("<Enter>", self.changehelpreverse)
        self.inversebutton.bind("<Enter>", self.changehelpinvert)
        self.approxbutton.bind("<Enter>", self.changehelpapprox)
        self.squarerootbutton.bind("<Enter>", self.changehelpsquare)
        self.pibutton.bind("<Enter>", self.changehelppi)
        self.backbutton.bind("<Enter>", self.changehelpback)
        self.clearbutton.bind("<Enter>", self.changehelpclear)
        self.helplabel.bind("<Enter>", self.changehelphelp)
        self.mainwindow.protocol("WM_DELETE_WINDOW", self.closeapplication)
        self.mainwindow.geometry("190x229+0+0")
        self.mainwindow.resizable(width = False, height = False)
        self.mainwindow.mainloop()
    def enternumber(self, number):
        entrynumber = self.calctext.get()
        if entrynumber == "0":
            if number == "0":
                return None
            if number == ".":
                entrynumber = ""
                number = "0.0"
            else:
                entrynumber = ""
        if entrynumber == "0.0":
            if number != "0":
                entrynumber = "0."
        if number == ".":
            for char in entrynumber:
                if char == ".":
                    return None
        entrynumber += number
        self.calctext.set(entrynumber)
    def operate(self, operator):
        entrynumber = self.calctext.get()
        self.equationlist.append(entrynumber)
        self.equationlist.append(operator)
        self.calctext.set("0")
    def equate(self, event = None):
        """Solve equation
Hotkey: ="""
        entrynumber = self.calctext.get()
        self.equationlist.append(entrynumber)
        if len(self.equationlist) < 3:
            self.equationlist = []
            return None
        while len(self.equationlist) > 1:
            number1 = self.equationlist.pop(0)
            operator = self.equationlist.pop(0)
            number2 = self.equationlist.pop(0)
            number1 = float(number1)
            number2 = float(number2)
            if operator == "+":
                answer = number1 + number2
            if operator == "-":
                answer = number1 - number2
            if operator == "*":
                answer = number1 * number2
            if operator == "/":
                answer = number1 / number2
            if operator == "**":
                answer = number1 ** number2
            self.equationlist.insert(0, answer)
        self.equationlist = []
        self.calctext.set(answer)
    def reversenumber(self, event = None):
        """Change sign(+-)
No hotkey."""
        entrynumber = self.calctext.get()
        entrynumber = float(entrynumber)
        entrynumber = -entrynumber
        entrynumber = str(entrynumber)
        self.calctext.set(entrynumber)
    def invertnumber(self, event = None):
        """Invert number
No hotkey."""
        entrynumber = self.calctext.get()
        entrynumber = float(entrynumber)
        entrynumber = 1 / entrynumber
        entrynumber = str(entrynumber)
        self.calctext.set(entrynumber)
    def piconstant(self, event = None):
        """Math constant π
No hotkey."""
        self.calctext.set("3.14159265359")
    def approximate(self, event = None):
        """Round up
Hotkey: ~"""
        entrynumber = self.calctext.get()
        entrynumber = float(entrynumber)
        entrynumber = int(entrynumber)
        self.calctext.set(entrynumber)
    def squareroot(self, event = None):
        """Square root-No hotkey
Approximate values"""
        entrynumber = self.calctext.get()
        entrynumber = float(entrynumber)
        divisor = 2.0
        increment = 1.0
        increment2 = 10.0
        accuracy = 0.01
        incrementbool = True
        if entrynumber < 0:
            return None
        while True:
            guess = entrynumber / divisor
            increment = divisor / increment2
            x = guess ** 2.0
            if x == entrynumber:
                self.calctext.set(str(guess))
                break
            if x > entrynumber - accuracy and x < entrynumber + accuracy:
                self.calctext.set(str(guess))
                break
            if x > entrynumber:
                divisor += increment
                if incrementbool == True:
                    incrementbool = False
                    increment2 = increment2 * 10
            if x < entrynumber:
                divisor -= increment
                if incrementbool == False:
                    incrementbool = True
                    increment2 = increment2 * 10
    def backspace(self, event = None):
        """Back
Hotkey: Backspace"""
        entrynumber = self.calctext.get()
        entrynumber = entrynumber[:-1]
        if entrynumber == "":
            entrynumber  = "0"
        self.calctext.set(entrynumber)
    def clearcalc(self, event = None):
        """Clear
Hotkey: Delete"""
        self.equationlist = []
        self.calctext.set("0")
    def enterone(self, event = None):
        """One
Hotkey: 1"""
        self.enternumber("1")
    def entertwo(self, event = None):
        """Two
Hotkey: 2"""
        self.enternumber("2")
    def enterthree(self, event = None):
        """Three
Hotkey: 3"""
        self.enternumber("3")
    def enterfour(self, event = None):
        """Four
Hotkey: 4"""
        self.enternumber("4")
    def enterfive(self, event = None):
        """Five
Hotkey: 5"""
        self.enternumber("5")
    def entersix(self, event = None):
        """Six
Hotkey: 6"""
        self.enternumber("6")
    def enterseven(self, event = None):
        """Seven
Hotkey: 7"""
        self.enternumber("7")
    def entereight(self, event = None):
        """Eight
Hotkey: 8"""
        self.enternumber("8")
    def enternine(self, event = None):
        """Nine
Hotkey: 9"""
        self.enternumber("9")
    def enterzero(self, event = None):
        """Zero
Hotkey: 0"""
        self.enternumber("0")
    def enterpoint(self, event = None):
        """Decimal point
Hotkey: ."""
        self.enternumber(".")
    def add(self, event = None):
        """Addition
Hotkey: +"""
        self.operate("+")
    def subtract(self, event = None):
        """Subtraction
Hotkey: -"""
        self.operate("-")
    def multiply(self, event = None):
        """Multiplication
Hotkey: *"""
        self.operate("*")
    def divide(self, event = None):
        """Division
Hotkey: /"""
        self.operate("/")
    def power(self, event = None):
        """Exponentiation
No hotkey"""
        self.operate("**")
    def changehelpcalc(self, event = None):
        self.helplabel.config(text = """PyCalc version 0.9
By CoolCanuck""")
    def changehelpone(self, event = None):
        self.helplabel.config(text = self.enterone.__doc__)
    def changehelptwo(self, event = None):
        self.helplabel.config(text = self.entertwo.__doc__)
    def changehelpthree(self, event = None):
        self.helplabel.config(text = self.enterthree.__doc__)
    def changehelpfour(self, event = None):
        self.helplabel.config(text = self.enterfour.__doc__)
    def changehelpfive(self, event = None):
        self.helplabel.config(text = self.enterfive.__doc__)
    def changehelpsix(self, event = None):
        self.helplabel.config(text = self.entersix.__doc__)
    def changehelpseven(self, event = None):
        self.helplabel.config(text = self.enterseven.__doc__)
    def changehelpeight(self, event = None):
        self.helplabel.config(text = self.entereight.__doc__)
    def changehelpnine(self, event = None):
        self.helplabel.config(text = self.enternine.__doc__)
    def changehelpzero(self, event = None):
        self.helplabel.config(text = self.enterzero.__doc__)
    def changehelppoint(self, event = None):
        self.helplabel.config(text = self.enterpoint.__doc__)
    def changehelpadd(self, event = None):
        self.helplabel.config(text = self.add.__doc__)
    def changehelpsubtract(self, event = None):
        self.helplabel.config(text = self.subtract.__doc__)
    def changehelpmultiply(self, event = None):
        self.helplabel.config(text = self.multiply.__doc__)
    def changehelpdivide(self, event = None):
        self.helplabel.config(text = self.divide.__doc__)
    def changehelppower(self, event = None):
        self.helplabel.config(text = self.power.__doc__)
    def changehelpequate(self, event = None):
        self.helplabel.config(text = self.equate.__doc__)
    def changehelpreverse(self, event = None):
        self.helplabel.config(text = self.reversenumber.__doc__)
    def changehelpinvert(self, event = None):
        self.helplabel.config(text = self.invertnumber.__doc__)
    def changehelpapprox(self, event = None):
        self.helplabel.config(text = self.approximate.__doc__)
    def changehelpsquare(self, event = None):
        self.helplabel.config(text = self.squareroot.__doc__)
    def changehelppi(self, event = None):
        self.helplabel.config(text = self.piconstant.__doc__)
    def changehelpclear(self, event = None):
        self.helplabel.config(text = self.clearcalc.__doc__)
    def changehelpback(self, event = None):
        self.helplabel.config(text = self.backspace.__doc__)
    def changehelphelp(self, event = None):
        self.helplabel.config(text = self.togglehelp.__doc__)
    def togglehelp(self, event = None):
        """Help display
Hotkey(Toggle): H"""
        x = self.mainwindow.geometry()
        windowlocation = ""
        count = 0
        for char in x:
            if char != "+":
                count += 1
                continue
            if char == "+":
                windowlocation = x[count:]
                break
        if self.helpon == True:
            self.helplabel.grid_remove()
            self.helpon = False
            self.mainwindow.geometry(str("190x195" + windowlocation))
            return None
        if self.helpon == False:
            self.helplabel.grid(column = 0, row = 6, columnspan = 5)
            self.helpon = True
            self.mainwindow.geometry(str("190x229" + windowlocation))
    def closeapplication(self, event = None):
        self.mainwindow.destroy()
        raise SystemExit
if __name__ == "__main__":
    application = PyCalcApplication()
