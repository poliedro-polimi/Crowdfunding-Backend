# Sito donazioni per PoliEdro

Il sito è scritto in Flask. Per eseguirlo in locale:

```shell
sudo pip install flask
sudo pip install --upgrade https://github.com/poliedro-polimi/PoliEdro-Donate/archive/master.zip
export POLIEDRO_DONATE_CONFIG="cfg.sample.py"
export FLASK_APP="poliedro_donate"
export FLASK_DEBUG=1
flask run
```

Per eseguirlo in locale con PyPy (sul server verrà utilizzato PyPy)

``` shell
# Debian/Ubuntu
sudo apt install pypy pypy-setuptools
sudo pypy -m easy_install pip
sudo pypy -m pip install flask
sudo pypy -m pip install --upgrade https://github.com/poliedro-polimi/PoliEdro-Donate/archive/master.zip
export POLIEDRO_DONATE_CONFIG="cfg.sample.py"
export FLASK_APP="poliedro_donate"
export FLASK_DEBUG=1
pypy -m flask run
```

È possibile installarlo con la modalità *development* di `setuptools`.
In questo modo non sarà necessario reinstallarlo dopo una modifica dei sorgenti, ma solo quando verranno aggiunti degli entry points.

```shell
git clone https://github.com/poliedro-polimi/PoliEdro-Donate.git
cd PoliEdro-Donate
# System Python PIP
sudo pip install -e .
# PyPy PIP
sudo pypy -m pip install -e .
```
