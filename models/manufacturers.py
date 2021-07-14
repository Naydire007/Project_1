class Manufacturers:
    def __init__(self, company_name, description, id = None):
        self.company_name = company_name
        self.description = description
        self.id = id 

    def company_name(self):
        return f"{self.company_name} {self.description}"