import tkinter as tk
from tkinter import PhotoImage, messagebox

class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Most Dangerous Writing App")
        self.root.geometry("600x500")
        self.root.config(bg="#E3F2FD")  # Light blue background color

        # Title Label
        self.title_label = tk.Label(self.root, text="The Most Dangerous Writing App", font=("Helvetica", 24, "bold"), bg="#E3F2FD", fg="#0D47A1")
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        # Create a frame to hold the text widget
        self.text_frame = tk.Frame(self.root, bg="#FFFFFF", bd=2, relief="solid")
        self.text_frame.place(relx=0.5, rely=0.4, anchor="center", width=500, height=200)

        # Create the text widget for typing
        self.text_widget = tk.Text(self.text_frame, wrap="word", font=("Helvetica", 14), bg="#E3F2FD", fg="#0D47A1", bd=0, padx=10, pady=10)
        self.text_widget.pack(expand=True, fill='both')
        self.text_widget.config(state=tk.DISABLED)  # Disable typing until the user clicks 'Start Writing'

        # Initialize timer and timer interval
        self.timer_interval = 5  # 5 seconds
        self.time_left = self.timer_interval

        # Visual timer label
        self.timer_label = tk.Label(self.root, text="", font=("Helvetica", 14, "bold"), fg="#D32F2F", bg="#E3F2FD")
        self.timer_label.place(relx=0.5, rely=0.9, anchor="center")

        # Start Writing button
        self.start_button = tk.Button(self.root, text="Start Writing", font=("Helvetica", 14, "bold"), bg="#1976D2", fg="#FFFFFF", activebackground="#1565C0", activeforeground="#FFFFFF", bd=0, padx=20, pady=10, command=self.start_writing, cursor="hand2")
        self.start_button.place(relx=0.5, rely=0.7, anchor="center")

        # Try Again button (initially hidden)
        self.try_again_button = tk.Button(self.root, text="Try Again", font=("Helvetica", 14, "bold"), bg="#1976D2", fg="#FFFFFF", activebackground="#1565C0", activeforeground="#FFFFFF", bd=0, padx=20, pady=10, command=self.try_again, cursor="hand2")
        self.try_again_button.place(relx=0.5, rely=0.7, anchor="center")
        self.try_again_button.place_forget()

    def start_writing(self):
        self.start_button.place_forget()  # Hide the start button
        self.text_widget.config(state=tk.NORMAL)  # Enable the text widget for typing
        self.text_widget.bind('<KeyRelease>', self.reset_timer)
        self.update_timer_label()  # Start the timer

    def reset_timer(self, event=None):
        self.time_left = self.timer_interval  # Reset time left to the full interval

    def update_timer_label(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"Time Left: {self.time_left} seconds")
            self.time_left -= 1
            self.root.after(1000, self.update_timer_label)
        else:
            self.clear_text()

    def clear_text(self):
        self.text_widget.delete(1.0, tk.END)  # Clear all text in the widget
        self.text_widget.config(state=tk.DISABLED)  # Disable typing
        messagebox.showwarning("Text Deleted", "You stopped typing! Your work has been deleted.")
        self.timer_label.config(text="")  # Clear timer label
        self.try_again_button.place(relx=0.5, rely=0.7, anchor="center")  # Show the Try Again button

    def try_again(self):
        self.try_again_button.place_forget()  # Hide the try again button
        self.text_widget.config(state=tk.NORMAL)  # Enable the text widget for typing
        self.time_left = self.timer_interval  # Reset timer
        self.update_timer_label()  # Restart timer loop

    def run(self):
        self.root.mainloop()  # Run the main loop of the application

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWritingApp(root)
    app.run()
