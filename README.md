# Back-end per il sito di crowdfunding di PoliEdro

Il back-end gestisce i pagamenti con PayPal e si occupa di memorizzare i dettagli delle donazioni e delle prenotazioni su un database.

Verrà hostato su PythonAnywhere ([poliedropolimi.pythonanywhere.com](https://poliedropolimi.pythonanywhere.com)).

Il [front-end](/poliedro-polimi/Crowdfunding-Frontend) invece è scritto in PHP, verrà hostato sul servizio di web hosting già utilizzato da PoliEdro ([donate.poliedro-polimi.it](https://donate.poliedro-polimi.it)).

Il back-end è scritto in Flask. Per eseguirlo in locale:

### 1. Creazione del virtualenv
```shell
python3 -m venv poliedro_venv
source poliedro_venv/bin/activate
```

### 2. Installazione
```shell
pip install --upgrade https://github.com/poliedro-polimi/Crowdfunding-Backend/archive/master.zip
```

##### Modalità development

Se si dispone di un clone del repository git, è possibile installare il pacchetto in modalità development, per rendere subito disponibili le modifiche al codice.

```shell
cd path/to/Crowdfunding-Backend
pip install -e .
```

### 3. Esecuzione
```shell
export FLASK_DEBUG=1
python -m poliedro_donate
```

