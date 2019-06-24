import sys

user1 = input("Enter your name here(player-1): ")
user2 = input("Enter your name here(player-2): ")
ua1 = input("%s , please enter your choice.. paper , rock or scissors?" %user1)
ua2 = input("%s , please enter your choice.. paper , rock or scissors?" %user2)

def compare(u1,u2):
        if u1 == u2:
            return(print("it is a tie !"))
        elif u1 == 'rock':
            if u2 == 'scissors':
                return(print("rock is the winner !"))
            else:
                return(print("paper wins !"))
        elif u1 == 'paper':
                if u2 == 'rock':
                    return(print("paper is the winner !"))
                else:
                    return(print("scissors win !"))
        elif u1 == 'scissors':
                    if u2 == 'paper':
                        return(print("scissors is the winner !"))
                    else:
                            return(print("rock win !"))
        else:
              return(print("invalid entry.. you have not entered rock,paper or scissors.. try again !"))
sys.exit

compare(ua1,ua2)
