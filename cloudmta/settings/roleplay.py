from django.utils.translation import ugettext as _

# Długość serialu w MTA
RP_SERIAL_LENGTH = 32

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
RP_SKINS_STATIC_DIRECTORY = 'img/skins'

# Format obrazków skinów
RP_SKINS_IMG_FORMAT = 'png'

# Typy własności przedmiotów
RP_ITEM_OWNER_TYPE_ID_NONE = 0
RP_ITEM_OWNER_TYPE_ID_CHARACTER = 1
RP_ITEM_OWNER_TYPE_ID_VEHICLE = 3
RP_ITEM_OWNER_TYPE_ID_DOOR = 4

# Typy własności pojazdów
RP_VEHICLE_OWNER_TYPE_ID_NONE = 0
RP_VEHICLE_OWNER_TYPE_ID_CHARACTER = 1
RP_VEHICLE_OWNER_TYPE_ID_GROUP = 2

# Typy właścicieli drzwi
RP_DOOR_OWNER_TYPE_ID_NONE = 0
RP_DOOR_OWNER_TYPE_ID_CHARACTER = 1
RP_DOOR_OWNER_TYPE_ID_GROUP = 2

# Maksymalna liczba grup na postać
RP_MAX_GROUP_NUMBER = 5

# Kiedy wygasają logi kar w profilu użytkowników (dni)
RP_PENALTY_LOGS_EXPIRY_DATE = 90*24*3600
