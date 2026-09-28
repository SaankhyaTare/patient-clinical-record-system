import sqlite3


def create_report():
    patient_id = input("Enter Patient ID: ").strip().upper()

    if patient_id.startswith("P"):
        patient_id = patient_id[1:]

    if not patient_id.isdigit():
        print("Invalid Patient ID.")
        return

    patient_id = int(patient_id)

    connection = sqlite3.connect("patients.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM patients WHERE id = ?",
        (patient_id,)
    )

    patient = cursor.fetchone()

    if patient is None:
        print("Patient not found.")
        connection.close()
        return

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

    filename = f"patient_P{patient_id:04d}_report.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("PATIENT CLINICAL REPORT\n")
        file.write("=" * 35 + "\n\n")

        file.write("Patient ID: P" + str(patient[0]).zfill(4) + "\n")
        file.write("Name: " + patient[1] + "\n")
        file.write("Age: " + str(patient[2]) + "\n")
        file.write("Gender: " + patient[3] + "\n")
        file.write("Phone: " + patient[4] + "\n")

        file.write("\nMEDICAL HISTORY\n")
        file.write("=" * 35 + "\n")

        if len(records) == 0:
            file.write("No medical records found.\n")
        else:
            for number, record in enumerate(records, start=1):
                file.write("\nVisit " + str(number) + "\n")
                file.write("Date: " + str(record[0]) + "\n")
                file.write("Symptoms: " + str(record[1]) + "\n")
                file.write("Observations: " + str(record[2]) + "\n")
                file.write("Notes: " + str(record[3]) + "\n")

    print("Report created:", filename)