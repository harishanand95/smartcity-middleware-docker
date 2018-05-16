import subprocess
import json
import ConfigParser
print("################### REGISTER API TESTING ###################")
register = subprocess.check_output("./tests/create_entity.sh streetlight", shell=True)
print(register)
registers = subprocess.check_output("cat /var/ideam/data/logs/tomcat/tomcat-stdo*", shell=True)
print(registers)
register = json.loads(register)
streetlight_key = register["apiKey"]
print(streetlight_key)
print("################### REGISTER API TESTING ###################")
register = subprocess.check_output("./tests/create_entity.sh dashboard", shell=True)
print(register)
register = json.loads(register)
dashboard_key = register["apiKey"]
print(dashboard_key)
print("################### PUBLISH API TESTING  ###################")
publish = subprocess.check_output("./tests/publish.sh " + streetlight_key, shell=True)
print(publish)
publish = subprocess.check_output("./tests/publish.sh abc", shell=True)
print(publish)
print("################### SHARE API TESTING  ###################")
share = subprocess.check_output("./tests/share.sh "+streetlight_key+" dashboard", shell=True)
print(share)
publish = subprocess.check_output("./tests/publish.sh " + streetlight_key, shell=True)
print(publish)
publish = subprocess.check_output("./tests/publish.sh " + streetlight_key, shell=True)
print(publish)
print("################### SUBSCRIBE API TESTING  ###################")
publish = subprocess.check_output("./tests/subscribe.sh " + dashboard_key, shell=True)
print(publish)
print("################### CATALOGUE API TEST   ###################")
cat = subprocess.check_output("./tests/catalogue.sh", shell=True)
print(cat)
print("################### SSH TO CONTAINER     ###################")
config = ConfigParser.ConfigParser()
config.readfp(open("/etc/ideam/ideam.conf"))
password = config.get('PASSWORDS', 'USER_ANSIBLE')
sshtest = subprocess.check_output("./tests/ssh_test.sh "+password, shell=True)
print(sshtest)
print("################### DEREGISTER API TEST  ###################")
deregister = subprocess.check_output("./tests/deregister.sh", shell=True)
print(deregister)
print("################### CATALOGUE API TEST   ###################")
cat = subprocess.check_output("./tests/catalogue.sh", shell=True)
print(cat)
print("################### DATABASE API TEST    ###################")
db = subprocess.check_output("./tests/database.sh " + streetlight_key, shell=True)
print(db)
db = subprocess.check_output("./tests/database.sh " + streetlight_key, shell=True)
print(db)
db = subprocess.check_output("./tests/database.sh " + streetlight_key, shell=True)
print(db)
db = subprocess.check_output("./tests/database.sh " + streetlight_key, shell=True)
print(db)
db = subprocess.check_output("./tests/database.sh " + streetlight_key, shell=True)
print(db)

