#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import main

class View(tk.Frame):
        """View class. Diary UI object."""
        def __init__(self, viewController):
                """__init__ function on View class.
                Constructs the UI."""
                self.frame = tk.Frame()
                self.frame.grid(row=0, column=0)
                self.vc = viewController

                menubar =tk.Menu(self.vc.parent)
                # file menu
                filemenu =tk.Menu(menubar, tearoff=0)
                filemenu.add_command(label="Tulosta viikko", command=self.vc.printWeek)
                filemenu.add_command(label="Sulje", command=self.vc.parent.quit)
                menubar.add_cascade(label="Tiedosto", menu=filemenu)

                # help menu
                helpmenu =tk.Menu(menubar, tearoff=0)
                helpmenu.add_command(label="Tietoja", command=self.about)
                menubar.add_cascade(label="Ohje", menu=helpmenu)

                # display the menu
                self.vc.parent.config(menu=menubar)

                #formatting window
                self.lbl_margin1 = tk.Label(self.frame, width=5, height=1) 
                self.lbl_margin2 = tk.Label(self.frame, width=12, height=1)
                self.lbl_padding = tk.Label(self.frame, width=12, height=1)
                self.lbl_padding2 = tk.Label(self.frame, width=12, height=1)
                self.lbl_padding3 = tk.Label(self.frame, width=12, height=1)
                self.lbl_padding4 = tk.Label(self.frame, width=12, height=1)
                self.lbl_padding5 = tk.Label(self.frame, width=12, height=1) 
                self.lbl_padding6 = tk.Label(self.frame, width=12, height=1)
                self.lbl_padding7 = tk.Label(self.frame, width=12, height=1) 
                self.lbl_padding8 = tk.Label(self.frame, width=12, height=1) 
                
                #creating components
                self.labelDay = tk.StringVar()
                self.labelMonthDay = tk.StringVar()
                self.labelMonth = tk.StringVar()
                self.labelYear = tk.StringVar()
                self.labelWeek = tk.StringVar()

                self.txt_night = tk.StringVar()
                self.txt_breakfast = tk.StringVar()
                self.txt_morning = tk.StringVar()
                self.txt_lunch = tk.StringVar()
                self.txt_afternoon = tk.StringVar()
                self.txt_dinner = tk.StringVar()
                self.txt_evening = tk.StringVar()

                self.lbl_weekday=tk.Label(self.frame,textvariable=self.labelDay, width=20, height=3)
                self.lbl_monthday  =tk.Label(self.frame,textvariable=self.labelMonthDay, width=3, height=3)
                self.lbl_month  =tk.Label(self.frame, textvariable=self.labelMonth, width=3, height=3)
                self.lbl_year  =tk.Label(self.frame, textvariable=self.labelYear, width=10, height=3)
                self.lbl_week  =tk.Label(self.frame, textvariable=self.labelWeek,width=20, height=3)
                self.lbl_sleep  =tk.Label(self.frame,text='Nukkumaan:',width=12, height=1)
                self.lbl_wakeup  =tk.Label(self.frame,text='Herätys:',width=12, height=1)
                self.lbl_night  =tk.Label(self.frame,text='Yö')
                self.lbl_breakfast  =tk.Label(self.frame,text='Aamupala')
                self.lbl_morning  =tk.Label(self.frame,text='Aamu')
                self.lbl_lunch  =tk.Label(self.frame,text='Lounas')
                self.lbl_afternoon  =tk.Label(self.frame,text='Iltapäivä')
                self.lbl_dinner  =tk.Label(self.frame,text='Päivällinen')
                self.lbl_evening  =tk.Label(self.frame,text='Ilta')
                
                self.box_sleephour = ttk.Combobox(self.frame, width=5)
                self.box_sleephour['values'] = ('t', '18', '19', '20', '21', '22', '23', '24', '1', '2','3', '4', '5', '6')
                self.box_sleephour.current(0)
                self.box_sleepminute = ttk.Combobox(self.frame, width=5)
                self.box_sleepminute['values'] = ('min', '0', '15', '30', '45')
                self.box_sleepminute.current(0)
                self.box_wakeuphour = ttk.Combobox(self.frame, width=5)
                self.box_wakeuphour['values'] = ('t', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15')
                self.box_wakeuphour.current(0)
                self.box_wakeupminute = ttk.Combobox(self.frame, width=5)
                self.box_wakeupminute['values'] = ('min', '0', '15', '30', '45')
                self.box_wakeupminute.current(0)

                self.btn_first_day  =tk.Button(self.frame, text="|<", command=self.vc.firstDay)
                self.btn_previous_day  =tk.Button(self.frame, text="<", command=self.vc.previousDay)
                self.btn_next_day  =tk.Button(self.frame, text=">", command=self.vc.nextDay)
                self.btn_last_day  =tk.Button(self.frame, text=">|", command=self.vc.lastDay)
                self.btn_today = tk.Button(self.frame, text="||", width=5, command=self.vc.today)
                self.btn_first_week  =tk.Button(self.frame, text="|<", command=self.vc.firstWeek)
                self.btn_previous_week  =tk.Button(self.frame, text="<", command=self.vc.previousWeek)
                self.btn_next_week  =tk.Button(self.frame, text=">", command=self.vc.nextWeek)
                self.btn_last_week  =tk.Button(self.frame, text=">|", command=self.vc.lastWeek)
                self.btn_save  =tk.Button(self.frame, text="Tallenna", height=2, command=self.vc.save)  

                self.txt_night  =tk.Text(self.frame, width=65, height=3)
                self.txt_breakfast  =tk.Text(self.frame, width=65, height=4)
                self.txt_morning  =tk.Text(self.frame, width=65, height=5)
                self.txt_lunch  =tk.Text(self.frame, width=65, height=4)
                self.txt_afternoon  =tk.Text(self.frame, width=65, height=8)
                self.txt_dinner  =tk.Text(self.frame, width=65, height=5)
                self.txt_evening  =tk.Text(self.frame, width=65, height=11)
                
                # rendering on the window
                self.lbl_margin1.grid(row=0, column=0)
                self.lbl_margin2.grid(row=0, column=1) 
                self.lbl_weekday.grid(row=1, column=2, columnspan=4, sticky=tk.E)
                self.lbl_monthday.grid(row=1, column=6)
                self.lbl_month.grid(row=1, column=7)
                self.lbl_year.grid(row=1, column=8, columnspan=2)
                self.lbl_week.grid(row=1, column=10, columnspan=4)
                self.lbl_padding.grid(row=3, column=1)
                self.lbl_sleep.grid(row=4, column=1) 
                self.lbl_wakeup.grid(row=5, column=1)
                self.lbl_padding2.grid(row=6, column=1)
                self.lbl_night.grid(row=7, column=1, sticky=tk.E)
                self.lbl_padding3.grid(row=8, column=1) 
                self.lbl_breakfast.grid(row=9, column=1 , sticky=tk.E)
                self.lbl_padding4.grid(row=10, column=1)
                self.lbl_morning.grid(row=11, column=1 , sticky=tk.E)
                self.lbl_padding5.grid(row=12, column=1)
                self.lbl_lunch.grid(row=13, column=1 , sticky=tk.E)
                self.lbl_padding6.grid(row=14, column=1)
                self.lbl_afternoon.grid(row=15, column=1 , sticky=tk.E)
                self.lbl_padding7.grid(row=16, column=1)
                self.lbl_dinner.grid(row=17, column=1 , sticky=tk.E)
                self.lbl_padding8.grid(row=18, column=1)
                self.lbl_evening.grid(row=19, column=1 , sticky=tk.E)
                
                self.btn_first_day.grid(row=2, column=2, sticky=tk.W)
                self.btn_previous_day.grid(row=2, column=3, sticky=tk.W)
                self.btn_next_day.grid(row=2, column=4, sticky=tk.W)
                self.btn_last_day.grid(row=2, column=5, sticky=tk.W)
                self.btn_today.grid(row=2, column=7,columnspan=2, sticky=tk.E)
                self.btn_first_week.grid(row=2, column=10, sticky=tk.W)
                self.btn_previous_week.grid(row=2, column=11, sticky=tk.W)
                self.btn_next_week.grid(row=2, column=12, sticky=tk.W)
                self.btn_last_week.grid(row=2, column=13, sticky=tk.W)
                self.btn_save.grid(row=4, column=10, columnspan=3, rowspan=2)

                self.box_sleephour.grid(row=4, column=2, columnspan=2, sticky=tk.E)
                self.box_sleepminute.grid(row=4, column=4, columnspan=2, sticky=tk.W)
                self.box_wakeuphour.grid(row=5, column=2, columnspan=2, sticky=tk.E)
                self.box_wakeupminute.grid(row=5, column=4, columnspan=2, sticky=tk.W)

                self.txt_night.grid(row=7, column=2, columnspan=12, sticky=tk.W)
                self.txt_breakfast.grid(row=9, column=2, columnspan=12, sticky=tk.W)
                self.txt_morning.grid(row=11, column=2, columnspan=12, sticky=tk.W)
                self.txt_lunch.grid(row=13, column=2, columnspan=12, sticky=tk.W)
                self.txt_afternoon.grid(row=15, column=2, columnspan=12, sticky=tk.W)
                self.txt_dinner.grid(row=17, column=2, columnspan=12, sticky=tk.W)
                self.txt_evening.grid(row=19, column=2, columnspan=12, sticky=tk.W)

        def currentDay(self):
                """currentDay function on View class.
                shows the day in process."""
                self.txt_night.delete("1.0", tk.END) 
                self.txt_breakfast.delete("1.0", tk.END)
                self.txt_morning.delete("1.0", tk.END)
                self.txt_lunch.delete("1.0", tk.END)
                self.txt_afternoon.delete("1.0", tk.END)
                self.txt_dinner.delete("1.0", tk.END)
                self.txt_evening.delete("1.0", tk.END)
                self.set_box_sleephour()
                self.set_box_sleepminute()
                self.set_box_wakeuphour()
                self.set_box_wakeupminute()       
                self.set_txt_night()
                self.set_txt_breakfast()
                self.set_txt_morning()
                self.set_txt_lunch()
                self.set_txt_afternoon()
                self.set_txt_dinner()
                self.set_txt_evening()
                
                index = self.vc.index
                currentWeekDay = self.vc.model.days[index].weekday 
                if currentWeekDay == 1:
                        self.labelDay.set("Maanantai")
                elif currentWeekDay == 2:
                        self.labelDay.set("Tiistai")
                elif currentWeekDay == 3:
                        self.labelDay.set("Keskiviikko")
                elif currentWeekDay == 4:
                        self.labelDay.set("Torstai")
                elif currentWeekDay == 5:
                        self.labelDay.set("Perjantai")
                elif currentWeekDay == 6:
                        self.labelDay.set("Lauantai")
                elif currentWeekDay == 7:
                        self.labelDay.set("Sunnuntai")
                else:
                        messagebox.showerror("Virhe", "Virheellinen viikonpäivänumero")

                self.labelMonthDay.set(str(self.vc.model.days[index].day) + ".")
                self.labelMonth.set(str(self.vc.model.days[index].month) + ".") 
                self.labelYear.set(self.vc.model.days[index].year) 
                self.labelWeek.set("vko " + str(self.vc.model.days[index].week))

        def about(self):
                """about function on View class."""
                messagebox.showinfo("Päiväkirja 0.1", "Päiväkirjan ylläpitosovellus v.0.1")

        def get_box_sleephour(self):
                """get_box_sleephour function on View class"""
                return self.box_sleephour.get()

        def set_box_sleephour(self):
                """set_box_sleephour function on View class."""
                sleephours = self.vc.model.days[self.vc.index].getSleepingTimeHours()
                if sleephours is not None:
                        self.box_sleephour.set(sleephours)
                else:
                        self.box_sleephour.set("t")
    
        def get_box_sleepminute(self):
                """get_box_sleepminute function on View class"""
                return self.box_sleepminute.get()

        def set_box_sleepminute(self):
                """set_box_sleepminute function on View class."""
                sleepminutes = self.vc.model.days[self.vc.index].getSleepingTimeMinutes()
                if sleepminutes is not None:
                        self.box_sleepminute.set(sleepminutes)
                else:
                        self.box_sleepminute.set("min")

        def get_box_wakeuphour(self):
                """get_box_wakeuphour function on View class"""
                return self.box_wakeuphour.get()

        def set_box_wakeuphour(self):
                """set_box_wakeuphour function on View class."""
                wakeuphours = self.vc.model.days[self.vc.index].getWakeupTimeHours()
                if wakeuphours is not None:
                        self.box_wakeuphour.set(wakeuphours)
                else:
                        self.box_wakeuphour.set("t")
    
        def get_box_wakeupminute(self):
                """get_box_wakeupminute function on View class"""
                return self.box_wakeupminute.get()

        def set_box_wakeupminute(self):
                """set_box_wakeupminute function on View class."""
                wakeupminutes = self.vc.model.days[self.vc.index].getWakeupTimeMinutes()
                if wakeupminutes is not None:
                        self.box_wakeupminute.set(wakeupminutes)
                else:
                        self.box_wakeupminute.set("min")

        def get_txt_night(self):
                """get_txt_night function on View class.
                Tailing newlines are stripped."""
                if self.txt_night.compare("end-1c", "==", "1.0"):
                        return ""
                else:
                        return self.txt_night.get("1.0", tk.END).rstrip()
                        #return self.txt_night.get().rstrip()

        def set_txt_night(self):
                """set_txt_night function on View class."""
                night = self.vc.model.days[self.vc.index].getNigth()
                self.txt_night.insert(tk.END, night)

        def get_txt_breakfast(self):
                """get_txt_breakfast function on View class.
                Tailing newlines are stripped."""
                if self.txt_breakfast.compare("end-1c", "==", "1.0"):
                        return ""
                else:
                        return self.txt_breakfast.get("1.0", tk.END).rstrip()
                        #return self.txt_breakfast.get().rstrip()

        def set_txt_breakfast(self):
                """set_txt_breakfast function on View class."""
                breakfast = self.vc.model.days[self.vc.index].getBreakfast()
                self.txt_breakfast.insert(tk.END, breakfast)

        def get_txt_morning(self):
                """get_txt_morning function on View class.
                Tailing newlines are stripped."""
                if self.txt_morning.compare("end-1c", "==", "1.0"):
                        return ""
                else:
                        return self.txt_morning.get("1.0", tk.END).rstrip()
                        #return self.txt_morning.get().rstrip()

        def set_txt_morning(self):
                """set_txt_morning function on View class."""
                morning = self.vc.model.days[self.vc.index].getMorning()
                self.txt_morning.insert(tk.END, morning)

        def get_txt_lunch(self):
                """get_txt_lunch function on View class.
                Tailing newlines are stripped."""
                if self.txt_lunch.compare("end-1c", "==", "1.0"):
                        return ""
                else:
                        return self.txt_lunch.get("1.0", tk.END).rstrip()
                        #return self.txt_lunch.get().rstrip()

        def set_txt_lunch(self):
                """set_txt_lunch function on View class."""
                lunch = self.vc.model.days[self.vc.index].getLunch()
                self.txt_lunch.insert(tk.END, lunch)

        def get_txt_afternoon(self):
                """get_txt_afternoon function on View class.
                Tailing newlines are stripped."""
                if self.txt_afternoon.compare("end-1c", "==", "1.0"):
                        return ""
                else:
                        return self.txt_afternoon.get("1.0", tk.END).rstrip()
                        #return self.txt_afternoon.get().rstrip()

        def set_txt_afternoon(self):
                """set_txt_afternoon function on View class."""
                afternoon = self.vc.model.days[self.vc.index].getAfternoon()
                self.txt_afternoon.insert(tk.END, afternoon)

        def get_txt_dinner(self):
                """get_txt_dinner function on View class.
                Tailing newlines are stripped."""
                if self.txt_dinner.compare("end-1c", "==", "1.0"):
                        return ""
                else:
                        return self.txt_dinner.get("1.0", tk.END).rstrip()
                        #return self.txt_dinner.get().rstrip()

        def set_txt_dinner(self):
                """set_txt_dinner function on View class."""
                dinner = self.vc.model.days[self.vc.index].getDinner()
                self.txt_dinner.insert(tk.END, dinner)

        def get_txt_evening(self):
                """get_txt_evening function on View class.
                Tailing newlines are stripped."""
                if self.txt_evening.compare("end-1c", "==", "1.0"):
                        return ""
                else:
                        return self.txt_evening.get("1.0", tk.END).rstrip()
                        #return self.txt_evening.get().rstrip()

        def set_txt_evening(self):
                """set_txt_evening function on View class."""
                evening = self.vc.model.days[self.vc.index].getEvening()
                self.txt_evening.insert(tk.END, evening)
