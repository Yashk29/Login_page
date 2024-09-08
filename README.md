# Login Verification System

This project is an **initial version** of a login verification system built using HTML, inline CSS, and Flask. It includes essential pages like index, home, sign-up, and login, with a Flask backend handling user authentication and login verification.

## Features

- **User Registration**: Allows users to sign up with basic credentials.
- **Login Authentication**: Validates user login and grants access to restricted pages.
- **Home Page Access**: Only authenticated users can view the home page.
- **Flask Backend**: Manages user sessions and authentication flow.
- **HTML & Inline CSS**: Provides a simple interface for user interaction.

## Pages Included

1. **Index Page**: The landing page of the application.
2. **Home Page**: Accessible only after successful login.
3. **Sign-up Page**: Allows users to create a new account.
4. **Login Page**: Authenticates users and grants access to the home page.

## Libraries and Tools Used

- **HTML**: Provides structure for web pages.
- **Inline CSS**: Styles the web pages directly within the HTML.
- **Flask**: Python-based framework for managing backend routes and login verification.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-repo
   ```

3. Install Flask if you haven't already:

   ```bash
   pip install flask
   ```

4. Run the Flask application:

   ```bash
   python app.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000` to access the system.

## Project Structure

- **index.html**: Landing page with links to sign up or log in.
- **home.html**: The protected page that users access after login.
- **signup.html**: Page where new users can register.
- **login.html**: Page for users to log in and verify their credentials.
- **app.py**: Backend file managing user sessions and authentication with Flask.

## Future Features to be Added

- **Password Encryption**: Adding encryption for secure storage of user credentials.
- **Password Reset Feature**: Implementing a system for users to reset their passwords.
- **Enhanced UI/UX**: Improving the design of the pages for a more modern look.
- **Database Integration**: Currently using in-memory data, but future versions will integrate a database like SQLite or MySQL.
- **Session Management**: Enhancing session handling for more secure login/logout flows.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
