# Back-end per il sito di crowdfunding di PoliEdro 

[![Build Status](https://travis-ci.org/poliedro-polimi/Crowdfunding-Backend.svg?branch=master)](https://travis-ci.org/poliedro-polimi/Crowdfunding-Backend) ![Language](https://img.shields.io/badge/language-python-blue.svg) ![Python versions](https://img.shields.io/badge/python-3.5%2C%203.6%2C%20pypy3-blue.svg) [![license](https://img.shields.io/github/license/poliedro-polimi/Crowdfunding-Backend.svg)](https://github.com/poliedro-polimi/Crowdfunding-Backend/blob/master/LICENSE) [![Author Gayness](https://img.shields.io/badge/author%20gayness-100%25-ff69b4.svg)](https://github.com/Depau) 




Il back-end gestisce i pagamenti con PayPal e si occupa di memorizzare i dettagli delle donazioni e delle prenotazioni su un database.

Verrà hostato su PythonAnywhere ([poliedropolimi.pythonanywhere.com](https://poliedropolimi.pythonanywhere.com)).

Il [front-end](https://github.com/poliedro-polimi/Crowdfunding-Frontend) invece è scritto in PHP, verrà hostato sul servizio di web hosting già utilizzato da PoliEdro ([donate.poliedro-polimi.it](https://donate.poliedro-polimi.it)).

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

## Compatibilità

Il software è scritto e viene testato su Python3 e PyPy3. La compatibilita con Python2 e PyPy non è garantita.

In linea di massima è compatibile con tutti i sistemi operativi per i quali è disponibile Python3 e tutte le dipendenze richieste; tuttavia viene testato solo su Linux.