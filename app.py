# step -1: importing modules
from flask import Flask, render_template
import sqlite3


# step -2: app creation & DB configuration
app = Flask(__name__)
db_Name = "hospital.db"




# step -3: DB initialization & schema creation
def init_db():
    conn = sqlite3.connect(db_Name)
    cursor = conn.cursor()


    # Create 'users' table with constraints and default values
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        UID INTEGER PRIMARY KEY AUTOINCREMENT,
        UNAME TEXT NOT NULL,
        Email TEXT CHECK(Email LIKE '%@gmail.com'),
        Phone TEXT NOT NULL,
        Role TEXT DEFAULT 'demo_user',
        Specialization TEXT DEFAULT 'NA',
        Experience INTEGER DEFAULT 2,
        Salary REAL DEFAULT 5000
    );
    """)


    # Data seeding into 'users' table if it is empty
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        # Array of user records featuring diverse roles (Surgeons, General Doctors, Compounders, Maintenance Staff)
        seed_users = [
            # Surgeon Doctors
            (
                "Dhanush",
                "DH@gmail.com",
                "8901239016",
                "surgeon doctor",
                "Cardio & Neuro",
                12,
                150000,
            ),
            (
                "Lingaran",
                "LM@gmail.com",
                "8901239023",
                "surgeon doctor",
                "Gynecologist & Orthopedic",
                10,
                135000,
            ),
            (
                "Suresh",
                "SH@gmail.com",
                "8912349016",
                "surgeon doctor",
                "Cardio & Neuro",
                8,
                120000,
            ),
            # General Doctors
            (
                "Dr. Ramesh",
                "ramesh.doc@gmail.com",
                "9876543210",
                "general doctor",
                "General Medicine",
                6,
                85000,
            ),
            (
                "Dr. Anitha",
                "anitha.med@gmail.com",
                "9876543211",
                "general doctor",
                "Pediatrics",
                5,
                80000,
            ),
            # Therapists
            (
                "Chiranjeevi",
                "MStar@gmail.com",
                "8901239123",
                "Therapist",
                "Psychiatrist",
                15,
                95000,
            ),
            # Compounders
            (
                "Rajesh Kumar",
                "rajesh.c@gmail.com",
                "9123456780",
                "compounder",
                "Pharmacy & Doses",
                4,
                30000,
            ),
            (
                "Sunitha Rao",
                "sunitha.comp@gmail.com",
                "9123456781",
                "compounder",
                "First Aid & Dressing",
                3,
                28000,
            ),
            # Maintenance Staff
            (
                "Venkatesh",
                "venky.maint@gmail.com",
                "9000111222",
                "maintainerStaff",
                "Sanitation & Hygiene",
                5,
                22000,
            ),
            (
                "Kalyan",
                "kalyan.maint@gmail.com",
                "9000111223",
                "maintainerStaff",
                "Equipment Maintenance",
                7,
                25000,
            ),
        ]


        # Parameterized insertion to safely add records without SQL syntax errors
        cursor.executemany(
            """
            INSERT INTO users(uname, email, phone, role, Specialization, Experience, Salary)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
            seed_users,
        )


        conn.commit()


    conn.close()




# step -4: routing
@app.route("/dashboard")
def dashboard():
    conn = sqlite3.connect(db_Name)
    cursor = conn.cursor()


    # Fetch all records from the 'users' table
    cursor.execute("""
        SELECT * FROM users;
    """)
    dataRecord = cursor.fetchall()
    conn.close()


    # Render dashboard.html and pass users dataset
    return render_template("dashboard.html", users=dataRecord)




# step -5: run & debug
if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=3000)





