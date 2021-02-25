
# Borders = [min x, max x] [min y, max y]
# H_direction = True (gehe horizontal) // False (gehe vertikal)
# move_forward = True (links nach rechts) //False (von oben nach unten)
# current_pos = momentane position starte bei [0,0]

# While True:

#     wenn H_direction True erhöhe current_pos[+1, 0]
#     bis current_pos[0]= borders[max x]
#     wenn move forward = True borders[min y] +1 
#     wenn move_forward = False borders[max x] -1
#     invertiere h H_direction

#     wenn H_direction False und move_forward = true erhöhe current_pos[0, +1]
#     bis current_pos[1]= borders[max y]
#     Wenn move_forward =True borders[max x] -1
#     wenn move_forward = False borders[min x] +1
#     invertiere h H_direction
#     invertiere move_forward
def snail(snail_map):
    Borders=[0,len(snail_map[0])-1,0,len(snail_map)-1]
    H_direction = True 
    move_forward = True
    doublecheck = False
    current_pos = [0,0]
    final_list=[snail_map[0][0]]
   # print(type(Borders[1]))
    print("boarder =", Borders)
    while True:
        # print("current pos: ",current_pos)
        # print("boarder: ", Borders)
        # print("current number: ",snail_map[current_pos[1]][current_pos[0]])



        if H_direction == True and move_forward == True: 
            print("lauf vorwärts")
            if current_pos[0] == Borders[1]:
                H_direction = False
                Borders[2]+=1
                doublecheck = True
                if current_pos[1] == Borders[3]:
                    break
                else:
                    continue
            else:
                current_pos[0] +=1
                
                # if doublecheck:
                #     print("current number: ",snail_map[current_pos[1]][current_pos[0]])
                #     break
            
                
        if H_direction == False and move_forward == True: 
            
            if current_pos[1] == Borders[3]:
                H_direction = True 
                move_forward = False
                Borders[1]-=1
                continue
            else:
                current_pos[1] +=1
        
        if H_direction == True and move_forward == False: 
            
            if current_pos[0] == Borders[0]:
                H_direction = False
                Borders[3]-=1
                continue 
            else:
                current_pos[0] -=1
            
        if H_direction == False and move_forward == False: 
            
            if current_pos[1] == Borders[2]:
                H_direction = True 
                move_forward = True
                Borders[0]+=1
                continue
               # break
            else:
                current_pos[1] -=1
        

        final_list.append(snail_map[current_pos[1]][current_pos[0]])
                
    print(final_list)
    return final_list


snailisnail = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(snailisnail)







# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]



