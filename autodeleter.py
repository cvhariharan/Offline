import pymysql,requests
db = pymysql.connect("localhost","root","10sa1017213","Offline")
cursor = db.cursor()
i=0;
ips =  []
row = []


while cursor.execute("SELECT * FROM files WHERE 1"):
    results = cursor.fetchall()
    print(results);
    for row in results:
        ip = row[2]
        if ip not in ips:
            ips.append(ip)
            port = row[8]
            username = row[6]
            password = row[7]
            try:
                r = requests.get("http://"+username+":"+password+"@"+ip+":"+port)
            except requests.exceptions.RequestException as e:
                cursor.execute('DELETE FROM files WHERE ip = \'%s\''%ips[i])
                db.commit()
        print("IP:"+ip+", Port:"+port)
        i = i+1
    
