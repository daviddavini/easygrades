import abc
import functools

class GradeObject(abc.ABC):

    @abc.abstractmethod
    def calculate_grade(self):
        '''Returns -- (float) percentage of grade earned.'''
        return None

    @abc.abstractmethod
    def earned(self):
        '''Returns -- (float) points earned'''
        pass

    #TODO: Add Cache
    @abc.abstractmethod
    def max(self):
        ''' Returns -- (float) max points possible'''
        pass

class Grade(GradeObject):

    def __init__(self, earned, max):
        self._earned = earned
        self._max = max

    def earned(self):
        return self._earned
    
    def max(self):
        return self._max

    def calculate_grade(self):
        return self.earned() / self.max()

class GradeAverage(GradeObject):

    def __init__(self, grades):
        '''grades -- list of Grades'''
        self.grades = grades

    def earned(self):
        return sum(g.earned() for g in self.grades)
 
    def max(self):
        return sum(g.max() for g in self.grades)

    def calculate_grade(self):
        return self.earned() / self.max()
