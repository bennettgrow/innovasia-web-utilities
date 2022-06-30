# innovasia-web-utilities
 
## Installation
Reccomended python version 3.10 or greater.
MSSQL databases are supported using client based Microsoft ODBC, hence SQLAlchemy utilizing pyodbc with a DSN. For a 32-bit SQL server, 32 bit python must be used with a 32 bit ODBC DSN. See configuration section below.

---

### Steps for 32 bit operations:
- Install python 3.10 32 bit
- Upgrade pip to the latest version
  
    ` py -3.10-32 -m pip install --upgrade pip `

- Clone this repository
- Create a virtual environment in the main directory.

    ` py  -3.10-32 -m venv venv-32`

- Enter the virtual environment

    ` .\venv-32\Scripts\activate `

- Install required packages

    ` pip install -r .\requirements.txt `

    > Note: Issues using pip to install legacy 32 bit packages exist. If "buildtools" cannot be installed with pip, install Microsoft C++ Buildtools (https://visualstudio.microsoft.com/visual-cpp-build-tools/), launch, modify, and enable "Desktop development using C++". Then reattempt installing packages.

- Exit the virtual environment when installation is complete

    ` deactivate `

---
### Configuration
A configuration file must be created in the main directory called `config.ini` . This allows, usually sensitive, information to be stored separately from the other files. Currently, `config.ini` must look something like this:

```
[flask]
debug=true
secret_key=somesecretkey

[odbc]
dsn=dsnname
uid=username
pwd=password
```
[flask] 
- debug set to anything other than `false` will run the app in debug mode.
- The secret key is used to encrypt cookies.

[odbc] 
- App is currently configured such that an ODBC DSN must be configured for use with a MSSQL database. As mentioned above, a 32-bit SQL server/DSN must use a 32-bit python installation. 

---
### To start the server:
- Enter the virtual environment

    ` .\venv-32\Scripts\activate`

- Run `run.py`

    ` python run.py `
---
### To stop the server
- `Ctrl-C` to halt
- `deactivate` to exit virtual environment
---
