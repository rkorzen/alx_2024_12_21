# Podstawy pracy z Pythonem

## 1. Instalacja Pythona

### Windows
- Pobierz instalator z [python.org](https://www.python.org/downloads/)
- Zalecana wersja: Python 3.8 lub nowsza
- Podczas instalacji zaznacz opcję "Add Python to PATH"
- Zaznacz opcję "Install pip"
- Sprawdź instalację w terminalu:
```bash
python --version
```

### MacOS
- Zainstaluj przez Homebrew:
```bash
brew install python
```
- Lub pobierz instalator z [python.org](https://www.python.org/downloads/)

### Linux
- Python jest zazwyczaj preinstalowany
- Jeśli nie, użyj menedżera pakietów:
```bash
# Ubuntu/Debian
sudo apt install python3

# Fedora
sudo dnf install python3
```

## 2. Środowiska wirtualne

### Po co używać środowisk wirtualnych?
- Izolacja zależności między projektami
- Unikanie konfliktów między wersjami pakietów
- Łatwiejsze zarządzanie wymaganiami projektu
- Możliwość pracy z różnymi wersjami Pythona

### Podstawowe narzędzia

#### venv (wbudowane)
```bash
# Tworzenie
python -m venv nazwa_srodowiska

# Aktywacja
# Windows
nazwa_srodowiska\Scripts\activate
# Unix
source nazwa_srodowiska/bin/activate

# Dezaktywacja
deactivate
```

#### virtualenv (rozszerzone możliwości)
```bash
# Instalacja
pip install virtualenv

# Tworzenie z konkretną wersją Pythona
virtualenv -p python3.8 nazwa_srodowiska
```

#### Zaawansowane narzędzia

##### Poetry
```bash
# Instalacja
curl -sSL https://install.python-poetry.org | python3 -

# Inicjalizacja projektu
poetry new nazwa_projektu

# Dodawanie zależności
poetry add requests

# Aktywacja środowiska
poetry shell
```

##### Pipenv
```bash
# Instalacja
pip install pipenv

# Tworzenie środowiska
pipenv install

# Aktywacja
pipenv shell
```

##### uv - nowoczesny menedżer pakietów Python

uv to nowoczesne narzędzie do zarządzania pakietami i środowiskami wirtualnymi w Pythonie, stworzone jako szybsza alternatywa dla pip. Napisane w języku Rust, oferuje znaczące przyspieszenie w porównaniu do tradycyjnych narzędzi.

Instalacja uv:
```bash
# Na systemach Unix (Linux/MacOS)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Przez pip (wszystkie systemy)
pip install uv

# Przez Homebrew (MacOS)
brew install uv
```

Weryfikacja instalacji:
```bash
uv --version
```

# Tworzenie środowiska
uv venv

# Instalacja pakietów (znacznie szybsza niż pip)
uv pip install requests

# Instalacja z requirements.txt
uv pip install -r requirements.txt

# Generowanie requirements.txt
uv pip freeze > requirements.txt
```

Zalety uv:
- Napisane w Rust, znacznie szybsze niż pip
- Kompatybilne z pip
- Współbieżna instalacja zależności
- Inteligentne cachowanie pakietów
- Obsługa wheel i sdist
- Zoptymalizowane rozwiązywanie zależności

### Aktywacja środowiska wirtualnego

Dla systemów Unix (Linux/MacOS):
```bash
source nazwa_srodowiska/bin/activate
# lub
. nazwa_srodowiska/bin/activate
```

Dla Windows PowerShell:
```powershell
.\nazwa_srodowiska\Scripts\Activate.ps1
```

Dla Windows Command Prompt:
```cmd
nazwa_srodowiska\Scripts\activate.bat
```

## 3. Uruchamianie skryptów

### Podstawowe uruchomienie
```bash
python script.py
```

### Zaawansowane opcje

#### Flagi interpretera
```bash
# Optymalizacja
python -O script.py

# Debugowanie
python -d script.py

# Sprawdzanie składni bez uruchamiania
python -m py_compile script.py
```

#### Moduły jako skrypty
```bash
# Uruchomienie modułu
python -m nazwa_modulu

# Uruchomienie z argumentami
python script.py arg1 arg2
```

#### IPython
```bash
# Instalacja
pip install ipython

# Uruchomienie
ipython

# Uruchomienie skryptu
%run script.py
```

### Zaawansowane opcje uruchamiania

```bash
# Uruchomienie z optymalizacją
python -O script.py  # usuwa asercje
python -OO script.py # usuwa asercje i docstringi

# Uruchomienie z debuggerem
python -m pdb script.py

# Sprawdzanie składni
python -m py_compile script.py

# Pomiar czasu wykonania
python -m timeit "kod_do_zmierzenia"

# Profiler
python -m cProfile script.py
```

## 4. Środowiska programistyczne (IDE)

### Visual Studio Code
- Darmowy, lekki, rozszerzalny
- Niezbędne rozszerzenia:
  - Python (Microsoft)
  - Pylance
  - Python Test Explorer
  - Python Docstring Generator

### PyCharm
- Profesjonalne IDE
- Dostępne w wersji Community (darmowa) i Professional
- Wbudowane narzędzia:
  - Debugger
  - Profiler
  - Zarządzanie środowiskami
  - Integracja z systemami kontroli wersji

### Jupyter Notebook/Lab
```bash
# Instalacja
pip install jupyter

# Uruchomienie
jupyter notebook
# lub
jupyter lab
```

### Spyder
- Dedykowany dla data science
- Podobny do RStudio
- Wbudowane narzędzia analityczne

## Dobre praktyki

### Zarządzanie projektem
- Używaj `.gitignore` dla środowisk wirtualnych
- Trzymaj `requirements.txt` lub `pyproject.toml` w repozytorium
- Dokumentuj zależności i proces instalacji

### Struktura projektu
```
projekt/
├── .gitignore
├── README.md
├── requirements.txt
├── src/
│   └── projekt/
│       ├── __init__.py
│       └── main.py
└── tests/
    └── __init__.py
```

### Narzędzia pomocnicze
- `black` - formatowanie kodu
- `flake8` - linter
- `mypy` - sprawdzanie typów
- `pytest` - testy jednostkowe

### Podstawowe zarządzanie pakietami (pip)
```bash
# Aktualizacja pip
python -m pip install --upgrade pip

# Instalacja pakietu
pip install nazwa_pakietu

# Instalacja konkretnej wersji
pip install nazwa_pakietu==1.0.0

# Aktualizacja pakietu
pip install --upgrade nazwa_pakietu
```

### Zmienne środowiskowe
- PYTHONPATH - ścieżka do modułów
- PYTHONHOME - lokalizacja instalacji Pythona
- VIRTUAL_ENV - ścieżka do aktywnego środowiska wirtualnego

### VS Code i środowiska wirtualne

1. Utworzenie środowiska:
   - Ctrl/Cmd + Shift + P
   - "Python: Create Environment"
   - Wybierz venv lub conda

2. Wybór interpretera:
   - Ctrl/Cmd + Shift + P
   - "Python: Select Interpreter"
   - Wybierz środowisko z listy

3. Integracja z terminalem:
   - VS Code automatycznie aktywuje wybrane środowisko w zintegrowanym terminalu

### Dobre praktyki bezpieczeństwa
- Nie przechowuj haseł i kluczy API w kodzie
- Używaj plików .env dla zmiennych środowiskowych
- Regularnie aktualizuj zależności
- Sprawdzaj znane podatności (np. używając safety)

### Dobre praktyki wydajności
- Używaj list comprehension zamiast pętli gdzie to możliwe
- Preferuj generatory dla dużych zbiorów danych
- Wykorzystuj wbudowane funkcje Pythona
- Profiluj kod przed optymalizacją
