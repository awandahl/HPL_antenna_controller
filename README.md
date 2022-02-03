# HPL_antenna_controller
 
<<<<<<< HEAD
 git clone https://github.com/awandahl/HPL_antenna_controller.git    
=======
 git clone https://github.com/awandahl/HPL_antenna_controller.git    
>>>>>>> 2d665b1160bbde2b085446121ce6cc3ce68b83e6
 
 cd HPL_antenna_controller    
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
ExecStart=/usr/bin/python3 /home/aw/HPL_ant_controller/ant.py

[Install]
WantedBy=multi-user.target
````

chmod +x /etc/systemd/system/ant_controller.service    

systemctl daemon-reload    
systemctl enable ant_controller.service    
systemctl start ant_controller.service    
systemctl stop ant_controller.service    

