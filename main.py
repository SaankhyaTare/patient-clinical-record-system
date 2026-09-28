from database import get_connection, create_tables
from validation import (
    valid_name,
    valid_age,
    valid_gender,
    valid_phone
)
from reference import find_matches
from reports import create_report

from datetime import datetime


create_tables()


def add_patient():
    print("\n--- Add Patient ---")

    name = input("Enter name: ").strip()

    if not valid_name(name):
        print("Name cannot be empty.")
        return

    age = input("Enter age: ").strip()

    if not valid_age(age):
        print("Invalid age.")
        return

    gender = input("Enter gender: ").strip()

    if not valid_gender(gender):
        print("Please enter Male, Female or Other.")
        return

    phone = input("Enter phone number: ").strip()

    if not valid_phone(phone):
        print("Invalid phone number.")
        return

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO patients (name, age, gender, phone)
        VALUES (?, ?, ?, ?)
        """,
        (name, int(age), gender, phone)
    )

    connection.commit()

    patient_id = cursor.lastrowid

    connection.close()

    print("\nPatient added successfully.")
    print("Patient ID: P" + str(patient_id).zfill(4))


def view_patients():
    print("\n--- All Patients ---")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()

    connection.close()

    if len(patients) == 0:
        print("No patients found.")
        return

    for patient in patients:
        print(
            "P" + str(patient[0]).zfill(4),
            "|", patient[1],
            "| Age:", patient[2],
            "|", patient[3],
            "|", patient[4]
        )


def search_patient():
    print("\n--- Search Patient ---")

    value = input("Enter Patient ID or name: ").strip()

    connection = get_connection()
    cursor = connection.cursor()

    if value.upper().startswith("P"):
        value = value[1:]

    if value.isdigit():
        cursor.execute(
            "SELECT * FROM patients WHERE id = ?",
            (int(value),)
        )
    else:
        cursor.execute(
            "SELECT * FROM patients WHERE name LIKE ?",
            ("%" + value + "%",)
        )

    patients = cursor.fetchall()

    connection.close()

    if len(patients) == 0:
        print("Patient not found.")
        return

    for patient in patients:
        print("\nPatient ID:", "P" + str(patient[0]).zfill(4))
        print("Name:", patient[1])
        print("Age:", patient[2])
        print("Gender:", patient[3])
        print("Phone:", patient[4])


def add_medical_record():
    print("\n--- Add Medical Record ---")

    patient_id = input("Enter Patient ID: ").strip().upper()

    if patient_id.startswith("P"):
        patient_id = patient_id[1:]

    if not patient_id.isdigit():
        print("Invalid Patient ID.")
        return

    patient_id = int(patient_id)

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT name FROM patients WHERE id = ?",
        (patient_id,)
    )

    patient = cursor.fetchone()

    if patient is None:
        print("Patient not found.")
        connection.close()
        return

    print("Patient:", patient[0])

    symptoms = input("Enter symptoms: ").strip()

    if symptoms == "":
        print("Symptoms cannot be empty.")
        connection.close()
        return

    observations = input("Enter observations: ").strip()
    notes = input("Enter notes: ").strip()

    date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute(
        """
        INSERT INTO medical_records
        (patient_id, date, symptoms, observations, notes)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            patient_id,
            date,
            symptoms,
            observations,
            notes
        )
    )

    connection.commit()
    connection.close()

    print("Medical record added successfully.")


def view_medical_history():
    print("\n--- Medical History ---")

    patient_id = input("Enter Patient ID: ").strip().upper()

    if patient_id.startswith("P"):
        patient_id = patient_id[1:]

    if not patient_id.isdigit():
        print("Invalid Patient ID.")
        return

    patient_id = int(patient_id)

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT name FROM patients WHERE id = ?",
        (patient_id,)
    )

    patient = cursor.fetchone()

    if patient is None:
        print("Patient not found.")
        connection.close()
        return

    print("\nPatient:", patient[0])
    print("Patient ID:", "P" + str(patient_id).zfill(4))

    cursor.execute(
        """
        SELECT date, symptoms, observations, notes
        FROM medical_records
        WHERE patient_id = ?
        """,
        (patient_id,)
    )

    records = cursor.fetchall()

    connection.close()

    if len(records) == 0:
        print("No medical records found.")
        return

    for number, record in enumerate(records, start=1):
        print("\nVisit", number)
        print("Date:", record[0])
        print("Symptoms:", record[1])
        print("Observations:", record[2])
        print("Notes:", record[3])


def clinical_reference():
    print("\n--- Clinical Reference ---")

    symptoms = input(
        "Enter symptoms separated by commas: "
    ).strip()

    matches = find_matches(symptoms)

    if len(matches) == 0:
        print("No reference matches found.")
        return

    for match in matches:
        print("\nCondition:", match["condition"])
        print("Matched symptoms:", ", ".join(match["matched"]))
        print("Reference match:", match["percentage"], "%")
        print("Description:", match["description"])
        print(
            "Reference medicines:",
            ", ".join(match["medicines"])
        )

    print("\nThis information is for reference only.")
    print("It is not a medical diagnosis or prescription.")


def dashboard():
    print("\n--- Dashboard ---")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM patients")
    patients = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM medical_records")
    records = cursor.fetchone()[0]

    connection.close()

    print("Total patients:", patients)
    print("Total medical records:", records)


def main():
    while True:
        print("\n==============================")
        print("PATIENT CLINICAL SYSTEM")
        print("==============================")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Add Medical Record")
        print("5. View Medical History")
        print("6. Clinical Reference")
        print("7. Generate Patient Report")
        print("8. Dashboard")
        print("9. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_patient()

        elif choice == "2":
            view_patients()

        elif choice == "3":
            search_patient()

        elif choice == "4":
            add_medical_record()

        elif choice == "5":
            view_medical_history()

        elif choice == "6":
            clinical_reference()

        elif choice == "7":
            create_report()

        elif choice == "8":
            dashboard()

        elif choice == "9":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()