Serverless
===

Pre-requisites
---
Python 2.7

Setup
---

1. Clone the repository
2. Install PyMySQL in the repository directory using `pip install PyMySQL -t .` In case you need to install pip or easy_install, use `sudo easy_install pip` or `curl https://bootstrap.pypa.io/ez_setup.py -o - | sudo python`
3. Create a file rds_config.py with variables
    - db_username
    - db_password
    - db_name
    - host
4. Run `python app.py`. Output should be
```shell
   INFO:root:SUCCESS: Connection to RDS mysql instance succeeded
   INFO:root:(1, 'Joe')
   (1, 'Joe')
   INFO:root:(2, 'Bob')
   (2, 'Bob')
   INFO:root:(3, 'Mary')
   (3, 'Mary')
```