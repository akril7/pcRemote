# pcRemote
pet-project

***<ins>WARNING: PROJECT VERY UNSECURITY, ITS JUST A PET PROJECT!!!</ins>***

## Overview

### Used technologies
- Language: ***Python***.
- Framework for server api: ***Django REST Framework***.
- Client use default package ***pty*** and ***aiopika*** (client for messages broker)
- Docker, Docker compose
- Also: RabbitMQ (as main message broker), Celery, Redis (message broker for celery)

## How to run
1. Run server on first terminal session: 
``` 
docker compose up -d --build
```
2. Setup environment for clients:
```
cd client
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt 
```
3. If you want, run client.py and register new user with command ***reg***:
```
python client.py
```
4. Run exec.py on second terminal session:
```
python exec.py <roomname>
```
5. Run send.py on third terminal session:
```
python send.py <roomname>
```

All commands (and keys) from send.py will send to exec.py and will execute there.
You can use three pc, just edit CONN_HOST in client/config.py, 

PS: default user - root, 1234
