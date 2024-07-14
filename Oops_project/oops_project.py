from tkinter import *
from tkinter import ttk

l = ["Librarian", "Admin", "admin@123"]
principal =["Principal","Principal","principal"]
#hod = open(r"C:\Users\srija\OneDrive\Desktop\hod.txt")
student = open("student.txt")
book = open("book.txt")
#faculty = open(r"C:\Users\srija\OneDrive\Desktop\faculty.txt")

s=[]
i=0

class Student:
    def __init__(self,student_name,email,password):
        self.student_name=student_name
        self.email=email
        self.password=password
    def add_Sfile(self):
        file = open('student.txt', 'a')
        s=[self.student_name," ",self.email," ",self.password]
        file.writelines(s)
        file.write("\n") 
        file.close()
class Book:
    def __init__(self,book_name_,author_,branch_):
        self.book_name_=book_name_
        self.author=author_
        self.branch=branch_
    def add_Bfile(self):
        file = open('book.txt', 'a')
        s=[self.book_name_," ",self.author," ",self.branch]
        file.writelines(s)
        file.write("\n")
        file.close()
class Student_Req:
    def __init__(self,student_name,yr_of_admn,book_name,author,branch):
        self.student_name=student_name
        self.yr_of_admn=yr_of_admn
        self.book_name=book_name
        self.author=author
        self.branch=branch
    def add_S_R_file(self):
        file = open('student_request.txt', 'a')
        s=[self.student_name," ",self.yr_of_admn," ",self.book_name," ",self.author," ",self.branch]
        file.writelines(s)
        file.write("\n")
        file.close()
     
        
def checklogin(a, b, c):
    flag = False
    student.seek(0)
    if a == "Student":
        for line in student:
            words = line.split()
            if len(words) == 0:
                print("No students registered.")
            if b == words[0]:
                flag = True
                break
            print(words[0])
        if flag:
            if c == words[2]:
                print("Open student")
                return True
            else:
                print("Wrong password for student.")
        else:
            print("Wrong username for student.")
    elif a == "Faculty":
        for line in faculty:
            words = line.split()
            if len(words) == 0: print("No faculty registered.")
            if b == words[0]:
                flag = True
                break
        if flag:
            if c == words[1]:
                print("Open faculty")
            else:
                print("Wrong password for faculty.")
        else:
            print("Wrong username for faculty.")
    elif a == "Hod":
        for line in student:
            words = line.split()
            if len(words) == 0: print("No hods registered.")
            if b == words[0]:
                flag = True
                break
        if flag:
            if c == words[1]:
                print("Open HOD")
            else:
                print("Wrong password for hod.")
        else:
            print("Wrong username for hod.")
    elif a == "Principal":
        if b == principal[1]:
            if c == principal[2]:
                print("principal open")
                return True
            else:
                print("Wrong Password")
        else:
            print("Wrong username")
    elif a == "Librarian":
        if b == l[1]:
            if c == l[2]:
                return True
            else:
                print("Wrong password")
    else:
        return False



def uup():
    usertype = user_type_.get()
    username = user_name_.get()
    password = user_password_.get()
    print(usertype)
    return [usertype, username, password]


def user(*args):
    print(user_type_.get())
    print(user_name_.get())
    print(user_password_.get())
    list = uup()
    result = checklogin(list[0], list[1], list[2])
    print(result)
    if result == True and list[0]=="Librarian":
        student = Tk()
        student.title("Library management system")
        student.geometry("1188x840")
        student.configure(bg='lightyellow')
        Label(student, text="LIBRARIAN", font=40, bg="pink").pack(side=TOP)
        Button(student, text="ADD BOOK", font=("CASTELLAR", 30), command=add_book, bg="light blue").place(x=100, y=150)
        Button(student, text="BOOK REPORT", font=("CASTELLAR", 30), command=book_report, bg="pink").place(x=100, y=220)
        Button(student, text="BOOK REQUEST", font=("CASTELLAR", 30), command=book_request, bg="light blue").place(x=100,
                                                                                                                  y=290)
        Button(student, text="ADD STUDENT", font=("CASTELLAR", 30), command=add_student, bg="pink").place(x=100, y=370)
        Button(student, text="STUDENT REPORT", font=("CASTELLAR", 30), command=student_report, bg="light blue").place(
            x=100, y=450)
        Button(student, text="ISSUE BOOK", font=("CASTELLAR", 30), command=issue_book, bg="pink").place(x=100, y=540)
         
    if result==True and list[0]=="Student":
        stu = Tk()
        stu.title("Library management system")
        stu.geometry("1188x840")
        stu.configure(bg='lightyellow')
        Label(stu, text="STUDENT", font=40, bg="pink").pack(side=TOP)
        Button(stu, text="MY ACCOUNT", font=("CASTELLAR", 30),command=my_account,bg="light blue").place(x=100, y=150)
        Button(stu, text="CHECK AVAILABILITY", font=("CASTELLAR",30),command=check_availability,bg="pink").place(x=100, y=230)
        Button(stu, text="RETURN BOOK", font=("CASTELLAR", 30),command=return_book,bg="light blue").place(x=100, y=310)
        Button(stu, text="PENALTY PAYMENTS", font=("CASTELLAR", 30),command=penalty_payments,bg="pink").place(x=100, y=390)
        Button(stu, text="REQUEST BOOK", font=("CASTELLAR", 30),command=request_book,bg="light blue").place(x=100, y=470)
        Button(stu, text="BOOKS BORROWED", font=("CASTELLAR", 30),command=student_borrow,bg="pink").place(x=100, y=550)
    
    if list[0]=="Anonymous":
        aut = Tk()
        aut.title("Library management system")
        aut.geometry("1188x840")
        aut.configure(bg='lightgreen')
        Label(aut, text="AUTONOMOUS USER PAGE", font=100, bg="pink").pack(side=TOP, fill="x")
        Button(aut, text="Library Information", command=open_lib_info, bg="lightblue", font=15, width=20, height=5).place(x=150, y=150)
        Button(aut, text="Books Information", command=open_text, bg="lightpink", font=15, width=20, height=5).place(x=150, y=250)
        

        
        
    else:
        print("Wrong credentials")


def open_lib_info():
    libtk=Tk()
    libtk.title("BOOK INFORMATION")
    libtk.geometry("1188x840")
    libtk.configure(bg='lightgreen')
    lib_info = open("lib_info.txt",'r')
    T=Text(libtk,height=50,width=100)
    T.pack()
    for line2 in lib_info:
        lib_line_=line2
        T.insert(END,lib_line_)
    book_info.close()
    print("Printed successfully")
def open_text():
    booktk=Tk()
    booktk.title("BOOK INFORMATION")
    booktk.geometry("1188x840")
    booktk.configure(bg='lightgreen')
    book_info = open("book.txt",'r')
    T=Text(booktk,height=50,width=100)
    T.pack()
    for line3 in book_info:
        book_line_=line3
        T.insert(END,book_line_)
    book_info.close()
    print("Printed successfully")
def student_borrow():
    s_b=Tk()
    s_b.title("ADD BOOK")
    s_b.geometry("1188x840")
    s_b.configure(bg='lightgreen')
    list=uup()
    s_bor=" "
    s_borrow=open("issue_book.txt",'r')
    s_borrow.seek(0)
    T=Text(s_b,height=50,width=100)
    T.pack()
    for line_5 in s_borrow:
        words_5=line_5.split()
        if list[1]==words_5[0]:
            s_bor=line_5
            T.insert(END,s_bor)
    s_borrow.close()
                
    
def add_book():
    a = Tk()
    a.title("ADD BOOK")
    a.geometry("1188x840")
    a.configure(bg='lightgreen')
    Label(a, text="ADD BOOK", font=("CASTELLAR", 60), bg="pink").place(x=350, y=150)
    Label(a, text="BOOK NAME", font=40, bg="pink").place(x=450, y=305)
    Label(a, text="AUTHOR", font=40, bg="lavender").place(x=450, y=350)
    Label(a, text="BRANCH", font=40, bg="pink").place(x=450, y=400)
    book_name = Entry(a)
    author = Entry(a)
    branch=Entry(a)
    book_name.place(x=600, y=305)
    author.place(x=600, y=350)
    branch.place(x=600,y=400)
    def add_book_1():
        book_name_ = book_name.get()
        author_ = author.get()
        branch_=branch.get()
        value = Book(book_name_,author_,branch_)
        s.append(value)
        value.add_Bfile()
    Button(a, text="Submit", command=add_book_1, font=40, bg="light pink").place(x=600, y=500)
    
def my_account():
    a=Tk()
    a.title("MY ACCOUNT")
    a.geometry("1188x840")
    a.configure(bg='lightgreen')
    Label(a, text="MY ACCOUNT", font=("CASTELLAR", 60), bg="pink").place(x=350, y=150)
    Label(a, text="PERSON NAME", font=40, bg="pink").place(x=450, y=305)
    Label(a, text="PERSON MAIL", font=40, bg="lavender").place(x=450, y=350)
    Label(a, text="ACCOUNT TYPE", font=40, bg="light blue").place(x=450, y=400)
    _student_name = Text(a,height=3,width=20)
    _srudent_mail = Text(a,height=3,width=20)
    _student_type=Text(a,height=3,width=20)
    _student_name.place(x=600, y=305)
    _srudent_mail.place(x=600, y=350)
    _student_type.place(x=600, y=400)
    list= uup()
    mail=" "
    myacc=open("student.txt",'r')
    for line4 in myacc:
        words_1=line4.split()
        if list[1]==words_1[0]:
            mail=words_1[2]
    myacc.close()
    _student_name.insert(END,list[1])
    _srudent_mail.insert(END,mail)
    _student_type.insert(END,"Student")
    
def check_availability():
    b=Tk()
    b.title("CHECK AVAILABILITY")
    b.geometry("1188x840")
    book_txt = open("book.txt",'r')
    T=Text(b,height=50,width=100)
    T.pack()
    for line_book in book_txt:
        book_line=line_book
        T.insert(END,book_line)
    print("Printed successfully")
    
def return_book():
    c=Tk()
    c.title("RETURN BOOK")
    c.geometry("1188x840")
    c.configure(bg='lightgreen')
    Label(c, text="RETURN BOOK", font=("CASTELLAR", 60), bg="pink").place(x=350, y=150)
    Label(c, text="STUDENT NAME", font=40, bg="pink").place(x=450, y=250)
    Label(c, text="BOOK BORROWED", font=40, bg="pink").place(x=450, y=300)
    Label(c, text="AUTHOR", font=40, bg="pink").place(x=450, y=350)
    Label(c, text="BRANCH", font=40, bg="lavender").place(x=450, y=400)
    Label(c, text="DATE OF ISSUE", font=40, bg="light blue").place(x=450, y=450)
    Label(c, text="RETURN DATE", font=40, bg="light blue").place(x=450, y=500)
    name_s=Entry(c)
    book_b = Entry(c)
    author_b = Entry(c)
    date_i=Entry(c)
    date_r=Entry(c)
    branch__b=Entry(c)
    name_s.place(x=600,y=250)
    book_b.place(x=600, y=300)
    author_b.place(x=600, y=350)
    branch__b.place(x=600, y=400)
    date_i.place(x=600, y=450)
    date_r.place(x=600, y=500)
    def return_book_():
        book_borrowed = book_b.get()
        name_student=name_s.get()
        author= author_b.get()
        date_of_issue = date_i.get()
        return_date= date_r.get()
        branch_b=branch__b.get()
        list=uup()
        r_b=open("issue_book.txt","r")  
        for r_l in r_b:
            words_6=r_l.split()
            if list[1]==name_student and words_6[2]==book_borrowed:
                return_1=open('return_book.txt','a')
                return_1.write(r_l)
                return_1.close()
        r_b.close()
        with open("issue_book.txt", "r") as i_b:
            l_3 = i_b.readlines()
            with open("issue_book.txt", "w") as i_b:
                for _l_3 in l_3:
                    if _l_3!=r_l:
                        i_b.write(_l_3)
        
        add_book=open("book.txt",'a')
        list_2=[book_borrowed," ",author," ",branch_b]
        add_book.write("\n")
        add_book.writelines(list_2)
        add_book.close()
    Button(c, text="Submit", command=return_book_, font=40, bg="light pink").place(x=600, y=600)
            
    
    
def penalty_payments():     #YET TO DO
    d=Tk()
    d.title("PENALTY PAYMENTS")
    d.geometry("1188x840")
    d.configure(bg='lightgreen')
    Label(d, text="PENALTY PAYMENTS", font=("CASTELLAR", 60), bg="pink").place(x=350, y=150)
    Label(d, text="BOOK BORROWED", font=40, bg="pink").place(x=450, y=305)
    Label(d, text="AUTHOR", font=40, bg="pink").place(x=450, y=350)
    Label(d, text="DATE OF ISSUE", font=40, bg="lavender").place(x=450, y=400)
    Label(d, text="TO BE RETURNED", font=40, bg="light blue").place(x=450, y=450)
    Label(d, text="RETURNED ON", font=40, bg="light blue").place(x=450, y=500)
    Label(d, text="PENALTY", font=40, bg="light blue").place(x=450, y=550)
    e = Entry(d)
    en = Entry(d)
    ent=Entry(d)
    entr=Entry(d)
    an=Entry(d)
    ans=Entry(d)
    e.place(x=600, y=305)
    en.place(x=600, y=350)
    ent.place(x=600, y=400)
    entr.place(x=600, y=450)
    an.place(x=600, y=500)
    ans.place(x=600, y=550)
    book_borrowed = e.get()
    print(book_borrowed)
    author= en.get()
    print(author)
    date_of_issue = ent.get()
    print(date_of_issue)
    to_be_returned=entr.get()
    print( to_be_returned)
    returned_on=an.get()
    print(returned_on)
    penalty=ans.get()
    print(penalty)


def book_report():
    b = Tk()
    b.title("BOOK REPORT")
    b.geometry("1188x840")
    b.configure(bg='lightblue')


def book_request():
    c = Tk()
    c.title("BOOK REQUEST")
    c.geometry("1188x840")
    student_txt = open("student_request.txt",'r')
    T=Text(c,height=50,width=100)
    T.pack()
    for line in student_txt:
        line_=line
        T.insert(END,line_)
    print("Printed successfully")
    

def add_student():
    d = Tk()
    d.title("ADD STUDENT")
    d.geometry("1188x840")
    d.configure(bg='lightyellow')
    Label(d, text="ADD STUDENT", font=("CASTELLAR", 60), bg="pink").place(x=350, y=200)
    Label(d, text="NAME", font=40, bg="pink").place(x=450, y=305)
    Label(d, text="EMAIL", font=40, bg="lavender").place(x=450, y=350)
    Label(d, text="PASSWORD", font=40, bg="pink").place(x=450, y=400)
    student_name_ = Entry(d)
    student_email = Entry(d)
    student_password = Entry(d)
    student_name_.place(x=600, y=305)
    student_email.place(x=600, y=350)
    student_password.place(x=600, y=400)
    def add_student_1():
        student_name = student_name_.get()
        password = student_password.get()
        email = student_email.get()
        value = Student(student_name, email, password)
        s.append(value)
        value.add_Sfile()
    Button(d, text="Submit", command=add_student_1, font=40, bg="light pink").place(x=600, y=600)


def student_report():
    e = Tk()
    e.title("STUDENT REPORT")
    e.geometry("1188x840")


def issue_book():
    st = Tk()
    st.title("Update student info.")
    st.geometry("1188x840")
    st.configure(bg="navyblue")
    Label(st, text="Update Student Information", font=("CASTELLAR",45)).place(x=50, y=150) #title label
    Label(st, text="Enter student name:", font=40).place(x=150, y=300)  #student name
    Label(st, text="Enter year of admission:", font=40).place(x=150, y=350)  #year of admission
    Label(st, text="Enter book name:", font=40).place(x=150, y=400)  #book name
    Label(st, text="Enter author name:", font=40).place(x=150, y=450)
    Label(st, text="Enter branch:", font=40).place(x=150, y=500)#author name
    Label(st, text="Enter date of issue:", font=40).place(x=150, y=550)  #date of issue
    Label(st, text="Enter date of return:", font=40).place(x=150, y=600)  #date of return
    s_n = Entry(st) #student name entry box
    s_n.place(x=350,y=300)
    student_name = s_n.get()

    
    y_a = Entry(st) #year of admission entry box
    y_a.place(x=350,y=350)

    
    b_n = Entry(st) #book name entry box
    b_n.place(x=350,y=400)

    
    a_n = Entry(st) #author name entry box
    a_n.place(x=350,y=450)
    
    b = Entry(st)
    b.place(x=350,y=500)
    
    d_i = Entry(st) #date of issue entry box
    d_i.place(x=350,y=550)

    
    d_r = Entry(st) #date of return entry box
    d_r.place(x=350,y=600)



        

    def issue_book_():
        student_name = s_n.get() #storing student name
        year_admission = y_a.get() #storing year of admisson
        book_name = b_n.get() #storing book name
        author_name = a_n.get() #storing author name
        date_issue = d_i.get() #storing date of issue
        date_return = d_r.get() #storing date of return
        _branch_=b.get()
        names=[student_name," ",year_admission," ",book_name," ",_branch_," ",date_issue," ",date_return]
        file_=open('disgusting.txt', 'w')
        file_.writelines(names)
        file_.close()
        student_txt = open("issue_book.txt",'a')
        print(date_issue)
        s=[student_name," ",year_admission," ",book_name," ",author_name," ",_branch_," ",date_issue," ",date_return]
        student_txt.write("\n")
        student_txt.writelines(s)
        student_txt.close()
        print("Issued book")
        
    Button(st, text="Submit", command=issue_book_, font=40). place(x=400,y=600)
    desired_word=" "
    desired_book=" "
    with open('disgusting.txt', 'r') as file_:
        for _line_ in file_:
            _words_ = _line_.split()
            desired_word=_words_[0]
            desired_book=_words_[2]


    print("3"+desired_word)
    print("3"+desired_book)
            
            
    file=open('student_request.txt', 'r')
    line_=" "
    
    for line in file:
        words = line.split()
        print("1"+words[0])
        print("2"+desired_word)
        if words[0]==desired_word:
            line_=line
            print(line_)
            print("HI")


    with open("student_request.txt", "r") as file:
        lines = file.readlines()
        with open("student_request.txt", "w") as file:
            for _line in lines:
                if _line!=line_:
                    file.write(_line)

                    
    _file=open('book.txt', 'r')
    line_b=" "
    
    for __line__ in _file:
        words_a = __line__.split()
        print("1"+words_a[0])
        print("2"+desired_book)
        if words_a[0]==desired_book:
            line_b=__line__
            print(line_b)
            print("HI")

    with open("book.txt", "r") as _file:
        lines_b_ = _file.readlines()
        with open("book.txt", "w") as _file:
            for b_line in lines_b_:
                if b_line!=line_b:
                    _file.write(b_line)

    

    
        
def request_book():
    g = Tk()
    g.title("REQUEST BOOK")
    g.geometry("1188x840")
    g.configure(bg='lightyellow')
    Label(g, text="REQUEST BOOK", font=("CASTELLAR", 60), bg="pink").place(x=350, y=200)
    Label(g, text="STUDENT NAME", font=40, bg="pink").place(x=450, y=305)
    Label(g, text="YEAR OF ADMISSION", font=40, bg="pink").place(x=450, y=350)
    Label(g, text="BOOK NAME", font=40, bg="pink").place(x=450, y=400)
    Label(g, text="AUTHOR", font=40, bg="pink").place(x=450, y=450)
    Label(g, text="BRANCH", font=40, bg="pink").place(x=450, y=500)
    student_name_ = Entry(g)
    student_name_.place(x=600, y=305)
    yr_of_admn_ = Entry(g)
    yr_of_admn_.place(x=600, y=350)
    book_name_ = Entry(g)
    book_name_.place(x=600, y=400)
    author_ = Entry(g)
    author_.place(x=600, y=450)
    branch_ = Entry(g)
    branch_.place(x=600, y=500)
    
    def student_request():
        student_name = student_name_.get()
        yr_of_admn = yr_of_admn_.get()
        book_name = book_name_ .get()
        author = author_.get()
        branch=branch_.get()
        print(student_name)
        S_R=Student_Req(student_name,yr_of_admn,book_name,author,branch)
        S_R.add_S_R_file()
        
    Button(g, text="Submit", command=student_request, font=40, bg="light pink").place(x=600, y=600)
    
     
    
lib = Tk()
lib.title("Library management system")
lib.geometry("1188x840")
lib.configure(bg='lightgreen')
Label(lib, text="CBIT LIBRARY MANAGEMENT SYSTEM", font=100, bg="pink").pack(side=TOP, fill="x")
Label(lib, text="LOGIN", font=("CASTELLAR", 40)).place(x=550, y=200)
vlist = ["Student", "Faculty", "HOD", "Principal", "Librarian", "Anonymous"]
user_type_ = StringVar()
Combo = ttk.Combobox(lib, textvariable=user_type_)
Combo["values"] = vlist
Combo["state"] = "readonly"
Combo.place(x=660, y=310)
Label(lib, text="Select user type", font=40, bg="pink").place(x=450, y=305)
Label(lib, text="USER NAME:", font=40, bg="lavender").place(x=450, y=350)
Label(lib, text="PASSWORD", font=40, bg="light blue").place(x=450, y=400)
user_name_ = Entry(lib)
user_password_ = Entry(lib)
user_name_.place(x=600, y=350)
user_password_.place(x=600, y=400)
Button(lib, text="Submit", command=user, font=40, bg="light pink").place(x=550, y=500)
lib.mainloop()
