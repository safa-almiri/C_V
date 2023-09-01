
class Experience:
    def __init__(self, company, job_title, start_date, end_date):
        self.company = company
        self.job_title = job_title
        self.start_date = start_date
        self.end_date = end_date

    def display_experience(self):
        print("Company:", self.company)
        print("Job Title:", self.job_title)
        print("Start Date:", self.start_date)
        print("End Date:", self.end_date)


class Education:
    def __init__(self, degree, institution, completion_date):
        self.degree = degree
        self.institution = institution
        self.completion_date = completion_date

    def display_education(self):
        print("Degree:", self.degree)
        print("Institution:", self.institution)
        print("Completion Date:", self.completion_date)


class Skill:
    def __init__(self, skill, percentage):
        self.skill = skill
        self.percentage = percentage

    def display_skill(self):
        print("Skill:", self.skill)
        print("Percentage:", self.percentage)


class CV:
    def __init__(self, name):
        self.name = name
        self.experiences = []
        self.education = []
        self.skills = []

    def add_experience(self, company, job_title, start_date, end_date):
        experience = Experience(company, job_title, start_date, end_date)
        self.experiences.append(experience)

    def add_education(self, degree, institution, completion_date):
        education = Education(degree, institution, completion_date)
        self.education.append(education)

    def add_skill(self, skill, percentage):
        skill = Skill(skill, percentage)
        self.skills.append(skill)

    def display_cv(self):
        print("Name:", self.name)
        print("\nExperiences:")
        for experience in self.experiences:
            experience.display_experience()
            print()
        print("\nEducation:")
        for education in self.education:
            education.display_education()
            print()
        print("\nSkills:")
        for skill in self.skills:
            skill.display_skill()
            print()


name = input("Enter your name: ")
cv = CV(name)

add_skills = input("Do you want to add skills? (yes/no): ")
while add_skills.lower() == "yes":
    skill = input("Enter skill: ")
    percentage = input("Enter percentage: ")
    cv.add_skill(skill, percentage)
    add_skills = input("Do you want to add more skills? (yes/no): ")

add_education = input("Do you want to add education? (yes/no): ")
while add_education.lower() == "yes":
    degree = input("Enter degree: ")
    institution = input("Enter institution: ")
    completion_date = input("Enter completion date: ")
    cv.add_education(degree, institution, completion_date)
    add_education = input("Do you want to add more education? (yes/no): ")

add_experience = input("Do you want to add experiences? (yes/no): ")
while add_experience.lower() == "yes":
    company = input("Enter company: ")
    job_title = input("Enter job title: ")
    start_date = input("Enter start date: ")
    end_date = input("Enter end date: ")
    cv.add_experience(company, job_title, start_date, end_date)
    add_experience = input("Do you want to add more experiences? (yes/no): ")

cv.display_cv()

