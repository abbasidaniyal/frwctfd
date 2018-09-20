![](https://github.com/CTFd/CTFd/blob/master/CTFd/themes/core/static/img/logo.png?raw=true)
====

# IEEE Fresher's Week 2018
IEEE Fresher's Week 2018 Capture the Flag

Powered by CTFd

## How to Serve
For Developers

### Getting Git

1. Install git from https://git-scm.com/

2. Run the following command in cmd/terminal
```
git clone https://github.com/zrthxn/frwctfd.git
```

### Install Python

1. Install Python 3 from https://www.python.org/downloads/

2. Add the Python scripts directory to System Environment Variable **PATH**
this is for pip to work from anywhere

3. Run the following command in cmd/terminal
```python 
pip install <requirements from CTFd>
```

### Get your IP Address

1. Run CMD

2. Run the following command in cmd/terminal
```
ipconfig
```

3. Copy your IPv4 address

### Serve CTFd

1. Open the CTFd folder

2. Open the files **serve.py** and **wsgi.py** with any text editor

3. Change the variable "host" from 127.0.0.1 to your IPv4 address

4. Run the following command in cmd/terminal
```python
py serve.py
```
