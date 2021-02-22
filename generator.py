from rules import*

class generator:

    def turn_alge(self, number):
        turn_alge_dic = {0: "a", 1:"b", 2:"c",
            3: "d", 4:"e", 5:"f", 6:"g", 7:"h"}
        return turn_alge_dic[number]
    def possible_matrix(self, mx, player, pieces, last_move):
        possible_states = [] #generate child_nodes
        final_options = []
        algebric_states = []
        for i in range(len(mx)):
            row = i//8
            col = i%8
            if mx[i].upper() in "P" and mx[i] in pieces:
                if player == "Black":
                    if row+1 < 8: final_options.append((row+1,col))
                    if row+2 < 8: final_options.append((row+2,col))
                    if row+1 < 8 and col+1 < 8: final_options.append((row+1,col+1))
                    if row+1 < 8 and col-1 > -1: final_options.append((row+1,col-1))
                else:
                    if row-1 > -1: final_options.append((row-1,col))
                    if row-2 > -1: final_options.append((row-2,col))
                    if row-1 > -1 and col+1 < 8: final_options.append((row-1,col+1))
                    if row-1 > -1 and col-1 > -1: final_options.append((row-1,col-1))

            if mx[i].upper() in "B" and mx[i] in pieces:
                current = (row,col)
                while current[0] > 0 and current[1] < 7:
                    current= (current[0]-1, current[1]+1)
                    final_options.append(current)
                current = (row,col)
                while current[0] > 0 and current[1] > 0:
                    current= (current[0]-1, current[1]-1)
                    final_options.append(current)
                current = (row,col)
                while current[0] < 7 and current[1] < 7:
                    current= (current[0]+1, current[1]+1)
                    final_options.append(current)
                current = (row,col)
                while current[0] < 7 and current[1] > 0:
                    current= (current[0]+1, current[1]-1)
                    final_options.append(current)
            if mx[i].upper() in "R" and mx[i] in pieces:
                current = (row,col)
                while current[0] > 0:
                    current= (current[0]-1, current[1])
                    final_options.append(current)
                current = (row,col)
                while current[1] > 0:
                    current= (current[0], current[1]-1)
                    final_options.append(current)
                current = (row,col)
                while current[0] < 7:
                    current= (current[0]+1, current[1])
                    final_options.append(current)
                current = (row,col)
                while current[1] < 7:
                    current= (current[0], current[1]+1)
                    final_options.append(current)
            if mx[i].upper() in "Q" and mx[i] in pieces:
                current = (row,col)
                while current[0] > 0 and current[1] < 7:
                    current= (current[0]-1, current[1]+1)
                    final_options.append(current)
                current = (row,col)
                while current[0] > 0 and current[1] > 0:
                    current= (current[0]-1, current[1]-1)
                    final_options.append(current)
                    current= (current[0]+1, current[1]-1)
                    final_options.append(current)
                current = (row,col)
                while current[0] > 0:
                    current= (current[0]-1, current[1])
                    final_options.append(current)
                current = (row,col)
                while current[1] > 0:
                    current= (current[0], current[1]-1)
                    final_options.append(current)
                current = (row,col)
                while current[0] < 7:
                    current= (current[0]+1, current[1])
                    final_options.append(current)
                current = (row,col)
                while current[1] < 7:
                    current = (current[0], current[1]+1)
                    final_options.append(current) 

            if mx[i].upper() in "K" and mx[i] in pieces:

                if row+1 < 8 and col+1 < 8: final_options.append((row+1, col+1))
                if row+1 <8: final_options.append((row+1, col))
                if row+1 <8 and col-1 > -1: final_options.append((row+1, col-1)) 
                if row-1 > -1 and col+1 < 8: final_options.append((row-1, col+1))
                if row-1 > -1: final_options.append((row-1, col))
                if row-1 > -1 and col-1 > -1: final_options.append((row-1, col-1))
                if col+1 <8: final_options.append((row, col+1))
                if col-1 > -1: final_options.append((row, col-1))

            if mx[i].upper() in "N" and mx[i] in pieces:

                if row+1 < 8 and col+ 2 < 8: final_options.append((row+1, col+2))
                if row+1 < 8 and col -2 > -1: final_options.append((row+1, col-2))
                if row+2 < 8 and col-1 > -1: final_options.append((row+2, col-1)) 
                if row+2 < 8 and col+1 < 8: final_options.append((row+2, col+1))
                if row-1 > -1 and col+2 < 8: final_options.append((row-1, col+2))
                if row-1 > -1 and col-2 > -1: final_options.append((row-1, col-2))
                if row-2 > -1 and col+1 < 8 :final_options.append((row-2, col+1))
                if row-2 > -1 and col-1 > -1 :final_options.append((row-2, col-1))

            for position in final_options:
                option = str(mx[:])
                result = rules.check_order(mx, (row,col), position, player, last_move)
                attacked = rules.is_attacked(mx, player, pieces, last_move)
                print("got a position")
                if result[0] and (row,col) != position and mx[position[0]*8 + position[1]] not in pieces and not attacked:
                    possible_states.append(generator.move(self, (row,col), position, player, result[1], option))
                    alge_order = generator.turn_alge(self, col) + str(8-row) +  generator.turn_alge(self, position[1]) + str(8-position[0])
                    algebric_states.append(alge_order)
                    print((row,col), position)
                    print(alge_order)
            final_options = []
        print(algebric_states)
        return (possible_states, algebric_states)

    def move(self, pos, final, player, order, mx):
        mx = list(mx)
        if order == "en_passant":
            mx[final[0]*8 + final[1]] = mx[pos[0]*8 + pos[1]]
            mx[pos[0]*8+ pos[1]] = "-"
            mx[pos[0]*8 + final[1]] = "-"
        elif order == "promotion":
            if player == "White":
                mx[final[0]*8 + final[1]] = "Q"
            elif player == "Black":
                mx[final[0]*8 + final[1]] = "q"
            mx[pos[0]*8 + pos[1]] = "-"
        else:
            mx[final[0]*8 + final[1]] = mx[pos[0]*8 + pos[1]]
            mx[pos[0]*8 + pos[1]] = "-"
        mx = "".join(mx)
        return mx

rules = rules()