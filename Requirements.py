import sys, subprocess

r"""
This script requires the following prerequisites to function properly:
  Install:
    - Python 3.13.7: https://www.python.org/downloads/release/python-3137/
    - ODBC Driver 17 or 18 for SQL Server: https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server
    - Microsoft Access Driver (*.mdb, *.accdb): https://www.microsoft.com/en-us/download/details.aspx?id=54920
  Setup:
    - In VS Code Settings, update Default interpreter path to: "C:\Users\USERNAME\AppData\Local\Programs\Python\Python313\python.exe"
    - Add "C:\Users\USERNAME\AppData\Local\Programs\Python\Python313\Scripts\" to PATHS (in "Edit the system variables" windows app)
    - Run the following CMD to install libraries using the specified python version: 
    - "C:\Users\USERNAME\AppData\Local\Programs\Python\Python313\python.exe" -m pip install pyodbc==5.2.0 sqlalchemy==2.0.43 pandas==2.3.1 numpy==2.3.2 openpyxl==3.1.5
    - Run the below script to confirm the correct versions installed
"""

def Install_Libraries():
    libraries = {
        "pyodbc": "5.2.0",
        "sqlalchemy": "2.0.43",
        "pandas": "2.3.1",
        "numpy": "2.3.2",
        "openpyxl": "3.1.5"
    }
    for library, version in libraries.items():
        result = subprocess.run([
            sys.executable,
            "-m",
            "pip",
            "install",
            f"{library}=={version}"
        ])
        if result.returncode != 0:
            print(f"Failed to install {library}")

def Validate_Libraries():
    import pyodbc, sqlalchemy, pandas, numpy, openpyxl 
    print("Python Library Checks:")
    requiredVersions = {
        "Python": "3.13.7",
        "pyodbc": "5.2.0",
        "SQLAlchemy": "2.0.43",
        "Pandas": "2.3.1",
        "NumPy": "2.3.2",
        "Openpyxl": "3.1.5"
    }
    libraryVersions = {
        "Python": sys.version.split()[0],
        "pyodbc": pyodbc.__version__,
        "SQLAlchemy": sqlalchemy.__version__,
        "Pandas": pandas.__version__,
        "NumPy": numpy.__version__,
        "Openpyxl": openpyxl.__version__
    }
    for name, installed in libraryVersions.items():
        required = requiredVersions.get(name)
        if required and installed != required:
            print(f"- {name}: {installed}  (*UPDATE REQUIRED: {required}*)")
        else:
            print(f"- {name}: {installed}")

def Validate_Drivers():
    import pyodbc
    print("ODBC Driver Checks:")
    drivers = pyodbc.drivers()
    # SQL Server ODBC Driver check
    if any(d in drivers for d in [
        "ODBC Driver 17 for SQL Server",
        "ODBC Driver 18 for SQL Server"
    ]):
        print("- SQL Server ODBC driver installed")
    else:
        raise RuntimeError(
            "- Missing SQL Server ODBC driver "
            "(ODBC Driver 17 or 18 required)"
        )
    # Microsoft Access Driver check
    if "Microsoft Access Driver (*.mdb, *.accdb)" in drivers:
        print("- Microsoft Access driver installed")
    else:
        print("- Missing Microsoft Access driver")

def main():
    Install_Libraries()
    Validate_Libraries()
    Validate_Drivers()
    
if __name__ == "__main__":
    main()