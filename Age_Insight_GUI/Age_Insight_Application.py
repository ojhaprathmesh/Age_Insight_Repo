from pytz import timezone
from tkinter import Tk, Frame, Label, LabelFrame, RIDGE
from tkcalendar import Calendar
from datetime import datetime as dt
import calendar


class AgeFinder:
    def __init__(self, root):
        self.root = root
        self.birth_info = ''
        self.current_info = ''

        # Store label references
        self.birth_calendar = None
        self.birth_date_labels = {}
        self.current_date_labels = {}
        self.age_labels = {}
        self.time_label = None

        self.initialize_ui()

    def initialize_ui(self):
        """Initialize the user interface."""
        self.root.geometry('800x500+200+50')
        self.root.title('Age Finder | Developed by Prathmesh')
        self.root.resizable(False, False)

        cal_frame = self.create_frame(self.root, 0, 0, 0.625, 1)
        date_frame = self.create_frame(self.root, 5 / 8, 0, 0.375, 0.5)
        age_frame = self.create_frame(self.root, 5 / 8, 0.5, 0.375, 1 / 3)
        time_frame = self.create_frame(self.root, 5 / 8, 5 / 6, 0.375, 1 / 6)

        self.birth_calendar = Calendar(cal_frame, selectmode='day', year=2000, month=1, day=1, date_pattern='ddmmyyyy')
        self.birth_calendar.bind("<<CalendarSelected>>", lambda event: self.update_labels())
        self.birth_calendar.place(x=0, y=0, relwidth=1, relheight=1)

        self.setup_labels(date_frame, age_frame)
        self.setup_time_label(time_frame)

        self.update_labels()
        self.update_clock()

    def create_frame(self, parent, relx, rely, relwidth, relheight):
        """Helper to create a frame with standard properties."""
        frame = Frame(parent, bd=4, relief=RIDGE, bg='white')
        frame.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
        return frame

    def setup_labels(self, date_frame, age_frame):
        """Set up labels for displaying birth date, current date, and calculated age."""
        for count, label in enumerate(["Birth Date", "Current Date"]):
            self.create_label(date_frame, label, 0, count / 2, 1, 1 / 6)

        # Birth and current date label frames
        self.birth_date_labels = self.create_date_labels(date_frame, 1 / 6, "Birth")
        self.current_date_labels = self.create_date_labels(date_frame, 2 / 3, "Current")

        # Age label frames
        self.age_labels = self.create_age_labels(age_frame)

    def create_date_labels(self, parent, rel_y, label_prefix):
        """Create label frames for displaying day, month, and year."""
        labels = {}
        for i, label in enumerate(["Date", "Month", "Year"]):
            labels[label.lower()] = self.create_label_frame(parent, relx=i / 3, rely=rel_y, relwidth=1 / 3,
                                                            relheight=1 / 3)
        return labels

    def create_age_labels(self, parent):
        """Create label frames for displaying age in days, months, and years."""
        labels = {}
        for i, label in enumerate(["Day(s)", "Month(s)", "Year(s)"]):
            text_frame = self.create_label_frame(parent, relx=i / 3, rely=0, relwidth=1 / 3, relheight=1 / 2)
            value_frame = self.create_label_frame(parent, relx=i / 3, rely=1 / 2, relwidth=1 / 3, relheight=1 / 2)

            Label(text_frame, text=label, font=('times new roman', 18, 'bold')).place(x=0, y=0, relwidth=1, relheight=1)
            labels[label.lower()] = value_frame
        return labels

    def create_label(self, parent, text, relx, rely, relwidth, relheight):
        """Helper to create a text label."""
        label_frame = LabelFrame(parent, bd=2, relief=RIDGE, bg='white')
        label_frame.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
        label = Label(label_frame, text=text, font=('times new roman', 20, 'bold'))
        label.place(x=0, y=0, relwidth=1, relheight=1)

    def create_label_frame(self, parent, relx, rely, relwidth, relheight):
        """Create a label frame."""
        label_frame = LabelFrame(parent, bd=2, relief=RIDGE, bg='white')
        label_frame.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
        return label_frame

    def setup_time_label(self, time_frame):
        """Set up the time label in the UI."""
        self.time_label = Label(time_frame, font=('times new roman', 36, 'bold'))
        self.time_label.place(x=0, y=0, relwidth=1, relheight=1)

    def update_labels(self):
        """Update the birth date, current date, and age labels."""
        self.get_dates()
        birth_date, current_date, age = self.process_dates()

        self.display_label_data(self.birth_date_labels, birth_date)
        self.display_label_data(self.current_date_labels, current_date)
        self.display_label_data(self.age_labels, age)

    def display_label_data(self, labels_dict, data_tuple):
        """Helper to display data in respective label frames."""
        for key, value in zip(labels_dict.keys(), data_tuple):
            Label(labels_dict[key], text=value, font=('times new roman', 30, 'bold')).place(x=0, y=0, relwidth=1,
                                                                                            relheight=1)

    def get_dates(self):
        """Retrieve the birth date from the calendar and the current date."""
        self.birth_info = self.birth_calendar.get_date()
        self.current_info = dt.now().strftime("%d%m%Y")

    def process_dates(self):
        """Process birth and current dates to calculate age."""
        birth_day, birth_month, birth_year = int(self.birth_info[:2]), int(self.birth_info[2:4]), int(
            self.birth_info[4:])
        current_day, current_month, current_year = int(self.current_info[:2]), int(self.current_info[2:4]), int(
            self.current_info[4:])

        birth_date = (birth_day, birth_month, birth_year)
        current_date = (current_day, current_month, current_year)

        birth = dt(birth_year, birth_month, birth_day)
        current = dt(current_year, current_month, current_day)

        age_delta = current - birth
        age_years, age_months, age_days = age_delta.days // 365, (age_delta.days % 365) // 30, age_delta.days % 30

        return birth_date, current_date, (age_days, age_months, age_years)

    def update_clock(self):
        """Update the clock every second."""
        ist = timezone('Asia/Kolkata')
        raw_tz = dt.now(ist)
        time_now = raw_tz.strftime("%H:%M:%S %p")
        self.time_label.config(text=time_now)
        self.time_label.after(500, self.update_clock)


# Run the application
root = Tk()
app = AgeFinder(root)
root.mainloop()
