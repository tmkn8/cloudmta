# Informacje
Repozytorium zawiera stronę internetową CloudMTA napisaną w Pythonie z użyciem Django. Po stronie front-endu używamy technologii takich jak Sass, Bower oraz Grunt.

# Instalacja
1. Sklonuj repozytorium. ``git clone git@gitlab.com:cloudmta/cloudmta-www.git``
2. Zainstaluj aplikacje Pythona wymagane przez ten projekt. ``pip install -r requiremenets.txt``
3. Ustaw szczegóły połączenia z bazą danych MySQL w ``cloudmta/settings/secrets.json``.
4. Zmigruj bazę danych komendą ``./mng_dev.py migrate`` lub ``./mng_prod.py``.
5. Wejdź w folder ``front`` i wykonaj komendy ``npm install``, ``bower install`` oraz ``grunt``.
6. Zainstaluj MyBB na tej samej bazie danych oraz stwórz użytkownika.
7. Wykonaj poniższy kod w ``./mng_dev.py shell`` lub ``./mng_prod.py shell``:
 ```
 from accounts.models import User
 u = User.objects.get(pk=1)
 u.is_staff = True
 u.is_superuser = True
 u.save()
 ```