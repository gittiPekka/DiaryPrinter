#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
import datetime
from datetime import date
import sqlite3
from tkinter import messagebox
import main

class Model():
    """Model class. Diary data object."""
    def __init__(self, modelController):
        """__init__ function on Model class.
        Constructs the data object."""
        self.days = list()
        self.mc = modelController
        self.standarddata()
        self.saveddata()
        self.printDays = list()

    def standarddata(self):
        """standarddata function on Model class.
        Sets standard information to the day elements."""
        year = self.mc.year
        for yday in range(1, date(year, 12, 31).timetuple().tm_yday + 1):
            ordinal = date(year, 1, 1).toordinal() + yday - 1
            record = main.Day(ordinal)
            self.days.append(record)

    def saveddata(self):
        """saveddata function on Model class.
        Sets personal information to the day elements."""
        path = '/work_sample/DiaryPrinter/database/db_days'
        year = self.mc.year
        start = date(year, 1, 1).toordinal()
        end = date(year, 12, 31).toordinal()
        try:
            conn = sqlite3.connect(path)
            c = conn.cursor()
            for ordinal in range(start, end + 1):
                t = (str(ordinal),)
                sql = "select"
                sql += " id,sleepingTimeHours,sleepingTimeMinutes,"
                sql += "wakeupTimeHours,wakeupTimeMinutes,"
                sql += "night,breakfast,morning,"
                sql += "lunch,afternoon,dinner,evening from days where id = ?"
                c.execute(sql, t)
                data = c.fetchone()
                if data is not None and data[1] is not None:
                    self.days[ordinal - start].setSleepingTimeHours(data[1])
                if data is not None and data[2] is not None:
                    self.days[ordinal - start].setSleepingTimeMinutes(data[2])
                if data is not None and data[3] is not None:
                    self.days[ordinal - start].setWakeupTimeHours(data[3])
                if data is not None and data[4] is not None:
                    self.days[ordinal - start].setWakeupTimeMinutes(data[4])
                if data is not None and data[5] is not None:
                    self.days[ordinal - start].setNight(data[5])
                if data is not None and data[6] is not None:
                    self.days[ordinal - start].setBreakfast(data[6])
                if data is not None and data[7] is not None:
                    self.days[ordinal - start].setMorning(data[7])
                if data is not None and data[8] is not None:
                    self.days[ordinal - start].setLunch(data[8])
                if data is not None and data[9] is not None:
                    self.days[ordinal - start].setAfternoon(data[9])
                if data is not None and data[10] is not None:
                    self.days[ordinal - start].setDinner(data[10])
                if data is not None and data[11] is not None:
                    self.days[ordinal - start].setEvening(data[11])
            c.close()
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Virhe alustustietojen hakemisessa", e.args[0])

    def printdata(self):
        """printdata function on Model class.
        Creates a weeks list for printing"""
        start = self.days[self.mc.index].getId()
        subtraction = self.days[self.mc.index].getWeekday() - 1
        ordinal = start - subtraction
        path = '/work_sample/DiaryPrinter/database/db_days'
        try:
            conn = sqlite3.connect(path)
            c = conn.cursor()
            i = 0
            while i < 7:
                self.printDays.append(main.Day(ordinal))
                t = (str(ordinal),)
                sql = "select"
                sql += " id,sleepingTimeHours,sleepingTimeMinutes,"
                sql += "wakeupTimeHours,wakeupTimeMinutes,"
                sql += "night,breakfast,morning,"
                sql += "lunch,afternoon,dinner,evening from days where id = ?"
                c.execute(sql, t)
                data = c.fetchone()
                if data is not None and data[1] is not None:
                    self.printDays[i].setSleepingTimeHours(data[1])
                if data is not None and data[2] is not None:
                    self.printDays[i].setSleepingTimeMinutes(data[2])
                if data is not None and data[3] is not None:
                    self.printDays[i].setWakeupTimeHours(data[3])
                if data is not None and data[4] is not None:
                    self.printDays[i].setWakeupTimeMinutes(data[4])
                if data is not None and data[5] is not None:
                    self.printDays[i].setNight(data[5])
                if data is not None and data[6] is not None:
                    self.printDays[i].setBreakfast(data[6])
                if data is not None and data[7] is not None:
                    self.printDays[i].setMorning(data[7])
                if data is not None and data[8] is not None:
                    self.printDays[i].setLunch(data[8])
                if data is not None and data[9] is not None:
                    self.printDays[i].setAfternoon(data[9])
                if data is not None and data[10] is not None:
                    self.printDays[i].setDinner(data[10])
                if data is not None and data[11] is not None:
                    self.printDays[i].setEvening(data[11])
                i += 1
                ordinal += 1
            c.close()
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Virhe tulostustietojen hakemisessa", e.args[0])

    def isRow(self):
        """isRow function on Model class.
        Returns true if the day in action is in database."""
        path = '/work_sample/DiaryPrinter/database/db_days'
        result = None
        try:
            conn = sqlite3.connect(path)
            c = conn.cursor()
            t = (str(self.days[self.mc.index].id),)
            c.execute("select id from days where id = ?", t)
            result = c.fetchone()
            c.close()
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Virhe id:n hakemisessa ", e.args[0])
        if result is not None:
            return True
        else:
            return False

    def dayToSave(self):
        saveDay = (self.days[self.mc.index].sleepingTimeHours,
        self.days[self.mc.index].sleepingTimeMinutes,
        self.days[self.mc.index].wakeupTimeHours,
        self.days[self.mc.index].wakeupTimeMinutes,
        self.days[self.mc.index].night,
        self.days[self.mc.index].breakfast,
        self.days[self.mc.index].morning,
        self.days[self.mc.index].lunch,
        self.days[self.mc.index].afternoon,
        self.days[self.mc.index].dinner,
        self.days[self.mc.index].evening,
        self.days[self.mc.index].id)
        return [saveDay]
  
    def insertDay(self):
        """insertDay function on Model class.
        Inserts a days data in the base."""
        path = '/work_sample/DiaryPrinter/database/db_days'   
        try:
            conn = sqlite3.connect(path)
            c = conn.cursor()
            sql = "insert into days (sleepingTimeHours,"
            sql += "sleepingTimeMinutes,wakeupTimeHours,"
            sql += "wakeupTimeMinutes,night,breakfast,"
            sql += "morning,lunch,afternoon,"
            sql += "dinner,evening,id)"
            sql += " values (?,?,?,?,?,?,?,?,?,?,?,?)"
            c.executemany(sql, self.dayToSave())
            conn.commit()
            c.close()
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Virhe tietojen syötössä ", e.args[0])

    def updateDay(self):
        """updateDay function on Model class.
        Updates days data in base."""
        path = '/work_sample/DiaryPrinter/database/db_days'
        try:
            conn = sqlite3.connect(path)
            c = conn.cursor()
            sql = "update days set sleepingTimeHours = (?)"
            sql += ", sleepingTimeMinutes = (?)"
            sql += ", wakeupTimeHours = (?)"
            sql += ", wakeupTimeMinutes = (?)"
            sql += ", night = (?)"
            sql += ", breakfast = (?)"
            sql += ", morning = (?)"
            sql += ", lunch = (?)"
            sql += ", afternoon = (?)"
            sql += ", dinner = (?)"
            sql += ", evening = (?)"
            sql += " where id = (?)"
            c.executemany(sql, self.dayToSave())
            conn.commit()
            c.close()
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Virhe tietojen päivityksessä ", e.args[0])

    def saveADay(self):
        """saveADay function on Model class.
        Saves days data to the base."""
        if self.isRow():
            self.updateDay()
        else:
            self.insertDay()
