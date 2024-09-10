# Age Insight Application

## Overview:
The Age Insight application allows users to calculate and display the age difference between two selected dates: the birth date and the current date. The user interacts with the application through an intuitive graphical user interface (GUI).

## Key Features:
- **User-Friendly Interface:**  
  The GUI provides a visually appealing and user-friendly design. Calendar widgets are used for easy date selection.

- **Real-Time Clock:**  
  The application displays the current time in real-time, updating every half second. The clock is implemented using the `pytz` library to account for time zones, with the default set to 'Asia/Kolkata'.

- **Date Processing:**  
  The application processes the selected birth and current dates to calculate the age in terms of days, months, and years.

- **Dynamic Label Updates:**  
  Labels dynamically update to show the selected birth and current dates, as well as the calculated age in days, months, and years.

## Repository Structure:
- **main.py:** Contains the main script for the Age Insight application.
- **README.md:** Provides documentation and instructions for using the application.
- **requirements.txt:** Lists the required Python packages for easy setup.

## Usage Instructions:
1. Clone the repository to your local machine.
2. Install the required dependencies using:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the `main.py` script to launch the Age Insight application.
4. Upon running the application, a GUI window will appear with the Age Insight interface.
5. Use the calendar widget to select the birth date by clicking on the desired date.
6. The current date is automatically set to the current date and time.
7. The application will dynamically display the selected birth and current dates, as well as the calculated age in days, months, and years.
8. The real-time clock at the bottom of the window continuously updates.

## Dependencies:
- Python 3.x
- Tkinter
- tkcalendar
- pytz

Exact version details mentioned in `requirements.txt` file.

## Developer:
Prathmesh Ojha

## Contributions:
Contributions to enhance or extend the functionality of the Age Insight application are welcome. Please fork the repository, make your changes, and submit a pull request.  
Feel free to open issues for bug reports, feature requests, or general feedback.

Happy Age Finding! 🎉
