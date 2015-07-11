from django.utils.translation import ugettext as _

# Domyślne pieniądze przy tworzeniu postaci
RP_DEFAULT_CHARACTER_MONEY = 350

# Wymagana liczba godzin na aktywnych postaciach przy zakładaniu innej w sekundach
RP_MIN_CHARACTER_TIME = 5*3600

# Liczba pytań w quizie
RP_TEST_QUESTIONS_NUMBERS = 3

# Minimalny wiek postaci
RP_MIN_AGE_OF_CHARACTER = 16

# Maksymalny wiek postaci
RP_MAX_AGE_OF_CHARACTER = 100

# Scieżka do plików skinów w static
RP_SKINS_STATIC_DIRECTORY = 'skins'

# Format obrazków skinów
RP_SKINS_IMG_FORMAT = 'png'

# Typy przedmiotów
ITEM_TYPE_CHOICES = (
    (1, 'Jakiś typ'),
)
