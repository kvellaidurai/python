class Instructor:
    def __init__(self):
        self.__instructor_name= None
        self.__experience=None
        self.__avg_feedback= None
        self.__technology_skill= None
            
    def set_technology_skill(self, technology_skill):
            self.__technology_skill= technology_skill

    def get_technology_skill(self):
        return self.__technology_skill
        
    def set_avg_feedback(self, avg_feedback):
            self.__avg_feedback= avg_feedback

    def get_avg_feedback(self):
        return self._avg_feedback
        
    def set_experience(self, experience):
            self.__experience = experience

    def get_experience(self):
        return self._experience
        
    def set_instructor_name(self, instructor_name):
            self.__instructor_name = instructor_name

    def get_instructor_name(self):
        return self.__instructor_name   
    
    def check_eligibility(self):
        if(self.__experience==3 and self.allocate_course(self._tech_skill)==True and self.__avg_feedback>=4.5):
            return True
            
    def allocate_course(self,technology):
        if((technology==self.__technology_skill) or (technology=="C++")):
            return True
        else:
            return False

Krish=Instructor()
Krish.set_technology_skill(["java","python"])
print(Krish.allocate_course("Java"))
