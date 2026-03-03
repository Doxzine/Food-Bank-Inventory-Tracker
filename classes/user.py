from .role import Role

class User():
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = Role(role)

    def can_do(self, permissions):
        return self.role.has_permission(permissions) ## Current role -> what you are trying to do -> what permissions you have -> y/n
    
    def __str__(self):
        return (f"{self.username} - {self.role.role_name}") ##Just testing to see your role and username
    
        