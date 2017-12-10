from flask import session

lang = {}

eng = {
    "language": "language",
    "eng": "english",
    "jpn": "japanese",
    "spn": "spanish",
    "ger": "german",
    "fre": "french",
    "hello": "hi",
    "accept": "OK",
    "cancel": "cancel",
    "save": "save",
    "unrated": "unrated",
    "by": "by",
    "delete": "delete",
    "confirm_delete": "Are you sure you want to delete \"{{ book }}\"?",
    "all": "all",
    "lend": "lend",
    "title": "title",
    "home": "home",
    "user": "user",
    "password": "password",
    "admin": "admin",
    "login": "login",
    "logout": "logout",
    "sort": "sort",
    "name": "name",
    "given_name": "First",
    "surname": "Last",
    "email": "email",
    "author": "author",
    "synopsis": "synopsis"
}

jpn = {
    "language": "言語",
    "eng": "英語",
    "jpn": "日本語",
    "spn": "スペイン語",
    "ger": "ドイツ語",
    "fre": "フランチェス語",
    "hello": "こうにちわ",
    "accept": "OK",
    "cancel": "キャンセル",
    "delete": "削除",
    "confirm_delete": "「{{ book }}」を削除してもよろしいですか？",
    "save": "ほぞん",
    "unrated": "評価なし",
    "by": "〜によって",
    "all": "すべて",
    "lend": "貸す",
    "yes": "はい",
    "title": "書名",
    "home": "ホームページ",
    "user": "りようしゃ",
    "password": "パスワード",
    "admin": "たんとうしゃ",
    "login": "ログイン ",
    "logout": "ログアウト",
    "sort": "ソート",
    "name": "名前",
    "given_name": "名",
    "surname": "姓",
    "email": "メールアドレス",
    "author": "著者",
    "synopsis": "概要"
}

spn = {
    "language": "idioma",
    "eng": "Inglés",
    "jpn": "japonés",
    "spn": "Español",
    "ger": "alemán",
    "fre": "francés",
    "hello": "Hola",
    "accept": "OK",
    "cancel": "cancelar",
    "save": "guardar",
    "unrated": "sin calificación",
    "by": "por",
    "delete": "borrar",
    "confirm_delete": "¿Estás seguro de que deseas eliminar el \"{{ book }}\"?",
    "all": "all (need spanish)",
    "lend": "lend (need spanish)",
    "yes": "Si",
    "title": "título",
    "home": "la página inicial",
    "user": "Internauta",
    "password": "la contraseña",
    "admin": "administrador",
    "login": "entrar",
    "logout": "cerrar sessión",
    "sort": "ordenar",
    "name": "nombre",
    "given_name": "nombre de pila",
    "surname": "apellido",
    "email": "email",
    "author": "Autor",
    "synopsis": "Sinopsis"
}

ger = {
    "language": "Sprache",
    "eng": "english",
    "jpn": "japanisch",
    "spn": "Spanisch",
    "ger": "Deutsche",
    "fre": "Französisch",
    "hello": "Hallo",
    "accept": "OK",
    "cancel": "stornieren",
    "save": "speichern",
    "unrated": "Unbewertet",
    "by": "durch",
    "delete": "dlöschen",
    "confirm_delete": "Möchten Sie \"{{ book }}\" wirklich löschen?",
    "all": "alle",
    "lend": "verleihen",
    "yes": "Ja",
    "title": "Titel",
    "home": "Startseite",
    "user": "Anwender",
    "password": "Passwort",
    "admin": "Administrator",
    "login": "einloggen",
    "logout": "ausloggen",
    "sort": "Sortieren",
    "name": "Name",
    "given_name": "Vorname",
    "surname": "Familien-oder Nachname",
    "email": "E-Mail-Adresse",
    "author": "Autor",
    "synopsis": "Zusammenfassung"
}

fre = {
    "language": "la langue",
    "eng": "Anglais",
    "jpn": "Japonais",
    "spn": "Espanol",
    "ger": "allemand",
    "fre": "français",
    "hello": "Bonjour",
    "accept": "OK",
    "cancel": "Annuler",
    "save": "Enregistre",
    "unrated": "non évalué",
    "by": "par",
    "delete": "effacer",
    "confirm_delete": "Êtes - vous sûr de vouloir supprimer \"{{ book }}\"?",
    "all": "tout",
    "lend": "prêter",
    "yes": "Oui",
    "title": "Titre",
    "home": "d'accueil",
    "user": "utilisateur",
    "password": "mot de passe",
    "admin": "administrateur",
    "login": "Connexion",
    "logout": "Connectez - Out",
    "sort": "Trier",
    "name": "nom complet",
    "given_name": "prénom",
    "surname": "nom de famille",
    "email": "adresse e-mail",
    "author": "auteur",
    "synopsis": "synopsis"
}

template = {
    "language": "",
    # "add any new languages here": "",
    "eng": "",
    "jpn": "",
    "spn": "",
    "ger": "",
    "fre": "",
    "hello": "",
    "accept": "",
    "cancel": "",
    "save": "",
    "unrated": "",
    "by": "",
    "delete": "",
    "confirm_delete": "",
    "all": "",
    "lend": "",
    "yes": "",
    "title": "",
    "home": "",
    "user": "",
    "password": "",
    "admin": "",
    "login": "",
    "logout": "",
    "sort": "",
    "name": "",
    "given_name": "",
    "surname": "",
    "email": "",
    "author": "",
    "synopsis": ""
}

# need to add new languages to dictionary
lang["eng"] = eng
lang["jpn"] = jpn
lang["spn"] = spn
lang["ger"] = ger
lang["fre"] = fre


def set_language():
    if 'lang' in session.keys():
        if session.get('lang'):
            return session['lang']
        else:
            return "eng"
    else:
        return "eng"