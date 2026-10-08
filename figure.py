import copy


class Figure:


    def __init__(self, color, position):

        self.color = color
        self.position = position
      

    def move(self):

        pass



class Pawn(Figure):


    def __init__(self, color, position):

        super().__init__(color, position)
        self.has_moved = False


    def move(self, future_position):
        
        possible_coordinates = []

        if self.color == "white":

            num = copy.copy(self.position)
            num[1] = num[1] + 1
            possible_coordinates.append(num)

            if self.has_moved == False:

                num = copy.copy(self.position)
                num[1] = num[1] + 2
                possible_coordinates.append(num)
                

        elif self.color == "black":

            num = copy.copy(self.position)
            num[1] = num[1] - 1
            possible_coordinates.append(num)

            if self.has_moved == False:

                num = copy.copy(self.position)
                num[1] = num[1] - 2
                possible_coordinates.append(num)
                

        if future_position in possible_coordinates:

           
            return True
        
        else:

            return False
        




class Rook(Figure):
     
    pass


class Knight(Figure):

    pass


class Bishop(Figure):

    pass


class Queen(Figure):

    pass


class King(Figure):

    pass