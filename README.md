This repository contains the source code for an Age Finder GUI application developed in Python using the Tkinter library for the user interface and the tkcalendar library for date picking functionality.

Overview:
    The Age Finder application allows users to calculate and display the age difference between two selected dates: the birth date and the current date. The user interacts with the application through an intuitive graphical user interface (GUI).

Key Features:

    - User-Friendly Interface:
        The GUI provides a visually appealing and user-friendly design.
        Calendar widgets are used for easy date selection.
        
    - Real-Time Clock:
        The application displays the current time in real-time, updating every half second.
        The clock is implemented using the pytz library to account for time zones, with the default set to 'Asia/Kolkata'.
    
    - Date Processing:
        The application processes the selected birth and current dates to calculate the age in terms of days, months, and years.
    
    - Dynamic Label Updates:
        Labels dynamically update to show the selected birth and current dates, as well as the calculated age in days, months, and years.

Repository Structure:

    - main.py: Contains the main script for the Age Finder application.
    - README.md: Provides documentation and instructions for using the application.
    - requirements.txt: Lists the required Python packages for easy setup.

Usage Instructions:

    - Clone the repository to your local machine.
    - Install the required dependencies using pip install -r requirements.txt.
    - Run the Age_Finder_GUI.py script to launch the Age Finder application.
    - Upon running the application, a GUI window will appear with the Age Finder interface.
    - Use the calendar widget to select the birth date by clicking on the desired date.
    - The current date is automatically set to the current date and time.
    - The application will dynamically display the selected birth and current dates, as well as the calculated age in days, months, and years.
    - The real-time clock at the bottom of the window continuously updates.

Dependencies:

    - Python 3.x
    - Tkinter
    - tkcalendar
    - pytz
    
Exact version details mentioned in "requirements.txt" file.

Developer:
    Prathmesh Ojha

Contributions:
    Contributions to enhance or extend the functionality of the Age Finder application are welcome. Please fork the repository, make your changes, and submit a pull request.
    Feel free to open issues for bug reports, feature requests, or general feedback.

Happy Age Finding! 🎉
