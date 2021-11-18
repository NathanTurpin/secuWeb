import sqlite3

# con = sqlite3.connect('database.db')
# print('Database opened successfully')
# con.execute('create table Users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, password TEXT NOT NULL)')
# print('Database created successfully')
# con.close()

# con = sqlite3.connect('database.db')
# print('Database opened successfully')
# con.execute('create table Chanels (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)')
# print('Database created successfully')
# con.close()

# con = sqlite3.connect('database.db')
# print('Database opened successfully')
# con.execute('create table Link (id INTEGER PRIMARY KEY AUTOINCREMENT, idUser INTEGER, idChanel INTEGER )')
# print('Database created successfully')
# con.close()

# con = sqlite3.connect('database.db')
# print('Database opened successfully')
# con.execute('UPDATE Users SET password =')
# print('Database created successfully')
# con.close()

def getNameUser(idUser):
    with sqlite3.connect("database.db") as con:
        cur = con.cursor() 
        cur.execute("SELECT * FROM Users WHERE id= ?", (idUser,))
        data = cur.fetchone()

        if data:
            nameUser = data[1]

        else:
            nameUser = 0

    return nameUser

def getChanels(idFichier):
    with sqlite3.connect("database.db") as con:
        cur = con.cursor() 
        data = cur.execute("SELECT * FROM fichier_Chanel_link WHERE idFichier= ?", (idFichier,))
        if data:
            chanels = [row[2] for row in data]
           
            return chanels[0]
        else:
            return 0

def getRoleFichier(idFichier):
    with sqlite3.connect("database.db") as con:
        cur = con.cursor() 
        data = cur.execute("SELECT * FROM fichier_Chanel_link WHERE idFichier= ?", (idFichier,))
        if data:
            role = [row[3] for row in data]
            
            return role[0]
        else:
            return 0

def getRole(idUser):
    roles = []
    chanels = []

    with sqlite3.connect("database.db") as con:
        cur = con.cursor() 

        cur.execute("SELECT * FROM roles_chanels_users_link WHERE idUser= ? ORDER BY idChanel ASC", (idUser,))
        rows = cur.fetchall()
        if rows:
            for row in rows:
                roles.insert(1,row[1])
                chanels.insert(1,row[2])
          

            # roles = [row[1] for row in data]
            # chanels = [row[2] for row in data2]
            nomRoles = getNomRole(roles)
            result = [nomRoles,chanels]
            return result
        else:
            return 0

def getNomRole(roles):
    nomRoles = []
    with sqlite3.connect("database.db") as con:
        cur = con.cursor() 
        for role in roles: 
            data = cur.execute("SELECT * FROM roles WHERE id= ?", (role,) )
            if data:
                nomRoles.insert(len(nomRoles),[row[1] for row in data])
            else:
                return 0
        return nomRoles

# Renvoie true si l'user a l'acces au chanel + son role
def getAcces(idUser,idChanel):
    # chanels = getChanels(idUser)
    result = getRole(idUser)
    # print(result)
    if result:
        role = result[0]
        chanel = result[1]
       
        # print(chanel.index(idChanel))
        if (chanel.index(idChanel) != None):
            print(role[chanel.index(idChanel)])

        else:
            return False
        return True
    else:
        return False

def getFile(idUser,idFichier):
    idChanel = getChanels(idFichier)
    
    t = getAcces(idUser,idChanel)
    print(t)
    idRoleFichier = getRoleFichier(idFichier)
    if t:
        if idRoleFichier ==1:
            print("vous avez les droits W/R sur ce fichier")
        else:
            print("vous avez les droits R sur ce fichier")
    else:
        return False


if __name__ == '__main__':
    # print(getAcces(6,1))
    # print(getAcces(1,8))
    # print(getAcces(1,6))

    # print(getFile(1,2))
    # print(getFile(1,1))
    # print(getFile(2,4))
   