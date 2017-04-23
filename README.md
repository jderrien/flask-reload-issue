Steps to reproduce the issue:

```
$ vagrant up
$ curl http://localhost:8080/debug

$ sed -i.bck -e 's/^import logging/#import logging/' flask_reload_issue/helpers/logger.py
$ touch flask_reload_issue.wsgi
$ curl http://localhost:8080/debug

$ mv flask_reload_issue/helpers/logger.py.bck flask_reload_issue/helpers/logger.py
$ touch flask_reload_issue.wsgi
$ curl http://localhost:8080/debug
```

```
$ vagrant up
$ curl http://localhost:8080/debug

$ sed -i.bck -e 's/^    #RaiseSyntaxError/    RaiseSyntaxError/' flask_reload_issue/helpers/logger.py
$ touch flask_reload_issue.wsgi
$ curl http://localhost:8080/debug

$ mv flask_reload_issue/helpers/logger.py.bck flask_reload_issue/helpers/logger.py
$ touch flask_reload_issue.wsgi
$ curl http://localhost:8080/debug
```
