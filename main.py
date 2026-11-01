
# ==========================================
# VACCINATION TRACKER SYSTEM
# PROG211 - OBJECT ORIENTED PROGRAMMING
# ==========================================


# Fixed list of supported vaccines
SUPPORTED_VACCINES = (
    ("Measles", 2),
    ("Polio", 4),
    ("COVID-19", 2),
    ("Yellow Fever", 1)
)


# ==========================================
# CLASS 1: VACCINE
# ==========================================

class Vaccine:

    def __init__(self, name, required_doses):
        self.name = name
        self.required_doses = required_doses

    # Instance method
    def display_info(self):
        print("Vaccine:", self.name)
        print("Required doses:", self.required_doses)

    # Static method
    @staticmethod
    def is_valid_dose_number(dose_number, required_doses):
        return (
            isinstance(dose_number, int)
            and 1 <= dose_number <= required_doses
        )

    # Class method
    @classmethod
    def from_supported_list(cls, vaccine_name):
        for name, doses in SUPPORTED_VACCINES:
            if name.lower() == vaccine_name.lower():
                return cls(name, doses)

        return None


# ==========================================
# CLASS 2: PATIENT
# ==========================================

class Patient:

    total_patients = 0

    def __init__(self, patient_id, age_group, district):

        if not self.is_valid_age_group(age_group):
            raise ValueError("Invalid age group.")

        if not isinstance(district, str) or not district.strip():
            raise ValueError("District cannot be empty.")

        self.patient_id = patient_id
        self.age_group = age_group
        self.district = district

        # Dictionary for storing vaccination records
        self.vaccinations = {}

        Patient.total_patients += 1

    # Instance method
    def record_vaccination(self, vaccine, dose_number, date):

        if not isinstance(vaccine, Vaccine):
            print("Error: Invalid vaccine.")
            return

        if not Vaccine.is_valid_dose_number(
            dose_number, vaccine.required_doses
        ):
            print("Error: Invalid dose number.")
            return

        if vaccine.name not in self.vaccinations:
            self.vaccinations[vaccine.name] = {}

        if dose_number in self.vaccinations[vaccine.name]:
            print("This dose has already been recorded.")
            return

        self.vaccinations[vaccine.name][dose_number] = date

        print(
            "Vaccination recorded:",
            vaccine.name,
            "- Dose",
            dose_number
        )

    # Instance method
    def is_fully_vaccinated(self, vaccine):

        recorded_doses = self.vaccinations.get(vaccine.name, {})

        return len(recorded_doses) >= vaccine.required_doses

    # Instance method
    def display_info(self):

        print("\nPatient ID:", self.patient_id)
        print("Age Group:", self.age_group)
        print("District:", self.district)

        print("Vaccination Records:")

        if not self.vaccinations:
            print("No vaccination records found.")

        else:
            for vaccine_name, doses in self.vaccinations.items():

                for dose_number, date in doses.items():
                    print(
                        vaccine_name,
                        "- Dose",
                        dose_number,
                        "- Date:",
                        date
                    )

    # Class method
    @classmethod
    def get_total_patients(cls):
        return cls.total_patients

    # Class method
    @classmethod
    def from_string(cls, patient_details):

        details = patient_details.split(",", 2)

        if len(details) != 3:
            raise ValueError(
                "Enter patient details as ID, age group, district."
            )

        patient_id, age_group, district = details

        return cls(
            patient_id.strip(),
            age_group.strip(),
            district.strip()
        )

    # Static method
    @staticmethod
    def is_valid_age_group(age_group):

        valid_groups = ["Infant", "Child", "Adult"]

        return age_group in valid_groups


# ==========================================
# MAIN PROGRAM
# ==========================================

# Main dictionary storing patient objects
patients = {}


def add_patient(patient):

    if patient.patient_id in patients:
        print("Patient ID already exists.")
        return

    patients[patient.patient_id] = patient
    print("Patient added successfully.")


# Create vaccine objects
measles = Vaccine.from_supported_list("Measles")
polio = Vaccine.from_supported_list("Polio")
covid = Vaccine.from_supported_list("COVID-19")


# Create patient objects
patient1 = Patient("P001", "Infant", "Western Area")
patient2 = Patient("P002", "Child", "Bo")
patient3 = Patient("P003", "Adult", "Kenema")


# Add patients to the main dictionary
add_patient(patient1)
add_patient(patient2)
add_patient(patient3)


# Record vaccinations
patient1.record_vaccination(measles, 1, "2026-10-01")
patient1.record_vaccination(measles, 2, "2026-10-20")

patient2.record_vaccination(polio, 1, "2026-10-05")
patient2.record_vaccination(polio, 2, "2026-10-25")

patient3.record_vaccination(covid, 1, "2026-10-10")


# Display all patient information
print("\n========== PATIENT RECORDS ==========")

for patient in patients.values():
    patient.display_info()


# Check vaccination status
print("\n========== VACCINATION STATUS ==========")

print(
    "Patient P001 fully vaccinated for Measles:",
    patient1.is_fully_vaccinated(measles)
)

print(
    "Patient P002 fully vaccinated for Polio:",
    patient2.is_fully_vaccinated(polio)
)


# Display total number of patients
print("\nTotal registered patients:",
      Patient.get_total_patients())
