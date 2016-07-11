### Tutorial for setting up a basic Flask REST API only application

#### Install dependencies
```
$ virtualenv .pyenv
$ source .pyenv/bin/activate
$ pip install -r requirements.txt
```

#### Run

```
$ python run.py
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
* Restarting with stat
```

Now hit `http://localhost:5000/api/users/` in your browser