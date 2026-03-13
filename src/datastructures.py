"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""
class Member:
    def __init__(self, member_id, first_name, age, lucky_numbers):
        self.id = member_id
        self.first_name = first_name
        self.age = age
        self.lucky_numbers = lucky_numbers

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "age": self.age,
            "lucky_numbers": self.lucky_numbers,
        }
    

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, first_name, age, lucky_numbers):
        new_member = Member(
            member_id=self._generate_id(),
            first_name=first_name,
            age=age,
            lucky_numbers=lucky_numbers
        )
        parsed_new_member = new_member.to_dict()
        parsed_new_member["last_name"] = self.last_name
        self._members.append(parsed_new_member)
        return new_member

    def delete_member(self, id):
        member_to_delete = self.get_member(id)
        if member_to_delete is None:
            return False
        self._members.remove(member_to_delete)
        return True

    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member
        return None

    def get_all_members(self):
        return self._members