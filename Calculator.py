import tkinter
from tkinter import *
from tkinter import messagebox

grade1 = []
grade1point = []
credit1 = []
grade2 = []
grade2point = []
credit2 = []


class Main(object):
    _images = []

    def __init__(self, root):
        self._frame_p = tkinter.Frame(root, background="#222831", )
        self._images.append(tkinter.PhotoImage('CGPALOGO.png', file='CGPALOGO.png'))
        self._label_1 = tkinter.Label(image="CGPALOGO.png", )
        self._label_1.grid(in_=self._frame_p, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                           rowspan=2,
                           sticky="nsew")
        self._frame_1 = tkinter.Frame(root, background="#393E46", )
        self._frame_2 = tkinter.Frame(root, background="#393E46", )
        self._frame_3 = tkinter.Frame(root, background="#393E46", )
        self._frame_4 = tkinter.Frame(root, background="#393E46", )
        self._frame_5 = tkinter.Frame(root, background="#393E46", )
        self._frame_6 = tkinter.Frame(root, background="#393E46", )
        self._frame_7 = tkinter.Frame(root, background="#393E46", )
        self._frame_8 = tkinter.Frame(root, background="#393E46", )
        self._frame_9 = tkinter.Frame(root, background="#393E46", )
        self._frame_10 = tkinter.Frame(root, background="#393E46", )
        self._frame_11 = tkinter.Frame(root, background="#393E46", )
        self._frame_12 = tkinter.Frame(root, background="#393E46", )
        self._frame_13 = tkinter.Frame(root, background="#393E46", )
        self._frame_14 = tkinter.Frame(root, background="#393E46", )
        self._frame_15 = tkinter.Frame(root, background="#393E46", )
        self._frame_16 = tkinter.Frame(root, background="#393E46", )
        self._frame_17 = tkinter.Frame(root, background="#393E46", )
        self._frame_18 = tkinter.Frame(root, background="#393E46", )
        self._frame_19 = tkinter.Frame(root, background="#393E46", )
        self._frame_20 = tkinter.Frame(root, background="#393E46", )
        self._frame_21 = tkinter.Frame(root, background="#393E46", )
        self._frame_24 = tkinter.Frame(root, background="#393E46", )
        self._frame_22 = tkinter.Frame(root, background="#393E46", )
        self._frame_23 = tkinter.Frame(root, background="#393E46", )
        self._frame_25 = tkinter.Frame(root, background="#393E46", )
        self._frame_26 = tkinter.Frame(root, background="#393E46", )
        self._frame_27 = tkinter.Frame(root, background="#393E46", )
        self._frame_28 = tkinter.Frame(root, background="#393E46", )
        self._frame_29 = tkinter.Frame(root, background="#393E46", )
        self._frame_30 = tkinter.Frame(root, background="#393E46", )
        self._frame_32 = tkinter.Frame(root, background="#393E46", )
        self._frame_33 = tkinter.Frame(root, background="#393E46", )
        self._frame_34 = tkinter.Frame(root, background="#393E46", )
        self._frame_35 = tkinter.Frame(root, background="#393E46", )
        self._frame_42 = tkinter.Frame(root, background="#393E46", )
        self._frame_43 = tkinter.Frame(root, background="#393E46", )
        self._frame_44 = tkinter.Frame(root, background="#393E46", )
        self._frame_45 = tkinter.Frame(root, background="#393E46", )
        self._frame_46 = tkinter.Frame(root, background="#393E46", )
        self._label_12 = tkinter.Label(self._frame_1, activebackground="#393E46", activeforeground="#1A374D",
                                       background="#393E46", font="{Times New Roman} 14 bold", foreground="#FFFFFF",
                                       text=" First Semester :", padx=8, pady=8)
        self._label_13 = tkinter.Label(root, activebackground="#E14D2A", background="#E14D2A",
                                       font="{Times New Roman} 12 bold", text="Course Title", foreground="#FFFFFF")
        self._label_14 = tkinter.Label(root, activebackground="#E14D2A", background="#E14D2A",
                                       font="{Times New Roman} 12 bold", text="Course Code", foreground="#FFFFFF")
        self._label_16 = tkinter.Label(root, activebackground="#E14D2A", background="#E14D2A", foreground="#FFFFFF",
                                       font="{Times New Roman} 12 bold", text="Credit", )
        self._label_20 = tkinter.Label(root, activebackground="#E14D2A", background="#E14D2A", foreground="#FFFFFF",
                                       font="{Times New Roman} 12 bold", text="Grade Obtained", )
        self.firstsub1 = tkinter.Entry(self._frame_2, justify="center", width=35, )
        self.firstcourse1 = tkinter.Entry(self._frame_3, justify="center", width=10, )
        self.firstcredit1 = tkinter.Entry(self._frame_4, justify="center", width=0, )
        self.firstgrade1 = tkinter.Entry(self._frame_5, justify="center", width=0, )
        self.firstsub2 = tkinter.Entry(self._frame_6, justify="center", width=35, )
        self.firstcourse2 = tkinter.Entry(self._frame_7, justify="center", width=10, )
        self.firstcredit2 = tkinter.Entry(self._frame_8, justify="center", width=0, )
        self.firstgrade2 = tkinter.Entry(self._frame_9, justify="center", width=0, )
        self.firstsub3 = tkinter.Entry(self._frame_10, justify="center", width=35, )
        self.firstcourse3 = tkinter.Entry(self._frame_11, justify="center", width=10, )
        self.firstcredit3 = tkinter.Entry(self._frame_12, justify="center", width=0, )
        self.firstgrade3 = tkinter.Entry(self._frame_13, justify="center", width=0, )
        self.firstsub4 = tkinter.Entry(self._frame_14, justify="center", width=35, )
        self.firstcourse4 = tkinter.Entry(self._frame_15, justify="center", width=10, )
        self.firstcredit4 = tkinter.Entry(self._frame_16, justify="center", width=0, )
        self.firstgrade4 = tkinter.Entry(self._frame_17, justify="center", width=0, )
        self.clear_all = tkinter.Button(root, activebackground="#9cc67a", background="#00ADB5", borderwidth=4,
                                        cursor="hand2", font="{Courier New} 11 bold", foreground="#FFFFFF",
                                        text="CLEAR ALL", )

        self.gradeInfo = tkinter.Button(root, activebackground="#9cc67a", background="#00ADB5", borderwidth=4,
                                        cursor="hand2", font="{Courier New} 11 bold", foreground="#FFFFFF",
                                        text="Grade Info", )
        self.firsttgpa = tkinter.Button(root, activebackground="#9cc67a", background="#00ADB5", borderwidth=5,
                                        cursor="hand2", font="{Courier New} 10 bold", foreground="#FFFFFF",
                                        text="Calculate TGPA", )
        self.firsttgpavalue = tkinter.Label(root, activebackground="#393E46", activeforeground="#1A374D",
                                            foreground="#FFFFFF",
                                            background="#393E46", font="{Times New Roman} 17 bold",
                                            text=0.00, )
        self._label_39 = tkinter.Label(self._frame_20, activebackground="#393E46", activeforeground="#1A374D",
                                       background="#393E46", foreground="#FFFFFF", font="{Times New Roman} 14 bold",
                                       text=" Second Semester :", )
        self._label_11 = tkinter.Label(self._frame_24, activebackground="#E14D2A", background="#E14D2A",
                                       foreground="#FFFFFF",
                                       font="{Times New Roman} 12 bold", text="Course Title", )
        self._label_15 = tkinter.Label(self._frame_24, activebackground="#E14D2A", background="#E14D2A",
                                       foreground="#FFFFFF",
                                       font="{Times New Roman} 12 bold", text="Course Code", )
        self._label_17 = tkinter.Label(self._frame_24, activebackground="#E14D2A", background="#E14D2A",
                                       foreground="#FFFFFF",
                                       font="{Times New Roman} 12 bold", text="Credit", )
        self._label_18 = tkinter.Label(self._frame_24, activebackground="#E14D2A", background="#E14D2A",
                                       foreground="#FFFFFF",
                                       font="{Times New Roman} 12 bold", text="Grade Obtained", )
        self.secondtgpa = tkinter.Button(root, activebackground="#9cc67a", background="#00ADB5", borderwidth=5,
                                         cursor="hand2", font="{Courier New} 10 bold", foreground="#FFFFFF",
                                         text="Calculate TGPA", )
        self.secondtgpavalue = tkinter.Label(root, activebackground="#393E46", activeforeground="#1A374D",
                                             background="#393E46", font="{Times New Roman} 17 bold",
                                             foreground="#FFFFFF",
                                             text=0.00, )
        self.secondsub1 = tkinter.Entry(self._frame_22, justify="center", width=35, )
        self.secondcourse1 = tkinter.Entry(self._frame_23, justify="center", width=10, )
        self.secondcredit1 = tkinter.Entry(self._frame_25, justify="center", width=0, )
        self.secondgrade1 = tkinter.Entry(self._frame_26, justify="center", width=0, )
        self.secondsub2 = tkinter.Entry(self._frame_27, justify="center", width=35, )
        self.secondcourse2 = tkinter.Entry(self._frame_28, justify="center", width=10, )
        self.secondcredit2 = tkinter.Entry(self._frame_29, justify="center", width=0, )
        self.secondgrade2 = tkinter.Entry(self._frame_30, justify="center", width=0)
        self.secondsub3 = tkinter.Entry(self._frame_34, justify="center", width=35, )
        self.secondcourse3 = tkinter.Entry(self._frame_33, justify="center", width=10, )
        self.secondcredit3 = tkinter.Entry(self._frame_32, justify="center", width=0, )
        self.secondgrade3 = tkinter.Entry(self._frame_42, justify="center", width=0, )
        self.secondsub4 = tkinter.Entry(self._frame_43, justify="center", width=35, )
        self.secondcourse4 = tkinter.Entry(self._frame_44, justify="center", width=10, )
        self.secondcredit4 = tkinter.Entry(self._frame_45, justify="center", width=0, )
        self.secondgrade4 = tkinter.Entry(self._frame_46, justify="center", width=0, )
        self.cgpa = tkinter.Button(root, activebackground="#9cc67a", background="#00ADB5", borderwidth=5,
                                   cursor="hand2", font="{Courier New} 15 bold", foreground="#FFFFFF",
                                   text="Calculate CGPA", )
        self._label_7 = tkinter.Label(root, borderwidth=8, activebackground="#E14D2A", background="#E14D2A",
                                      font="{Wide Latin} 12 bold", foreground="#FFFFFF",
                                      text="""Please find your CGPA
and take steps for improvements""", pady=10)
        self._label_32 = tkinter.Label(root, borderwidth=8, activebackground="#222831", background="#222831",
                                       font="{Wide Latin} 17", foreground="#FFFFFF",
                                       text="""Your CGPA is :""", )
        self.cgpavalue = tkinter.Label(root, activebackground="#222831", activeforeground="#1A374D",
                                       background="#222831", font="{Times New Roman} 30 bold", foreground="#FFFFFF",
                                       text=0.00, )

        # widget commands
        self.clear_all.configure(command=self.clear_text_command)
        self.gradeInfo.configure(command=self.give_grade_info)
        self.firsttgpa.configure(command=self.firsttgpa_command)
        self.secondtgpa.configure(command=self.secondtgpa_command)
        self.cgpa.configure(command=self.cgpa_command)

        # geometry
        self._frame_p.grid(column=3, row=0, sticky="news")
        self._frame_1.grid(in_=root, column=1, row=4, columnspan=4, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                           sticky="news")
        self._frame_2.grid(in_=root, column=1, row=6, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                           sticky="news")
        self._frame_3.grid(in_=root, column=2, row=6, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                           sticky="news")
        self._frame_4.grid(in_=root, column=3, row=6, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                           sticky="news")
        self._frame_5.grid(in_=root, column=4, row=6, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                           sticky="news")
        self._frame_6.grid(in_=root, column=1, row=7, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                           sticky="news")
        self._frame_7.grid(in_=root, column=2, row=7, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                           sticky="news")
        self._frame_8.grid(in_=root, column=3, row=7, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                           sticky="news")
        self._frame_9.grid(in_=root, column=4, row=7, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                           sticky="news")
        self._frame_10.grid(in_=root, column=1, row=8, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_11.grid(in_=root, column=2, row=8, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_12.grid(in_=root, column=3, row=8, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_13.grid(in_=root, column=4, row=8, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_14.grid(in_=root, column=1, row=9, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_15.grid(in_=root, column=2, row=9, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_16.grid(in_=root, column=3, row=9, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_17.grid(in_=root, column=4, row=9, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_18.grid(in_=root, column=1, row=10, columnspan=2, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_20.grid(in_=root, column=1, row=11, columnspan=4, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_24.grid(in_=root, column=1, row=12, columnspan=4, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_22.grid(in_=root, column=1, row=13, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_23.grid(in_=root, column=2, row=13, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_25.grid(in_=root, column=3, row=13, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_26.grid(in_=root, column=4, row=13, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_27.grid(in_=root, column=1, row=14, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_28.grid(in_=root, column=2, row=14, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_29.grid(in_=root, column=3, row=14, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_30.grid(in_=root, column=4, row=14, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_32.grid(in_=root, column=3, row=15, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_33.grid(in_=root, column=2, row=15, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_34.grid(in_=root, column=1, row=15, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_35.grid(in_=root, column=1, row=17, columnspan=2, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_42.grid(in_=root, column=4, row=15, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_43.grid(in_=root, column=1, row=16, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_44.grid(in_=root, column=2, row=16, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_45.grid(in_=root, column=3, row=16, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._frame_46.grid(in_=root, column=4, row=16, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="news")
        self._label_7.grid(in_=root, column=5, row=4, columnspan=2, ipadx=0, ipady=0, padx=0, pady=0, rowspan=2,
                           sticky="nsew")
        self._label_11.grid(in_=self._frame_24, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                            rowspan=1, sticky="nsew")
        self._label_15.grid(in_=self._frame_24, column=2, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                            rowspan=1, sticky="nsew")
        self._label_17.grid(in_=self._frame_24, column=3, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                            rowspan=1, sticky="nsew")
        self._label_18.grid(in_=self._frame_24, column=4, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                            rowspan=1, sticky="nsew")
        self._label_12.grid(in_=self._frame_1, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                            rowspan=1, sticky="w")
        self._label_13.grid(in_=root, column=1, row=5, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="nsew")
        self._label_14.grid(in_=root, column=2, row=5, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="nsew")
        self._label_16.grid(in_=root, column=3, row=5, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="nsew")
        self._label_20.grid(in_=root, column=4, row=5, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="nsew")
        self._label_32.grid(in_=root, column=5, row=9, columnspan=2, ipadx=0, ipady=0, padx=0, pady=0, rowspan=3,
                            sticky="nsew")
        self._label_39.grid(in_=self._frame_20, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                            rowspan=1, sticky="w")
        self.firstsub1.grid(in_=self._frame_2, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                            rowspan=1, sticky="ew")
        self.firstcourse1.grid(in_=self._frame_3, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                               rowspan=1, sticky="ew")
        self.firstcredit1.grid(in_=self._frame_4, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                               rowspan=5, sticky="ew", )
        self.firstgrade1.grid(in_=self._frame_5, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                              rowspan=1, sticky="ew")
        self.firstsub2.grid(in_=self._frame_6, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                            rowspan=1, sticky="ew")
        self.firstcourse2.grid(in_=self._frame_7, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                               rowspan=1, sticky="ew")
        self.firstcredit2.grid(in_=self._frame_8, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                               rowspan=1, sticky="ew")
        self.firstgrade2.grid(in_=self._frame_9, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                              rowspan=1, sticky="ew")
        self.firstsub3.grid(in_=self._frame_10, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                            rowspan=1, sticky="ew")
        self.firstcourse3.grid(in_=self._frame_11, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                               rowspan=1, sticky="ew")
        self.firstcredit3.grid(in_=self._frame_12, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                               rowspan=1, sticky="ew")
        self.firstgrade3.grid(in_=self._frame_13, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                              rowspan=1, sticky="ew")
        self.firstsub4.grid(in_=self._frame_14, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                            rowspan=1, sticky="ew")
        self.firstcourse4.grid(in_=self._frame_15, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                               rowspan=1, sticky="ew")
        self.firstcredit4.grid(in_=self._frame_16, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                               rowspan=1, sticky="ew")
        self.firstgrade4.grid(in_=self._frame_17, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                              rowspan=1, sticky="ew")
        self.firsttgpa.grid(in_=root, column=3, row=10, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="nsew")
        self.firsttgpavalue.grid(in_=root, column=4, row=10, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                                 sticky="nsew")
        self.secondtgpa.grid(in_=root, column=3, row=17, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                             sticky="nsew")
        self.secondtgpavalue.grid(in_=root, column=4, row=17, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                                  sticky="nsew")
        self.secondsub1.grid(in_=self._frame_22, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                             rowspan=1, sticky="ew")
        self.secondcourse1.grid(in_=self._frame_23, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                                rowspan=1, sticky="ew")
        self.secondcredit1.grid(in_=self._frame_25, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                                rowspan=1, sticky="ew")
        self.secondgrade1.grid(in_=self._frame_26, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                               rowspan=1, sticky="ew")
        self.secondsub2.grid(in_=self._frame_27, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                             rowspan=1, sticky="ew")
        self.secondcourse2.grid(in_=self._frame_28, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                                rowspan=1, sticky="ew")
        self.secondcredit2.grid(in_=self._frame_29, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                                rowspan=1, sticky="ew")
        self.secondgrade2.grid(in_=self._frame_30, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                               rowspan=1, sticky="ew")
        self.secondsub3.grid(in_=self._frame_34, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                             rowspan=1, sticky="ew")
        self.secondcourse3.grid(in_=self._frame_33, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                                rowspan=1, sticky="ew")
        self.secondcredit3.grid(in_=self._frame_32, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                                rowspan=1, sticky="ew")
        self.secondgrade3.grid(in_=self._frame_42, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                               rowspan=1, sticky="ew")
        self.secondsub4.grid(in_=self._frame_43, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                             rowspan=1, sticky="ew")
        self.secondcourse4.grid(in_=self._frame_44, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                                rowspan=1, sticky="ew")
        self.secondcredit4.grid(in_=self._frame_45, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                                rowspan=1, sticky="ew")
        self.secondgrade4.grid(in_=self._frame_46, column=1, row=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0,
                               rowspan=1, sticky="ew")
        self.clear_all.grid(in_=root, column=5, row=14, columnspan=3, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="nsew")
        self.gradeInfo.grid(in_=root, column=5, row=7, columnspan=3, ipadx=0, ipady=0, padx=0, pady=0, rowspan=1,
                            sticky="nsew")
        self.cgpa.grid(in_=root, column=5, row=16, columnspan=3, ipadx=0, ipady=0, padx=0, pady=0, rowspan=2,
                       sticky="nsew")
        self.cgpavalue.grid(in_=root, column=5, row=12, columnspan=2, ipadx=0, ipady=0, padx=0, pady=0, rowspan=2,
                            sticky="nsew")

        self._frame_10.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_10.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_24.grid_rowconfigure(1, weight=0, minsize=5, pad=0)
        self._frame_24.grid_columnconfigure(1, weight=0, minsize=240, pad=0)
        self._frame_24.grid_columnconfigure(2, weight=0, minsize=181, pad=0)
        self._frame_24.grid_columnconfigure(3, weight=0, minsize=175, pad=0)
        self._frame_24.grid_columnconfigure(4, weight=1, minsize=67, pad=0)
        self._frame_25.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_25.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_26.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_26.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_27.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_27.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_28.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_28.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_29.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_29.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_3.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_3.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_30.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_30.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_32.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_32.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_33.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_33.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_34.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_34.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_4.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_4.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_42.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_42.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_43.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_43.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_44.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_44.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_45.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_45.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_46.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_46.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_5.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_5.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_6.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_6.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_7.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_7.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_8.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_8.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_9.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_9.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_10.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_10.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_11.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_11.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_12.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_12.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_13.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_13.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_14.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_14.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_15.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_15.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_16.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_16.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_17.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_17.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_2.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_2.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_20.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_20.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_22.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_22.grid_columnconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_23.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._frame_23.grid_columnconfigure(1, weight=0, minsize=40, pad=0)


class CustomMain(Main):
    print("CGPA Calculator Opened")

    def clear_text_command(self, ):
        self.firstsub1.delete(0, END)
        self.firstsub2.delete(0, END)
        self.firstsub3.delete(0, END)
        self.firstsub4.delete(0, END)
        self.firstcourse1.delete(0, END)
        self.firstcourse2.delete(0, END)
        self.firstcourse3.delete(0, END)
        self.firstcourse4.delete(0, END)
        self.firstcredit1.delete(0, END)
        self.firstcredit2.delete(0, END)
        self.firstcredit3.delete(0, END)
        self.firstcredit4.delete(0, END)
        self.firstgrade1.delete(0, END)
        self.firstgrade2.delete(0, END)
        self.firstgrade3.delete(0, END)
        self.firstgrade4.delete(0, END)
        self.secondsub1.delete(0, END)
        self.secondsub2.delete(0, END)
        self.secondsub3.delete(0, END)
        self.secondsub4.delete(0, END)
        self.secondcourse1.delete(0, END)
        self.secondcourse2.delete(0, END)
        self.secondcourse3.delete(0, END)
        self.secondcourse4.delete(0, END)
        self.secondgrade1.delete(0, END)
        self.secondgrade2.delete(0, END)
        self.secondgrade3.delete(0, END)
        self.secondgrade4.delete(0, END)
        self.secondcredit1.delete(0, END)
        self.secondcredit2.delete(0, END)
        self.secondcredit3.delete(0, END)
        self.secondcredit4.delete(0, END)
        self.firsttgpavalue.config(text=0.00)
        self.secondtgpavalue.config(text=0.00)
        self.cgpavalue.config(text=0.00)

    def give_grade_info(self):
        self.image = tkinter.Toplevel()
        self.image.title('Grade - credit')
        self.image.minsize(399, 631)
        self.image.maxsize(399, 631)
        self.canvas = tkinter.Canvas(self.image, width=399, height=631)
        self.canvas.grid()
        self.photu = tkinter.PhotoImage(file='GradePoint.png', master=root)
        self.canvas.create_image(0, 0, image=self.photu, anchor=NW)
        self.image.mainloop()
        pass

    def firsttgpa_command(self, ):
        try:
            print("Semester1 TGPA Button Pressed.")
            list = ['O', 'o', 'A+', 'a+', 'A', 'a', 'B+', 'b+', 'B', 'b', 'C+', 'c+', 'c', 'C', 'E', 'e', 'F', 'f', 'g',
                    'G', 'I', 'i']
            num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
            if (self.firstgrade1.get() in list) and (self.firstgrade2.get() in list) and (
                    self.firstgrade3.get() in list) and \
                    (self.firstgrade4.get() in list) and (int(self.firstcredit1.get()) in num) and (
                    int(self.firstcredit2.get()) in num) and \
                    (int(self.firstcredit3.get()) in num) and (int(self.firstcredit4.get()) in num):

                a1, b1, c1, d1 = self.firstcredit1.get(), self.firstcredit2.get(), self.firstcredit3.get(), self.firstcredit4.get()
                credit1.append(int(a1))
                credit1.append(int(b1))
                credit1.append(int(c1))
                credit1.append(int(d1))
                print(credit1)
                e1, f1, g1, h1 = self.firstgrade1.get(), self.firstgrade2.get(), self.firstgrade3.get(), self.firstgrade4.get()
                e1 = e1.upper()
                grade1.append(e1)
                f1 = f1.upper()
                grade1.append(f1)
                g1 = g1.upper()
                grade1.append(g1)
                h1 = h1.upper()
                grade1.append(h1)
                print(grade1)
                y = 0
                while y < 4:
                    if grade1[y] == "O":
                        number = 10
                        grade1point.append(number)
                    elif grade1[y] == "A+":
                        number = 9
                        grade1point.append(number)
                    elif grade1[y] == "A":
                        number = 8
                        grade1point.append(number)
                    elif grade1[y] == "B+":
                        number = 7
                        grade1point.append(number)
                    elif grade1[y] == "B":
                        number = 6
                        grade1point.append(number)
                    elif grade1[y] == "C+":
                        number = 5
                        grade1point.append(number)
                    elif grade1[y] == "C":
                        number = 4
                        grade1point.append(number)
                    elif grade1[y] == "D+":
                        number = 3
                        grade1point.append(number)
                    elif grade1[y] == "D":
                        number = 2
                        grade1point.append(number)
                    elif grade1[y] == "E":
                        number = 0
                        grade1point.append(number)
                    y = y + 1
                print(grade1point)
                i = 0
                self.tgpa1, first_part1, second_part1 = 0.00, 0, 0
                while i < 4:
                    first_part1 += credit1[i] * grade1point[i]
                    second_part1 += credit1[i]
                    i = i + 1
                self.tgpa1 = first_part1 / second_part1
                self.tgpa1 = "{:.2f}".format(self.tgpa1)
                print(self.tgpa1)
                self.firsttgpavalue["text"] = self.tgpa1
            else:
                messagebox.showinfo("Information",
                                    "Please choose credit and grades from following values only.\n\n Grades = [ 'O' , 'o' , 'A+' , 'a+' , 'A' , 'a' , 'B+' , 'b+' , 'B' , 'b' , 'C+' , 'c+' , 'c' , 'C' , 'E' , 'e' , 'F' , 'f' , 'g' ,'G' , 'I' , 'i' ]\n\nCredits = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]")
        except:
            messagebox.showerror("Error", "Something went wrong..!!!\nPlease Try again")
        pass

    def secondtgpa_command(self):
        try:
            print("Semester2 TGPA Button Pressed.")
            list = ['O', 'o', 'A+', 'a+', 'A', 'a', 'B+', 'b+', 'B', 'b', 'C+', 'c+', 'c', 'C', 'E', 'e', 'F', 'f', 'g',
                    'G', 'I', 'i']
            num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
            if (self.firstgrade1.get() in list) and (self.firstgrade2.get() in list) and (
                    self.firstgrade3.get() in list) and \
                    (self.firstgrade4.get() in list) and (int(self.firstcredit1.get()) in num) and (
                    int(self.firstcredit2.get()) in num) and \
                    (int(self.firstcredit3.get()) in num) and (int(self.firstcredit4.get()) in num):
                a2, b2, c2, d2 = self.secondcredit1.get(), self.secondcredit2.get(), self.secondcredit3.get(), self.secondcredit4.get()
                credit2.append(int(a2))
                credit2.append(int(b2))
                credit2.append(int(c2))
                credit2.append(int(d2))
                print(credit2)
                e2, f2, g2, h2 = self.secondgrade1.get(), self.secondgrade2.get(), self.secondgrade3.get(), self.secondgrade4.get()
                e2 = e2.upper()
                grade2.append(e2)
                f2 = f2.upper()
                grade2.append(f2)
                g2 = g2.upper()
                grade2.append(g2)
                h2 = h2.upper()
                grade2.append(h2)
                print(grade2)
                z = 0
                while z < 4:
                    if grade2[z] == "O":
                        number = 10
                        grade2point.append(number)
                    elif grade2[z] == "A+":
                        number = 9
                        grade2point.append(number)
                    elif grade2[z] == "A":
                        number = 8
                        grade2point.append(number)
                    elif grade2[z] == "B+":
                        number = 7
                        grade2point.append(number)
                    elif grade2[z] == "B":
                        number = 6
                        grade2point.append(number)
                    elif grade2[z] == "C+":
                        number = 5
                        grade2point.append(number)
                    elif grade2[z] == "C":
                        number = 4
                        grade2point.append(number)
                    elif grade2[z] == "D+":
                        number = 3
                        grade2point.append(number)
                    elif grade2[z] == "D":
                        number = 2
                        grade2point.append(number)
                    elif grade2[z] == "E":
                        number = 0
                        grade2point.append(number)
                    z = z + 1
                print(grade2point)
                j = 0
                self.tgpa2, first_part2, second_part2 = 0.00, 0, 0
                while j < 4:
                    first_part2 += credit2[j] * grade2point[j]
                    second_part2 += credit2[j]
                    j = j + 1
                self.tgpa2 = first_part2 / second_part2
                self.tgpa2 = "{:.2f}".format(self.tgpa2)
                print(self.tgpa2)
                self.secondtgpavalue["text"] = self.tgpa2
                print("tgpa1=", self.tgpa1)
                print("tgpa2=", self.tgpa2)
            else:
                messagebox.showinfo("Information",
                                    "Please choose credit and grades from following values only.\n\n Grades = [ 'O', 'o', 'A+', 'a+', 'A', 'a', 'B+', 'b+', 'B', 'b', 'C+', 'c+', 'c', 'C', 'E', 'e', 'F', 'f, 'g','G', 'I', 'i']\n\nCredits= [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]")
        except:
            messagebox.showerror("Error", "Something went wrong..!!!\nPlease Try again")
        pass

    def cgpa_command(self, ):
        try:
            print("CGPA Button Pressed.")
            if self.firstcredit1.get() == "" and self.firstcredit2.get() == "" and self.firstcredit3.get() == "" and \
                    self.firstcredit4.get() == "" and self.secondcredit1.get() == "" and self.secondcredit2.get() == "" and self.secondcredit3.get() == "" and \
                    self.secondcredit4.get() == "" and self.firstgrade1.get() == "" and self.firstgrade2.get() == "" and self.firstgrade3.get() == "" and \
                    self.firstgrade4.get() == "" and self.secondgrade1.get() == "" and self.secondgrade2.get() == "" and self.secondgrade3.get() == "" and \
                    self.secondgrade4.get() == "":
                messagebox.showwarning("Warning..!!", "Provide all required details\nthen Proceed.")
            else:
                self.cgp = (float(self.firsttgpavalue['text']) + float(self.secondtgpavalue['text'])) / 2
                self.cgp = "{:.2f}".format(self.cgp)
                self.cgpavalue['text'] = str(self.cgp)

        except:
            messagebox.showerror("Error", "Something went wrong..!!!\nPlease Try again")
        pass


if __name__ == '__main__':
    root = Tk()
    demo = CustomMain(root)
    root.title('CGPA Calculator')
    root.maxsize(978, 610)
    root.minsize(976, 609)
    root.wm_iconbitmap('Icon.ico')
    root.configure(bg="#222831")
    root.mainloop()
