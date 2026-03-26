import customtkinter as ctk
from tkinter import messagebox
import mysql.connector as mysql 
from database import get_db_connection, setup_database



# --- GUI Application ---
class SignUpApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sign Up")
        
       
        window_width = 700
        window_height = 730
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
       

        self.configure(fg_color="#A9B5DF")

        # Main Glass Frame
        self.main_frame = ctk.CTkFrame(
            self, 
            width=650, 
            height=600, 
            corner_radius=40,
            fg_color="#D1D8E0",
            border_width=2,
            border_color="#FFFFFF"
        )
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Title
        self.title_label = ctk.CTkLabel(
            self.main_frame, text="Sign Up", 
            font=("Arial Bold", 32), text_color="#000000"
        )
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        # Input Row Helper Function
        def create_input_row(label_text, placeholder, y_pos):
            lbl = ctk.CTkLabel(
                self.main_frame, text=label_text, 
                font=("Arial Bold", 14), fg_color="#FFFFFF",
                corner_radius=8, width=200, height=45, text_color="#000000"
            )
            lbl.place(x=60, y=y_pos)
            
            entry = ctk.CTkEntry(
                self.main_frame, width=300, height=45, 
                placeholder_text=placeholder, corner_radius=8,
                fg_color="#F3F4F6", border_width=0, text_color="#000000"
            )
            entry.place(x=280, y=y_pos)
            return entry

        self.first_name_entry = create_input_row("First Name *", "Enter your first name", 150)
        self.last_name_entry = create_input_row("Last Name *", "Enter your last name", 215)
        self.email_entry = create_input_row("Email Address *", "name@example.com", 280)
        self.password_entry = create_input_row("Create Password *", "•••••••", 345)
        self.password_entry.configure(show="•")

        self.terms_check = ctk.CTkCheckBox(
            self.main_frame, text="I agree to the Terms & Conditions",
            font=("Arial", 12), text_color="#333", border_width=2
        )
        self.terms_check.place(x=60, y=410)

        self.signup_btn = ctk.CTkButton(
            self.main_frame, text="Sign Up", 
            command=self.register_user,
            width=160, height=50, corner_radius=10,
            fg_color="#1a73e8", hover_color="#1557b0",
            font=("Arial Bold", 16)
        )
        self.signup_btn.place(relx=0.5, rely=0.8, anchor="center")

        self.login_label = ctk.CTkLabel(
            self.main_frame, text="Already have an account?", 
            font=("Arial", 13), text_color="#333"
        )
        self.login_label.place(relx=0.45, rely=0.9, anchor="center")

       
        self.login_link = ctk.CTkButton(
            self.main_frame, text="Log In", 
            fg_color="transparent", hover=False, width=50,
            text_color="#1a73e8", font=("Arial Bold", 13),
            command=self.go_to_login
        )
        self.login_link.place(relx=0.62, rely=0.9, anchor="center")

    def register_user(self):
        f_name = self.first_name_entry.get()
        l_name = self.last_name_entry.get()
        email = self.email_entry.get()
        pwd = self.password_entry.get()

        if not all([f_name, l_name, email, pwd]):
            messagebox.showwarning("Empty fields", "please complete all information.")
            return
        
        if not self.terms_check.get():
            messagebox.showwarning("Terms", "Please agree to the terms and conditions.")
            return

        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (f_name, l_name, email, pwd))
                conn.commit()
                messagebox.showinfo("Success", "Account created successfully!")
                self.clear_fields()
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"An error occurred during registration: {e}")
            finally:
                conn.close()

    def clear_fields(self):
        self.first_name_entry.delete(0, 'end')
        self.last_name_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')

   
    def go_to_login(self):
        self.destroy() 
        try:
            import login 
            login_page = login.LoginApp()
            login_page.mainloop()
        except Exception as e:
            messagebox.showerror("Error", f"Unable to open the login page: {e}")

if __name__ == "__main__":
    setup_database()
    app = SignUpApp()
    app.mainloop()