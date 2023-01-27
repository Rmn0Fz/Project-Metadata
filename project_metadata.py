from datetime import datetime

class Project_manager:
    '''Define the Project Manager, the person to whom the project was assigned'''
    
    def __init__(self, name: str, email: str, phone: str):

        self.name   = name
        self.email  = email
        self.phone  = phone

class Project(Project_manager):
    '''Define a project that will be asigned to a Project Manager'''
    
    def __init__(self,  name: str, email: str, phone: str, project_name: str,
    project_manager: Project_manager, start_date: datetime.date(), end_date: datetime.date()):

        super().__init__(name, email, phone)

        self.project_name       = project_name
        self.project_manager    = project_manager
        self.start_date         = start_date
        self.end_date           = end_date

class Project_phase(Project):
    '''Define project progres'''
    def __init__(self, start_date: datetime.date, end_date: datetime.date):

        super().__init__(start_date, end_date)

        def phase(self):
            current_date    = datetime.now().date()
            total_days      = self.end_date - self.start_date
            elapsed_days    = current_date - self.start_date
            progres         = (elapsed_days / total_days) * 100

            if progres == 100:
                return "Project is finish"

            elif progres:
                return f"Project is {progres}% completed"

            else:
                return "Project has not been lounched yet!"

class Project_task(Project):
    ''' Define project description'''
    
    def __init__(self, task_description: str, name: str, email: str, phone: str, project_name: str,
    project_manager: Project_manager, start_date: datetime.date(), end_date: datetime.date()):

        super(). __init__(self,  name, email, phone, project_name, project_manager, start_date, end_date)

        self.task_description = task_description

class Document(Project_task):
    '''Define document that contain metadata from coresponding classes'''
    
    def __init__(self, doc_name: str, file: str, created_by: str, created_date: datetime.date(), last_modified_by: str, last_modified_date: datetime.date(), 
    description: str, name: str, email: str, phone: str, project_name: str,
    project_manager: Project_manager, start_date: datetime.date(), end_date: datetime.date()):

        super().__init__(description, name, email, phone, project_name, project_manager, start_date, end_date)
        
        self.doc_name           = doc_name
        self.file               = file
        self.created_by         = created_by
        self.created_date       = created_date
        self.last_modified_by   = last_modified_by
        self.last_modified_date = last_modified_date
        