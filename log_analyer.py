import re 

log_file = "auth.log"

failed_login_pattern = re.compile(r"Failed password")
ip_pattern = re.compile(r"\d+\.\d+\.\d+\.\d+")

failed_attempts = {}

with open(log_file, "r") as file:
    for line in file:
       if failed_login_pattern.search(line):
         ip = ip_pattern.search(line)
         if ip:
            ip = ip.group()
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1


print("Suspicious Login Attempts:\n")

for ip, count in failed_attempts.items():
    if count > 3:
       print(f"ALERT: {ip} attempted login {count} times")

