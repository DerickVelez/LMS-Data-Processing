from pydantic import BaseModel, EmailStr, validator
from typing import List, Optional
from datetime import datetime, date, time
        
        
        
class Addresses(BaseModel):
    address_id: int
    current_address: str
    permanent_address: str
    
class Departments(BaseModel):
    department_id: int
    department_name: str
    department_code: str
    
class Semesters(BaseModel):
    semester_id: int
    year_from: date 
    year_to: date
        
class Courses(BaseModel):
    course_id: int
    course: str
    course_type: str

class Transcrips(BaseModel):
    transcript_id: int
    requested_by: str
    generated_date: datetime
    
class Institution(BaseModel):
    institution_name: str
    intitution_type: str
    region: str
    province: str
    municipality: str
    
class Students(BaseModel):
    student_id: int
    current_address_id: int
    permanent_address_id: int
    gender: str
    first_name: str
    middle_name: str
    last_name: str
    cell_number: int
    email: EmailStr
    
class DegreePrograms(BaseModel):
    degree_program_id: int
    department_id: int
    
class Sections(BaseModel):
    section_id: int
    course_id: int
    
class StudentEnrollment(BaseModel):
    student_enrollement_id: int
    student_id: int
    degree_program_id: int
    semester_id: int
    institution_name: str
    
class StudentEnrollmentCourses(BaseModel):
    student_course_id: int
    student_enrollment_id: int
    course_id: int
    
class TranscriptContents(BaseModel):
    transcript_id: int
    student_course_id: int
    
