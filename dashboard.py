import customtkinter as ctk
from tkinter import ttk, messagebox
import mysql.connector as mysql
from database import get_db_connection

class StudentDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Student Database Management System")
        
        window_width = 1100
        window_height = 650

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
       

        self.configure(fg_color="#A9B5DF")

        # --- Header Section ---
        self.header_frame = ctk.CTkFrame(self, height=100, corner_radius=0, fg_color="#87CEEB")
        self.header_frame.pack(fill="x", side="top")

        ctk.CTkLabel(self.header_frame, text="Students Database Management System", font=("Arial Bold", 32), text_color="black").pack(pady=(10, 0))
        ctk.CTkLabel(self.header_frame, text="L K R      UNIVERSITY", font=("Arial Bold", 24), text_color="black").pack()

        # --- Main Body Frame ---
        self.main_frame = ctk.CTkFrame(self, fg_color="#D1D8E0", corner_radius=20, border_width=2, border_color="white")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Left Side - Student Info Form
        self.info_frame = ctk.CTkFrame(self.main_frame, width=400, fg_color="transparent")
        self.info_frame.pack(side="left", fill="both", padx=20, pady=20)

        ctk.CTkLabel(self.info_frame, text="STUDENT INFO", font=("Arial Bold", 16), text_color="black").pack(anchor="w")
        
        self.entries = {}
        labels = [("Student Id:", "sid"), ("First Name:", "fname"), ("Surname:", "sname"), 
                  ("Date of Birth:", "dob"), ("Age:", "age"), ("Gender:", "gender"), 
                  ("Address:", "addr"), ("Mobile:", "mob")]
        
        for label_text, key in labels:
            row_frame = ctk.CTkFrame(self.info_frame, fg_color="transparent")
            row_frame.pack(fill="x", pady=5)
            ctk.CTkLabel(row_frame, text=label_text, width=120, anchor="w", text_color="black", font=("Arial Bold", 13)).pack(side="left")
            entry = ctk.CTkEntry(row_frame, width=220, fg_color="white", text_color="black")
            entry.pack(side="right", padx=5)
            self.entries[key] = entry

        # Right Side - Student Details Display
        self.details_frame = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=10)
        self.details_frame.pack(side="right", fill="both", expand=True, padx=20, pady=40)
        
        # Table (Treeview)
        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 11), rowheight=25)
        self.tree = ttk.Treeview(self.details_frame, columns=("ID", "FName", "SName", "Age", "Mob"), show="headings")
        self.tree.heading("ID", text="ID"); self.tree.heading("FName", text="First Name")
        self.tree.heading("SName", text="Surname"); self.tree.heading("Age", text="Age")
        self.tree.heading("Mob", text="Mobile")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        self.tree.bind("<ButtonRelease-1>", self.get_cursor)

        # --- Bottom Buttons ---
        self.button_frame = ctk.CTkFrame(self, height=70, fg_color="#87CEEB", corner_radius=0)
        self.button_frame.pack(fill="x", side="bottom")

        buttons = [("Add New", self.add_new), ("Display", self.display_data), ("Clear", self.clear_fields), 
                   ("Delete", self.delete_data), ("Search", self.search_data), ("Update", self.update_data), ("Exit", self.quit)]

        for text, cmd in buttons:
            ctk.CTkButton(self.button_frame, text=text, command=cmd, width=120, height=40, fg_color="white", 
                          text_color="black", hover_color="#D1D8E0", font=("Arial Bold", 14), 
                          border_width=1, border_color="gray").pack(side="left", padx=10, expand=True)

        self.display_data() 

    # --- Database Functions ---
    def add_new(self):
        data = {k: v.get().strip() for k, v in self.entries.items()}
        if not data['sid'] or not data['fname']:
            messagebox.showerror("Error", "Student ID and First Name are mandatory!")
            return
        
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO students VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, tuple(data.values()))
                conn.commit()
                messagebox.showinfo("Success", "Student added successfully!")
                self.display_data()
                self.clear_fields()
            except mysql.Error as e:
                messagebox.showerror("Error", f"Could not add record: {e}")
            finally:
                conn.close()

    def display_data(self):
        self.tree.delete(*self.tree.get_children())
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT student_id, first_name, surname, age, mobile FROM students")
                for row in cursor.fetchall():
                    self.tree.insert("", "end", values=row)
            except mysql.Error as e:
                print(f"Error fetching data: {e}")
            finally:
                conn.close()

    def clear_fields(self):
        for entry in self.entries.values():
            entry.delete(0, 'end')

    def get_cursor(self, ev):
        cursor_row = self.tree.focus()
        content = self.tree.item(cursor_row)
        row = content['values']
        if row:
            self.clear_fields()
            conn = get_db_connection()
            if conn:
                try:
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM students WHERE student_id=%s", (row[0],))
                    full_data = cursor.fetchone()
                    if full_data:
                       
                        keys = ['sid', 'fname', 'sname', 'dob', 'age', 'gender', 'addr', 'mob']
                        for i, key in enumerate(keys):
                            self.entries[key].insert(0, str(full_data[i]))
                finally:
                    conn.close()

    def delete_data(self):
        sid = self.entries['sid'].get().strip()
        if not sid:
            messagebox.showwarning("Warning", "Please select a student record to delete!")
            return
        if messagebox.askyesno("Confirm", f"Are you sure you want to delete ID: {sid}?"):
            conn = get_db_connection()
            if conn:
                try:
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM students WHERE student_id=%s", (sid,))
                    conn.commit()
                    messagebox.showinfo("Success", "Record deleted successfully!")
                    self.display_data()
                    self.clear_fields()
                finally:
                    conn.close()

    def update_data(self):
        sid = self.entries['sid'].get().strip()
        if not sid:
            messagebox.showwarning("Update", "Please select a record from the table to update!")
            return

        data = {k: v.get().strip() for k, v in self.entries.items()}
        if messagebox.askyesno("Confirm", "Do you want to update this record?"):
            conn = get_db_connection()
            if conn:
                try:
                    cursor = conn.cursor()
                    query = """UPDATE students SET 
                               first_name=%s, surname=%s, dob=%s, age=%s, 
                               gender=%s, address=%s, mobile=%s 
                               WHERE student_id=%s"""
                    params = (data['fname'], data['sname'], data['dob'], data['age'], 
                              data['gender'], data['addr'], data['mob'], sid)
                    cursor.execute(query, params)
                    conn.commit()
                    messagebox.showinfo("Success", "Record updated successfully!")
                    self.display_data()
                except mysql.Error as e:
                    messagebox.showerror("Error", f"Update failed: {e}")
                finally:
                    conn.close()

    def search_data(self):
        val = self.entries['sid'].get().strip()
        if not val:
            messagebox.showwarning("Search", "Enter Student ID or Name to search")
            self.display_data()
            return
        
        self.tree.delete(*self.tree.get_children())
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                
                query = "SELECT student_id, first_name, surname, age, mobile FROM students WHERE student_id=%s OR first_name LIKE %s"
                cursor.execute(query, (val, f"%{val}%"))
                rows = cursor.fetchall()
                if rows:
                    for row in rows:
                        self.tree.insert("", "end", values=row)
                else:
                    messagebox.showinfo("Not Found", "No results found.")
                    self.display_data()
            finally:
                conn.close()

if __name__ == "__main__":
    app = StudentDashboard()
    app.mainloop()