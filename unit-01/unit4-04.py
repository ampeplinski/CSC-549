from random import randint
class MUD[T]:
    def __init__(self, rooms:dict, /) -> T:
        self._room = rooms
        self._location = "R1"

    def __setitem__(self, room_name: str, roomlinks: dict, /) -> T:
        self._room[room_name] = roomlinks

    def __getitem__(self, room_name: str, /) -> T:
        self._options_list = []
        for key in self._room[room_name].keys():
            self._options_list.append(key)
        return str(self._options_list)

    def getroom(self):
        return self._location

    def setroom(self, choice):
        #if choice == "north":
        #print(self._room[self._location][choice])
        self._location = self._room[self._location][choice]
        #print(self._location)
        return self._location

def main():
    choice = None
    cross = MUD({"R1":"north"})
    R1 = {"north":"R2"}
    R2 = {"south":"R1",
            "north":"R3"}
    R3 = {"north":"R6",
            "south":"R2",
            "east":"R5",
            "west":"R4"}
    R4 = {"east":"R3"}
    R5 = {"west":"R3"}
    R6 = {"south":"R3"}
    cross["R1"] = R1
    cross["R2"] = R2
    cross["R3"] = R3
    cross["R4"] = R4
    cross["R5"] = R5
    cross["R6"] = R6
    while True:
        if choice == None:
            choice = "R1"

        print(f"You are in room: {cross.getroom()}")
        choice = input(f"exits are: {cross[choice]} ")
        choice = cross.setroom(choice)
        #print(choice)
        #print({cross[location]})

    
        #input("You are in R1, exits: "))

if __name__ == "__main__":
    main()