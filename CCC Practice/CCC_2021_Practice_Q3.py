#Get the number of friends
number_of_friends = int(input("Input how many friends you have (between 1 and 2000: "))

#Get the ptd values of these friends


#Converting the ptd input values into integers
friends = []
inputoffriends = 1
while inputoffriends <= number_of_friends:
    friend_p_t_d = input("Input the ptd properties: ")
    friend_ptd = friend_p_t_d.split()
    
    for x in range(len(friend_ptd)):
        friend_ptd[x] = int(friend_ptd[x])
    
    friends.append(friend_ptd)
    inputoffriends += 1

print(friends)



#Solving
positionindex = 0
timeindex = 1
distanceindex = 2
friend_number = 0

position = friends[friend_number][positionindex]
time = friends[friend_number][timeindex]
distance = friends[friend_number][distanceindex]


