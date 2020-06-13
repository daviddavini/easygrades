class Course:

    def __init__(self, grades, weights = 1, drops = 0):
        
        # Format grades
        if isinstance(grades, list):
            grades = {'default': grades}
        
        