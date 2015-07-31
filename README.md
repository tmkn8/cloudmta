# Informacje
Repozytorium zawiera stronę internetową CloudMTA napisaną w Pythonie z użyciem Django. Po stronie front-endu używamy technologii takich jak Sass, Bower oraz Grunt.

# Instalacja w środowisku lokalnym
Jeżeli chcesz pokodzić na swoim hoście lokalnym, to możesz skorzystać z poniższej instrukcji, żeby skonfigurować środowisko.

**W środowisku lokalnym nie używamy backendu MyBB do logowania.**

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


Wejdź w folder `vm-www` i pobierz moduły Puppeta.
```
cd vm-www
git submodule init
git submodule update
```


Włącz Vagranta. Proces zajmie trochę czasu (z 10-15 minut), gdyż Puppet musi skonfigurować maszynę.
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


Teraz musimy dodać plik ustawień z `SECRET_KEY`, który nie jest trzymany w repozytorium. Stwórz plik `cloudmta/settings/secrets.json` o poniższej treści i wstaw w nim swój klucz.

*Możesz użyć [generatora](http://www.miniwebtool.com/django-secret-key-generator/), żeby uzyskać klucz.*
```
{
  "SECRET_KEY": "Twój klucz"
}
```


Odpal środowisko wirtualne Pythona.
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


Zedytuj plik `etc/hosts` Twojego systemu operacyjnego (hosta, nie gościa), żeby dodać domenę.
```
127.0.0.1   cloudmta.dev
```


Strona powinna odpowiadać jak należy pod adresem `http://cloudmta.dev:8080/`.

Teraz należy skompilować SCSS. Aby to zrobić udaj się do folderu z plikami frontu strony oraz zainstaluj wszystkie zależności.
```
cd /cloudmta/front
npm install
bower install
```


Uruchom Grunt w celu skompilowania wszystkich potrzebnych plików.
```
grunt
```


Front strony powinien działać jak należy.


# Ustawienia projektu
Większość ustawień jest trzymanych w repozytorium. Ustawienia, które zawierają hasła oraz klucz aplikacji, są trzymanie poza repozytorium w pliku `cloudmta/settings/secrets.json`. Przykłady plik ustawień znajduje się w `cloudmta/settings/secrets.json.example` ([link](https://gitlab.com/cloudmta/www/blob/master/cloudmta/settings/secrets.json.example)).
