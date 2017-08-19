import pymysql,requests,time
db = pymysql.connect("localhost","root","password","Offline")
cursor = db.cursor()
i=0;
ips =  []
row = []

while True:
    while cursor.execute("SELECT * FROM files WHERE 1"):
        results = cursor.fetchall()
        #print(results);
        for row in results:
            ip = row[3]
            port = row[7]
            username = row[5]
            password = row[6]
            try:
                r = requests.get("http://"+username+":"+password+"@"+ip+":"+str(port))
                print(r.status_code)
            except requests.exceptions.RequestException as e:
                com = "DELETE FROM files WHERE ip = \""+ip+"\""
                cursor.execute(com)
                db.commit()
            print("IP:"+ip+", Port:"+str(port))
        time.sleep(10)
    time.sleep(15)
