from linkedList import LinkedList
import copy
import itertools
alph = ["a", "b", "c", "d", "e", "f", "g", "h", "g", "i", "k", "l", "m"]
n = 4 # nombre de joueurs
N = [alph[i] for i in range(n)] #ensemble représentant les joueurs
dR = {-1, 0, 1} # ensemble images par l'application dexter

def s(R):
    s = {}
    for x in N:
        s[x] = R[x][0]
    
    return s

def d1(R):
    d = {}
    for x in N:
        d[x] = R[x][1]
        
    return d

def roll_call_generate(N) :
    """genere les appels nominaux d'un jeux N
    en utilisant un algorithme de recherche basé 
    sur  le backtracking
    """
    
    nbr = 0 # nombre de roll call générés
    images = [[(i + 1, j) for j in dR] for i in range(n)]
    rollCalls = []
    
    #fonction de recherche 
    def backStrackingSearch(node, R, images):
        nonlocal nbr
        if node == None :
            rollCalls.append(copy.deepcopy(R))
        else:
            images2 = copy.deepcopy(images)
            for img in images:
                images2.remove(img)
                for image in img :
                    R[node.data] = image
                    backStrackingSearch(node.next_node, R, images2)
                images2.append(img)
                
    structure = LinkedList()
    R = {}
    for player in N:
        structure.append(player) 
        R[player] = []
    
    backStrackingSearch(structure.head, R, images)
    
    return rollCalls
    

def display(rollCalls):
    for rollcall in rollCalls:
        print(f'{rollCalls.index(rollcall) + 1}.{rollcall}')
        
if __name__ == "__main__":
    rollcalls = roll_call_generate(N)
    with open(f'rollcall_{n}_player.txt', "w") as f:
         for rollcall in rollcalls :
             f.write(f'{rollcalls.index(rollcall) + 1}.{str(rollcall)}\n')
    display(roll_call_generate(N))

        

    
    
    


                