#!/usr/bin/env python3

import ipdb

class Person:
    approved_jobs = ["Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal", "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"]


    def get_name(self) -> str:
        return self._name

    def set_name(self, name) -> None:
        if (type(name) == str and len(name) > 1 and len(name) < 25):
            title_cased_nm = " ".join(list(map(lambda word: word[0].capitalize() + word[1:], name.split(' '))))
            self._name = title_cased_nm
        else:
            print("Name must be string between 1 and 25 characters.") 

    def get_job(self):
        return self._job

    def set_job(self, job):
        if(type(job) == str and job in Person.approved_jobs):
            print(type(job))
            self._job = job
            # print("!!!!!!THE RESULT IS TRUE!!!!!!" + self.job)
        else:
            print("Job must be in list of approved jobs.")

        

    name = property(get_name, set_name)
    job = property(get_job, set_job)

    pass

# ipdb.set_trace()
