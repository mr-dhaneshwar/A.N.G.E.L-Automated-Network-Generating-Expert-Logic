from tkinter import *
from Face_lock import *
from threading import *
from login import *
from tkinter import messagebox
from tkcalendar import DateEntry
from PIL import ImageTk, Image
from Helptext import *

theme = 'Light'


def change_theme():
    global theme
    if theme == 'Light':
        c = 'Black'
        bglb.configure(bg=c)
        theme_check.configure(bg=c)
        name_lb.configure(bg=c)
        helpbt.configure(bg=c, activebackground=c)
        settingbt.configure(bg=c, activebackground=c)
        silent_button.configure(bg=c, activebackground=c)
        start_button.configure(bg=c, activebackground=c)
        sframe.config(bg=c)
        slist.configure(bg=c, fg='White')
        closebt.configure(bg=c, activebackground=c)
        speak_status_lb.config(bg=c)
        marathi_rb.configure(bg=c, activebackground=c)
        english_rb.configure(bg=c, activebackground=c)
        hindi_rb.configure(bg=c, activebackground=c)
        try:
            hframe.configure(bg=c)
            my_frame.configure(bg=c)
            clr_button.configure(bg=c, activebackground=c)
            f_label.configure(bg=c)
            help_label.configure(bg=c)
            close_button.configure(bg=c, activebackground=c)
            status.configure(bg=c)
            anime.configure(bg=c)
            scrollbar.configure(bg=c)
            output.configure(bg=c, fg='White', insertbackground='White')
            help_text.configure(bg=c, fg='White', insertbackground='White')

        except Exception as e:
            print("error converting dark theme", e)

        theme = 'Dark'
    else:
        c = 'White'
        bglb.configure(bg=c)
        theme_check.configure(bg=c)
        silent_button.configure(bg=c, activebackground=c)
        name_lb.configure(bg=c)
        helpbt.configure(bg=c, activebackground=c)
        settingbt.configure(bg=c, activebackground=c)
        start_button.configure(bg=c, fg='Blue', activebackground=c)
        sframe.config(bg=c)
        slist.configure(bg=c, fg='Black')
        closebt.configure(bg=c, activebackground=c)
        speak_status_lb.config(bg=c)
        marathi_rb.configure(bg=c)
        english_rb.configure(bg=c)
        hindi_rb.configure(bg=c)
        try:
            hframe.configure(bg=c)
            my_frame.configure(bg=c)
            clr_button.configure(bg=c, activebackground=c)
            f_label.configure(bg=c)
            help_label.configure(bg=c)
            close_button.configure(bg=c, activebackground=c)
            status.configure(bg=c)
            anime.configure(bg=c)
            scrollbar.configure(bg=c)
            output.configure(bg=c, fg='Black', insertbackground='Black')
            help_text.configure(bg=c, fg='Black', insertbackground='Black')

        except Exception as e:
            print("error converting dark theme", e)
        theme = 'Light'


class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tipwindow = None

    def showtip(self):
        if self.tipwindow or not self.text:
            return
        x, y, _, _ = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() - 10
        y = y + self.widget.winfo_rooty() + 60
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT, background="#ffffe0",
                      relief=SOLID, borderwidth=1, font=("tahoma", "10", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


def create_tooltip(widget, text):
    toolTip = ToolTip(widget, text)

    def enter(event):
        toolTip.showtip()

    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


def show_error(e):
    e = str(e)
    messagebox.showerror("Error", e+' Click ok to restrart')
    close()


def off_speak():
    global speak_status

    if speak_status == 1:
        speak_status = 0
        silent_button.configure(image=sound_png)
        speak_status_lb.config(text='Turn ON')
        return False
    else:
        speak_status = 1
        silent_button.configure(image=silence_png)
        speak_status_lb.config(text='Turn OFF')
        return True


def speak_check():
    if speak_status == 1:
        return True
    else:
        return False


def get_lang():
    return lang.get()


def write(text):
    output.config(state=NORMAL)
    output.insert('end', text + '\n')
    output.config(state=DISABLED)


def clear():
    output.delete(1.0, END)


def change_leble(line, no):
    global status, anime, my_frame, art_img
    status.configure(text=line)
    anime.configure(image=art_img[no])


def set_img(img):

    if img == 1:
        start_img.configure(image=start1_png)
    elif img == 2:
        start_img.configure(image=start2_png)


def close():
    my_frame.destroy()


location = 'D:\\Angel\\image\\'


def new_frame(main):
    global my_frame, f_label, scrollbar, output, broom_png, clr_button, close_button, close_png, smile_png, anime, t
    global confused_png, gotit_png, idea_png, listening_png, love_png, status, location, art_img, start_img

    if theme == "Dark":
        c = 'Black'
        fc = 'White'
    else:
        c = 'White'
        fc = 'Black'

    my_frame = Frame(root, width=1100, height=700,
                     bg=c, relief=GROOVE, borderwidth=8)
    my_frame.place(x=100, y=0)

    broom_png = PhotoImage(file=location + "clean.png")
    clr_button = Button(my_frame, image=broom_png,
                        cursor='hand2', relief=FLAT, bg=c, command=clear)
    clr_button.place(x=250, y=8)
    create_tooltip(clr_button, 'Clear chat')

    start_img = Label(my_frame, image=None, height=220, width=220, bg=c)
    start_img.place(x=10, y=50)

    status = Label(my_frame, text='connecting....',
                   bg=c, fg='Red', font=('Arial', 16, 'bold'))
    status.place(x=40, y=380)

    smile_png = PhotoImage(file=location + "smile.png")
    confused_png = PhotoImage(file=location + "confused.png")
    gotit_png = PhotoImage(file=location + "gotit.png")
    idea_png = PhotoImage(file=location + "idea.png")
    listening_png = PhotoImage(file=location + "listening.png")
    love_png = PhotoImage(file=location + "love.png")
    art_img = ["", smile_png, confused_png,
               gotit_png, idea_png, listening_png, love_png]

    anime = Label(my_frame, image=smile_png, height=220, width=220, bg=c)
    anime.place(x=8, y=460)

    f_label = Label(my_frame, relief=GROOVE, height=2, width=63, borderwidth=2,
                    text='Automated Network Generating Expert Logic  ( ANGEL )', bg=c, fg='Red', font=('Arial', 12))
    f_label.place(x=305, y=5)

    t = Thread(target=main)
    t.start()

    close_button = Button(my_frame, image=close_png,
                          cursor='hand2', relief=FLAT, bg=c, command=close)
    close_button.place(x=1010, y=8)
    create_tooltip(close_button, 'Close')

    scrollbar = Scrollbar(my_frame, orient=VERTICAL)
    scrollbar.place(x=1065, relheight=1)

    output = Text(my_frame, bg=c, fg=fc, insertbackground=fc, height=24, width=80, relief=GROOVE, borderwidth=2,
                  yscrollcommand=scrollbar.set, font=('Segoe UI', 11))
    output.place(x=250, y=65)
    scrollbar.config(command=output.yview)
    output.config(yscrollcommand=scrollbar.set)

    # def scroll_to_bottom(event):
    #     output.yview_moveto(1.0)
    # output.bind('<Configure>', scroll_to_bottom)


def face(op):
    if op == 1:
        reset_face()
        face_sample()  # take face samples
        face_train()  # train face model
        logframe.destroy()
    else:
        reset_face()
        close_setting()
        signin_frame(2)


def set_user():
    use = user.get().lower()
    pas = code.get()
    nam = name.get()
    date = dob.get()

    print(date)

    if use == '':
        messagebox.showerror("Invalid", "pleste enter Username")
    elif pas == '':
        messagebox.showerror("Invalid", "pleste enter Passwors")
    elif nam == '':
        messagebox.showerror("Invalid", "pleste enter Name")
    elif date == '' or date == None:
        messagebox.showerror("Invalid", "pleste enter Date of birth")
    elif singup(use, pas, nam, date) == 1:
        messagebox.showinfo("singed in", 'Account created succesfull')
        signin_frame(2)
    elif singin(use, pas) == 'not connect':
        messagebox.showerror("Server Error", "Not connected to the server")
    elif singup(use, pas, nam, date) == 2:
        messagebox.showinfo("Exist", 'User already exist')
    else:
        messagebox.showerror("Invalid", "Somthing went wrong")


def get_user():
    use = user.get().lower()
    pas = code.get()
    if use == '':
        messagebox.showerror("Invalid", "pleste enter Username")
    elif pas == '':
        messagebox.showerror("Invalid", "pleste enter Passwors")
    elif singin(use, pas) == 'not connect':
        messagebox.showerror("Server Error", "Not connected to the server")
    elif singin(use, pas) == 1:
        messagebox.showinfo("loged in", 'login succesfull')
        signin_frame(4)
    else:
        msg = singin(use, pas)
        if msg == 2:
            messagebox.showerror("Invalid", 'invalid password')
        else:
            messagebox.showerror(
                "Invalid", "Username not found please Sing Up")


def forgot_pass():
    use = user.get().lower()
    date = dob.get()
    pas = code.get()

    if use == '':
        messagebox.showerror("Invalid", "pleste enter Username")
    elif date == '' or date == None:
        messagebox.showerror("Invalid", "pleste Select Date of birth")
    elif forgot(use, date) == 2:
        messagebox.showerror("Invalid", 'invalid credentials')
    elif pas == '':
        messagebox.showerror("Invalid", "pleste enter new Passwors")
    elif forgot(use, date, pas) == 'not connect':
        messagebox.showerror("Server Error", "Not connected to the server")
    elif forgot(use, date, pas) == 1:
        messagebox.showinfo("Succes", 'Password reset succesfully')
        signin_frame(2)


def signin_frame(step):
    global logframe, name, user, code, dob
    try:
        logframe.destroy()
    except Exception as e:
        print('problem in sing in frame', e)
    logframe = Frame(root, width=1200, height=700,
                     relief=GROOVE, borderwidth=8)
    logframe.place(x=0, y=0)

    logbglb = Label(logframe, image=logbgimg)
    logbglb.place(relheight=1, relwidth=1)

    Label(logframe, border=0, text='Welcome', bg='#ab23ff',
          fg="white", font=('Times', 40, 'bold',)).place(x=470, y=10)

    frame = Frame(logframe, width=500, height=500, bg="white")
    frame.place(x=350, y=100)

    if step == 1:

        heading = Label(frame, text='Sign Up', fg="#57a1f8",
                        bg='white', font=('Times', 25, 'bold'))
        heading.place(x=170, y=5)

        namelb = Label(frame, text='Name: ', fg="#57a1f8",
                       bg='white', font=('Times', 18, 'bold'))
        namelb.place(x=20, y=70)
        name = Entry(frame, width=30, fg='black', border=0,
                     bg='white', font=('Arial', 11))
        name.place(x=180, y=80)

        Frame(frame, width=300, height=2, bg='black').place(x=180, y=110)

        userlb = Label(frame, text='Username: ', fg="#57a1f8",
                       bg='white', font=('Times', 18, 'bold'))
        userlb.place(x=20, y=150)
        user = Entry(frame, width=30, fg='black', border=0,
                     bg='white', font=('Arial', 11))
        user.place(x=180, y=160)

        Frame(frame, width=300, height=2, bg='black').place(x=180, y=190)

        codelb = Label(frame, text='Password: ', fg="#57a1f8",
                       bg='white', font=('Times', 18, 'bold'))
        codelb.place(x=20, y=230)
        code = Entry(frame, width=30, fg='black', border=0,
                     bg='white', show='*', font=('Arial', 11))
        code.place(x=180, y=240)

        Frame(frame, width=300, height=2, bg='black').place(x=180, y=270)

        doblb = Label(frame, text='DOB: ', fg="#57a1f8",
                      bg='white', font=('Times', 18, 'bold'))
        doblb.place(x=20, y=310)

        dob = DateEntry(frame, date_pattern='yyyy-mm-dd', firstweekday='sunday',
                        locale='en_US', width=27, fg='black', bg='white', font=('Arial', 11))
        dob.place(x=180, y=320)

        Frame(frame, width=300, height=2, bg='black').place(x=180, y=350)

        sinupgbt = Button(frame, width=15, pady=7, text="Sign Up", cursor='hand2', font=(
            'Times', 15, 'bold'), bg="#57a1f8", fg='white', relief=GROOVE, command=set_user)
        sinupgbt.place(x=150, y=370)

        qlb1 = Label(frame, text="Already have account? -->",
                     fg='black', bg='white', font=('Arial', 12))
        qlb1.place(x=70, y=450)

        sign_inbt = Button(frame, width=6, text='Sign In', border=0, bg='white', cursor='hand2',
                           fg="#57a1f7", command=lambda: signin_frame(2), font=('Arial', 12))
        sign_inbt.place(x=330, y=445)

    elif step == 2:

        heading = Label(frame, text='Sign In', fg="#57a1f8",
                        bg='white', font=('Times', 25, 'bold'))
        heading.place(x=170, y=5)

        userlb = Label(frame, text='Username: ', fg="#57a1f8",
                       bg='white', font=('Times', 18, 'bold'))
        userlb.place(x=20, y=90)
        user = Entry(frame, width=30, fg='black', border=0,
                     bg='white', font=('Arial', 11))
        user.place(x=180, y=100)

        Frame(frame, width=300, height=2, bg='black').place(x=180, y=130)

        codelb = Label(frame, text='Password: ', fg="#57a1f8",
                       bg='white', font=('Times', 18, 'bold'))
        codelb.place(x=20, y=170)
        code = Entry(frame, width=30, fg='black', border=0,
                     bg='white', show='*', font=('Arial', 11))
        code.place(x=180, y=180)

        Frame(frame, width=300, height=2, bg='black').place(x=180, y=210)

        singbt = Button(frame, width=15, pady=7, text="Sign in", cursor='hand2', font=(
            'Times', 15, 'bold'), bg="#57a1f8", fg='white', relief=GROOVE, command=get_user)
        singbt.place(x=150, y=270)

        qlb1 = Label(frame, text="Forgot Password? -->",
                     fg='black', bg='white', font=('Arial', 12))
        qlb1.place(x=70, y=400)

        forgot = Button(frame, width=14, text='Forgot Password', border=0, bg='white',
                        cursor='hand2', fg="#57a1f7", command=lambda: signin_frame(3), font=('Arial', 12))
        forgot.place(x=280, y=395)

        qlb2 = Label(frame, text="Don't have account? -->",
                     fg='black', bg='white', font=('Arial', 12))
        qlb2.place(x=70, y=450)

        sign_upbt = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2',
                           fg="#57a1f7", command=lambda: signin_frame(1), font=('Arial', 12))
        sign_upbt.place(x=310, y=445)

    elif step == 3:
        heading = Label(frame, text='Forgot !', fg="#57a1f8",
                        bg='white', font=('Times', 25, 'bold'))
        heading.place(x=170, y=5)

        userlb = Label(frame, text='Username: ', fg="#57a1f8",
                       bg='white', font=('Times', 18, 'bold'))
        userlb.place(x=20, y=150)
        user = Entry(frame, width=30, fg='black', border=0,
                     bg='white', font=('Arial', 11))
        user.place(x=180, y=160)

        Frame(frame, width=300, height=2, bg='black').place(x=180, y=190)

        doblb = Label(frame, text='DOB: ', fg="#57a1f8",
                      bg='white', font=('Times', 18, 'bold'))
        doblb.place(x=20, y=230)
        dob = DateEntry(frame, date_pattern='yyyy-mm-dd', firstweekday='sunday',
                        locale='en_US', width=27, fg='black', bg='white', font=('Arial', 11))
        dob.place(x=180, y=240)

        Frame(frame, width=300, height=2, bg='black').place(x=180, y=270)

        codelb = Label(frame, text='New Password: ', fg="#57a1f8",
                       bg='white', font=('Times', 18, 'bold'))
        codelb.place(x=20, y=310)
        code = Entry(frame, width=25, fg='black', border=0,
                     bg='White', show='*', font=('Arial', 11))
        code.place(x=230, y=320)

        Frame(frame, width=250, height=2, bg='black').place(x=230, y=350)

        resetbt = Button(frame, width=15, pady=7, text="Reset", cursor='hand2', font=(
            'Times', 15, 'bold'), bg="#57a1f8", fg='white', relief=GROOVE, command=forgot_pass)
        resetbt.place(x=140, y=380)

        qlb1 = Label(frame, text="Return to singin -->",
                     fg='black', bg='white', font=('Arial', 12))
        qlb1.place(x=70, y=450)

        sign_inbt = Button(frame, width=6, text='Sign In', border=0, bg='white', cursor='hand2',
                           fg="#57a1f7", command=lambda: signin_frame(2), font=('Arial', 12))
        sign_inbt.place(x=270, y=445)

    elif step == 4:
        heading = Label(frame, text='Add Face lock', fg="#57a1f8",
                        bg='white', font=('Times', 25, 'bold'))
        heading.place(x=130, y=50)

        facebt = Button(frame, image=facegbgimg, relief=GROOVE, cursor='hand2',
                        borderwidth=10, bg='White', command=lambda: face(1))
        facebt.place(x=150, y=150)

        notelb = Label(frame, text="Note--> Stay in the light and look into the Camera",
                       fg='red', bg='white', font=('Arial', 12))
        notelb.place(x=20, y=400)


def close_setting():
    sframe.destroy()


def setting_frame():
    global sframe, theme_check, silent_button, closebt, speak_info, slist, speak_status_lb, marathi_rb, english_rb, hindi_rb

    if theme == "Dark":
        c = 'Black'
        fc = 'White'
    else:
        c = 'White'
        fc = 'black'

    sframe = Frame(root, bg=c, width=400, height=700,
                   relief=GROOVE, borderwidth=8)
    sframe.place(x=800, y=0)

    if speak_status == 1:
        speak_image = silence_png
        speak_info = 'Turn OFF'
    else:
        speak_image = sound_png
        speak_info = 'Turn ON'

    slist = Label(sframe, bg=c, fg=fc, justify=LEFT,
                  text='Speak Status\n\n\n\nTheme\n\n\nLanguage', font='Arial 16 bold')
    slist.place(x=10, y=10)

    silent_button = Button(sframe, bg=c, image=speak_image,
                           cursor='hand2', relief=FLAT, command=off_speak)
    silent_button.place(x=10, y=60)
    create_tooltip(silent_button, 'Speak Status')

    speak_status_lb = Label(sframe, bg=c, fg='blue',
                            text=speak_info, font='Arial 12')
    speak_status_lb.place(x=80, y=70)

    theme_check = Checkbutton(sframe, bg=c, text='Dark Theme',
                              font='Arial 14', cursor='hand2', command=change_theme, fg='Blue')
    theme_check.place(x=10, y=180)
    create_tooltip(theme_check, 'Change Theme')
    if theme == 'Dark':
        theme_check.select()
    else:
        theme_check.deselect()

    marathi_rb = Radiobutton(
        sframe, text="Marathi", font='Arial 14', bg=c, fg='blue', variable=lang, value=1)
    marathi_rb.place(x=10, y=290)
    english_rb = Radiobutton(
        sframe, text="English", font='Arial 14', bg=c, fg='blue', variable=lang, value=2)
    english_rb.place(x=10, y=330)
    hindi_rb = Radiobutton(sframe, text="Hindi", font='Arial 14',
                           bg=c, fg='blue', variable=lang, value=3)
    hindi_rb.place(x=10, y=370)

    closebt = Button(sframe, image=close_png, cursor='hand2',
                     bg=c, relief=FLAT, command=close_setting)
    closebt.place(x=335, y=5)
    create_tooltip(closebt, 'Close')
    logoutbt = Button(sframe, text='Logout', cursor='hand2', font=(
        'Times', 12, 'bold'), bg="red", fg='white', relief=GROOVE, command=lambda: face(2))
    logoutbt.place(x=300, y=600)
    create_tooltip(logoutbt, 'Logout')


def close_hframe():
    hframe.destroy()


def help_page():
    global hframe, help_text, user_guid, help_label, help_close_button

    if theme == "Dark":
        c = 'Black'
        fc = 'White'
    else:
        c = 'White'
        fc = 'black'

    hframe = Frame(root, bg=c, width=750, height=700,
                   relief=GROOVE, borderwidth=8)
    hframe.place(x=450, y=0)

    help_label = Label(hframe, text='USER GUIDE', bg=c,
                       fg='Red', font=('Arial', 16, 'bold'))
    help_label.place(x=3, y=5)

    help_close_button = Button(
        hframe, image=close_png, cursor='hand2', relief=FLAT, bg=c, command=close_hframe)
    help_close_button.place(x=660, y=5)
    create_tooltip(help_close_button, 'Close')

    help_scrollbar = Scrollbar(hframe, orient=VERTICAL)
    help_scrollbar.place(x=710, relheight=1)

    help_text = Text(hframe, bg=c, fg=fc, insertbackground=fc, height=25, width=70, relief=GROOVE, borderwidth=2,
                     yscrollcommand=help_scrollbar.set, font=('Segoe UI', 11))
    help_text.place(x=3, y=50)
    user_guid = user_guid

    help_text.insert('end', user_guid)
    help_text.config(state=DISABLED)
    help_scrollbar.config(command=help_text.yview)
    help_text.config(yscrollcommand=help_scrollbar.set)


speak_status = 1


def my_window(main):
    global bglb, lang, name_lb, silence_png, start_button, close_png, speak_status, settingbt, sound_png, root, photo, logbgimg, facegbgimg, settingbt, helpbt, start1_png, start2_png
    root = Tk()
    root.geometry('1200x700')
    root.configure(bg='White')
    root.resizable(False, False)
    root.title('ANGEL_2.0')
    logo = PhotoImage(file="D:\\Angel\\image\\logo.png")
    root.iconphoto(False, logo)

    lang = IntVar()
    lang.set(2)

    temp1 = Image.open(location + 'start1.png')
    # resize image
    resized = temp1.resize((230, 230), Image.LANCZOS)
    start1_png = ImageTk.PhotoImage(resized)

    temp2 = Image.open(location + 'start2.png')
    # resize image
    resized = temp2.resize((230, 230), Image.LANCZOS)
    start2_png = ImageTk.PhotoImage(resized)

    # login page background
    logbgopen = Image.open('D:\\Angel\\image\\login bg.png')
    # resize image
    resized = logbgopen.resize((1200, 700), Image.LANCZOS)
    logbgimg = ImageTk.PhotoImage(resized)

    # login page background
    facebgopen = Image.open('D:\\Angel\\image\\face-id.png')
    # resize image
    resized = facebgopen.resize((200, 200), Image.LANCZOS)
    facegbgimg = ImageTk.PhotoImage(resized)

    photo = PhotoImage(file=location + "background.png")
    bglb = Label(root, image=photo)
    bglb.place(relwidth=1, relheight=1)

    # login page background
    logohelp = Image.open('D:\\Angel\\image\\help.png')
    # resize image
    resized = logohelp.resize((45, 45), Image.LANCZOS)
    help_img = ImageTk.PhotoImage(resized)

    helpbt = Button(root, image=help_img, cursor='hand2',
                    relief=FLAT, command=help_page)
    helpbt.place(x=1140, y=10)
    create_tooltip(helpbt, 'Help?')

    # login page background
    logosopen = Image.open('D:\\Angel\\image\\simage.png')
    # resize image
    resized = logosopen.resize((45, 45), Image.LANCZOS)
    setting_img = ImageTk.PhotoImage(resized)

    settingbt = Button(root, image=setting_img, cursor='hand2',
                       relief=FLAT, command=setting_frame)
    settingbt.place(x=1140, y=80)
    create_tooltip(settingbt, 'Settings')

    # login page background
    silence_png = Image.open('D:\\Angel\\image\\silence.png')
    # resize image
    resized = silence_png.resize((45, 45), Image.LANCZOS)
    silence_png = ImageTk.PhotoImage(resized)

    # login page background
    sound_png = Image.open('D:\\Angel\\image\\sound.png')
    # resize image
    resized = sound_png.resize((45, 45), Image.LANCZOS)
    sound_png = ImageTk.PhotoImage(resized)

    close_png = PhotoImage(file=location + "close.png")

    name_lb = Label(root, text='A\nN\nG\nE\nL', font=('Arial', 50), fg='Blue')
    name_lb.place(x=20, y=70)

    startimg = PhotoImage(file='D:\\Angel\\image\\play.png')

    start_button = Button(root, image=startimg, cursor='hand2',
                          relief=FLAT, command=lambda: new_frame(main))
    start_button.place(x=800, y=372)

    create_tooltip(start_button, 'Start')

    # implementing face lock system

    if os.listdir('D:\\Angel\\samples'):
        if face_match():
            print('welcome')
        else:
            signin_frame(4)
    else:
        signin_frame(2)

    root.mainloop()
