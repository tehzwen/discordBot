import pymysql

class dataSet:
    def __init__(self, connection):
        self.userList = []
        self.currentID = 0
        self.cnx = connection

    def setCurrentID(self, val):
        self.currentID = val

    def getCurrentID(self):
        return self.currentID

#d1 = dataSet()

def editPoints(cnx, amount, user):
    cursor = cnx.cursor()
    
    currentPoints = getPoints(cnx, user)
    #for names in nameList:
        #if user == names[0]:
    
    add_points = ("UPDATE users SET bigpoints=%s WHERE name=%s")
    
    currentPoints += amount
    add_data = (currentPoints, user)
                

    cursor.execute(add_points, add_data)
    cnx.commit()



def traversePrint(idList, nameList, pointsList):
    for i in range(len(idList)):
        print("ID:", idList[i], "Name:", nameList[i], "Points:", pointsList[i])


def removeUser(cnx, name):
    cursor = cnx.cursor()
    remove_user = "DELETE FROM users WHERE name=%s;"
    user_data = (name,)
    
    cursor.execute(remove_user, user_data)

    cnx.commit()
    cursor.close()

def addnewUser(d1, name):
    nameList = getuserNames(d1.cnx)
    simpleList = []
    cursor = d1.cnx.cursor()

    for userName in nameList:
        
        simpleList.append(userName[0])
    if name not in simpleList:

        add_user = ("INSERT INTO users"
                    "(id, name, bigpoints)"
                    "VALUES (%s, %s, %s)")

        data_user = (0, name, 1000)
        d1.currentID += 1

        cursor.execute(add_user, data_user)

        d1.cnx.commit()
        
    else:
        print("User ", name, " has already been added to the Database.")
        
    
    cursor.close()

def getPoints(cnx, user):
    cursor = cnx.cursor()
    
    query = ("SELECT bigpoints FROM users WHERE name=%s")

    user_data = (user,)

    cursor.execute(query, user_data)

    for points in cursor:
        return points[0]


def getuserID(cnx):
    cursor = cnx.cursor()
    idList = []
    query = ("SELECT id FROM users")
    cursor.execute(query)

    for id in cursor:
        idList.append(id)

    cursor.close()
    return idList

def printuserID(idList):
    for user in idList:
        print (user)

def getuserNames(cnx):
    cursor = cnx.cursor()
    nameList = []
    query = ("SELECT name FROM users")
    cursor.execute(query)

    for name in cursor:
        nameList.append(name)

    cursor.close()

    return nameList

def printuserNames(nameList):
    for name in nameList:
        print(name)

def getuserPoints(cnx):
    cursor = cnx.cursor()
    pointsList = []
    query = ("SELECT bigpoints FROM users")
    cursor.execute(query)

    for points in cursor:
        pointsList.append(points)

    cursor.close()

    return pointsList

def printuserPoints(pointsList):
    for points in pointsList:
        print(points)




#cnx.close()
