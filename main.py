#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
import tkinter as tk
import datetime
from datetime import date 
import controller

def daysInTheYear(year):
    d2 = datetime.datetime(year, 12, 31) 
    d1 = datetime.datetime(year, 1, 1)  
    return (d2 - d1).days + 1 

def isNumber(entry):
    try:
        if entry is None:
            return False
        else:
            float(entry)
            return True
    except ValueError:
        return False

class Day():
    """Day class. Diary day object."""
    def __init__(self, ordinal):
        """__init__ function on Day class.
        Constructs the day object."""
        self.year = date.fromordinal(ordinal).year
        self.month = date.fromordinal(ordinal).month
        self.day = date.fromordinal(ordinal).day
        self.week = date.fromordinal(ordinal).isocalendar()[1]
        self.weekday = date.fromordinal(ordinal).isoweekday()
        self.sleepingTimeHours = None
        self.sleepingTimeMinutes = None
        self.wakeupTimeHours = None
        self.wakeupTimeMinutes = None
        self.night = ""
        self.breakfast = ""
        self.morning = ""
        self.lunch = ""
        self.afternoon = ""
        self.dinner = ""
        self.evening = ""
        self.id = ordinal

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = int(id)

    def getYear(self):
        return self.year

    def setYear(self, year):
        self.year = int(year)

    def getMonth(self):
        return self.month

    def setMonth(self, month):
        if month >= 1 and month <= 12:
            self.month = int(month)
        else:
            self.month = None

    def getDay(self):
        return self.day

    def setDay(self, day):
        if day >= 1 and day <= 31:
            self.day = int(day)
        else:
            self.day = None

    def getWeek(self):
        return self.week

    def setWeek(self, week):
        if week >= 1 and week <= 53:
            self.week = int(week)
        else:
            self.week = None

    def getWeekday(self):
        return self.weekday

    def setWeekday(self, weekday):
        if weekday >= 1 and weekday <= 7:
            self.weekday = int(weekday)
        else:
            self.weekday = None

    def getSleepingTimeHours(self):
        return self.sleepingTimeHours

    def setSleepingTimeHours(self, sleephours):
        if isNumber(sleephours):
            self.sleepingTimeHours = int(sleephours)
        else:
            self.sleepingTimeHours = None

    def getSleepingTimeMinutes(self):
        return self.sleepingTimeMinutes

    def setSleepingTimeMinutes(self, sleepminutes):
        if isNumber(sleepminutes):
            self.sleepingTimeMinutes = int(sleepminutes)
        else:
            self.sleepingTimeMinutes = None

    def getWakeupTimeHours(self):
        return self.wakeupTimeHours

    def setWakeupTimeHours(self, wakeuphours):
        if isNumber(wakeuphours):
            self.wakeupTimeHours = int(wakeuphours)
        else:
            self.wakeupTimeHours = None

    def getWakeupTimeMinutes(self):
            return self.wakeupTimeMinutes

    def setWakeupTimeMinutes(self, wakeupminutes):
        if isNumber(wakeupminutes):
            self.wakeupTimeMinutes = int(wakeupminutes)
        else:
            self.wakeupTimeMinutes = None

    def getNigth(self):
        return self.night
    
    def setNight(self, night):
        self.night = "" + night

    def getBreakfast(self):
        return self.breakfast

    def setBreakfast(self, breakfast):
        self.breakfast = "" + breakfast

    def getMorning(self):
        return self.morning

    def setMorning(self, morning):
        self.morning = "" + morning

    def getLunch(self):
        return self.lunch

    def setLunch(self, lunch):
        self.lunch = "" + lunch

    def getAfternoon(self):
        return self.afternoon

    def setAfternoon(self,afternoon):
        self.afternoon = "" + afternoon

    def getDinner(self):
        return self.dinner

    def setDinner(self, dinner):
        self.dinner = "" + dinner

    def getEvening(self):
        return self.evening

    def setEvening(self, evening):
        self.evening = "" + evening

def main():
    """#############################################################################################
    Program:    DIARY PRINT

    Files:    main.py, controller.py, view.py, model.py, db_days, create_table_days.sql, 
              week_backward.png, week_forward.png, week_ home.pgn, diary.css.
        
    Description:    Prints personal diary files in html

    Author:    Pekka Paldánius (PP)

    Environments:    Linux Z87MPlus 3.16.0-38-generic #52~14.04.1-Ubuntu SMP 
                    Fri May 8 09:43:57 UTC 2015 
                    x86_64 x86_64 x86_64 GNU/Linux, python 3.4, SQLite 3.6.18,
                     Firefox Quantum 57.0.1(64-bit)

    Remarks:        This is computer hobbyists homework

    Updates:        0.1 29.12.2017 (PP)

        
    Global main function on main.py
 
    ################################################################################################"""
    root = tk.Tk()
    root.geometry("700x950+300+300")
    root.title("Päiväkirja")
    app = controller.Controller(root)
    root.mainloop()

if __name__ == '__main__':
    main()
