class DegreeProgram:
    def __init__(self):
        self.degree_program_list = []
    
    def create_degreee_program(self,degree_program_id, degree_program_name, department_id):
        new_row = (degree_program_id, degree_program_name, department_id)  
        if degree_program_id not in self.degree_program_list:
            self.degree_program_list.append(new_row)
        else:
            print("Input is already in the list.")

    def update_degree_program(self,program_id,new_name=None,new_department_id=None):
        for index, item in enumerate(self.degree_program_list):
            if item[0] == program_id:
                new_item = (
                    item[0],
                    new_name if new_name is not None else item[1],
                    new_department_id if new_department_id is not None else item[2]
                )
                self.degree_program_list[index] = new_item
                print("Program updated:", new_item)
                return
        print("Program with ID", program_id, "not found.")
    
    def delete_degree_program_by_id(self, program_id):
        for index, (id_) in enumerate(self.degree_program_list):
            if id_[0] == program_id:
                del self.degree_program_list[index]
                return
            else:
                print("Id not found in the list.")
    
    def find_by_id(self,program_id):
        for index, (id_) in enumerate(self.degree_program_list):
            if id_[0] == program_id:
                print("Here is the row:",self.degree_program_list[index])
                return
          
        
   

dp = Degree_Program()

#create row
dp.create_degreee_program(1, "BS in Nursing", 1)  
dp.create_degreee_program(2, "BS in Nursing", 2)
dp.create_degreee_program(3,"BS in Architecture",3)
print("Created",dp.degree_program_list)


# Update row
dp.update_degree_program(2, new_name="BS in Nursing Science")
print("Updated",dp.degree_program_list)

#delete row 
dp.delete_degree_program_by_id(1)
print("Deleted",dp.degree_program_list)


#find by id
dp.find_by_id(3)