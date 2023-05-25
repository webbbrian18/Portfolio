#Brian Webb
#ITEC 209
#Patient Charges.py
#4/8/2023

class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone_number, emergency_contact_name, emergency_contact_phone):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone
    
    def get_first_name(self):
        return self.first_name
    
    def set_first_name(self, first_name):
        self.first_name = first_name
    
    def get_middle_name(self):
        return self.middle_name
    
    def set_middle_name(self, middle_name):
        self.middle_name = middle_name
    
    def get_last_name(self):
        return self.last_name
    
    def set_last_name(self, last_name):
        self.last_name = last_name
    
    def get_address(self):
        return self.address
    
    def set_address(self, address):
        self.address = address
    
    def get_city(self):
        return self.city
    
    def set_city(self, city):
        self.city = city
    
    def get_state(self):
        return self.state
    
    def set_state(self, state):
        self.state = state
    
    def get_zip_code(self):
        return self.zip_code
    
    def set_zip_code(self, zip_code):
        self.zip_code = zip_code
    
    def get_phone_number(self):
        return self.phone_number
    
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
    
    def get_emergency_contact_name(self):
        return self.emergency_contact_name
    
    def set_emergency_contact_name(self, emergency_contact_name):
        self.emergency_contact_name = emergency_contact_name
    
    def get_emergency_contact_phone(self):
        return self.emergency_contact_phone
    
    def set_emergency_contact_phone(self, emergency_contact_phone):
        self.emergency_contact_phone = emergency_contact_phone


class Procedure:
    def __init__(self, name, date, practitioner, charge):
        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.charge = charge
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_date(self):
        return self.date
    
    def set_date(self, date):
        self.date = date
    
    def get_practitioner(self):
        return self.practitioner
    
    def set_practitioner(self, practitioner):
        self.practitioner = practitioner
    
    def get_charge(self):
        return self.charge
    
    def set_charge(self, charge):
        self.charge = charge


# Example usage
patient = Patient(
    "Nowhere", "", "Man", "123 Anywhere St", "Carbondale", "IL", "12345", "123-456-7890", "Nowhere Woman", "555-123-4567"
)

procedure1 = Procedure("Physical Exam", "2023-04-08", "Dr. Irvine", "$250")
procedure2 = Procedure("X-ray", "08-04-2023", "Dr. Jamison", "$500")
procedure3 = Procedure("Blood test", "08-04-2023", "Dr. Smith", "$200")

procedures = [procedure1, procedure2, procedure3]

# Print some information about the patient and procedures
print("Patient name:", patient.get_first_name(), patient.get_middle_name(), patient.get_last_name())
print("Patient address:", patient.get_address(), patient.get_city(), patient.get_state(), patient.get_zip_code())
print("Patient phone number:", patient.get_phone_number())
print("Emergency contact name:", patient.get_emergency_contact_name())
print("Emergency contact phone number:", patient.get_emergency_contact_phone())

for procedure in procedures:
    print("Procedure name:", procedure.get_name())
    print("Procedure date:", procedure.get_date())
    print("Procedure practitioner:", procedure.get_practitioner())
    print("Procedure charge:", procedure.get_charge())

