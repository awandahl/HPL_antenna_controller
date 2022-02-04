# HPL_antenna_controller
 

git clone https://github.com/awandahl/HPL_antenna_controller.git    

cd HPL_antenna_controller    
python3 ant.py    
 
asus_ant.py is the same script written for Asus Tinker Board 2


Run at system start:    

nano /etc/systemd/system/ant_controller.service    

```` 
[Unit]
Description=ant_controller
After=multi-user.target

[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/python3 /home/[user]/HPL_antenna_controller/ant.py

[Install]
WantedBy=multi-user.target
````

chmod +x /etc/systemd/system/ant_controller.service    

systemctl daemon-reload    
systemctl enable ant_controller.service    
systemctl start ant_controller.service    
systemctl stop ant_controller.service    

