# Rokto Dorkar

**Rokto Dorkar** is a web-based platform designed to manage blood donation needs. The platform connects blood donors with individuals in need of blood, making it easier for both parties to find and share life-saving blood. Built with **HTML**, **CSS**, **JavaScript**, and **Python Django**, the project aims to improve access to blood donation services.
<!-- 
## Demo

For a visual demonstration of **Rokto Dorkar**, you can check out our video demo here:

[Video Demo Link]
-->

## Features

### User Capabilities
## Features

- **Authentication**: Users can create accounts and log in to the platform.
- **Donor Search**: Users can search for available blood donors based on blood type, location, and other criteria. The search is location-based, helping users find nearby donors. The platform uses **OpenStreetMap API** to extract the user's and donor's **longitude** and **latitude**, and calculates the distance between them. If the distance is within **30 km**, the donor is considered available.
- **Donor Information**: Users can view the contact number of donors and see the location of the donor. 
 Donors also have profile pictures displayed along with their information.
- **Donation History**: Users can view when a donor last donated blood, ensuring transparency and tracking of donations.
- **Admin Panel**: Admins have the ability to manage users and monitor the entire platform.
- **Request and Donation Status**: Users can check the availability of donations, providing real-time updates.


## Technology Stack

- **Frontend**: Developed with **HTML**, **CSS**, and **JavaScript**.
- **Backend**: Built using **Python Django**.
- **Database**: **SQLite** is used to store data.
- **Authentication**: User authentication is handled by Django's built-in authentication system.

## Local Setup

To get **Rokto Dorkar** up and running on your local machine, follow these instructions:

### Prerequisites

Before setting up the project, make sure you have the following installed:
- **Python 3.x**: Required to run the backend.
- **pip**: Python package installer to install dependencies.
- **SQLite**: Comes pre-installed with Python for database management.
  
### Steps

1. **Clone the Repository**:
   
   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/AhsanulAnam-Saboj/Rokto-Dorkar.git
   cd Rokto-Dorkar

2. **Create and Activate a Virtual Environment**:

   It is recommended to use a virtual environment to manage project dependencies. To create and activate the virtual environment, follow these steps:

   - **On Windows**:
     1. Open your command prompt or terminal in the project's directory.
     2. Run the following command to create a virtual environment:

        ```bash
        python -m venv venv
        ```

     3. To activate the virtual environment, run:

        ```bash
        venv\Scripts\activate
        ```

   - **On macOS/Linux**:
     1. Open your terminal in the project's directory.
     2. Run the following command to create a virtual environment:

        ```bash
        python3 -m venv venv
        ```

     3. To activate the virtual environment, run:

        ```bash
        source venv/bin/activate
        ```

   After activating the virtual environment, your terminal should show the name of the virtual environment (e.g., `(venv)`), indicating that it is active.

   **Note**: If the virtual environment is active, all Python and pip commands will use the environment's packages instead of system-wide ones.
3. **Install Dependencies**:

   After activating the virtual environment, you need to install all the required dependencies for the project. To do this, run the following command in your terminal:

   ```bash
   pip install -r requirements.txt
4. **Database Setup**:

   **Rokto Dorkar** uses SQLite (or any other configured database) to store user data, blood donation requests, and more. To set up the database, you need to run the migrations that will create the necessary database tables.

   To apply the migrations, run the following command:

   ```bash
   python manage.py migrate

5. **Start the Development Server**:

   Once the dependencies are installed and the database is set up, you can start the development server to run the application locally. To start the server, use the following command:

   ```bash
   python manage.py runserver

## Support and Contact

If you encounter any issues or need assistance during setup or usage, feel free to reach out for help. Here are the options for support:

- **Email**: For more direct communication, you can contact me at: [Mail](mailto:ahsanulanamsaboj1999@gmail.com).
- **LinkedIn**: You can also connect with me on [LinkedIn](https://www.linkedin.com/in/ahsanulanam) for support or inquiries.

Your feedback and contributions are highly appreciated!

