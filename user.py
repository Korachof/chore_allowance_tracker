class User:
    def __init__(self, name, spending_money, one_off_goal_list, ongoing_chore_list, completed_goal_list):
        self._name = name
        self._spending_money = spending_money
        self._one_off_goal_list = one_off_goal_list
        self._ongoing_chore_list = ongoing_chore_list
        self._completed_goal_list = completed_goal_list

    def get_name(self):
        """returns name (STR)"""
        return self._name
    
    def set_name(self, new_name):
        """sets/edits name (STR)
        returns: UPDATED self._name (STR)"""
        self._name = new_name
        return self._name
    
    def get_spending_money(self):
        """returns spending money (FLOAT)"""
        return self._spending_money
    
    def add_spending_money(self, new_amount):
        """add new_amount to spending_money
        returns: UPDATED self._spending_money"""
        self._spending_money += new_amount

    def get_one_off_goal_list(self):
        """returns one_off_goal_list (LIST)"""
        return self._one_off_goal_list
    
    def get_ongoing_chore_list(self):
        """returns ongoing_chore_list (LIST)"""
        return self._ongoing_chore_list
    
    def completed_goal_list(self):
        """returns completed_goal_list (LIST)"""
        return self._completed_goal_list