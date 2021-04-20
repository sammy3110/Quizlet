from tkinter import *
from tkinter import messagebox
from ReadQuestions import Questions
import tkinter as tk

class Quiz_Gui:

    def __init__(self):
        self.window = Tk(className = " Quizlet - By Shyam")
        self.currentQuestion = 0
        self.answers = {}
        self.window.resizable(False, False)
        self.window.geometry("800x500")
        photo = PhotoImage(file = "Images/icon.png")
        self.window.iconphoto(False, photo)
        self.createWelcomeWindow()
        self.getQuestions()
        self.window.mainloop()
    
    def createWelcomeWindow(self):

        self.welcomeFrame = Frame(self.window)
        self.welcomeFrame.pack()
        self.lbl_Welcome = Label(self.welcomeFrame, font=("Avenir Next LT Pro", 20), pady=50, text="WELCOME TO QUIZLET")
        self.lbl_Welcome.pack()
        self.btn_Start = Button(self.welcomeFrame, text="START", font=("Avenir Next LT Pro", 20), bg="White", command=self.createMainWindow)
        self.btn_Start.pack()
    
    def createMainWindow(self):
        self.welcomeFrame.destroy()
        self.createQuestionFrame()
        self.createQuestionPanelFrame()
    
    def getQuestions(self):
        i = Questions()
        self.questions = i.fetchQuestions()
        self.originalAnswers = {}
        for each in self.questions.keys():
            self.originalAnswers[each] = (int(self.questions[each][5]))
        print(self.originalAnswers)

    def changeColor(self, value):
        l = [1,2,3,4]
        self.d = {1: self.option1, 2: self.option2, 3:self.option3, 4:self.option4}
        if value > 0:
            self.d[value]['fg'] = "Green"
            l.remove(value)
        for each in l:
            self.d[each]['fg'] = "Black"

    def displayQuestion(self, event):
        self.questionFrame.grid(row=0, column=1)
        no = self.lb_Questions.get(ANCHOR)
        self.currentQuestion = int(no[9:])
        question_no = self.questions[int(no[9:])]
        self.disQ(question_no)
        for each in self.d:
            self.d[each].pack()
        self.btn_submit.pack()

    def disQ(self, question_no):
        self.lbl_questionBox['text'] = question_no[0]
        self.option1['text'] = question_no[1]
        self.option2['text'] = question_no[2]
        self.option3['text'] = question_no[3]
        self.option4['text'] = question_no[4]

        try:
            a = self.answers[self.currentQuestion]
            self.var.set(a)
            self.changeColor(a)
        except:
            self.var.set(0)
            self.changeColor(0)
    
    def setAnswer(self, value):
        self.answers[self.currentQuestion] = value
        print(self.answers)
        self.changeColor(value)

    def printScore(self, var):
        score = 0
        a = [b for b in range(1,11)]
        if var == "n":
            for each in a:
                if self.answers[each] == self.originalAnswers[each]:
                    score += 1
        else:
            for each in self.answers.keys():
                if self.answers[each] == self.originalAnswers[each]:
                    score += 1

        self.frm_QuestionPanelFrame.destroy()
        self.questionFrame.destroy()
        lbl_Score = Label(self.window, text="Your Score is {} out of 10".format(score), font=("Avenir Next LT Pro", 20), pady=50)
        lbl_Score.pack()

        btn_exit = Button(self.window, text="EXIT", font=("Avenir Next LT Pro", 20), command=self.exit, highlightthickness = 2, bd=1, bg="White")
        btn_exit.pack()

    def exit(self):
        self.window.destroy()

    def submitAnswers(self):
        l = len(self.answers)
        if l < 10:
            msg = "You have answered {} questions out of 10. Are you sure you want to submit?".format(l)
            submit = messagebox.askquestion(title="SUBMIT INFO", message=msg)
            if submit == 'yes':
                self.printScore("y")
        else:
            self.printScore("n")

    def createQuestionFrame(self):

        self.questionFrame = tk.Frame(self.window, padx=80)
        self.questionFrame.grid(row=0, column=1)

        # frm_QNumber = Frame(self.questionFrame)
        # frm_QNumber.pack()
        # self.lbl_questionNumber = Label(frm_QNumber, font=("Avenir Next LT Pro", 19), text="", bd=5)
        # # self.lbl_questionNumber.pack()

        frm_Q = Frame(self.questionFrame)
        frm_Q.pack()
        self.lbl_questionBox = Label(frm_Q, font=("Avenir Next LT Pro", 20), pady=10, text="Click any question to start.")
        self.lbl_questionBox.pack()

        self.var = IntVar()
        frm_op1 = Frame(self.questionFrame)
        frm_op1.pack()
        self.option1 = Radiobutton(frm_op1, text="", anchor="w", variable = self.var, value=1, font=("Avenir Next LT Pro", 15), command = lambda: self.setAnswer(self.var.get()))


        frm_op2 = Frame(self.questionFrame)
        frm_op2.pack()
        self.option2 = Radiobutton(frm_op2, text="", anchor="w", variable = self.var, value=2, font=("Avenir Next LT Pro", 15), command = lambda: self.setAnswer(self.var.get()))


        frm_op3 = Frame(self.questionFrame)
        frm_op3.pack()
        self.option3 = Radiobutton(frm_op3, text="", anchor="w", variable = self.var, value=3, font=("Avenir Next LT Pro", 15), pady=15, command = lambda: self.setAnswer(self.var.get()))

        frm_op4 = Frame(self.questionFrame)
        frm_op4.pack()
        self.option4 = Radiobutton(frm_op4, text="", anchor="w", variable = self.var, value=4, font=("Avenir Next LT Pro", 15), pady=15, command = lambda: self.setAnswer(self.var.get()))

        self.btn_submit = Button(self.questionFrame, text="SUBMIT", highlightthickness = 2, bd=1, font=("Avenir Next LT Pro", 15), bg="White", command=self.submitAnswers)
        # self.btn_submit.pack()
        # self.btn_nxt = Button(questionFrame, text="NEXT", highlightthickness = 2, bd=1, font=("Avenir Next LT Pro", 15), bg="White", command=self.nextQue)
        # self.btn_nxt.grid(row=4, column=1)

    def createQuestionPanelFrame(self):

        self.frm_QuestionPanelFrame = Frame(self.window, padx=5)
        self.frm_QuestionPanelFrame.grid(row=0, column=0)

        self.lb_Questions = Listbox(self.frm_QuestionPanelFrame,  font=("Avenir Next LT Pro", 15), height=21, width=15)
        for i in range(1,11):
            self.lb_Questions.insert(i, "Question {}".format(i))
        self.lb_Questions.bind('<<ListboxSelect>>', self.displayQuestion)
        self.lb_Questions.selection_set( first = 0 )
        self.lb_Questions.pack()

Quiz_Gui()