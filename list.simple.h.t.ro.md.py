a = [10,20,30]

a.append( 40 )
a.insert( 0, -10 )

clients = ["John","Marry","Kate"]

clientsHighPriority = ["Tob","Pete"]
clientsLowPriority = ["Vicky","Lessly"]

clients.append(clientsLowPriority[0])
clients.append(clientsLowPriority[1])
clients.insert(0, clientsHighPriority[0])
clients.insert(0, clientsHighPriority[1])

for i in range(len(clients)):
    print(i, clients[i])
