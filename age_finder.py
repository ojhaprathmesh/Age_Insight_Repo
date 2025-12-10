from pytz import timezone
from tkinter import (
    Tk, Frame, Label, LabelFrame, RIDGE,
    Menu, messagebox, Toplevel
)
from tkcalendar import Calendar
from datetime import datetime as dt
import logging

# Configure logging settings
logging.basicConfig(
    filename='./age_finder.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class ToolTip:
    def __init__(self, widget, text):
        """Initialize tooltip for a given widget with specified text"""
        self.widget = widget
        self.text = text

        self.tooltip_window = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        """Show tooltip when mouse enters widget"""
        if self.tooltip_window is not None:
            return

        # Get widget position
        try:
            x, y, _, _ = self.widget.bbox("insert")
        except Exception:
            x = y = 0

        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20

        # Using Toplevel instead of a second Tk root
        self.tooltip_window = Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)
        self.tooltip_window.wm_geometry(f"+{x}+{y}")

        label = Label(
            self.tooltip_window,
            text=self.text,
            bg="yellow",
            relief="solid",
            borderwidth=1
        )
        label.pack()

    def hide_tooltip(self, event=None):
        """Hide tooltip when mouse leaves widget"""
        if self.tooltip_window is not None:
            self.tooltip_window.destroy()
            self.tooltip_window = None


class AgeFinder:
    """Main application class for Age Calculator"""

    def __init__(self, root):
        self.root = root
        self.birth_info = ''
        self.current_info = ''

        # Application configuration settings
        self.config = {
            'theme': {
                'bg_color': 'white',
                'fg_color': 'black',
                'font_family': 'times new roman',
                'accent_color': '#007bff'
            },
            'timezone': 'Asia/Kolkata'
        }

        # Store label references
        self.birth_calendar = None
        self.birth_date_labels = {}
        self.current_date_labels = {}
        self.age_labels = {}
        self.time_label = None

        # Setup UI components
        self.initialize_ui()
        self.create_menu()
        self.bind_shortcuts()

    # ----------------- UI INITIALIZATION -----------------

    def initialize_ui(self):
        """Initialize and setup the user interface components"""
        try:
            # Configure main window
            self.root.geometry('800x500+200+50')
            self.root.title('Age Finder | Developed by Prathmesh')
            self.root.resizable(False, False)
            self.root.configure(bg=self.config['theme']['bg_color'])

            # Create main frames
            cal_frame = self.create_frame(self.root, 0, 0, 0.625, 1)
            date_frame = self.create_frame(self.root, 5 / 8, 0, 0.375, 0.5)
            age_frame = self.create_frame(self.root, 5 / 8, 0.5, 0.375, 1 / 3)
            time_frame = self.create_frame(self.root, 5 / 8, 5 / 6, 0.375, 1 / 6)

            # Setup calendar widget
            self.birth_calendar = Calendar(
                cal_frame,
                selectmode='day',
                year=2000,
                month=1,
                day=1,
                date_pattern='ddmmyyyy'
            )
            self.birth_calendar.bind("<<CalendarSelected>>",
                                     lambda event: self.update_labels())
            self.birth_calendar.place(x=0, y=0, relwidth=1, relheight=1)

            # Setup other UI components
            self.setup_labels(date_frame, age_frame)
            self.setup_time_label(time_frame)
            self.create_tooltips()

            # Initialize displays
            self.update_labels()
            self.update_clock()

            logging.info("UI initialized successfully")
        except Exception as e:
            logging.error(f"Error initializing UI: {str(e)}")
            messagebox.showerror("Error", f"Failed to initialize UI: {str(e)}")

    def create_frame(self, parent, relx, rely, relwidth, relheight):
        """Helper to create a frame with standard properties."""
        frame = Frame(
            parent,
            bd=4,
            relief=RIDGE,
            bg=self.config['theme']['bg_color']
        )
        frame.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
        return frame

    # ----------------- LABEL SETUP -----------------

    def setup_labels(self, date_frame, age_frame):
        """Set up labels for displaying birth date, current date, and calculated age."""
        # Section titles
        for count, label in enumerate(["Birth Date", "Current Date"]):
            self.create_label(
                date_frame,
                label,
                0,
                count / 2,
                1,
                1 / 6
            )

        # Birth and current date label frames
        self.birth_date_labels = self.create_date_labels(
            date_frame,
            rel_y=1 / 6
        )
        self.current_date_labels = self.create_date_labels(
            date_frame,
            rel_y=2 / 3
        )

        # Age label frames
        self.age_labels = self.create_age_labels(age_frame)

    def create_date_labels(self, parent, rel_y):
        """Create label frames for displaying day, month, and year."""
        labels = {}
        for i, _label in enumerate(["Date", "Month", "Year"]):
            labels[_label.lower()] = self.create_label_frame(
                parent,
                relx=i / 3,
                rely=rel_y,
                relwidth=1 / 3,
                relheight=1 / 3
            )
        return labels

    def create_age_labels(self, parent):
        """Create label frames for displaying age in days, months, and years."""
        labels = {}
        for i, _label in enumerate(["Day(s)", "Month(s)", "Year(s)"]):
            text_frame = self.create_label_frame(
                parent,
                relx=i / 3,
                rely=0,
                relwidth=1 / 3,
                relheight=1 / 2
            )
            value_frame = self.create_label_frame(
                parent,
                relx=i / 3,
                rely=1 / 2,
                relwidth=1 / 3,
                relheight=1 / 2
            )

            Label(
                text_frame,
                text=_label,
                font=(self.config['theme']['font_family'], 18, 'bold'),
                bg=self.config['theme']['bg_color'],
                fg=self.config['theme']['fg_color']
            ).place(x=0, y=0, relwidth=1, relheight=1)

            labels[_label.lower()] = value_frame
        return labels

    def create_label(self, parent, text, relx, rely, relwidth, relheight):
        """Helper to create a text label."""
        label_frame = LabelFrame(
            parent,
            bd=2,
            relief=RIDGE,
            bg=self.config['theme']['bg_color']
        )
        label_frame.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
        label = Label(
            label_frame,
            text=text,
            font=(self.config['theme']['font_family'], 20, 'bold'),
            bg=self.config['theme']['bg_color'],
            fg=self.config['theme']['fg_color']
        )
        label.place(x=0, y=0, relwidth=1, relheight=1)

    def create_label_frame(self, parent, relx, rely, relwidth, relheight):
        """Create a label frame."""
        label_frame = LabelFrame(
            parent,
            bd=2,
            relief=RIDGE,
            bg=self.config['theme']['bg_color']
        )
        label_frame.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
        return label_frame

    def setup_time_label(self, time_frame):
        """Set up the time label in the UI."""
        self.time_label = Label(
            time_frame,
            font=(self.config['theme']['font_family'], 36, 'bold'),
            bg=self.config['theme']['bg_color'],
            fg=self.config['theme']['fg_color']
        )
        self.time_label.place(x=0, y=0, relwidth=1, relheight=1)

    # ----------------- DATA / AGE CALCULATION -----------------

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
            Label(
                labels_dict[key],
                text=value,
                font=(self.config['theme']['font_family'], 30, 'bold'),
                bg=self.config['theme']['bg_color'],
                fg=self.config['theme']['fg_color']
            ).place(x=0, y=0, relwidth=1, relheight=1)

    def get_dates(self):
        """Retrieve the birth date from the calendar and the current date."""
        self.birth_info = self.birth_calendar.get_date()
        self.current_info = dt.now().strftime("%d%m%Y")

    def process_dates(self):
        """Process birth and current dates to calculate age."""
        birth_day = int(self.birth_info[:2])
        birth_month = int(self.birth_info[2:4])
        birth_year = int(self.birth_info[4:])

        current_day = int(self.current_info[:2])
        current_month = int(self.current_info[2:4])
        current_year = int(self.current_info[4:])

        birth_date = (birth_day, birth_month, birth_year)
        current_date = (current_day, current_month, current_year)

        birth = dt(birth_year, birth_month, birth_day)
        current = dt(current_year, current_month, current_day)

        age_delta = current - birth
        age_years = age_delta.days // 365
        age_months = (age_delta.days % 365) // 30
        age_days = age_delta.days % 30

        return birth_date, current_date, (age_days, age_months, age_years)

    # ----------------- CLOCK -----------------

    def update_clock(self):
        """Update the clock every half second."""
        try:
            ist = timezone(self.config['timezone'])
            raw_tz = dt.now(ist)
            time_now = raw_tz.strftime("%H:%M:%S %p")
            self.time_label.config(text=time_now)
            self.time_label.after(500, self.update_clock)
        except Exception as e:
            logging.error(f"Error updating clock: {str(e)}")

    # ----------------- MENU & SHORTCUTS -----------------

    def create_menu(self):
        """Create the main menu bar."""
        menubar = Menu(self.root)

        # File menu
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Help menu
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menubar)

    def bind_shortcuts(self):
        """Bind keyboard shortcuts."""
        self.root.bind("<Control-q>", lambda event: self.root.quit())
        self.root.bind("<F5>", lambda event: self.update_labels())

    def show_about(self):
        """Show 'About' message box."""
        messagebox.showinfo(
            "About",
            "Age Finder\nDeveloped by Prathmesh\n\nSelect your birth date to see your age."
        )

    # ----------------- TOOLTIPS -----------------

    def create_tooltips(self):
        """Attach tooltips to key widgets."""
        try:
            ToolTip(self.birth_calendar, "Select your date of birth here")
        except Exception as e:
            logging.warning(f"Failed to attach tooltip: {str(e)}")


# Application entry point
if __name__ == "__main__":
    try:
        root = Tk()
        app = AgeFinder(root)
        root.mainloop()
    except Exception as e:
        logging.critical(f"Application crashed: {str(e)}")
        messagebox.showerror("Critical Error", f"Application crashed: {str(e)}")
