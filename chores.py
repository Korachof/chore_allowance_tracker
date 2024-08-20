class Chore:
    def __init__(self, name, description, cash_amount):
        self._name = name
        self._description = description
        self._cash_amount = cash_amount

    def get_name(self):
        """returns name (STR)"""
        return self._name
    
    def get_description(self):
        """returns description (STR)"""
        return self._description
    
    def get_cash_amount(self):
        """returns cash amount (FLOAT)"""
        return self._cash_amount
    
    def set_name(self, new_name):
        """sets/edits name (STR)
        returns: UPDATED self._name (STR)"""
        self._name = new_name
        return self._name

    def set_description(self, new_description):
        """sets/edits description (STR)
        returns: UPDATED self._description (STR)"""
        self._description = new_description
        return self._description

    def set_cash_amount(self, new_cash_amount):
        """sets/edits self._cash_amount (FLOAT)
        returns: UPDATED self._cash_amount (FLOAT)"""
        self._cash_amount = new_cash_amount
        return self._cash_amount
    

class OneOffGoal(Chore):
    def __init__(self, name, description, cash_amount, deadline, goal_size):
        super().__init__(name, description, cash_amount)
        self._deadline = deadline
        self._goal_size = goal_size

    def get_deadline(self):
        """returns deadline (STR)"""
        return self._deadline

    def set_deadline(self, new_deadline):
        """sets/edits deadline (STR)
        returns: UPDATED self._deadline (STR)"""
        self._deadline = new_deadline
        return self._deadline
    
    def get_goal_size(self):
        """returns goal_size (STR)
        options: Large, Small"""
        return self._goal_size
    
    def set_goal_size(self, new_size):
        """sets/edits goal size (STR)
        returns: UPDATED self._goal_size (STR)"""
        self._goal_size = new_size
        return self._goal_size


class OngoingChore(Chore):
    def __init__(self, name, description, cash_amount, completed_count):
        super().__init__(name, description, cash_amount)
        self._completed_count = completed_count

    def get_completed_count(self):
        """returns completed_count (INT)"""
        return self._completed_count
    
    def incr_count(self):
        """increments completed_count (INT) by 1
        returns self._completed_count"""
        self._completed_count += 1
        return self._completed_count
    

class NegativeHabit(OngoingChore):
    def __init__(self, name, description, cash_amount, completed_count):
        super().__init__(name, description, cash_amount,  completed_count)

    


    

        



    