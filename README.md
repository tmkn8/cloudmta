# Informacje
Repozytorium zawiera stronę internetową CloudMTA napisaną w Pythonie z użyciem Django. Po stronie front-endu używamy technologii takich jak Sass, Bower oraz Grunt.

# Instalacja w środowisku programistycznym
Jeżeli chcesz pokodzić na swoim hoście lokalnym, to możesz skorzystać z poniższej instrukcji, żeby skonfigurować środowisko.
## Wymagania
* Vagrant
* VirtualBox
* Git

## Proces
Sklonuj dwa repozytoria - wirtualną maszynę oraz stronę WWW. Obydwa repozytoria muszą być sklonowane w jednym folderze.
```
git clone git@gitlab.com:cloudmta/vm-www.git
git clone git@gitlab.com:cloudmta/www.git
```

Wejdź w folder `vm-cloudmta-www` i pobierz moduły Puppeta.
```
cd vm-cloudmta-www
git submodule init
git submodule update
```

Włącz Vagranta. Proces zajmie trochę czasu, gdyż musi skonfigurować maszynę.
```
vagrant up
```

W razie wystąpienia błędów przy poprzednim, wpisz poniższą komendę.
```
vagrant reload --provision
```

Zaloguj się do maszyny przez SSH oraz przejdź do folderu projektu w maszynie wirtualnej.
```
vagrant ssh
cd /cloudmta
```

Odpal środowisko wirtualnej.
```
source env/bin/activate
```

Przeprowadź migrację bazy danych.
```
./mng_dev.py migrate
```

Jeżeli nie poprosiło Cię o stworzenie użytkownika, zrób to teraz.
```
./mng_dev.py createsuperuser
```

Zrestartuj serwer WSGI.
```
sudo service gunicorn restart
```

Zedytuj plik `etc/hosts`, żeby dodać domenę.
```
127.0.0.1   cloudmta.dev
```

Strona powinna działać jak należy pod adresem `http://cloudmta.dev:8080/`