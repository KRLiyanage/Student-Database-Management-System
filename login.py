import customtkinter as ctk
from tkinter import messagebox
import mysql.connector as mysql
from database import get_db_connection, setup_database

# --- GUI Application ---
class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Log In - K L University")
        
        window_width = 580
        window_height = 600

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
       

        self.configure(fg_color="#A9B5DF") 

        # Main Glass Frame
        self.main_frame = ctk.CTkFrame(
            self, 
            width=450, 
            height=500, 
            corner_radius=40,
            fg_color="#D1D8E0",
            border_width=2,
            border_color="#FFFFFF"
        )
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Title
        self.title_label = ctk.CTkLabel(
            self.main_frame, 
            text="Log In", 
            font=("Arial Bold", 32), 
            text_color="#000000"
        )
        self.title_label.place(relx=0.5, rely=0.15, anchor="center")

        # Label:    Email
        self.lbl_user = ctk.CTkLabel(
            self.main_frame, 
            text="Email Address", 
            font=("Arial", 14, "bold"), 
            text_color="#3498db"
        )
        self.lbl_user.place(x=65, y=145)

        # Email Input
        self.email_entry = ctk.CTkEntry(
            self.main_frame, 
            width=330, 
            height=45, 
            placeholder_text="Email Address",
            fg_color="#FFFFFF",
            text_color="#000000",
            border_width=0,
            corner_radius=8
        )
        self.email_entry.place(relx=0.5, rely=0.4, anchor="center")

        self.lbl_user = ctk.CTkLabel(
            self.main_frame, 
            text="Password ", 
            font=("Arial", 14, "bold"), 
            text_color="#3498db"
        )
        self.lbl_user.place(x=65, y=225)
        
        # Password Input
        self.password_entry = ctk.CTkEntry(
            self.main_frame, 
            width=330, 
            height=45, 
            placeholder_text="Password",
            show="•",
            fg_color="#FFFFFF",
            text_color="#000000",
            border_width=0,
            corner_radius=8
        )
        self.password_entry.place(relx=0.5, rely=0.55, anchor="center")

        # Login Button
        self.login_btn = ctk.CTkButton(
            self.main_frame, 
            text="Log In", 
            command=self.login_action,
            width=160, 
            height=50, 
            corner_radius=10,
            fg_color="#1a73e8", 
            hover_color="#1557b0", 
            font=("Arial Bold", 16)
        )
        self.login_btn.place(relx=0.5, rely=0.75, anchor="center")

        # Sign Up Link
        self.signup_label = ctk.CTkLabel(self.main_frame, text="Don't have an account?", font=("Arial", 13), text_color="#333")
        self.signup_label.place(relx=0.45, rely=0.9, anchor="center")

        self.signup_btn = ctk.CTkButton(
            self.main_frame, text="Sign Up", fg_color="transparent", hover=False, 
            text_color="#1a73e8", width=50, font=("Arial Bold", 13),
            command=self.open_signup 
        )
        self.signup_btn.place(relx=0.65, rely=0.9, anchor="center")

    def login_action(self):
        email_val = self.email_entry.get().strip()
        password_val = self.password_entry.get().strip()

        if not email_val or not password_val:
            messagebox.showwarning("Input Error", "Please enter your email and password.")
            return

        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
              
                query = "SELECT * FROM users WHERE email=%s AND password=%s"
                cursor.execute(query, (email_val, password_val))
                user = cursor.fetchone()

                if user:
                    messagebox.showinfo("Success", f"Successfully logged in! Welcome {user[1]}.")
                    
                   
                    self.destroy() 
                    self.open_dashboard()
                else:
                    messagebox.showerror("Error", "Incorrect email or password.")
                
                cursor.close()
                conn.close()
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}")

    def open_dashboard(self):
        try:
          
            import dashboard 
            app = dashboard.StudentDashboard() 
            app.mainloop()
        except Exception as e:
            messagebox.showerror("Error", f"Unable to open the dashboard: {e}")

    def open_signup(self):
        try:
            self.destroy()
            import sinig 
            app = sinig.SignUpApp() 
            app.mainloop()
        except Exception as e:
            messagebox.showerror("Error", f"Unable to open the Sign Up page: {e}")

if __name__ == "__main__":
    setup_database() 
    app = LoginApp()
    app.mainloop()