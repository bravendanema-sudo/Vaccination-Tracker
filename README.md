# Vaccination Tracker System

**Course:** PROG211 – Object-Oriented Programming Methods 1  
**Project Domain:** Health  
**Programming Language:** Python 3

## 1. Project Overview

The Vaccination Tracker System is a Python-based application developed to demonstrate Object-Oriented Programming (OOP) concepts through the management of patient vaccination records.

The system allows users to register patients, record vaccine doses, view vaccination histories, and check whether patients have completed their required vaccine doses.

## 2. Project Objectives

The main objectives are to:

- Apply classes and objects in Python.
- Demonstrate the use of constructors, attributes, and methods.
- Store and manage patient vaccination records using a dictionary.
- Validate vaccination dose numbers.
- Check vaccination completion status.
- Demonstrate reusable and modular programming.

## 3. System Classes

The system contains two main classes.

### 3.1 Vaccine Class

The `Vaccine` class manages vaccine information.

**Attributes:**
- `name` – stores the vaccine name.
- `required_doses` – stores the number of doses required.

**Methods:**
- `display_info()` – displays vaccine information.
- `is_valid_dose_number()` – checks whether a dose number is valid.
- `from_supported_list()` – creates a vaccine object from the supported vaccine list.

### 3.2 Patient Class

The `Patient` class manages patient information and vaccination records.

**Attributes:**
- `patient_id` – stores the patient's identification number.
- `age_group` – stores the patient's age group.
- `district` – stores the patient's district.
- `vaccinations` – stores the patient's vaccination records.

**Methods:**
- `record_vaccination()` – records a vaccine dose.
- `is_fully_vaccinated()` – checks vaccination completion.
- `display_info()` – displays patient information.
- `get_total_patients()` – returns the total number of patients.
- `from_string()` – creates a patient object from a string.
- `is_valid_age_group()` – validates the patient's age group.

## 4. Object-Oriented Programming Concepts

The project demonstrates:

- Classes and objects
- Constructors (`__init__`)
- Attributes
- Instance methods
- Class methods
- Static methods
- Object interaction

## 5. Data Structures

The main data structure used is a **dictionary**.

The `patients` dictionary stores patient objects using their patient IDs as keys.

Each patient also has a dictionary that stores vaccination records.

A tuple is used to store the fixed list of supported vaccines.

## 6. Main System Features

- Register new patients.
- Store patient information.
- Record vaccination doses.
- Prevent duplicate dose records.
- Validate vaccine dose numbers.
- Display patient vaccination histories.
- Check whether a patient has completed the required doses.
- Count registered patients.

## 7. DPG Principles

The project aims to demonstrate the following Digital Public Goods principles:

**Privacy:** The demonstration uses patient IDs instead of collecting patient names or contact details. It still stores age groups and districts, so this is a privacy-conscious demonstration rather than a guarantee of complete privacy.

**Inclusion:** The system supports different age groups and districts.

**Reusability:** The classes and methods are organised so they can be reused and extended.

**Open-source readiness:** The Python source code can be shared and improved. An appropriate open-source licence should be added before distributing the project as open-source software.

## 8. System Requirements

- Python 3 installed on the computer.
- A Python editor such as IDLE, Visual Studio Code, or PyCharm.
- No additional Python packages are required.

## 9. Installation and Execution

1. Download or clone the project from GitHub.
2. Open the project folder.
3. Open a terminal in the project folder.
4. Run the following command:

```bash
python main.py
```

## 10. Example Output

```text
Patient P001 fully vaccinated for Measles: True
Patient P002 fully vaccinated for Polio: False

Total registered patients: 3
```

## 11. Current Limitations and Future Improvements

The current version uses sample patient information and does not save records permanently after the program closes.

Future improvements could include:

- Adding permanent database storage.
- Developing a graphical user interface.
- Adding more vaccine types.
- Allowing users to update or remove patient records.
- Adding secure user authentication.

## 12. Project Files

| File | Description |
|---|---|
| `main.py` | Main Python source code |
| `README.md` | Project documentation |

## 13. Important Notice

This project is an academic demonstration of Python programming concepts. It is not intended to replace professional medical records or provide medical advice.

## 14. Author

PROG211 Student Project