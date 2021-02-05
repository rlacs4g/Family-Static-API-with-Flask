
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name,
            "age": 33,
            "Lucky_numbers": [7,13,22]
            },
            {
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": last_name,
            "age": 35,
            "Lucky_numbers": [10, 14, 3]
            },
            {
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": last_name,
            "age": 5,
            "Lucky_numbers": [1]
            },            
        ]

#Jane Jackson
#35 Years old
#Lucky Numbers: 10, 14, 3

#Jimmy Jackson
#5 Years old
#Lucky Numbers: 1

        #John Jackson
       # 33 Years old
       # Lucky Numbers: 7, 13, 22

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        if "id" not in member:
            member["id"] = self._generateId()
        member["last_name"] = self.last_name
        self._members.append(member)
        return member

    def delete_member(self, id):
        # fill this method and update the return
        status = ""
        try: 
            for i,x in self._members:
                if x.id == id:
                    self._members.pop(i)   
            status = "Successfully deleted member."
        except:
            status = "Something went wrong. Couldn't delete member."

        return status

    def get_member(self, id):
        # fill this method and update the return
        member = {}
        for x in self._members:
            if x['id'] == id:
                member = x
                break
            else:
                member = False

        return member

    def delete_member(self, id):
        status = False
        for index, item in enumerate(self._members, start=0):
            if item["id"] == id:
                self._members.pop(index)
                status = True

        return status

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
