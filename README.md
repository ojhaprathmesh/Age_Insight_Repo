# Age Insight Application

## Overview
The **Age Insight** application is a lightweight Tkinter-based GUI tool that calculates and displays the age difference between a selected birth date and the current date. Users intuitively select their birth date using an interactive calendar widget (defaulting to January 1, 2000), and the application instantly displays their age broken down into days, months, and years. A real-time clock synchronized to Asia/Kolkata timezone (IST) is displayed at the bottom of the interface.

## Key Features
- **Interactive Calendar Widget:**  
  Intuitive calendar interface for easy birth date selection with immediate visual feedback.

- **Real-Time Clock Display:**  
  Live clock showing current time in Asia/Kolkata timezone (IST), updating every 500ms using the `pytz` library for accurate timezone handling.

- **Precise Age Calculation:**  
  Automatically calculates age breakdown into days, months, and years based on the selected birth date and current date.

- **Dynamic UI Updates:**  
  All display labels refresh in real-time as dates are selected, providing instant feedback to the user.

- **Keyboard Shortcuts:**  
  - `Ctrl+Q` – Quick exit
  - `F5` – Refresh age calculation

- **Application Logging:**  
  Comprehensive logging system (`age_finder.log`) tracks application initialization, errors, and warnings at INFO level for debugging and monitoring.

- **Custom Styling:**  
  Professional UI with configurable theme settings (white background, black text, Times New Roman font, blue accents) and 4px ridged borders for visual separation.

## Repository Structure
```
Age_Insight_Repo/
├── age_finder.py       # Main application file with AgeFinder class
├── timer.png           # Icon image for the application window
├── age_icon.ico        # Possible icon
├── requirements.txt    # Python dependencies
├── README.md           # This file
├── LICENSE             # License information
└── age_finder.log      # Application log file (auto-generated)
```

## Dependencies
- **Python 3.x**
- **Tkinter** (included with Python)
- **tkcalendar** (v1.6.1) – Calendar widget for date selection
- **pytz** (v2025.2) – Timezone handling
- **Babel** (v2.17.0) – Internationalization support

All exact versions are documented in `requirements.txt`.

## Installation & Setup

### Prerequisites
- Python 3.x installed on your system
- pip package manager

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/ojhaprathmesh/Age_Insight_Repo.git
   cd Age_Insight_Repo
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:

   **Windows:**

   ```bash
   .venv\Scripts\Activate.ps1
   ```

   **macOS / Linux:**

   ```bash
   source .venv/bin/activate
   ```

4. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Launch the application:

   ```bash
   python age_finder.py
   ```

## Usage Guide
1. Launch the application using `python age_finder.py`
2. The GUI window opens with a calendar on the left and date/age display on the right
3. Click on a date in the calendar to select your birth date
4. The application automatically:
   - Updates the birth date display
   - Calculates your current age (in days, months, years)
   - Shows the current date for reference
5. A live clock displays at the bottom, showing current time in IST
6. Use keyboard shortcuts for quick actions:
   - Press `F5` to manually refresh calculations
   - Press `Ctrl+Q` to exit the application

## Code Architecture

### Main Class: `AgeFinder`
The application is built around a single `AgeFinder` class that manages all UI and logic. Key components:

#### Configuration
- **Theme Settings:** White background, black text, Times New Roman font, blue accent color
- **Timezone:** Fixed to 'Asia/Kolkata' (IST) for all time-related operations
- **Window Size:** Fixed at 800x500 pixels, non-resizable
- **Icon:** Loads `timer.png` as window icon (with fallback if not found)

#### UI Layout (4-Section Design)
The window is divided into 4 main frames using relative positioning:

1. **Calendar Frame** (62.5% width, full height)
   - Interactive tkcalendar widget with day selection mode
   - Default date: January 1, 2000
   - Date format: `ddmmyyyy`
   - Triggers age calculation on selection

2. **Date Display Frame** (37.5% width, 50% height)
   - Shows "Birth Date" and "Current Date"
   - Each with Day/Month/Year sub-sections
   - Displays selected dates from calendar

3. **Age Display Frame** (37.5% width, 33.3% height)
   - Shows calculated age as "Day(s)", "Month(s)", "Year(s)"
   - Uses simplified 30-day month approximation

4. **Time Frame** (37.5% width, 16.7% height)
   - Large 36pt bold clock display
   - Updates every 500ms with IST timezone

#### Key Methods

**UI Initialization:**
- `initialize_ui()` – Sets up 4-frame layout, calendar, labels, and initial displays
- `create_frame()` – Factory method for creating frames with standard 4px ridged borders
- `setup_labels()` – Populates date and age display sections with label frames
- `create_date_labels()` – Creates Day/Month/Year label frames
- `create_age_labels()` – Creates Day(s)/Month(s)/Year(s) display frames
- `create_label()` – Creates section title labels
- `create_label_frame()` – Creates bordered frames for data display
- `setup_time_label()` – Creates the clock label

**Date Processing:**
- `get_dates()` – Retrieves calendar-selected birth date and current system date
- `process_dates()` – Parses dates (ddmmyyyy format) and calculates age difference:
  - Age in years: `age_delta.days // 365`
  - Age in months: `(age_delta.days % 365) // 30`
  - Age in days: `age_delta.days % 30`
- `update_labels()` – Orchestrates date retrieval, processing, and UI refresh
- `display_label_data()` – Updates label frames with calculated values

**Clock Management:**
- `update_clock()` – Updates time display every 500ms using `pytz.timezone('Asia/Kolkata')`
- Uses recursive `after()` callback for continuous updates

**Menu & Shortcuts:**
- `create_menu()` – Creates menu bar with File (Exit) and Help (About) menus
- `bind_shortcuts()` – Binds `Ctrl+Q` (exit) and `F5` (refresh)
- `show_about()` – Displays about dialog with application info

#### Error Handling & Logging
- **Logging Level:** INFO
- **Log File:** `./age_finder.log`
- **Format:** `%(asctime)s - %(levelname)s - %(message)s`
- **Events Logged:**
  - UI initialization success
  - Icon loading failures (warnings)
  - UI errors with detailed messages
  - Clock update errors
  - Critical application crashes

#### Entry Point
- Standard Python entry point: `if __name__ == "__main__"`
- Creates Tk root window and AgeFinder instance
- Catches critical exceptions with error dialogs

## Developer
**Prathmesh Ojha**

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes with clear commit messages
4. Submit a pull request with a description of your changes

Feel free to open issues for:
- Bug reports
- Feature requests
- General feedback or suggestions
- Documentation improvements

## License
See the `LICENSE` file for license information.

---

**Happy Age Finding! 🎉**
