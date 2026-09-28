from datetime import datetime

routers = ['R1-Colombo', 'R2-Kandy', 'R3-Galle']
print("Backup patan gannawa...")

for name in routers:
    config = f"hostname {name}\ninterface gig0/0\n ip address 192.168.1.1 255.255.255.0"
    date = datetime.now().strftime("%Y-%m-%d")
    filename = f"backup-{name}-{date}.txt"
    
    with open(filename, 'w') as f:
        f.write(config)
    
    print(f"Done: {filename}")

print("Ivarai! Desktop eka balanna")