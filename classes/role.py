ROLES = {
    "viewer": [],
    "scanner": ["scan_add", "scan_remove"],
    "stocker": ["scan_add"],
    "admin": ["scan_add", "scan_remove", "delete_item", "manage_users"]  
}


class Role():
    def __init__(self, role_name):
        self.role_name = role_name
        self.permissions = ROLES.get(role_name, []) ##Based off role name what permissions you have in the dictionary
        
    def has_permission(self, action):
        return action in self.permissions ##Y/N to what you are trying to do based off permissions
        
        