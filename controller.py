#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
from datetime import date
from tkinter import messagebox
import model
import view
import main

class Controller():
    """Controller class."""
    def __init__(self, parent):
        self.parent = parent
        self.year = date.today().year
        self.index = date.today().timetuple().tm_yday - 1
        self.view = view.View(self)
        self.model = model.Model(self)
        self.view.currentDay()

    saveQuestion = "Tietoja on muutettu. Haluatko jatkaa tallentamatta?"

    def firstDay(self):
        self.saveEdited()
        if self.model.days[self.index].weekday == 2 and self.index > 0:
            self.index -= 1
        elif self.model.days[self.index].weekday == 2 and self.index == 0:
            self.year -= 1
            self.index = main.daysInTheYear(self.year) - 1
            self.model = model.Model(self)
        elif self.model.days[self.index].weekday == 3 and self.index > 1:
            self.index -= 2
        elif self.model.days[self.index].weekday == 3 and self.index <= 1:
            self.year -= 1
            self.index = self.index - 2 + main.daysInTheYear(self.year)
            self.model = model.Model(self)
        elif self.model.days[self.index].weekday == 4 and self.index > 2:
            self.index -= 3
        elif self.model.days[self.index].weekday == 4 and self.index <= 2:
            self.year -= 1
            self.index = self.index - 3 + main.daysInTheYear(self.year)
            self.model = model.Model(self)
        elif self.model.days[self.index].weekday == 5 and self.index > 3:
            self.index -= 4
        elif self.model.days[self.index].weekday == 5 and self.index <= 3:
            self.year -= 1
            self.index = self.index - 4 + main.daysInTheYear(self.year)
            self.model = model.Model(self)
        elif self.model.days[self.index].weekday == 6 and self.index > 4:
            self.index -= 5
        elif self.model.days[self.index].weekday == 6 and self.index <= 4:
            self.year -= 1
            self.index = self.index - 5 + main.daysInTheYear(self.year)
            self.model = model.Model(self)
        elif self.model.days[self.index].weekday == 7 and self.index > 5:
            self.index -= 6
        elif self.model.days[self.index].weekday == 7 and self.index <= 5:
            self.year -= 1
            self.index = self.index - 6 + main.daysInTheYear(self.year)
            self.model = model.Model(self)
        elif self.model.days[self.index].weekday == 1 and self.index > 6:
            self.index -= 7
        elif self.model.days[self.index].weekday == 1 and self.index <= 6:
            self.year -= 1
            self.index = self.index - 7 + main.daysInTheYear(self.year)
            self.model = model.Model(self)
        self.view.currentDay()

    def previousDay(self):
        """previousDay on Controller class.
        Browses a day back and if needed saves changes."""
        self.saveEdited()
        if self.index > 0:
            self.index -= 1
        elif self.index == 0:
            self.year -= 1
            self.index = main.daysInTheYear(self.year) - 1
            self.model = model.Model(self)
        self.view.currentDay()
        
    def nextDay(self):
        """extDay function on Controller class.
        Browses a day ahead and if needed saves changes."""
        self.saveEdited()
        if self.index < len(self.model.days) - 1:
            self.index += 1
        elif self.index == len(self.model.days) - 1:
            self.year += 1
            self.index = 0
            self.model = model.Model(self)
        self.view.currentDay()
        
    def lastDay(self):
        """lastDay"""
        self.saveEdited()
        if self.model.days[self.index].weekday == 1 and self.index < len(self.model.days) - 6:
            self.index += 6
        elif self.model.days[self.index].weekday == 1 and self.index >= len(self.model.days) - 6:
            self.year += 1
            self.index = self.index + 6 - len(self.model.days) 
            self.model = model.Model(self)
        elif self.model.days[self.index].weekday == 2 and self.index < len(self.model.days) - 5:
            self.index += 5
        elif self.model.days[self.index].weekday == 2 and self.index >= len(self.model.days) - 5:
            self.year += 1
            self.index = self.index + 5 - len(self.model.days) 
            self.model = model.Model(self)
        elif self.model.days[self.index].weekday == 3 and self.index < len(self.model.days) - 4:
            self.index += 4
        elif self.model.days[self.index].weekday == 3 and self.index >= len(self.model.days) - 4:
            self.year += 1
            self.index = self.index + 4 - len(self.model.days) 
            self.model = model.Model(self)
        elif self.model.days[self.index].weekday == 4 and self.index < len(self.model.days) - 3:
            self.index += 3
        elif self.model.days[self.index].weekday == 4 and self.index >= len(self.model.days) - 3:
            self.year += 1
            self.index = self.index + 3 - len(self.model.days) 
            self.model = model.Model(self)
        elif self.model.days[self.index].weekday == 5 and self.index < len(self.model.days) - 2:
            self.index += 2
        elif self.model.days[self.index].weekday == 5 and self.index >= len(self.model.days) - 2:
            self.year += 1
            self.index = self.index + 2 - len(self.model.days) 
            self.model = model.Model(self)
        elif self.model.days[self.index].weekday == 6 and self.index < len(self.model.days) - 1:
            self.index += 1
        elif self.model.days[self.index].weekday == 6 and self.index == len(self.model.days) - 1:
            self.year += 1
            self.index = self.index + 1 - len(self.model.days) 
            self.model = model.Model(self)
        elif self.model.days[self.index].weekday == 7 and self.index < len(self.model.days) - 7:
            self.index += 7
        elif self.model.days[self.index].weekday == 7 and self.index >= len(self.model.days) - 7:
            self.year += 1
            self.index = self.index + 7 - len(self.model.days) 
            self.model = model.Model(self)
        self.view.currentDay()

    def today(self):
        """today"""
        self.saveEdited()
        Controller(self.parent)

    def firstWeek(self):
        """firstWeek"""
        self.saveEdited()
        self.index = 0
        self.view.currentDay()
        
    def previousWeek(self):
        """previousWeek"""
        self.saveEdited()
        if (self.index - 7) >= 0:
            self.index -= 7
        elif (self.index - 7) < 0:
            self.year -= 1
            self.index = (self.index - 7) + main.daysInTheYear(self.year)
            self.model = model.Model(self)
        self.view.currentDay()


    def nextWeek(self):
        self.saveEdited()
        if (self.index + 7) < len(self.model.days):
            self.index += 7
        elif (self.index + 7) >= len(self.model.days):
            self.year += 1
            self.index = (self.index + 7) - len(self.model.days)
            self.model = model.Model(self)
        self.view.currentDay()

    def lastWeek(self):
        self.saveEdited()
        self.index = len(self.model.days) - 1
        self.view.currentDay()

    def save(self):
        if main.isNumber(self.view.get_box_sleephour()):
            self.model.days[self.index].setSleepingTimeHours(int(self.view.get_box_sleephour()))
        if main.isNumber(self.view.get_box_sleepminute()):
            self.model.days[self.index].setSleepingTimeMinutes(int(self.view.get_box_sleepminute()))
        if main.isNumber(self.view.get_box_wakeuphour()):
            self.model.days[self.index].setWakeupTimeHours(int(self.view.get_box_wakeuphour()))
        if main.isNumber(self.view.get_box_wakeupminute()):
            self.model.days[self.index].setWakeupTimeMinutes(int(self.view.get_box_wakeupminute()))
        self.model.days[self.index].setNight(self.view.get_txt_night()) 
        self.model.days[self.index].setBreakfast(self.view.get_txt_breakfast())
        self.model.days[self.index].setMorning(self.view.get_txt_morning())
        self.model.days[self.index].setLunch(self.view.get_txt_lunch())
        self.model.days[self.index].setAfternoon(self.view.get_txt_afternoon())
        self.model.days[self.index].setDinner(self.view.get_txt_dinner())
        self.model.days[self.index].setEvening(self.view.get_txt_evening())
        self.model.saveADay()
        self.view.currentDay()
        messagebox.showinfo("Tiedote", "Päivä tallennettu")

    def season(self):
        month = self.model.days[self.index].month
        result = ""
        if month >= 1 and month <= 3:
                result = "Talvi"
        elif  month >= 4 and month <= 6:
                result = "Kevät"
        elif  month >= 7 and month <= 9:
                result = "Kesä"
        elif month >= 10 and month <= 12:
                result = "Syksy"
        else:
                messagebox.showerror("Virhe", "Virheellinen kuukausi")
        return result

    def htmlBegin(self):
        cssPath = "file:///work_sample/DiaryPrinter/styles/diary.css"
        html = "<!DOCTYPE html>\n<html>"
        html += "\n<head>\n\t<meta http-equiv=\"Content-Type\" content=\"text/html;charset=utf-8\" />"
        html += "\n\t<link rel=\"stylesheet\"type=\"text/css\" href=\"" + cssPath + "\" />"
        html += "\n<title>Viikko " + str(self.model.days[self.index].week) + "</title>\n</head>"
        html += "\n<body>\n\t<div id=\"sisalto\">"
        html += "\n\t\t<div id=\"yotausta\"></div>\n\t\t<div id=\"navigaatiotausta\"></div>"
        html += "\n\t\t<div id=\"aamutausta\"></div>\n\t\t<div id=\"iltapaivatausta\"></div>"
        html += "\n\t\t<div id=\"iltatausta\"></div>\n\t\t<div id=\"maanantaitausta\"></div>"
        html += "\n\t\t<div id=\"tiistaitausta\"></div>\n\t\t<div id=\"keskiviikkotausta\"></div>"
        html += "\n\t\t<div id=\"torstaitausta\"></div>\n\t\t<div id=\"perjantaitausta\"></div>"
        html += "\n\t\t<div id=\"lauantaitausta\"></div>\n\t\t<div id=\"sunnuntaitausta\"></div>"
        html += "\n\t\t<div id=\"otsikkotausta\"></div>\n\t\t<div id=\"atausta\"></div> "
        html += "\n\t\t<div id=\"navigaatio\">\n\t\t\t<div id=\"backward\">\n\t\t\t\t<a href=\""
        html += str(self.model.days[self.index].week - 1)
        html += ".html\">\n\t\t\t\t\t<img src=\"./icons/week_backward.png\" alt=\"backward\" align=\"middle\">"
        html += "\n\t\t\t\t</a>\n\t\t\t</div>\n\t\t\t<div id=\"home\">\n\t\t\t\t<a href=\"../"
        html += self.season()
        html += ".html\">\n\t\t\t\t\t<img src=\"./icons/week_home.png\" alt=\"home\" align=\"middle\">\n\t\t\t\t</a>"
        html += "\n\t\t\t</div>\n\t\t\t<div id=\"forward\">\n\t\t\t\t<a href=\""
        html += str(self.model.days[self.index].week + 1)
        html += ".html\">\n\t\t\t\t\t<img src=\"./icons/week_forward.png\" alt=\"forward\" align=\"middle\">"
        html += "\n\t\t\t\t</a>\n\t\t\t</div>\n\t\t</div>\n\t\t<div id=\"otsikko\">\n\t\t\t<h1>Viikko "
        html += str(self.model.days[self.index].week)
        html += "</h1>\n\t\t</div>\n\t\t<div id=\"a2\">\n\t\t\t<h3>Maanantai</h3>\n\t\t</div>\n\t\t<div id=\"a3\">"
        html += "\n\t\t\t<h3>Tiistai</h3>\n\t\t</div>\n\t\t<div id=\"a4\">\n\t\t\t<h3>Keskiviikko</h3>\n\t\t</div>"
        html += "\n\t\t<div id=\"a5\">\n\t\t\t<h3>Torstai</h3>\n\t\t</div>\n\t\t<div id=\"a6\">\n\t\t\t<h3>Perjantai</h3>"
        html += "\n\t\t</div>\n\t\t<div id=\"a7\">\n\t\t\t<h3>Lauantai</h3>\n\t\t</div>\n\t\t<div id=\"a8\">\n\t\t\t<h3>Sunnuntai</h3>\n\t\t</div>"
        html += "\n\t\t<div id=\"yo1\">\n\t\t\t<div id=\"yo2\">\n\t\t\t\t<span class=\"tunti\">Y</span><br>\n\t\t\t\t<span class=\"tunti\">ö</span><br>"
        html += "\n\t\t\t</div>\n\t\t</div>\n\t\t<div id=\"aamu1\">\n\t\t\t<div id=\"aamu2\">\n\t\t\t\t<span class=\"tunti\">A</span><br>"
        html += "\n\t\t\t\t<span class=\"tunti\">a</span><br>\n\t\t\t\t<span class=\"tunti\">m</span><br>\n\t\t\t\t<span class=\"tunti\">u</span>"
        html += "<br>\n\t\t\t</div>\n\t\t</div>\n\t\t<div id=\"iltapaiva1\">\n\t\t\t<div id=\"iltapaiva2\">\n\t\t\t\t<span class=\"tunti\">I</span><br>"
        html += "\n\t\t\t\t<span class=\"tunti\">l</span><br>\n\t\t\t\t<span class=\"tunti\">t</span><br>\n\t\t\t\t<span class=\"tunti\">a</span><br>"
        html += "\n\t\t\t\t<span class=\"tunti\">p</span><br>\n\t\t\t\t<span class=\"tunti\">ä</span><br>\n\t\t\t\t<span class=\"tunti\">i</span><br>"
        html += "\n\t\t\t\t<span class=\"tunti\">v</span><br>\n\t\t\t\t<span class=\"tunti\">ä</span><br>\n\t\t\t</div>"
        html += "\n\t\t</div>\n\t\t<div id=\"ilta1\">\n\t\t\t<div id=\"ilta2\">\n\t\t\t\t<span class=\"tunti\">I</span><br>"
        html += "\n\t\t\t\t<span class=\"tunti\">l</span><br>\n\t\t\t\t<span class=\"tunti\">t</span><br>"
        html += "\n\t\t\t\t<span class=\"tunti\">a</span><br>\n\t\t\t</div>\n\t\t</div>"
        html += "\n\t\t<!--=============SISÄLTÖ=====================================================================-->"
        return html

    def dayToPrint(self, j):
        currentWeekDay = self.model.printDays[j].getWeekday()
        result = ""
        if currentWeekDay == 1:
                result = "maanantai"
        elif currentWeekDay == 2:
                result = "tiistai"
        elif currentWeekDay == 3:
                result = "keskiviikko"
        elif currentWeekDay == 4:
                result = "torstai"
        elif currentWeekDay == 5:
                result = "perjantai"
        elif currentWeekDay == 6:
                result = "lauantai"
        elif currentWeekDay == 7:
                result = "sunnuntai"
        else:
                messagebox.showerror("Virhe", "Virheellinen viikonpäivänumero")
        return result

    def printDays(self):
        html = ""
        i = 0
        while i < 7:
            html += "\n\n\t\t<!--============="
            html += self.dayToPrint(i)
            html += "===================================================================-->"
            html += "\n\t\t<div id=\"yo"
            html += self.dayToPrint(i)
            html += "\">\n\t\t\t<div class=\"nukkumaan otsake\">Nukkumaan:\n\t\t\t</div>"
            html += "\n\t\t\t<div class=\"nukkumisaika syote\">"
            html += "\n\t\t\t"
            if self.model.printDays[i].sleepingTimeHours is not None:
                html += str(self.model.printDays[i].sleepingTimeHours) + ":"
            if self.model.printDays[i].sleepingTimeMinutes is not None:
                html += str(self.model.printDays[i].sleepingTimeMinutes)
            html += "\n\t\t</div>\n\t\t<div class=\"heratys otsake\">"
            html += "Herätys:</div>\n\t\t<div class=\"heratysaika syote\">"
            html += "\n\t\t\t" 
            if self.model.printDays[i].wakeupTimeHours is not None:
                html += str(self.model.printDays[i].wakeupTimeHours) + ":"
            if self.model.printDays[i].wakeupTimeMinutes is not None:
                html += str(self.model.printDays[i].wakeupTimeMinutes)
            html += "\n\t\t</div>\n\t\t<div class=\"yo syote\">"
            html += "\n\t\t\t" + str(self.model.printDays[i].night)
            html += "\n\t\t</div>\n\t</div>\n\t<div id=\"aamu"
            html += self.dayToPrint(i)
            html += "\">\n\t\t<div class=\"aamupalaotsake otsake\">"
            html += "\n\t\t\tAamupala:\n\t\t</div>\n\t\t<div class=\"aamupala syote\">"
            html += "\n\t\t\t" + str(self.model.printDays[i].breakfast)
            html += "\n\t\t</div>\n\t\t<div class=\"aamu syote\">"
            html += "\n\t\t\t" + str(self.model.printDays[i].morning)
            html += "\n\t\t</div>\n\t</div>\n\t<div id=\"iltapaiva"
            html += self.dayToPrint(i)
            html += "\">\n\t\t<div class=\"lounasotsake otsake\">\n\t\t\tLounas:"
            html += "\n\t\t</div>\n\t\t<div class=\"lounas syote\">"
            html += "\n\t\t\t" + str(self.model.printDays[i].lunch)
            html += "\n\t\t</div>\n\t\t<div class=\"iltapaiva syote\">"
            html += "\n\t\t\t" + str(self.model.printDays[i].afternoon)
            html += "\n\t\t</div>\n\t</div>\n\t<div id=\"ilta"
            html += self.dayToPrint(i)
            html += "\">\n\t\t<div class=\"paivallisotsake otsake\">\n\t\t\tPäivällinen:"
            html += "\n\t\t</div>\n\t\t<div class=\"paivallinen syote\">"
            html += "\n\t\t\t" + str(self.model.printDays[i].dinner)
            html += "\n\t\t</div>\n\t\t<div class=\"ilta syote\">"
            html += "\n\t\t\t" + str(self.model.printDays[i].evening)
            html += "\n\t\t</div>\n\t</div>"
            i += 1
        return html

    def printWeek(self):
        """printWeek function on Controller class.
        Prints weeks diary."""
        html = self.htmlBegin()
        self.model.printdata()
        html += self.printDays()
        html += "\n</body>\n</html>"
        try:
            f = open("/work_sample/DiaryPrinter/" +
            str(self.model.days[self.index].week) +
            ".html", "w")
            f.write(html)
            f.close()
        except IOError:
            messagebox.showerror("Virhe", "Virhe viikon tulostuksessa")
        messagebox.showinfo("Tiedote", "Viikkopäiväkirja tulostettu")

    def isEdited(self):
        """isEdited function on Controller class.
        Checks if any input field is edited."""
        result = False
        index = self.index
        sleephour = self.view.get_box_sleephour()
        sleepminute = self.view.get_box_sleepminute()
        wakeuphour = self.view.get_box_wakeuphour()
        wakeupminute = self.view.get_box_wakeupminute()
        night = self.view.get_txt_night().rstrip("\n")
        breakfast = self.view.get_txt_breakfast().rstrip("\n")
        morning = self.view.get_txt_morning().rstrip("\n")
        lunch = self.view.get_txt_lunch().rstrip("\n")
        afternoon = self.view.get_txt_afternoon().rstrip("\n")
        dinner = self.view.get_txt_dinner().rstrip("\n")
        evening = self.view.get_txt_evening().rstrip("\n")

        if  sleephour != "t" and str(self.model.days[index].sleepingTimeHours) != sleephour:
            result = True
            print("sleepingTimeHours oli: " + str(self.model.days[index].sleepingTimeHours))
            print("sleephour oli: " + str(sleephour))            
            print("!= sleephour")
        elif sleepminute != "min" and str(self.model.days[index].sleepingTimeMinutes) != sleepminute:
            result = True
            print("!= sleepminute")
        elif wakeuphour != "t" and str(self.model.days[index].wakeupTimeHours) != wakeuphour:
            result = True
            print("!= wakeuphour")
        elif wakeupminute != "min" and str(self.model.days[index].wakeupTimeMinutes) != wakeupminute:
            result = True
            print("!= wakeupminute")
        elif self.model.days[index].night.rstrip("\n") != night:
            result = True
            print("!= night")
            print("[index].night oli: " + str(self.model.days[index].night))
            print("night oli: " + str(night)) 
        elif str(self.model.days[index].breakfast).rstrip("\n") != breakfast:
            result = True
            print("!= breakfast")
            print("[index].breakfast oli: " + str(self.model.days[index].breakfast).rstrip("\n"))
            print("breakfast oli: " + str(breakfast)) 
        elif str(self.model.days[index].morning).rstrip("\n") != morning:
            result = True
            print("!= morning")
        elif str(self.model.days[index].lunch).rstrip("\n") != lunch:
            result = True
            print("!= lunch")
        elif str(self.model.days[index].afternoon).rstrip("\n") != afternoon:
            result = True
            print("!= afternoon")
        elif str(self.model.days[index].dinner).rstrip("\n") != dinner:
            result = True
            print("!= dinner")
        elif str(self.model.days[index].evening).rstrip("\n") != evening:
            result = True
            print("!= evening")
        return result

    def saveEdited(self):
        """saveEdited function on Controller class.
        Saves edited data.."""
        if self.isEdited():
            if messagebox.askokcancel("Kysymys", self.saveQuestion):
                pass
            else:
                self.save()
