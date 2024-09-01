# The Most Dangerous Writing App - Desktop Version

This is a Python-based desktop application inspired by the online app [The Most Dangerous Writing App](https://www.squibler.io/dangerous-writing-prompt-app). The desktop version provides a writing environment where your progress is erased if you stop typing for more than 5 seconds. This project utilizes the Tkinter library for the graphical user interface (GUI).

## Features

- **Light Blue Modern UI**: A clean and aesthetically pleasing interface with a light blue color theme.
- **Custom Timer**: A countdown timer that deletes all text if the user stops typing for more than 5 seconds.
- **Interactive Controls**: "Start Writing" button to initiate the countdown and "Try Again" button for resetting the session after the text is deleted.
- **Responsive Text Box**: A text widget where the user can type, styled with a modern font and color scheme.

## Preview

![App Preview]()

## Installation

### Prerequisites

- Python 3.x
- Tkinter (usually comes pre-installed with Python on most platforms)

### Cloning the Repository

To clone the repository, run the following command in your terminal:

\```bash
git clone https://github.com/yourusername/the-most-dangerous-writing-app-desktop.git
\```

### Running the Application

Navigate to the project directory and run the `main.py` file:

\```bash
cd the-most-dangerous-writing-app-desktop
python main.py
\```

This will open the application window, where you can start using the writing app.

## Usage

1. **Start Writing**: Click the "Start Writing" button to begin. The text box will be activated, and the countdown timer will start.
2. **Type Continuously**: Keep typing to prevent the countdown from reaching zero. If you stop typing for more than 5 seconds, all your text will be deleted.
3. **Try Again**: If your text is deleted, you can press the "Try Again" button to restart the session.

## Customization

### Changing the Timer Interval

The default timer interval is set to 5 seconds. You can adjust this by modifying the `self.timer_interval` variable in the `DangerousWritingApp` class:

\```python
self.timer_interval = 5  # Change this value to set a different interval
\```

### Modifying the UI Theme

The application uses a light blue color theme. You can customize colors and fonts by adjusting the relevant attributes in the code, such as `bg`, `fg`, and `font` in the Tkinter widgets.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgments

- Inspired by [The Most Dangerous Writing App](https://www.squibler.io/dangerous-writing-prompt-app)
- UI design inspired by modern application interfaces

