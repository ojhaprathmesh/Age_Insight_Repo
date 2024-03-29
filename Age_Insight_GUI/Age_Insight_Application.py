from pytz import timezone
from tkinter import Tk, Frame, Label, LabelFrame, RIDGE
from tkcalendar import Calendar
from datetime import datetime as dt


class AgeFinder:
    def __init__(self, self_root):
        self.root = self_root

        self.birthInfo = ''
        self.currentInfo = ''

        self.birthCalendar = None
        self.birthDateLabelFrame = None
        self.currentDateLabelFrame = None
        self.birthMonthLabelFrame = None
        self.currentMonthLabelFrame = None
        self.birthYearLabelFrame = None
        self.currentYearLabelFrame = None
        self.ageDaysLabelFrame = None
        self.ageMonthsLabelFrame = None
        self.ageYearsLabelFrame = None
        self.ageDaysTextLabelFrame = None
        self.ageMonthsTextLabelFrame = None
        self.ageYearsTextLabelFrame = None
        self.timeLabel = None
        self.initialize_ui()

    def initialize_ui(self):

        self.root.geometry('800x500+200+50')
        self.root.title('Age Finder | Developed by Prathmesh')
        self.root.resizable(False, False)

        cal_frame = Frame(self.root, bd=4, relief=RIDGE, bg='white')
        cal_frame.place(x=0, y=0, relwidth=0.625, relheight=1)

        date_frame = Frame(self.root, bd=4, relief=RIDGE, bg='white')
        date_frame.place(relx=5 / 8, rely=0, relwidth=0.375, relheight=1 / 2)

        age_frame = Frame(self.root, bd=4, relief=RIDGE, bg='white')
        age_frame.place(relx=5 / 8, rely=1 / 2, relwidth=0.375, relheight=1 / 3)

        time_frame = Frame(self.root, bd=4, relief=RIDGE, bg='white')
        time_frame.place(relx=5 / 8, rely=5 / 6, relwidth=0.375, relheight=1 / 6)

        self.birthCalendar = Calendar(cal_frame, selectmode='day', year=2000, month=1, day=1, date_pattern='ddmmyyyy')
        self.birthCalendar.bind("<<CalendarSelected>>", lambda event: self.update_label())
        self.birthCalendar.place(x=0, y=0, relwidth=1, relheight=1)

        for count, label in enumerate(["Birth Date", "Current Date"]):
            label_frame = LabelFrame(date_frame, bd=2, relief=RIDGE, bg='white')
            label_frame.place(relx=0, rely=count / 2, relwidth=1, relheight=1 / 6)

            date_label = Label(label_frame, text=label, font=('times new roman', 20, 'bold'))
            date_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.birthDateLabelFrame = LabelFrame(date_frame, bd=2, relief=RIDGE, bg='white')
        self.birthDateLabelFrame.place(relx=0, rely=1 / 6, relwidth=1 / 3, relheight=1 / 3)

        self.currentDateLabelFrame = LabelFrame(date_frame, bd=2, relief=RIDGE, bg='white')
        self.currentDateLabelFrame.place(relx=0, rely=2 / 3, relwidth=1 / 3, relheight=1 / 3)

        self.birthMonthLabelFrame = LabelFrame(date_frame, bd=2, relief=RIDGE, bg='white')
        self.birthMonthLabelFrame.place(relx=1 / 3, rely=1 / 6, relwidth=1 / 3, relheight=1 / 3)

        self.currentMonthLabelFrame = LabelFrame(date_frame, bd=2, relief=RIDGE, bg='white')
        self.currentMonthLabelFrame.place(relx=1 / 3, rely=2 / 3, relwidth=1 / 3, relheight=1 / 3)

        self.birthYearLabelFrame = LabelFrame(date_frame, bd=2, relief=RIDGE, bg='white')
        self.birthYearLabelFrame.place(relx=2 / 3, rely=1 / 6, relwidth=1 / 3, relheight=1 / 3)

        self.currentYearLabelFrame = LabelFrame(date_frame, bd=2, relief=RIDGE, bg='white')
        self.currentYearLabelFrame.place(relx=2 / 3, rely=2 / 3, relwidth=1 / 3, relheight=1 / 3)

        self.ageDaysLabelFrame = LabelFrame(age_frame, bd=2, relief=RIDGE, bg='white')
        self.ageDaysLabelFrame.place(relx=0, rely=1 / 2, relwidth=1 / 3, relheight=1 / 2)

        self.ageMonthsLabelFrame = LabelFrame(age_frame, bd=2, relief=RIDGE, bg='white')
        self.ageMonthsLabelFrame.place(relx=1 / 3, rely=1 / 2, relwidth=1 / 3, relheight=1 / 2)

        self.ageYearsLabelFrame = LabelFrame(age_frame, bd=2, relief=RIDGE, bg='white')
        self.ageYearsLabelFrame.place(relx=2 / 3, rely=1 / 2, relwidth=1 / 3, relheight=1 / 2)

        self.ageDaysTextLabelFrame = LabelFrame(age_frame, bd=2, relief=RIDGE, bg='white')
        self.ageDaysTextLabelFrame.place(relx=0, rely=0, relwidth=1 / 3, relheight=1 / 2)

        self.ageMonthsTextLabelFrame = LabelFrame(age_frame, bd=2, relief=RIDGE, bg='white')
        self.ageMonthsTextLabelFrame.place(relx=1 / 3, rely=0, relwidth=1 / 3, relheight=1 / 2)

        self.ageYearsTextLabelFrame = LabelFrame(age_frame, bd=2, relief=RIDGE, bg='white')
        self.ageYearsTextLabelFrame.place(relx=2 / 3, rely=0, relwidth=1 / 3, relheight=1 / 2)

        age_years_text_label = Label(self.ageYearsTextLabelFrame, text='Year(s)', font=('times new roman', 18, 'bold'))
        age_years_text_label.place(x=0, y=0, relwidth=1, relheight=1)

        age_months_text_label = Label(self.ageMonthsTextLabelFrame, text='Month(s)',
                                      font=('times new roman', 18, 'bold'))
        age_months_text_label.place(x=0, y=0, relwidth=1, relheight=1)

        age_days_text_label = Label(self.ageDaysTextLabelFrame, text='Day(s)', font=('times new roman', 18, 'bold'))
        age_days_text_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.timeLabel = Label(time_frame, font=('times new roman', 36, 'bold'))
        self.timeLabel.place(x=0, y=0, relwidth=1, relheight=1)

        self.get_text()
        self.update_clock()

    def update_label(self):
        self.get_text()

    def update_clock(self):
        ist = timezone('Asia/Kolkata')
        raw_tz = dt.now(ist)
        time_now = raw_tz.strftime("%H:%M:%S %p")
        self.timeLabel.config(text=time_now)
        self.timeLabel.after(500, self.update_clock)

    def get_text(self):
        self.get_dates()
        req_tuple = self.process_dates()
        self.display_labels(req_tuple)

    def get_dates(self):
        self.birthInfo = self.birthCalendar.get_date()
        x = str(dt.date(dt.now()))
        d_list = [char for char in x if char != '-']
        self.currentInfo = ''.join(d_list)

    def process_dates(self):

        birth_date, current_date, birth_month, current_month, birth_year, current_year = map(int, (self.birthInfo[:2],
                                                                                                   self.currentInfo[6:],
                                                                                                   self.birthInfo[2:4],
                                                                                                   self.currentInfo[
                                                                                                   4:6],
                                                                                                   self.birthInfo[4:],
                                                                                                   self.currentInfo[
                                                                                                   :4]))

        if birth_month == 2:
            if birth_year % 4 != 0:
                total_days = 28  # Total Days
            else:
                total_days = 29

        elif birth_month % 2 == 0:
            if birth_month < 8:
                total_days = 30
            else:
                total_days = 31
        else:
            if birth_month > 8:
                total_days = 30
            else:
                total_days = 31

        if current_date - birth_date < 0:
            age_days = total_days - abs(current_date - birth_date)
            age_months = -1
        else:
            age_days = abs(current_date - birth_date)
            age_months = 0

        if current_month - birth_month < 1:
            age_months += 12 - abs(current_month - birth_month)
            age_years = -1
        else:
            age_months += abs(current_month - birth_month)
            age_years = 0

        if age_months == 12:
            age_months = 0
            age_years += 1

        age_years = age_years + abs(current_year - birth_year)

        return (birth_date, birth_date, birth_year), (current_date, current_month, current_year), (
            age_days, age_months, age_years)

    def display_labels(self, req_tuple):
        label_frames = [self.birthDateLabelFrame, self.birthMonthLabelFrame, self.birthYearLabelFrame,
                        self.currentDateLabelFrame, self.currentMonthLabelFrame, self.currentYearLabelFrame,
                        self.ageDaysLabelFrame, self.ageMonthsLabelFrame, self.ageYearsLabelFrame]

        labels_text = [req_tuple[i // 3][i % 3] for i in range(9)]
        label_text_frames = zip(labels_text, label_frames)

        for text, frame in label_text_frames:
            Label(frame, text=text, font=('times new roman', 30, 'bold')).place(x=0, y=0, relwidth=1, relheight=1)


root = Tk()
obj = AgeFinder(root)
root.mainloop()
