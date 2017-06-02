import pymysql,requests,time
db = pymysql.connect("localhost","root","10sa1017213","Offline")
cursor = db.cursor()
i=0;
ips =  []
row = []

while True:
    while cursor.execute("SELECT * FROM files WHERE 1"):
        results = cursor.fetchall()
        print(results);
        for row in results:
            ip = row[2]
            port = row[8]
            username = row[6]
            password = row[7]
            try:
                r = requests.get("http://"+username+":"+password+"@"+ip+":"+port)
            except requests.exceptions.RequestException as e:
                cursor.execute('DELETE FROM files WHERE ip = \'%s\''%ip)
                db.commit()
            print("IP:"+ip+", Port:"+port)
        time.sleep(10)
    time.sleep(15)
