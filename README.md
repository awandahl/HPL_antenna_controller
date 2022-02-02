# antenna_controller_RPi
 
 git clone https://github.com/awandahl/antenna_controller_RPi.git    
 
 cd antenna_controller_RPi    
 python3 ant.py    
 
 
Run at system start:    

 nano /etc/systemd/system/ant_controller.service    

```` 
[Unit]
Description=ant_controller
After=multi-user.target

[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/python3 /home/aw/ant_controller/ant.py

[Install]
WantedBy=multi-user.target
````

chmod +x /etc/systemd/system/ant_controller.service    

systemctl daemon-reload    
systemctl enable ant_controller.service    
systemctl start ant_controller.service    
systemctl stop ant_controller.service    

