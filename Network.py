import User


class SocialNetwork:
    __instance = None
    __is_initialized = False

    def __new__(cls, name: str):
        if cls.__instance is None:
            cls.__instance =  super().__new__(cls)
        return cls.__instance

    def __init__(self, name: str):
        if self.__is_initialized:
            return
        self.name = name
        self.users: dict[str, User] = dict()
        self.__is_initialized=True

    def sing_up(self, username, password):
        if username not in self.users:
            if 4 <= len(password) & len(password) >= 8:
                new_user = User(username, password)

    def SocialNetwork(self,twitter): #fix
        Twitter = self.__init__(twitter)
        print("The social network "+Twitter+" was created!")


    def login(self, name, password): #connect to the net
        if name in self.user.name & self.user.name.password == password:
            name.flag == True

    def logout(self, name, password):  #disconnect from the net
        if name in self.users & self.users[name].password == password:
            name.flag == False

    def __str__(self): #dict.values like iterator return string

