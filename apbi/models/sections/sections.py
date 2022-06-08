"""All sections and categories from bazos."""


from typing import Optional, Type


class Category:
    """Base category class."""

    section_name: str = None
    section_rss: str = None
    category_name: str = None
    category_rss: str = None

    search: str = None
    postal_code: str = None
    vicinity: int = None
    price_min: int = None
    price_max: int = None

    def __init__(
        self,
        search: str = None,
        postal_code: str = None,
        vicinity: int = None,
        price_min: int = None,
        price_max: int = None,
    ):
        self.search = search
        self.postal_code = postal_code
        self.vicinity = vicinity
        self.price_min = price_min
        self.price_max = price_max


class SECTION_ZVIERATA(Category):
    """SECTION_ZVIERATA."""

    section_name = "zvierata"
    section_rss = "zv"

    AKVARIJNE_RYBICKY: Optional[Type["AKVARIJNE_RYBICKY"]] = None
    DROBNE_CICAVCE: Optional[Type["DROBNE_CICAVCE"]] = None
    KONE: Optional[Type["KONE"]] = None
    KONE_POTREBY: Optional[Type["KONE_POTREBY"]] = None
    KONE_SLUZBY: Optional[Type["KONE_SLUZBY"]] = None
    MACKY: Optional[Type["MACKY"]] = None
    PSY: Optional[Type["PSY"]] = None
    VTACTVO: Optional[Type["VTACTVO"]] = None
    TERARIJNE_ZVIERATA: Optional[Type["TERARIJNE_ZVIERATA"]] = None
    OSTATNE_DOMACE: Optional[Type["OSTATNE_DOMACE"]] = None
    KRYTIE: Optional[Type["KRYTIE"]] = None
    STRATENI_A_NAJDENI: Optional[Type["STRATENI_A_NAJDENI"]] = None
    CHOVATELSKE_POTREBY: Optional[Type["CHOVATELSKE_POTREBY"]] = None
    SLUZBY_PRE_ZVIERATA: Optional[Type["SLUZBY_PRE_ZVIERATA"]] = None
    HYDINA: Optional[Type["HYDINA"]] = None
    KRALIKY: Optional[Type["KRALIKY"]] = None
    OVCE_A_KOZY: Optional[Type["OVCE_A_KOZY"]] = None
    PRASATA: Optional[Type["PRASATA"]] = None
    DOBYTOK: Optional[Type["DOBYTOK"]] = None
    OSTATNE_HOSPODARSKE: Optional[Type["OSTATNE_HOSPODARSKE"]] = None


class AKVARIJNE_RYBICKY(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> AKVARIJNE_RYBICKY."""

    category_name = "ryba"
    category_rss = "33"


class DROBNE_CICAVCE(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> DROBNE_CICAVCE."""

    category_name = "cicavec"
    category_rss = "34"


class KONE(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> KONE."""

    category_name = "kon"
    category_rss = "35"


class KONE_POTREBY(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> KONE_POTREBY."""

    category_name = "konepotreby"
    category_rss = "50"


class MACKY(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> MACKY."""

    category_name = "macka"
    category_rss = "36"


class PSY(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> PSY."""

    category_name = "pes"
    category_rss = "37"


class VTACTVO(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> VTACTVO."""

    category_name = "vtak"
    category_rss = "38"


class TERARIJNE_ZVIERATA(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> TERARIJNE_ZVIERATA."""

    category_name = "zviera"
    category_rss = "39"


class OSTATNE_DOMACE(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> OSTATNE_DOMACE."""

    category_name = "ostatnidomaci"
    category_rss = "40"


class KRYTIE(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> KRYTIE."""

    category_name = "kryti"
    category_rss = "42"


class STRATENI_A_NAJDENI(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> STRATENI_A_NAJDENI."""

    category_name = "strateni"
    category_rss = "255"


class CHOVATELSKE_POTREBY(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> CHOVATELSKE_POTREBY."""

    category_name = "potreby"
    category_rss = "41"


class HYDINA(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> HYDINA."""

    category_name = "hydina"
    category_rss = "44"


class KRALIKY(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> KRALIKY."""

    category_name = "kralik"
    category_rss = "45"


class OVCE_A_KOZY(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> OVCE_A_KOZY."""

    category_name = "koza"
    category_rss = "46"


class PRASATA(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> PRASATA."""

    category_name = "prase"
    category_rss = "47"


class DOBYTOK(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> DOBYTOK."""

    category_name = "dobytok"
    category_rss = "48"


class OSTATNE_HOSPODARSKE(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> OSTATNE_HOSPODARSKE."""

    category_name = "ostatnihospodarska"
    category_rss = "49"


class SECTION_DETI(Category):
    """SECTION_DETI."""

    section_name = "deti"
    section_rss = "de"

    AUTOSEDACKY: Optional[Type["AUTOSEDACKY"]] = None
    BABY_MONITORY: Optional[Type["BABY_MONITORY"]] = None
    BICYKLE: Optional[Type["BICYKLE"]] = None
    DETSKA_LITERATURA: Optional[Type["DETSKA_LITERATURA"]] = None
    HRACKY: Optional[Type["HRACKY"]] = None
    CHODITKA_A_HOPSADLA: Optional[Type["CHODITKA_A_HOPSADLA"]] = None
    KOCIKY: Optional[Type["KOCIKY"]] = None
    KOJENECKE_POTREBY: Optional[Type["KOJENECKE_POTREBY"]] = None
    NABYTOK_PRE_DETI: Optional[Type["NABYTOK_PRE_DETI"]] = None
    NOSICE: Optional[Type["NOSICE"]] = None
    ODRAZADLA: Optional[Type["ODRAZADLA"]] = None
    SEDACKY_NA_BICYKEL: Optional[Type["SEDACKY_NA_BICYKEL"]] = None
    SPORTOVE_POTREBY: Optional[Type["SPORTOVE_POTREBY"]] = None
    SKOLSKE_POTREBY: Optional[Type["SKOLSKE_POTREBY"]] = None
    STRAZENIE_DETI: Optional[Type["STRAZENIE_DETI"]] = None
    OSTATNE: Optional[Type["OSTATNE"]] = None
    BODY_DUPACKY_A_OVERALY: Optional[Type["BODY_DUPACKY_A_OVERALY"]] = None
    BUNDY_A_KABATIKY: Optional[Type["BUNDY_A_KABATIKY"]] = None
    CIAPKY_A_KLOBUCIKY: Optional[Type["CIAPKY_A_KLOBUCIKY"]] = None
    NOHAVICE_KRATASY_A_TEPLAKY: Optional[Type["NOHAVICE_KRATASY_A_TEPLAKY"]] = None
    KOMBINEZY: Optional[Type["KOMBINEZY"]] = None
    KOMPLETY: Optional[Type["KOMPLETY"]] = None
    MIKINY_A_SVETRE: Optional[Type["MIKINY_A_SVETRE"]] = None
    OBUV: Optional[Type["OBUV"]] = None
    PLAVKY: Optional[Type["PLAVKY"]] = None
    PONOZKY_A_PANCUSKY: Optional[Type["PONOZKY_A_PANCUSKY"]] = None
    PYZAMKA_A_ZUPANCEKY: Optional[Type["PYZAMKA_A_ZUPANCEKY"]] = None
    RUKAVICE_A_SALY: Optional[Type["RUKAVICE_A_SALY"]] = None
    SPODNA_BIELIZEN: Optional[Type["SPODNA_BIELIZEN"]] = None
    SUKNICKY_A_SATOCKY: Optional[Type["SUKNICKY_A_SATOCKY"]] = None
    TEHOTENSKE_OBLECENIE: Optional[Type["TEHOTENSKE_OBLECENIE"]] = None
    TRICKA_A_KOSIELKY: Optional[Type["TRICKA_A_KOSIELKY"]] = None
    OSTATNE_OBLECENIE: Optional[Type["OSTATNE_OBLECENIE"]] = None


class AUTOSEDACKY(SECTION_DETI):
    """SECTION_DETI -> AUTOSEDACKY."""

    category_name = "autosedacky"
    category_rss = "120"


class BABY_MONITORY(SECTION_DETI):
    """SECTION_DETI -> BABY_MONITORY."""

    category_name = "baby"
    category_rss = "121"


class BICYKLE(SECTION_DETI):
    """SECTION_DETI -> BICYKLE."""

    category_name = "bicykle"
    category_rss = "452"


class HRACKY(SECTION_DETI):
    """SECTION_DETI -> HRACKY."""

    category_name = "hracky"
    category_rss = "122"


class CHODITKA_A_HOPSADLA(SECTION_DETI):
    """SECTION_DETI -> CHODITKA_A_HOPSADLA."""

    category_name = "choditka"
    category_rss = "123"


class KOCIKY(SECTION_DETI):
    """SECTION_DETI -> KOCIKY."""

    category_name = "kociky"
    category_rss = "124"


class KOJENECKE_POTREBY(SECTION_DETI):
    """SECTION_DETI -> KOJENECKE_POTREBY."""

    category_name = "kojenecke"
    category_rss = "126"


class NABYTOK_PRE_DETI(SECTION_DETI):
    """SECTION_DETI -> NABYTOK_PRE_DETI."""

    category_name = "nabytok"
    category_rss = "127"


class NOSICE(SECTION_DETI):
    """SECTION_DETI -> NOSICE."""

    category_name = "nositka"
    category_rss = "128"


class ODRAZADLA(SECTION_DETI):
    """SECTION_DETI -> ODRAZADLA."""

    category_name = "odrazadla"
    category_rss = "130"


class SEDACKY_NA_BICYKEL(SECTION_DETI):
    """SECTION_DETI -> SEDACKY_NA_BICYKEL."""

    category_name = "sedacky"
    category_rss = "131"


class SPORTOVE_POTREBY(SECTION_DETI):
    """SECTION_DETI -> SPORTOVE_POTREBY."""

    category_name = "sportove"
    category_rss = "132"


class SKOLSKE_POTREBY(SECTION_DETI):
    """SECTION_DETI -> SKOLSKE_POTREBY."""

    category_name = "skolske"
    category_rss = "133"


class OSTATNE(SECTION_DETI):
    """SECTION_DETI -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "135"


class BODY_DUPACKY_A_OVERALY(SECTION_DETI):
    """SECTION_DETI -> BODY_DUPACKY_A_OVERALY."""

    category_name = "dupacky"
    category_rss = "136"


class BUNDY_A_KABATIKY(SECTION_DETI):
    """SECTION_DETI -> BUNDY_A_KABATIKY."""

    category_name = "bundy"
    category_rss = "137"


class CIAPKY_A_KLOBUCIKY(SECTION_DETI):
    """SECTION_DETI -> CIAPKY_A_KLOBUCIKY."""

    category_name = "ciapky"
    category_rss = "138"


class NOHAVICE_KRATASY_A_TEPLAKY(SECTION_DETI):
    """SECTION_DETI -> NOHAVICE_KRATASY_A_TEPLAKY."""

    category_name = "nohavice"
    category_rss = "139"


class KOMBINEZY(SECTION_DETI):
    """SECTION_DETI -> KOMBINEZY."""

    category_name = "kombinezy"
    category_rss = "140"


class KOMPLETY(SECTION_DETI):
    """SECTION_DETI -> KOMPLETY."""

    category_name = "komplety"
    category_rss = "438"


class MIKINY_A_SVETRE(SECTION_DETI):
    """SECTION_DETI -> MIKINY_A_SVETRE."""

    category_name = "mikiny"
    category_rss = "141"


class OBUV(SECTION_DETI):
    """SECTION_DETI -> OBUV."""

    category_name = "obuv"
    category_rss = "129"


class PLAVKY(SECTION_DETI):
    """SECTION_DETI -> PLAVKY."""

    category_name = "plavky"
    category_rss = "142"


class PONOZKY_A_PANCUSKY(SECTION_DETI):
    """SECTION_DETI -> PONOZKY_A_PANCUSKY."""

    category_name = "ponozky"
    category_rss = "143"


class PYZAMKA_A_ZUPANCEKY(SECTION_DETI):
    """SECTION_DETI -> PYZAMKA_A_ZUPANCEKY."""

    category_name = "pyzamka"
    category_rss = "144"


class RUKAVICE_A_SALY(SECTION_DETI):
    """SECTION_DETI -> RUKAVICE_A_SALY."""

    category_name = "rukavice"
    category_rss = "145"


class SPODNA_BIELIZEN(SECTION_DETI):
    """SECTION_DETI -> SPODNA_BIELIZEN."""

    category_name = "bielizen"
    category_rss = "146"


class SUKNICKY_A_SATOCKY(SECTION_DETI):
    """SECTION_DETI -> SUKNICKY_A_SATOCKY."""

    category_name = "suknicky"
    category_rss = "147"


class TRICKA_A_KOSIELKY(SECTION_DETI):
    """SECTION_DETI -> TRICKA_A_KOSIELKY."""

    category_name = "tricka"
    category_rss = "148"


class OSTATNE_OBLECENIE(SECTION_DETI):
    """SECTION_DETI -> OSTATNE_OBLECENIE."""

    category_name = "oblecenie"
    category_rss = "125"


class SECTION_REALITY(Category):
    """SECTION_REALITY."""

    section_name = "reality"
    section_rss = "re"

    BYTY: Optional[Type["BYTY"]] = None
    DOMY: Optional[Type["DOMY"]] = None
    NOVE_PROJEKTY: Optional[Type["NOVE_PROJEKTY"]] = None
    GARAZE: Optional[Type["GARAZE"]] = None
    HOTELY_RESTAURACIE: Optional[Type["HOTELY_RESTAURACIE"]] = None
    CHALUPY_CHATY: Optional[Type["CHALUPY_CHATY"]] = None
    KANCELARIE: Optional[Type["KANCELARIE"]] = None
    OBCHODNE_PRIESTORY: Optional[Type["OBCHODNE_PRIESTORY"]] = None
    POZEMKY: Optional[Type["POZEMKY"]] = None
    SKLADY: Optional[Type["SKLADY"]] = None
    ZAHRADY: Optional[Type["ZAHRADY"]] = None
    OSTATNE: Optional[Type["OSTATNE"]] = None
    BYTY: Optional[Type["BYTY"]] = None
    DOMY: Optional[Type["DOMY"]] = None
    NOVE_PROJEKTY: Optional[Type["NOVE_PROJEKTY"]] = None
    PODNAJOM_SPOLUBYVAJUCI: Optional[Type["PODNAJOM_SPOLUBYVAJUCI"]] = None
    GARAZE: Optional[Type["GARAZE"]] = None
    HOTELY_RESTAURACIE: Optional[Type["HOTELY_RESTAURACIE"]] = None
    UBYTOVANIE: Optional[Type["UBYTOVANIE"]] = None
    KANCELARIE: Optional[Type["KANCELARIE"]] = None
    OBCHODNE_PRIESTORY: Optional[Type["OBCHODNE_PRIESTORY"]] = None
    POZEMKY: Optional[Type["POZEMKY"]] = None
    SKLADY: Optional[Type["SKLADY"]] = None
    ZAHRADY: Optional[Type["ZAHRADY"]] = None
    OSTATNE: Optional[Type["OSTATNE"]] = None


class BYTY(SECTION_REALITY):
    """SECTION_REALITY -> BYTY."""

    category_name = "predam/byt"
    category_rss = "152&typ=1"


class DOMY(SECTION_REALITY):
    """SECTION_REALITY -> DOMY."""

    category_name = "predam/dom"
    category_rss = "155&typ=1"


class NOVE_PROJEKTY(SECTION_REALITY):
    """SECTION_REALITY -> NOVE_PROJEKTY."""

    category_name = "predam/projekty"
    category_rss = "166&typ=1"


class GARAZE(SECTION_REALITY):
    """SECTION_REALITY -> GARAZE."""

    category_name = "predam/garaz"
    category_rss = "160&typ=1"


class HOTELY_RESTAURACIE(SECTION_REALITY):
    """SECTION_REALITY -> HOTELY_RESTAURACIE."""

    category_name = "predam/restauracie"
    category_rss = "165&typ=1"


class CHALUPY_CHATY(SECTION_REALITY):
    """SECTION_REALITY -> CHALUPY_CHATY."""

    category_name = "predam/chata"
    category_rss = "157&typ=1"


class KANCELARIE(SECTION_REALITY):
    """SECTION_REALITY -> KANCELARIE."""

    category_name = "predam/kancelar"
    category_rss = "161&typ=1"


class OBCHODNE_PRIESTORY(SECTION_REALITY):
    """SECTION_REALITY -> OBCHODNE_PRIESTORY."""

    category_name = "predam/priestory"
    category_rss = "164&typ=1"


class POZEMKY(SECTION_REALITY):
    """SECTION_REALITY -> POZEMKY."""

    category_name = "predam/pozemok"
    category_rss = "158&typ=1"


class SKLADY(SECTION_REALITY):
    """SECTION_REALITY -> SKLADY."""

    category_name = "predam/sklad"
    category_rss = "162&typ=1"


class ZAHRADY(SECTION_REALITY):
    """SECTION_REALITY -> ZAHRADY."""

    category_name = "predam/zahrada"
    category_rss = "159&typ=1"


class OSTATNE(SECTION_REALITY):
    """SECTION_REALITY -> OSTATNE."""

    category_name = "predam/ostatni"
    category_rss = "163&typ=1"


class BYTY(SECTION_REALITY):
    """SECTION_REALITY -> BYTY."""

    category_name = "prenajmu/byt"
    category_rss = "152&typ=3"


class DOMY(SECTION_REALITY):
    """SECTION_REALITY -> DOMY."""

    category_name = "prenajmu/dom"
    category_rss = "155&typ=3"


class NOVE_PROJEKTY(SECTION_REALITY):
    """SECTION_REALITY -> NOVE_PROJEKTY."""

    category_name = "prenajmu/projekty"
    category_rss = "166&typ=3"


class PODNAJOM_SPOLUBYVAJUCI(SECTION_REALITY):
    """SECTION_REALITY -> PODNAJOM_SPOLUBYVAJUCI."""

    category_name = "prenajmu/podnajom"
    category_rss = "156&typ=3"


class GARAZE(SECTION_REALITY):
    """SECTION_REALITY -> GARAZE."""

    category_name = "prenajmu/garaz"
    category_rss = "160&typ=3"


class HOTELY_RESTAURACIE(SECTION_REALITY):
    """SECTION_REALITY -> HOTELY_RESTAURACIE."""

    category_name = "prenajmu/restauracie"
    category_rss = "165&typ=3"


class KANCELARIE(SECTION_REALITY):
    """SECTION_REALITY -> KANCELARIE."""

    category_name = "prenajmu/kancelar"
    category_rss = "161&typ=3"


class OBCHODNE_PRIESTORY(SECTION_REALITY):
    """SECTION_REALITY -> OBCHODNE_PRIESTORY."""

    category_name = "prenajmu/priestory"
    category_rss = "164&typ=3"


class POZEMKY(SECTION_REALITY):
    """SECTION_REALITY -> POZEMKY."""

    category_name = "prenajmu/pozemok"
    category_rss = "158&typ=3"


class SKLADY(SECTION_REALITY):
    """SECTION_REALITY -> SKLADY."""

    category_name = "prenajmu/sklad"
    category_rss = "162&typ=3"


class ZAHRADY(SECTION_REALITY):
    """SECTION_REALITY -> ZAHRADY."""

    category_name = "prenajmu/zahrada"
    category_rss = "159&typ=3"


class OSTATNE(SECTION_REALITY):
    """SECTION_REALITY -> OSTATNE."""

    category_name = "prenajmu/ostatni"
    category_rss = "163&typ=3"


class SECTION_PRACA(Category):
    """SECTION_PRACA."""

    section_name = "praca"
    section_rss = "pr"

    ADMINISTRATIVA: Optional[Type["ADMINISTRATIVA"]] = None
    CHEMIA_A_POTRAVINARSTVO: Optional[Type["CHEMIA_A_POTRAVINARSTVO"]] = None
    DOPRAVA_A_LOGISTIKA: Optional[Type["DOPRAVA_A_LOGISTIKA"]] = None
    FINANCIE_A_EKONOMIKA: Optional[Type["FINANCIE_A_EKONOMIKA"]] = None
    IT_A_TELEKOMUNIKACIE: Optional[Type["IT_A_TELEKOMUNIKACIE"]] = None
    MARKETING_A_REKLAMA: Optional[Type["MARKETING_A_REKLAMA"]] = None
    MANAGEMENT: Optional[Type["MANAGEMENT"]] = None
    OBCHOD_A_PREDAJ: Optional[Type["OBCHOD_A_PREDAJ"]] = None
    OBRANA_A_BEZPECNOST: Optional[Type["OBRANA_A_BEZPECNOST"]] = None
    POHOSTINSTVA_A_UBYTOVANIE: Optional[Type["POHOSTINSTVA_A_UBYTOVANIE"]] = None
    PRACA_V_DOMACNOSTI: Optional[Type["PRACA_V_DOMACNOSTI"]] = None
    PRAVO_LEGISLATIVA: Optional[Type["PRAVO_LEGISLATIVA"]] = None
    PRIEMYSEL_A_VYROBA: Optional[Type["PRIEMYSEL_A_VYROBA"]] = None
    REMESELNE_PRACE: Optional[Type["REMESELNE_PRACE"]] = None
    SERVIS_A_SLUZBY: Optional[Type["SERVIS_A_SLUZBY"]] = None
    STAVEBNICTVO: Optional[Type["STAVEBNICTVO"]] = None
    TECHNIKA_A_ENERGETIKA: Optional[Type["TECHNIKA_A_ENERGETIKA"]] = None
    TLAC_A_POLYGRAFIA: Optional[Type["TLAC_A_POLYGRAFIA"]] = None
    VYSKUM_A_VYVOJ: Optional[Type["VYSKUM_A_VYVOJ"]] = None
    VZDELAVANIE_A_PERSONALISTIKA: Optional[Type["VZDELAVANIE_A_PERSONALISTIKA"]] = None
    ZDRAVOTNICTVO: Optional[Type["ZDRAVOTNICTVO"]] = None
    POLNOHOSPODARSTVO: Optional[Type["POLNOHOSPODARSTVO"]] = None
    BRIGADY: Optional[Type["BRIGADY"]] = None
    OSTATNE: Optional[Type["OSTATNE"]] = None


class ADMINISTRATIVA(SECTION_PRACA):
    """SECTION_PRACA -> ADMINISTRATIVA."""

    category_name = "administrativa"
    category_rss = "341"


class CHEMIA_A_POTRAVINARSTVO(SECTION_PRACA):
    """SECTION_PRACA -> CHEMIA_A_POTRAVINARSTVO."""

    category_name = "potravinarstvo"
    category_rss = "342"


class DOPRAVA_A_LOGISTIKA(SECTION_PRACA):
    """SECTION_PRACA -> DOPRAVA_A_LOGISTIKA."""

    category_name = "logistika"
    category_rss = "343"


class FINANCIE_A_EKONOMIKA(SECTION_PRACA):
    """SECTION_PRACA -> FINANCIE_A_EKONOMIKA."""

    category_name = "financie"
    category_rss = "344"


class IT_A_TELEKOMUNIKACIE(SECTION_PRACA):
    """SECTION_PRACA -> IT_A_TELEKOMUNIKACIE."""

    category_name = "it"
    category_rss = "345"


class MARKETING_A_REKLAMA(SECTION_PRACA):
    """SECTION_PRACA -> MARKETING_A_REKLAMA."""

    category_name = "marketing"
    category_rss = "346"


class MANAGEMENT(SECTION_PRACA):
    """SECTION_PRACA -> MANAGEMENT."""

    category_name = "management"
    category_rss = "347"


class OBCHOD_A_PREDAJ(SECTION_PRACA):
    """SECTION_PRACA -> OBCHOD_A_PREDAJ."""

    category_name = "obchod"
    category_rss = "348"


class OBRANA_A_BEZPECNOST(SECTION_PRACA):
    """SECTION_PRACA -> OBRANA_A_BEZPECNOST."""

    category_name = "bezpecnost"
    category_rss = "349"


class POHOSTINSTVA_A_UBYTOVANIE(SECTION_PRACA):
    """SECTION_PRACA -> POHOSTINSTVA_A_UBYTOVANIE."""

    category_name = "ubytovanie"
    category_rss = "350"


class PRACA_V_DOMACNOSTI(SECTION_PRACA):
    """SECTION_PRACA -> PRACA_V_DOMACNOSTI."""

    category_name = "domacnost"
    category_rss = "351"


class PRAVO_LEGISLATIVA(SECTION_PRACA):
    """SECTION_PRACA -> PRAVO_LEGISLATIVA."""

    category_name = "pravo"
    category_rss = "352"


class PRIEMYSEL_A_VYROBA(SECTION_PRACA):
    """SECTION_PRACA -> PRIEMYSEL_A_VYROBA."""

    category_name = "priemysel"
    category_rss = "353"


class REMESELNE_PRACE(SECTION_PRACA):
    """SECTION_PRACA -> REMESELNE_PRACE."""

    category_name = "remeslo"
    category_rss = "354"


class SERVIS_A_SLUZBY(SECTION_PRACA):
    """SECTION_PRACA -> SERVIS_A_SLUZBY."""

    category_name = "sluzby"
    category_rss = "355"


class STAVEBNICTVO(SECTION_PRACA):
    """SECTION_PRACA -> STAVEBNICTVO."""

    category_name = "stavebnictvo"
    category_rss = "357"


class TECHNIKA_A_ENERGETIKA(SECTION_PRACA):
    """SECTION_PRACA -> TECHNIKA_A_ENERGETIKA."""

    category_name = "technika"
    category_rss = "358"


class TLAC_A_POLYGRAFIA(SECTION_PRACA):
    """SECTION_PRACA -> TLAC_A_POLYGRAFIA."""

    category_name = "tlac"
    category_rss = "359"


class VYSKUM_A_VYVOJ(SECTION_PRACA):
    """SECTION_PRACA -> VYSKUM_A_VYVOJ."""

    category_name = "vyskum"
    category_rss = "360"


class VZDELAVANIE_A_PERSONALISTIKA(SECTION_PRACA):
    """SECTION_PRACA -> VZDELAVANIE_A_PERSONALISTIKA."""

    category_name = "personalistika"
    category_rss = "361"


class ZDRAVOTNICTVO(SECTION_PRACA):
    """SECTION_PRACA -> ZDRAVOTNICTVO."""

    category_name = "zdravotnictvo"
    category_rss = "362"


class POLNOHOSPODARSTVO(SECTION_PRACA):
    """SECTION_PRACA -> POLNOHOSPODARSTVO."""

    category_name = "polnohospodarstvo"
    category_rss = "363"


class BRIGADY(SECTION_PRACA):
    """SECTION_PRACA -> BRIGADY."""

    category_name = "brigada"
    category_rss = "364"


class OSTATNE(SECTION_PRACA):
    """SECTION_PRACA -> OSTATNE."""

    category_name = "ostatni"
    category_rss = "365"


class SECTION_AUTO(Category):
    """SECTION_AUTO."""

    section_name = "auto"
    section_rss = "au"

    ALFA_ROMEO: Optional[Type["ALFA_ROMEO"]] = None
    AUDI: Optional[Type["AUDI"]] = None
    BMW: Optional[Type["BMW"]] = None
    CITROEN: Optional[Type["CITROEN"]] = None
    DACIA: Optional[Type["DACIA"]] = None
    FIAT: Optional[Type["FIAT"]] = None
    FORD: Optional[Type["FORD"]] = None
    HONDA: Optional[Type["HONDA"]] = None
    HYUNDAI: Optional[Type["HYUNDAI"]] = None
    CHEVROLET: Optional[Type["CHEVROLET"]] = None
    KIA: Optional[Type["KIA"]] = None
    MAZDA: Optional[Type["MAZDA"]] = None
    MERCEDESBENZ: Optional[Type["MERCEDESBENZ"]] = None
    MITSUBISHI: Optional[Type["MITSUBISHI"]] = None
    NISSAN: Optional[Type["NISSAN"]] = None
    OPEL: Optional[Type["OPEL"]] = None
    PEUGEOT: Optional[Type["PEUGEOT"]] = None
    RENAULT: Optional[Type["RENAULT"]] = None
    SEAT: Optional[Type["SEAT"]] = None
    SUZUKI: Optional[Type["SUZUKI"]] = None
    SKODA: Optional[Type["SKODA"]] = None
    TOYOTA: Optional[Type["TOYOTA"]] = None
    VOLKSWAGEN: Optional[Type["VOLKSWAGEN"]] = None
    VOLVO: Optional[Type["VOLVO"]] = None
    OSTATNE_ZNACKY: Optional[Type["OSTATNE_ZNACKY"]] = None
    AUTORADIA: Optional[Type["AUTORADIA"]] = None
    GPS_NAVIGACIA: Optional[Type["GPS_NAVIGACIA"]] = None
    HAVAROVANE: Optional[Type["HAVAROVANE"]] = None
    NAHRADNE_DIELY: Optional[Type["NAHRADNE_DIELY"]] = None
    PNEUMATIKY_KOLESA: Optional[Type["PNEUMATIKY_KOLESA"]] = None
    PRISLUSENSTVO: Optional[Type["PRISLUSENSTVO"]] = None
    TUNING: Optional[Type["TUNING"]] = None
    VETERANY: Optional[Type["VETERANY"]] = None
    AUTOBUSY: Optional[Type["AUTOBUSY"]] = None
    DODAVKY: Optional[Type["DODAVKY"]] = None
    MIKROBUSY: Optional[Type["MIKROBUSY"]] = None
    KARAVANY_VOZIKY: Optional[Type["KARAVANY_VOZIKY"]] = None
    NAKLADNE_AUTA: Optional[Type["NAKLADNE_AUTA"]] = None
    PICKUP: Optional[Type["PICKUP"]] = None
    STROJE: Optional[Type["STROJE"]] = None
    OSTATNE: Optional[Type["OSTATNE"]] = None
    HAVAROVANE: Optional[Type["HAVAROVANE"]] = None
    NAHRADNE_DIELY: Optional[Type["NAHRADNE_DIELY"]] = None
    MOTOCYKLE_SKUTRE: Optional[Type["MOTOCYKLE_SKUTRE"]] = None


class ALFA_ROMEO(SECTION_AUTO):
    """SECTION_AUTO -> ALFA_ROMEO."""

    category_name = "alfa"
    category_rss = "439"


class AUDI(SECTION_AUTO):
    """SECTION_AUTO -> AUDI."""

    category_name = "audi"
    category_rss = "79"


class BMW(SECTION_AUTO):
    """SECTION_AUTO -> BMW."""

    category_name = "bmw"
    category_rss = "80"


class CITROEN(SECTION_AUTO):
    """SECTION_AUTO -> CITROEN."""

    category_name = "citroen"
    category_rss = "81"


class DACIA(SECTION_AUTO):
    """SECTION_AUTO -> DACIA."""

    category_name = "dacia"
    category_rss = "457"


class FIAT(SECTION_AUTO):
    """SECTION_AUTO -> FIAT."""

    category_name = "fiat"
    category_rss = "82"


class FORD(SECTION_AUTO):
    """SECTION_AUTO -> FORD."""

    category_name = "ford"
    category_rss = "83"


class HONDA(SECTION_AUTO):
    """SECTION_AUTO -> HONDA."""

    category_name = "honda"
    category_rss = "116"


class HYUNDAI(SECTION_AUTO):
    """SECTION_AUTO -> HYUNDAI."""

    category_name = "hyundai"
    category_rss = "84"


class CHEVROLET(SECTION_AUTO):
    """SECTION_AUTO -> CHEVROLET."""

    category_name = "chevrolet"
    category_rss = "117"


class KIA(SECTION_AUTO):
    """SECTION_AUTO -> KIA."""

    category_name = "kia"
    category_rss = "118"


class MAZDA(SECTION_AUTO):
    """SECTION_AUTO -> MAZDA."""

    category_name = "mazda"
    category_rss = "85"


class MERCEDESBENZ(SECTION_AUTO):
    """SECTION_AUTO -> MERCEDESBENZ."""

    category_name = "mercedes"
    category_rss = "86"


class MITSUBISHI(SECTION_AUTO):
    """SECTION_AUTO -> MITSUBISHI."""

    category_name = "mitsubishi"
    category_rss = "441"


class NISSAN(SECTION_AUTO):
    """SECTION_AUTO -> NISSAN."""

    category_name = "nissan"
    category_rss = "87"


class OPEL(SECTION_AUTO):
    """SECTION_AUTO -> OPEL."""

    category_name = "opel"
    category_rss = "88"


class PEUGEOT(SECTION_AUTO):
    """SECTION_AUTO -> PEUGEOT."""

    category_name = "peugeot"
    category_rss = "89"


class RENAULT(SECTION_AUTO):
    """SECTION_AUTO -> RENAULT."""

    category_name = "renault"
    category_rss = "90"


class SEAT(SECTION_AUTO):
    """SECTION_AUTO -> SEAT."""

    category_name = "seat"
    category_rss = "91"


class SUZUKI(SECTION_AUTO):
    """SECTION_AUTO -> SUZUKI."""

    category_name = "suzuki"
    category_rss = "119"


class SKODA(SECTION_AUTO):
    """SECTION_AUTO -> SKODA."""

    category_name = "skoda"
    category_rss = "92"


class TOYOTA(SECTION_AUTO):
    """SECTION_AUTO -> TOYOTA."""

    category_name = "toyota"
    category_rss = "93"


class VOLKSWAGEN(SECTION_AUTO):
    """SECTION_AUTO -> VOLKSWAGEN."""

    category_name = "volkswagen"
    category_rss = "94"


class VOLVO(SECTION_AUTO):
    """SECTION_AUTO -> VOLVO."""

    category_name = "volvo"
    category_rss = "95"


class OSTATNE_ZNACKY(SECTION_AUTO):
    """SECTION_AUTO -> OSTATNE_ZNACKY."""

    category_name = "ostatni"
    category_rss = "96"


class HAVAROVANE(SECTION_AUTO):
    """SECTION_AUTO -> HAVAROVANE."""

    category_name = "havarovana"
    category_rss = "97"


class NAHRADNE_DIELY(SECTION_AUTO):
    """SECTION_AUTO -> NAHRADNE_DIELY."""

    category_name = "nahradnidily"
    category_rss = "98"


class PNEUMATIKY_KOLESA(SECTION_AUTO):
    """SECTION_AUTO -> PNEUMATIKY_KOLESA."""

    category_name = "pneumatiky"
    category_rss = "115"


class PRISLUSENSTVO(SECTION_AUTO):
    """SECTION_AUTO -> PRISLUSENSTVO."""

    category_name = "prislusenstvo"
    category_rss = "424"


class TUNING(SECTION_AUTO):
    """SECTION_AUTO -> TUNING."""

    category_name = "tuning"
    category_rss = "113"


class VETERANY(SECTION_AUTO):
    """SECTION_AUTO -> VETERANY."""

    category_name = "veterany"
    category_rss = "114"


class AUTOBUSY(SECTION_AUTO):
    """SECTION_AUTO -> AUTOBUSY."""

    category_name = "autobusy"
    category_rss = "107"


class DODAVKY(SECTION_AUTO):
    """SECTION_AUTO -> DODAVKY."""

    category_name = "dodavka"
    category_rss = "100"


class MIKROBUSY(SECTION_AUTO):
    """SECTION_AUTO -> MIKROBUSY."""

    category_name = "mikrobus"
    category_rss = "101"


class KARAVANY_VOZIKY(SECTION_AUTO):
    """SECTION_AUTO -> KARAVANY_VOZIKY."""

    category_name = "karavany"
    category_rss = "111"


class NAKLADNE_AUTA(SECTION_AUTO):
    """SECTION_AUTO -> NAKLADNE_AUTA."""

    category_name = "nakladne"
    category_rss = "112"


class PICKUP(SECTION_AUTO):
    """SECTION_AUTO -> PICKUP."""

    category_name = "pickup"
    category_rss = "99"


class OSTATNE(SECTION_AUTO):
    """SECTION_AUTO -> OSTATNE."""

    category_name = "ostatniuzitkova"
    category_rss = "102"


class HAVAROVANE(SECTION_AUTO):
    """SECTION_AUTO -> HAVAROVANE."""

    category_name = "havarovanauzitkova"
    category_rss = "103"


class NAHRADNE_DIELY(SECTION_AUTO):
    """SECTION_AUTO -> NAHRADNE_DIELY."""

    category_name = "nahradnidilyuzitkova"
    category_rss = "104"


class SECTION_MOTOCYKLE(Category):
    """SECTION_MOTOCYKLE."""

    section_name = "motocykle"
    section_rss = "mt"

    CESTNE_MOTOCYKLE: Optional[Type["CESTNE_MOTOCYKLE"]] = None
    CESTOVNE_MOTOCYKLE: Optional[Type["CESTOVNE_MOTOCYKLE"]] = None
    ENDURO: Optional[Type["ENDURO"]] = None
    CHOPPER: Optional[Type["CHOPPER"]] = None
    MINIBIKE: Optional[Type["MINIBIKE"]] = None
    MOPEDY: Optional[Type["MOPEDY"]] = None
    SKUTRE: Optional[Type["SKUTRE"]] = None
    SKUTRE_VODNE: Optional[Type["SKUTRE_VODNE"]] = None
    SKUTRE_SNEZNE: Optional[Type["SKUTRE_SNEZNE"]] = None
    STVORKOLKY: Optional[Type["STVORKOLKY"]] = None
    TROJKOLKY: Optional[Type["TROJKOLKY"]] = None
    VETERANY: Optional[Type["VETERANY"]] = None
    NAHRADNE_DIELY: Optional[Type["NAHRADNE_DIELY"]] = None
    OBLECENIE_OBUV_HELMY: Optional[Type["OBLECENIE_OBUV_HELMY"]] = None
    OSTATNE: Optional[Type["OSTATNE"]] = None


class CESTNE_MOTOCYKLE(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> CESTNE_MOTOCYKLE."""

    category_name = "cestne"
    category_rss = "186"


class CESTOVNE_MOTOCYKLE(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> CESTOVNE_MOTOCYKLE."""

    category_name = "cestovne"
    category_rss = "187"


class ENDURO(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> ENDURO."""

    category_name = "enduro"
    category_rss = "188"


class CHOPPER(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> CHOPPER."""

    category_name = "chopper"
    category_rss = "189"


class MINIBIKE(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> MINIBIKE."""

    category_name = "minibike"
    category_rss = "190"


class MOPEDY(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> MOPEDY."""

    category_name = "mopedy"
    category_rss = "192"


class SKUTRE(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> SKUTRE."""

    category_name = "skutre"
    category_rss = "193"


class SKUTRE_VODNE(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> SKUTRE_VODNE."""

    category_name = "vodne"
    category_rss = "194"


class SKUTRE_SNEZNE(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> SKUTRE_SNEZNE."""

    category_name = "snezne"
    category_rss = "191"


class STVORKOLKY(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> STVORKOLKY."""

    category_name = "stvorkolky"
    category_rss = "195"


class TROJKOLKY(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> TROJKOLKY."""

    category_name = "trojkolky"
    category_rss = "196"


class VETERANY(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> VETERANY."""

    category_name = "veterany"
    category_rss = "197"


class NAHRADNE_DIELY(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> NAHRADNE_DIELY."""

    category_name = "diely"
    category_rss = "198"


class OBLECENIE_OBUV_HELMY(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> OBLECENIE_OBUV_HELMY."""

    category_name = "helmy"
    category_rss = "199"


class OSTATNE(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "200"


class SECTION_STROJE(Category):
    """SECTION_STROJE."""

    section_name = "stroje"
    section_rss = "st"

    CERPADLA: Optional[Type["CERPADLA"]] = None
    CISTIACE_STROJE: Optional[Type["CISTIACE_STROJE"]] = None
    DREVOOBRABACIE_STROJE: Optional[Type["DREVOOBRABACIE_STROJE"]] = None
    GENERATORY: Optional[Type["GENERATORY"]] = None
    HISTORICKE_STROJE: Optional[Type["HISTORICKE_STROJE"]] = None
    MOTORY: Optional[Type["MOTORY"]] = None
    KOVOOBRABACIE_STROJE: Optional[Type["KOVOOBRABACIE_STROJE"]] = None
    POLNOHOSPODARSKA_TECHNIKA: Optional[Type["POLNOHOSPODARSKA_TECHNIKA"]] = None
    POTRAVINARSKE_STROJE: Optional[Type["POTRAVINARSKE_STROJE"]] = None
    SKLADOVA_TECHNIKA: Optional[Type["SKLADOVA_TECHNIKA"]] = None
    STAVEBNE_STROJE: Optional[Type["STAVEBNE_STROJE"]] = None
    TEXTILNE_STROJE: Optional[Type["TEXTILNE_STROJE"]] = None
    TLACIARENSKE_STROJE: Optional[Type["TLACIARENSKE_STROJE"]] = None
    VYBAVENIE_PREVADZKARNE: Optional[Type["VYBAVENIE_PREVADZKARNE"]] = None
    VYROBNA_LINKA: Optional[Type["VYROBNA_LINKA"]] = None
    NAHRADNE_DIELY: Optional[Type["NAHRADNE_DIELY"]] = None
    OSTATNE: Optional[Type["OSTATNE"]] = None


class CERPADLA(SECTION_STROJE):
    """SECTION_STROJE -> CERPADLA."""

    category_name = "cerpadla"
    category_rss = "208"


class CISTIACE_STROJE(SECTION_STROJE):
    """SECTION_STROJE -> CISTIACE_STROJE."""

    category_name = "cistiace"
    category_rss = "209"


class DREVOOBRABACIE_STROJE(SECTION_STROJE):
    """SECTION_STROJE -> DREVOOBRABACIE_STROJE."""

    category_name = "drevoobrabacie"
    category_rss = "210"


class GENERATORY(SECTION_STROJE):
    """SECTION_STROJE -> GENERATORY."""

    category_name = "generatory"
    category_rss = "211"


class HISTORICKE_STROJE(SECTION_STROJE):
    """SECTION_STROJE -> HISTORICKE_STROJE."""

    category_name = "historicke"
    category_rss = "212"


class MOTORY(SECTION_STROJE):
    """SECTION_STROJE -> MOTORY."""

    category_name = "motory"
    category_rss = "214"


class KOVOOBRABACIE_STROJE(SECTION_STROJE):
    """SECTION_STROJE -> KOVOOBRABACIE_STROJE."""

    category_name = "kovoobrabacie"
    category_rss = "215"


class POLNOHOSPODARSKA_TECHNIKA(SECTION_STROJE):
    """SECTION_STROJE -> POLNOHOSPODARSKA_TECHNIKA."""

    category_name = "polnohospodarska"
    category_rss = "216"


class POTRAVINARSKE_STROJE(SECTION_STROJE):
    """SECTION_STROJE -> POTRAVINARSKE_STROJE."""

    category_name = "potravinarske"
    category_rss = "213"


class SKLADOVA_TECHNIKA(SECTION_STROJE):
    """SECTION_STROJE -> SKLADOVA_TECHNIKA."""

    category_name = "skladova"
    category_rss = "217"


class STAVEBNE_STROJE(SECTION_STROJE):
    """SECTION_STROJE -> STAVEBNE_STROJE."""

    category_name = "stavebne"
    category_rss = "218"


class TEXTILNE_STROJE(SECTION_STROJE):
    """SECTION_STROJE -> TEXTILNE_STROJE."""

    category_name = "textilne"
    category_rss = "219"


class TLACIARENSKE_STROJE(SECTION_STROJE):
    """SECTION_STROJE -> TLACIARENSKE_STROJE."""

    category_name = "tlaciarenske"
    category_rss = "220"


class VYBAVENIE_PREVADZKARNE(SECTION_STROJE):
    """SECTION_STROJE -> VYBAVENIE_PREVADZKARNE."""

    category_name = "prevadzkarne"
    category_rss = "221"


class VYROBNA_LINKA(SECTION_STROJE):
    """SECTION_STROJE -> VYROBNA_LINKA."""

    category_name = "linka"
    category_rss = "222"


class NAHRADNE_DIELY(SECTION_STROJE):
    """SECTION_STROJE -> NAHRADNE_DIELY."""

    category_name = "diely"
    category_rss = "223"


class OSTATNE(SECTION_STROJE):
    """SECTION_STROJE -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "224"


class SECTION_DOM_A_ZAHRADA(Category):
    """SECTION_DOM_A_ZAHRADA."""

    section_name = "dom"
    section_rss = "du"

    BAZENY: Optional[Type["BAZENY"]] = None
    CERPADLA: Optional[Type["CERPADLA"]] = None
    DVERE_BRANY: Optional[Type["DVERE_BRANY"]] = None
    KLIMATIZACIE: Optional[Type["KLIMATIZACIE"]] = None
    KOSACKY: Optional[Type["KOSACKY"]] = None
    KOTLE_KACHLE_BOJLERY: Optional[Type["KOTLE_KACHLE_BOJLERY"]] = None
    MALOTRAKTORY_KULTIVATORY: Optional[Type["MALOTRAKTORY_KULTIVATORY"]] = None
    MIESACKY: Optional[Type["MIESACKY"]] = None
    NARADIE: Optional[Type["NARADIE"]] = None
    OKNA: Optional[Type["OKNA"]] = None
    PILY: Optional[Type["PILY"]] = None
    SNEZNA_TECHNIKA: Optional[Type["SNEZNA_TECHNIKA"]] = None
    STAVEBNY_MATERIAL: Optional[Type["STAVEBNY_MATERIAL"]] = None
    RADIATORY: Optional[Type["RADIATORY"]] = None
    RASTLINY: Optional[Type["RASTLINY"]] = None
    VYBAVENIE_DIELNE: Optional[Type["VYBAVENIE_DIELNE"]] = None
    VYSAVACE_FUKACE: Optional[Type["VYSAVACE_FUKACE"]] = None
    ZAHRADNE_GRILY: Optional[Type["ZAHRADNE_GRILY"]] = None
    ZAHRADNY_NABYTOK: Optional[Type["ZAHRADNY_NABYTOK"]] = None
    ZAHRADNA_TECHNIKA: Optional[Type["ZAHRADNA_TECHNIKA"]] = None
    OSTATNE: Optional[Type["OSTATNE"]] = None


class BAZENY(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> BAZENY."""

    category_name = "bazeny"
    category_rss = "238"


class CERPADLA(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> CERPADLA."""

    category_name = "cerpadla"
    category_rss = "239"


class DVERE_BRANY(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> DVERE_BRANY."""

    category_name = "dvere"
    category_rss = "447"


class KLIMATIZACIE(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> KLIMATIZACIE."""

    category_name = "klimatizacie"
    category_rss = "240"


class KOSACKY(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> KOSACKY."""

    category_name = "kosacky"
    category_rss = "247"


class KOTLE_KACHLE_BOJLERY(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> KOTLE_KACHLE_BOJLERY."""

    category_name = "kotle"
    category_rss = "241"


class MALOTRAKTORY_KULTIVATORY(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> MALOTRAKTORY_KULTIVATORY."""

    category_name = "malotraktory"
    category_rss = "242"


class MIESACKY(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> MIESACKY."""

    category_name = "miesacky"
    category_rss = "244"


class NARADIE(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> NARADIE."""

    category_name = "naradie"
    category_rss = "245"


class OKNA(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> OKNA."""

    category_name = "okna"
    category_rss = "448"


class PILY(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> PILY."""

    category_name = "pily"
    category_rss = "449"


class SNEZNA_TECHNIKA(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> SNEZNA_TECHNIKA."""

    category_name = "snezna"
    category_rss = "248"


class STAVEBNY_MATERIAL(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> STAVEBNY_MATERIAL."""

    category_name = "stavebny"
    category_rss = "249"


class RADIATORY(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> RADIATORY."""

    category_name = "radiatory"
    category_rss = "246"


class RASTLINY(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> RASTLINY."""

    category_name = "rastliny"
    category_rss = "243"


class VYBAVENIE_DIELNE(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> VYBAVENIE_DIELNE."""

    category_name = "vybavenie"
    category_rss = "250"


class VYSAVACE_FUKACE(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> VYSAVACE_FUKACE."""

    category_name = "vysavace"
    category_rss = "251"


class ZAHRADNE_GRILY(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> ZAHRADNE_GRILY."""

    category_name = "grily"
    category_rss = "252"


class ZAHRADNA_TECHNIKA(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> ZAHRADNA_TECHNIKA."""

    category_name = "technika"
    category_rss = "253"


class OSTATNE(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "254"


class SECTION_PC(Category):
    """SECTION_PC."""

    section_name = "pc"
    section_rss = "pc"

    DVD_BLURAY_MECHANIKY: Optional[Type["DVD_BLURAY_MECHANIKY"]] = None
    FOTOAPARATY: Optional[Type["FOTOAPARATY"]] = None
    GPS_NAVIGACIA: Optional[Type["GPS_NAVIGACIA"]] = None
    GRAFICKE_KARTY: Optional[Type["GRAFICKE_KARTY"]] = None
    HARD_DISKY_SSD: Optional[Type["HARD_DISKY_SSD"]] = None
    HERNE_KONZOLY: Optional[Type["HERNE_KONZOLY"]] = None
    HERNE_ZARIADENIA: Optional[Type["HERNE_ZARIADENIA"]] = None
    HRY: Optional[Type["HRY"]] = None
    CHLADICE: Optional[Type["CHLADICE"]] = None
    KLAVESNICE_MYSI: Optional[Type["KLAVESNICE_MYSI"]] = None
    KOPIROVACIE_STROJE: Optional[Type["KOPIROVACIE_STROJE"]] = None
    MOBILNE_TELEFONY: Optional[Type["MOBILNE_TELEFONY"]] = None
    MODEMY: Optional[Type["MODEMY"]] = None
    LCD_MONITORY: Optional[Type["LCD_MONITORY"]] = None
    MP3_PREHRAVACE: Optional[Type["MP3_PREHRAVACE"]] = None
    NOTEBOOKY: Optional[Type["NOTEBOOKY"]] = None
    PAMATE: Optional[Type["PAMATE"]] = None
    PC_POCITACE: Optional[Type["PC_POCITACE"]] = None
    PROCESORY: Optional[Type["PROCESORY"]] = None
    SIETOVE_KOMPONENTY: Optional[Type["SIETOVE_KOMPONENTY"]] = None
    SCANERY: Optional[Type["SCANERY"]] = None
    SKRINE_ZDROJE: Optional[Type["SKRINE_ZDROJE"]] = None
    SOFTWARE: Optional[Type["SOFTWARE"]] = None
    SPOTREBNY_MATERIAL: Optional[Type["SPOTREBNY_MATERIAL"]] = None
    TABLETY_ECITACKY: Optional[Type["TABLETY_ECITACKY"]] = None
    TLACIARNE: Optional[Type["TLACIARNE"]] = None
    WIRELESS_WIFI: Optional[Type["WIRELESS_WIFI"]] = None
    ZAKLADNE_DOSKY: Optional[Type["ZAKLADNE_DOSKY"]] = None
    ZALOZNE_ZDROJE: Optional[Type["ZALOZNE_ZDROJE"]] = None
    ZVUKOVE_KARTY: Optional[Type["ZVUKOVE_KARTY"]] = None
    OSTATNE: Optional[Type["OSTATNE"]] = None


class DVD_BLURAY_MECHANIKY(SECTION_PC):
    """SECTION_PC -> DVD_BLURAY_MECHANIKY."""

    category_name = "cd"
    category_rss = "1"


class GPS_NAVIGACIA(SECTION_PC):
    """SECTION_PC -> GPS_NAVIGACIA."""

    category_name = "gps"
    category_rss = "32"


class GRAFICKE_KARTY(SECTION_PC):
    """SECTION_PC -> GRAFICKE_KARTY."""

    category_name = "graficka"
    category_rss = "4"


class HARD_DISKY_SSD(SECTION_PC):
    """SECTION_PC -> HARD_DISKY_SSD."""

    category_name = "hdd"
    category_rss = "5"


class HERNE_KONZOLY(SECTION_PC):
    """SECTION_PC -> HERNE_KONZOLY."""

    category_name = "playstation"
    category_rss = "25"


class HERNE_ZARIADENIA(SECTION_PC):
    """SECTION_PC -> HERNE_ZARIADENIA."""

    category_name = "volanty"
    category_rss = "29"


class HRY(SECTION_PC):
    """SECTION_PC -> HRY."""

    category_name = "hry"
    category_rss = "30"


class CHLADICE(SECTION_PC):
    """SECTION_PC -> CHLADICE."""

    category_name = "chladic"
    category_rss = "27"


class KLAVESNICE_MYSI(SECTION_PC):
    """SECTION_PC -> KLAVESNICE_MYSI."""

    category_name = "mys"
    category_rss = "6"


class KOPIROVACIE_STROJE(SECTION_PC):
    """SECTION_PC -> KOPIROVACIE_STROJE."""

    category_name = "kopirka"
    category_rss = "7"


class MODEMY(SECTION_PC):
    """SECTION_PC -> MODEMY."""

    category_name = "modem"
    category_rss = "2"


class LCD_MONITORY(SECTION_PC):
    """SECTION_PC -> LCD_MONITORY."""

    category_name = "monitor"
    category_rss = "9"


class MP3_PREHRAVACE(SECTION_PC):
    """SECTION_PC -> MP3_PREHRAVACE."""

    category_name = "mp3"
    category_rss = "26"


class NOTEBOOKY(SECTION_PC):
    """SECTION_PC -> NOTEBOOKY."""

    category_name = "notebook"
    category_rss = "10"


class PAMATE(SECTION_PC):
    """SECTION_PC -> PAMATE."""

    category_name = "pamet"
    category_rss = "11"


class PC_POCITACE(SECTION_PC):
    """SECTION_PC -> PC_POCITACE."""

    category_name = "pc"
    category_rss = "12"


class PROCESORY(SECTION_PC):
    """SECTION_PC -> PROCESORY."""

    category_name = "procesor"
    category_rss = "13"


class SIETOVE_KOMPONENTY(SECTION_PC):
    """SECTION_PC -> SIETOVE_KOMPONENTY."""

    category_name = "sit"
    category_rss = "14"


class SCANERY(SECTION_PC):
    """SECTION_PC -> SCANERY."""

    category_name = "scaner"
    category_rss = "15"


class SKRINE_ZDROJE(SECTION_PC):
    """SECTION_PC -> SKRINE_ZDROJE."""

    category_name = "case"
    category_rss = "16"


class SOFTWARE(SECTION_PC):
    """SECTION_PC -> SOFTWARE."""

    category_name = "software"
    category_rss = "17"


class SPOTREBNY_MATERIAL(SECTION_PC):
    """SECTION_PC -> SPOTREBNY_MATERIAL."""

    category_name = "spotrebny"
    category_rss = "31"


class TABLETY_ECITACKY(SECTION_PC):
    """SECTION_PC -> TABLETY_ECITACKY."""

    category_name = "tablet"
    category_rss = "24"


class TLACIARNE(SECTION_PC):
    """SECTION_PC -> TLACIARNE."""

    category_name = "tlaciaren"
    category_rss = "18"


class WIRELESS_WIFI(SECTION_PC):
    """SECTION_PC -> WIRELESS_WIFI."""

    category_name = "wifi"
    category_rss = "28"


class ZAKLADNE_DOSKY(SECTION_PC):
    """SECTION_PC -> ZAKLADNE_DOSKY."""

    category_name = "motherboard"
    category_rss = "19"


class ZALOZNE_ZDROJE(SECTION_PC):
    """SECTION_PC -> ZALOZNE_ZDROJE."""

    category_name = "ups"
    category_rss = "20"


class ZVUKOVE_KARTY(SECTION_PC):
    """SECTION_PC -> ZVUKOVE_KARTY."""

    category_name = "sound"
    category_rss = "21"


class OSTATNE(SECTION_PC):
    """SECTION_PC -> OSTATNE."""

    category_name = "ostatni"
    category_rss = "22"


class SECTION_MOBILY(Category):
    """SECTION_MOBILY."""

    section_name = "mobil"
    section_rss = "mo"

    APPLE: Optional[Type["APPLE"]] = None
    HTC: Optional[Type["HTC"]] = None
    HUAWEI_HONOR: Optional[Type["HUAWEI_HONOR"]] = None
    LG: Optional[Type["LG"]] = None
    MOTOROLA_LENOVO: Optional[Type["MOTOROLA_LENOVO"]] = None
    NOKIA_MICROSOFT: Optional[Type["NOKIA_MICROSOFT"]] = None
    SAMSUNG: Optional[Type["SAMSUNG"]] = None
    SONY: Optional[Type["SONY"]] = None
    XIAOMI: Optional[Type["XIAOMI"]] = None
    OSTATNE_ZNACKY: Optional[Type["OSTATNE_ZNACKY"]] = None
    BATERIE: Optional[Type["BATERIE"]] = None
    BEZDROTOVE_TELEFONY: Optional[Type["BEZDROTOVE_TELEFONY"]] = None
    DATOVE_KABELY: Optional[Type["DATOVE_KABELY"]] = None
    FAXY: Optional[Type["FAXY"]] = None
    GPS_NAVIGACIA: Optional[Type["GPS_NAVIGACIA"]] = None
    HEADSETY: Optional[Type["HEADSETY"]] = None
    HF_SADY_DO_AUTA: Optional[Type["HF_SADY_DO_AUTA"]] = None
    INTELIGENTNE_HODINKY: Optional[Type["INTELIGENTNE_HODINKY"]] = None
    KLASICKE_TELEFONY: Optional[Type["KLASICKE_TELEFONY"]] = None
    KRYTY: Optional[Type["KRYTY"]] = None
    NABIJACKY: Optional[Type["NABIJACKY"]] = None
    PAMATOVE_KARTY: Optional[Type["PAMATOVE_KARTY"]] = None
    OSTATNE: Optional[Type["OSTATNE"]] = None


class APPLE(SECTION_MOBILY):
    """SECTION_MOBILY -> APPLE."""

    category_name = "apple"
    category_rss = "435"


class HTC(SECTION_MOBILY):
    """SECTION_MOBILY -> HTC."""

    category_name = "htc"
    category_rss = "436"


class HUAWEI_HONOR(SECTION_MOBILY):
    """SECTION_MOBILY -> HUAWEI_HONOR."""

    category_name = "huawei"
    category_rss = "305"


class LG(SECTION_MOBILY):
    """SECTION_MOBILY -> LG."""

    category_name = "lg"
    category_rss = "301"


class MOTOROLA_LENOVO(SECTION_MOBILY):
    """SECTION_MOBILY -> MOTOROLA_LENOVO."""

    category_name = "motorola"
    category_rss = "302"


class NOKIA_MICROSOFT(SECTION_MOBILY):
    """SECTION_MOBILY -> NOKIA_MICROSOFT."""

    category_name = "nokia"
    category_rss = "303"


class SAMSUNG(SECTION_MOBILY):
    """SECTION_MOBILY -> SAMSUNG."""

    category_name = "samsung"
    category_rss = "304"


class SONY(SECTION_MOBILY):
    """SECTION_MOBILY -> SONY."""

    category_name = "ericsson"
    category_rss = "306"


class XIAOMI(SECTION_MOBILY):
    """SECTION_MOBILY -> XIAOMI."""

    category_name = "xiaomi"
    category_rss = "451"


class OSTATNE_ZNACKY(SECTION_MOBILY):
    """SECTION_MOBILY -> OSTATNE_ZNACKY."""

    category_name = "mobily"
    category_rss = "307"


class BATERIE(SECTION_MOBILY):
    """SECTION_MOBILY -> BATERIE."""

    category_name = "baterie"
    category_rss = "308"


class BEZDROTOVE_TELEFONY(SECTION_MOBILY):
    """SECTION_MOBILY -> BEZDROTOVE_TELEFONY."""

    category_name = "bezdrotove"
    category_rss = "316"


class DATOVE_KABELY(SECTION_MOBILY):
    """SECTION_MOBILY -> DATOVE_KABELY."""

    category_name = "kabely"
    category_rss = "309"


class FAXY(SECTION_MOBILY):
    """SECTION_MOBILY -> FAXY."""

    category_name = "faxy"
    category_rss = "317"


class HEADSETY(SECTION_MOBILY):
    """SECTION_MOBILY -> HEADSETY."""

    category_name = "headsety"
    category_rss = "310"


class HF_SADY_DO_AUTA(SECTION_MOBILY):
    """SECTION_MOBILY -> HF_SADY_DO_AUTA."""

    category_name = "hf"
    category_rss = "311"


class INTELIGENTNE_HODINKY(SECTION_MOBILY):
    """SECTION_MOBILY -> INTELIGENTNE_HODINKY."""

    category_name = "smartwatch"
    category_rss = "450"


class KLASICKE_TELEFONY(SECTION_MOBILY):
    """SECTION_MOBILY -> KLASICKE_TELEFONY."""

    category_name = "telefony"
    category_rss = "318"


class KRYTY(SECTION_MOBILY):
    """SECTION_MOBILY -> KRYTY."""

    category_name = "kryty"
    category_rss = "440"


class NABIJACKY(SECTION_MOBILY):
    """SECTION_MOBILY -> NABIJACKY."""

    category_name = "nabijacky"
    category_rss = "312"


class PAMATOVE_KARTY(SECTION_MOBILY):
    """SECTION_MOBILY -> PAMATOVE_KARTY."""

    category_name = "karty"
    category_rss = "313"


class OSTATNE(SECTION_MOBILY):
    """SECTION_MOBILY -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "315"


class SECTION_FOTO(Category):
    """SECTION_FOTO."""

    section_name = "foto"
    section_rss = "fo"

    ANALOGOVE_FOTOAPARATY: Optional[Type["ANALOGOVE_FOTOAPARATY"]] = None
    DIGITALNE_FOTOAPARATY: Optional[Type["DIGITALNE_FOTOAPARATY"]] = None
    DRONY: Optional[Type["DRONY"]] = None
    VIDEOKAMERY: Optional[Type["VIDEOKAMERY"]] = None
    ZRKADLOVKY: Optional[Type["ZRKADLOVKY"]] = None
    BATERIE: Optional[Type["BATERIE"]] = None
    BLESKY_A_OSVETLENIE: Optional[Type["BLESKY_A_OSVETLENIE"]] = None
    BRASNE_A_PUZDRA: Optional[Type["BRASNE_A_PUZDRA"]] = None
    DATOVE_KABLE: Optional[Type["DATOVE_KABLE"]] = None
    FILTRE: Optional[Type["FILTRE"]] = None
    NABIJACKY: Optional[Type["NABIJACKY"]] = None
    OBJEKTIVY: Optional[Type["OBJEKTIVY"]] = None
    PAMATOVE_KARTY: Optional[Type["PAMATOVE_KARTY"]] = None
    STATIVY: Optional[Type["STATIVY"]] = None
    OSTATNE: Optional[Type["OSTATNE"]] = None


class ANALOGOVE_FOTOAPARATY(SECTION_FOTO):
    """SECTION_FOTO -> ANALOGOVE_FOTOAPARATY."""

    category_name = "kinofilm"
    category_rss = "443"


class DIGITALNE_FOTOAPARATY(SECTION_FOTO):
    """SECTION_FOTO -> DIGITALNE_FOTOAPARATY."""

    category_name = "digitalne"
    category_rss = "256"


class DRONY(SECTION_FOTO):
    """SECTION_FOTO -> DRONY."""

    category_name = "drony"
    category_rss = "456"


class VIDEOKAMERY(SECTION_FOTO):
    """SECTION_FOTO -> VIDEOKAMERY."""

    category_name = "videokamery"
    category_rss = "258"


class ZRKADLOVKY(SECTION_FOTO):
    """SECTION_FOTO -> ZRKADLOVKY."""

    category_name = "zrkadlovky"
    category_rss = "257"


class BATERIE(SECTION_FOTO):
    """SECTION_FOTO -> BATERIE."""

    category_name = "baterie"
    category_rss = "259"


class BLESKY_A_OSVETLENIE(SECTION_FOTO):
    """SECTION_FOTO -> BLESKY_A_OSVETLENIE."""

    category_name = "blesky"
    category_rss = "442"


class BRASNE_A_PUZDRA(SECTION_FOTO):
    """SECTION_FOTO -> BRASNE_A_PUZDRA."""

    category_name = "brasne"
    category_rss = "260"


class DATOVE_KABLE(SECTION_FOTO):
    """SECTION_FOTO -> DATOVE_KABLE."""

    category_name = "kable"
    category_rss = "262"


class FILTRE(SECTION_FOTO):
    """SECTION_FOTO -> FILTRE."""

    category_name = "filtre"
    category_rss = "263"


class NABIJACKY(SECTION_FOTO):
    """SECTION_FOTO -> NABIJACKY."""

    category_name = "nabijacky"
    category_rss = "264"


class OBJEKTIVY(SECTION_FOTO):
    """SECTION_FOTO -> OBJEKTIVY."""

    category_name = "objektivy"
    category_rss = "261"


class PAMATOVE_KARTY(SECTION_FOTO):
    """SECTION_FOTO -> PAMATOVE_KARTY."""

    category_name = "karty"
    category_rss = "265"


class STATIVY(SECTION_FOTO):
    """SECTION_FOTO -> STATIVY."""

    category_name = "stativy"
    category_rss = "266"


class OSTATNE(SECTION_FOTO):
    """SECTION_FOTO -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "267"


class SECTION_ELEKTRO(Category):
    """SECTION_ELEKTRO."""

    section_name = "elektro"
    section_rss = "el"

    DIGESTORY: Optional[Type["DIGESTORY"]] = None
    CHLADNICKY: Optional[Type["CHLADNICKY"]] = None
    MIKROVLNNE_RURY: Optional[Type["MIKROVLNNE_RURY"]] = None
    MRAZNICKY: Optional[Type["MRAZNICKY"]] = None
    PRACKY: Optional[Type["PRACKY"]] = None
    SPORAKY: Optional[Type["SPORAKY"]] = None
    SUSICKY: Optional[Type["SUSICKY"]] = None
    UMYVACKY_RIADU: Optional[Type["UMYVACKY_RIADU"]] = None
    OSTATNE_BIELA: Optional[Type["OSTATNE_BIELA"]] = None
    AUTORADIA: Optional[Type["AUTORADIA"]] = None
    DOMACE_KINA: Optional[Type["DOMACE_KINA"]] = None
    FOTOAPARATY: Optional[Type["FOTOAPARATY"]] = None
    GPS_NAVIGACIA: Optional[Type["GPS_NAVIGACIA"]] = None
    HIFI_SYSTEMY_RADIA: Optional[Type["HIFI_SYSTEMY_RADIA"]] = None
    HUDOBNE_NASTROJE: Optional[Type["HUDOBNE_NASTROJE"]] = None
    MP3_PREHRAVACE: Optional[Type["MP3_PREHRAVACE"]] = None
    PROJEKTORY: Optional[Type["PROJEKTORY"]] = None
    REPRO_SUSTAVY: Optional[Type["REPRO_SUSTAVY"]] = None
    SLUCHADLA: Optional[Type["SLUCHADLA"]] = None
    TELEVIZORY: Optional[Type["TELEVIZORY"]] = None
    VIDEO_DVD_PREHRAVACE: Optional[Type["VIDEO_DVD_PREHRAVACE"]] = None
    VIDEOKAMERY: Optional[Type["VIDEOKAMERY"]] = None
    ZOSILNOVACE: Optional[Type["ZOSILNOVACE"]] = None
    OSTATNE_AUDIO_VIDEO: Optional[Type["OSTATNE_AUDIO_VIDEO"]] = None
    EPILATORY_DEPILATORY: Optional[Type["EPILATORY_DEPILATORY"]] = None
    FENY_KULMY: Optional[Type["FENY_KULMY"]] = None
    HOLIACE_STROJCEKY: Optional[Type["HOLIACE_STROJCEKY"]] = None
    KAVOVARY: Optional[Type["KAVOVARY"]] = None
    NABIJACKY_BATERII: Optional[Type["NABIJACKY_BATERII"]] = None
    RUCNE_SLAHACE_MIXERY: Optional[Type["RUCNE_SLAHACE_MIXERY"]] = None
    SVIETIDLA_LAMPY: Optional[Type["SVIETIDLA_LAMPY"]] = None
    SIJACIE_STROJE: Optional[Type["SIJACIE_STROJE"]] = None
    VYSAVACE: Optional[Type["VYSAVACE"]] = None
    VYSIELACKY: Optional[Type["VYSIELACKY"]] = None
    ZVLHCOVACE_VZDUCHU: Optional[Type["ZVLHCOVACE_VZDUCHU"]] = None
    ZEHLICKY: Optional[Type["ZEHLICKY"]] = None
    OSTATNE_DROBNE: Optional[Type["OSTATNE_DROBNE"]] = None


class DIGESTORY(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> DIGESTORY."""

    category_name = "digestory"
    category_rss = "389"


class CHLADNICKY(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> CHLADNICKY."""

    category_name = "chladnicky"
    category_rss = "390"


class MIKROVLNNE_RURY(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> MIKROVLNNE_RURY."""

    category_name = "mikrovlnky"
    category_rss = "391"


class MRAZNICKY(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> MRAZNICKY."""

    category_name = "mraznicky"
    category_rss = "392"


class PRACKY(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> PRACKY."""

    category_name = "pracky"
    category_rss = "394"


class SPORAKY(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> SPORAKY."""

    category_name = "sporaky"
    category_rss = "395"


class SUSICKY(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> SUSICKY."""

    category_name = "susicky"
    category_rss = "396"


class UMYVACKY_RIADU(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> UMYVACKY_RIADU."""

    category_name = "umyvacky"
    category_rss = "393"


class OSTATNE_BIELA(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> OSTATNE_BIELA."""

    category_name = "ostatnebila"
    category_rss = "397"


class AUTORADIA(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> AUTORADIA."""

    category_name = "autoradia"
    category_rss = "398"


class DOMACE_KINA(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> DOMACE_KINA."""

    category_name = "kina"
    category_rss = "400"


class HIFI_SYSTEMY_RADIA(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> HIFI_SYSTEMY_RADIA."""

    category_name = "hifi"
    category_rss = "402"


class PROJEKTORY(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> PROJEKTORY."""

    category_name = "projektory"
    category_rss = "404"


class REPRO_SUSTAVY(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> REPRO_SUSTAVY."""

    category_name = "repro"
    category_rss = "405"


class SLUCHADLA(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> SLUCHADLA."""

    category_name = "sluchadla"
    category_rss = "399"


class TELEVIZORY(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> TELEVIZORY."""

    category_name = "televizory"
    category_rss = "406"


class VIDEO_DVD_PREHRAVACE(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> VIDEO_DVD_PREHRAVACE."""

    category_name = "dvd"
    category_rss = "407"


class ZOSILNOVACE(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> ZOSILNOVACE."""

    category_name = "zosilnovace"
    category_rss = "409"


class OSTATNE_AUDIO_VIDEO(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> OSTATNE_AUDIO_VIDEO."""

    category_name = "ostatneav"
    category_rss = "410"


class EPILATORY_DEPILATORY(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> EPILATORY_DEPILATORY."""

    category_name = "depilatory"
    category_rss = "411"


class FENY_KULMY(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> FENY_KULMY."""

    category_name = "feny"
    category_rss = "412"


class HOLIACE_STROJCEKY(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> HOLIACE_STROJCEKY."""

    category_name = "holiace"
    category_rss = "413"


class KAVOVARY(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> KAVOVARY."""

    category_name = "kavovary"
    category_rss = "414"


class NABIJACKY_BATERII(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> NABIJACKY_BATERII."""

    category_name = "nabijacky"
    category_rss = "415"


class RUCNE_SLAHACE_MIXERY(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> RUCNE_SLAHACE_MIXERY."""

    category_name = "mixery"
    category_rss = "421"


class SVIETIDLA_LAMPY(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> SVIETIDLA_LAMPY."""

    category_name = "lampy"
    category_rss = "416"


class SIJACIE_STROJE(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> SIJACIE_STROJE."""

    category_name = "sijacie"
    category_rss = "417"


class VYSAVACE(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> VYSAVACE."""

    category_name = "vysavace"
    category_rss = "418"


class VYSIELACKY(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> VYSIELACKY."""

    category_name = "vysielacky"
    category_rss = "419"


class ZVLHCOVACE_VZDUCHU(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> ZVLHCOVACE_VZDUCHU."""

    category_name = "zvlhcovace"
    category_rss = "420"


class ZEHLICKY(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> ZEHLICKY."""

    category_name = "zehlicky"
    category_rss = "422"


class OSTATNE_DROBNE(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> OSTATNE_DROBNE."""

    category_name = "ostatne"
    category_rss = "423"


class SECTION_SPORT(Category):
    """SECTION_SPORT."""

    section_name = "sport"
    section_rss = "sp"

    FITNESS_JOGGING: Optional[Type["FITNESS_JOGGING"]] = None
    GOLF: Optional[Type["GOLF"]] = None
    FUTBAL: Optional[Type["FUTBAL"]] = None
    INLINES_SKATEBOARDING: Optional[Type["INLINES_SKATEBOARDING"]] = None
    KEMPING: Optional[Type["KEMPING"]] = None
    LETECTVO: Optional[Type["LETECTVO"]] = None
    LOPTOVE_HRY: Optional[Type["LOPTOVE_HRY"]] = None
    POLOVNICTVO_LOV: Optional[Type["POLOVNICTVO_LOV"]] = None
    PAINTBALL: Optional[Type["PAINTBALL"]] = None
    RYBOLOV: Optional[Type["RYBOLOV"]] = None
    SPOLOCENSKE_HRY: Optional[Type["SPOLOCENSKE_HRY"]] = None
    TENIS_SQUASH_BADMINTON: Optional[Type["TENIS_SQUASH_BADMINTON"]] = None
    TURISTIKA_HOROLEZECTVO: Optional[Type["TURISTIKA_HOROLEZECTVO"]] = None
    VODNE_SPORTY_POTAPANIE: Optional[Type["VODNE_SPORTY_POTAPANIE"]] = None
    VSETKO_OSTATNE: Optional[Type["VSETKO_OSTATNE"]] = None
    DETSKE_BICYKLE: Optional[Type["DETSKE_BICYKLE"]] = None
    KOLOBEZKY: Optional[Type["KOLOBEZKY"]] = None
    HORSKE_BICYKLE: Optional[Type["HORSKE_BICYKLE"]] = None
    CESTNE_BICYKLE: Optional[Type["CESTNE_BICYKLE"]] = None
    SUCIASTKY_A_DIELY: Optional[Type["SUCIASTKY_A_DIELY"]] = None
    OSTATNA_CYKLISTIKA: Optional[Type["OSTATNA_CYKLISTIKA"]] = None
    BEZKOVANIE: Optional[Type["BEZKOVANIE"]] = None
    LYZOVANIE: Optional[Type["LYZOVANIE"]] = None
    SKIALPY: Optional[Type["SKIALPY"]] = None
    SNOWBOARDING: Optional[Type["SNOWBOARDING"]] = None
    HOKEJ_KORCULOVANIE: Optional[Type["HOKEJ_KORCULOVANIE"]] = None
    OSTATNE_ZIMNE: Optional[Type["OSTATNE_ZIMNE"]] = None


class FITNESS_JOGGING(SECTION_SPORT):
    """SECTION_SPORT -> FITNESS_JOGGING."""

    category_name = "fitness"
    category_rss = "320"


class GOLF(SECTION_SPORT):
    """SECTION_SPORT -> GOLF."""

    category_name = "golf"
    category_rss = "321"


class FUTBAL(SECTION_SPORT):
    """SECTION_SPORT -> FUTBAL."""

    category_name = "futbal"
    category_rss = "322"


class INLINES_SKATEBOARDING(SECTION_SPORT):
    """SECTION_SPORT -> INLINES_SKATEBOARDING."""

    category_name = "korcule"
    category_rss = "323"


class KEMPING(SECTION_SPORT):
    """SECTION_SPORT -> KEMPING."""

    category_name = "kemping"
    category_rss = "319"


class LETECTVO(SECTION_SPORT):
    """SECTION_SPORT -> LETECTVO."""

    category_name = "letectvo"
    category_rss = "446"


class LOPTOVE_HRY(SECTION_SPORT):
    """SECTION_SPORT -> LOPTOVE_HRY."""

    category_name = "loptove"
    category_rss = "324"


class POLOVNICTVO_LOV(SECTION_SPORT):
    """SECTION_SPORT -> POLOVNICTVO_LOV."""

    category_name = "lov"
    category_rss = "325"


class PAINTBALL(SECTION_SPORT):
    """SECTION_SPORT -> PAINTBALL."""

    category_name = "paintball"
    category_rss = "326"


class RYBOLOV(SECTION_SPORT):
    """SECTION_SPORT -> RYBOLOV."""

    category_name = "rybareni"
    category_rss = "327"


class SPOLOCENSKE_HRY(SECTION_SPORT):
    """SECTION_SPORT -> SPOLOCENSKE_HRY."""

    category_name = "hry"
    category_rss = "328"


class TENIS_SQUASH_BADMINTON(SECTION_SPORT):
    """SECTION_SPORT -> TENIS_SQUASH_BADMINTON."""

    category_name = "tenis"
    category_rss = "329"


class TURISTIKA_HOROLEZECTVO(SECTION_SPORT):
    """SECTION_SPORT -> TURISTIKA_HOROLEZECTVO."""

    category_name = "turistika"
    category_rss = "330"


class VODNE_SPORTY_POTAPANIE(SECTION_SPORT):
    """SECTION_SPORT -> VODNE_SPORTY_POTAPANIE."""

    category_name = "vodni"
    category_rss = "331"


class VSETKO_OSTATNE(SECTION_SPORT):
    """SECTION_SPORT -> VSETKO_OSTATNE."""

    category_name = "ostatni"
    category_rss = "332"


class KOLOBEZKY(SECTION_SPORT):
    """SECTION_SPORT -> KOLOBEZKY."""

    category_name = "kolobezky"
    category_rss = "444"


class HORSKE_BICYKLE(SECTION_SPORT):
    """SECTION_SPORT -> HORSKE_BICYKLE."""

    category_name = "horska"
    category_rss = "333"


class CESTNE_BICYKLE(SECTION_SPORT):
    """SECTION_SPORT -> CESTNE_BICYKLE."""

    category_name = "cestne"
    category_rss = "334"


class SUCIASTKY_A_DIELY(SECTION_SPORT):
    """SECTION_SPORT -> SUCIASTKY_A_DIELY."""

    category_name = "soucastky"
    category_rss = "335"


class OSTATNA_CYKLISTIKA(SECTION_SPORT):
    """SECTION_SPORT -> OSTATNA_CYKLISTIKA."""

    category_name = "cyklistika"
    category_rss = "336"


class BEZKOVANIE(SECTION_SPORT):
    """SECTION_SPORT -> BEZKOVANIE."""

    category_name = "bezky"
    category_rss = "445"


class LYZOVANIE(SECTION_SPORT):
    """SECTION_SPORT -> LYZOVANIE."""

    category_name = "lyze"
    category_rss = "337"


class SKIALPY(SECTION_SPORT):
    """SECTION_SPORT -> SKIALPY."""

    category_name = "skialpy"
    category_rss = "459"


class SNOWBOARDING(SECTION_SPORT):
    """SECTION_SPORT -> SNOWBOARDING."""

    category_name = "snowboard"
    category_rss = "338"


class HOKEJ_KORCULOVANIE(SECTION_SPORT):
    """SECTION_SPORT -> HOKEJ_KORCULOVANIE."""

    category_name = "hokej"
    category_rss = "339"


class OSTATNE_ZIMNE(SECTION_SPORT):
    """SECTION_SPORT -> OSTATNE_ZIMNE."""

    category_name = "zimni"
    category_rss = "340"


class SECTION_HUDBA(Category):
    """SECTION_HUDBA."""

    section_name = "hudba"
    section_rss = "hu"

    BICIE_NASTROJE: Optional[Type["BICIE_NASTROJE"]] = None
    DYCHOVE_NASTROJE: Optional[Type["DYCHOVE_NASTROJE"]] = None
    KLAVESOVE_NASTROJE: Optional[Type["KLAVESOVE_NASTROJE"]] = None
    SLACIKOVE_NASTROJE: Optional[Type["SLACIKOVE_NASTROJE"]] = None
    STRUNOVE_NASTROJE: Optional[Type["STRUNOVE_NASTROJE"]] = None
    OSTATNE_NASTROJE: Optional[Type["OSTATNE_NASTROJE"]] = None
    DVD_CD_MC_LP: Optional[Type["DVD_CD_MC_LP"]] = None
    HUDOBNICI_A_SKUPINY: Optional[Type["HUDOBNICI_A_SKUPINY"]] = None
    KONCERTY: Optional[Type["KONCERTY"]] = None
    VYUKA_HUDBY: Optional[Type["VYUKA_HUDBY"]] = None
    NOTY_TEXTY: Optional[Type["NOTY_TEXTY"]] = None
    SKUSOBNE: Optional[Type["SKUSOBNE"]] = None
    SVETELNA_TECHNIKA: Optional[Type["SVETELNA_TECHNIKA"]] = None
    VSTUPENKY: Optional[Type["VSTUPENKY"]] = None
    ZVUKOVA_TECHNIKA: Optional[Type["ZVUKOVA_TECHNIKA"]] = None
    OSTATNE: Optional[Type["OSTATNE"]] = None


class BICIE_NASTROJE(SECTION_HUDBA):
    """SECTION_HUDBA -> BICIE_NASTROJE."""

    category_name = "bicie"
    category_rss = "285"


class DYCHOVE_NASTROJE(SECTION_HUDBA):
    """SECTION_HUDBA -> DYCHOVE_NASTROJE."""

    category_name = "dychove"
    category_rss = "286"


class KLAVESOVE_NASTROJE(SECTION_HUDBA):
    """SECTION_HUDBA -> KLAVESOVE_NASTROJE."""

    category_name = "klavesove"
    category_rss = "287"


class SLACIKOVE_NASTROJE(SECTION_HUDBA):
    """SECTION_HUDBA -> SLACIKOVE_NASTROJE."""

    category_name = "slacikove"
    category_rss = "288"


class STRUNOVE_NASTROJE(SECTION_HUDBA):
    """SECTION_HUDBA -> STRUNOVE_NASTROJE."""

    category_name = "strunove"
    category_rss = "289"


class OSTATNE_NASTROJE(SECTION_HUDBA):
    """SECTION_HUDBA -> OSTATNE_NASTROJE."""

    category_name = "nastroje"
    category_rss = "290"


class DVD_CD_MC_LP(SECTION_HUDBA):
    """SECTION_HUDBA -> DVD_CD_MC_LP."""

    category_name = "nahravky"
    category_rss = "291"


class HUDOBNICI_A_SKUPINY(SECTION_HUDBA):
    """SECTION_HUDBA -> HUDOBNICI_A_SKUPINY."""

    category_name = "skupiny"
    category_rss = "292"


class KONCERTY(SECTION_HUDBA):
    """SECTION_HUDBA -> KONCERTY."""

    category_name = "koncerty"
    category_rss = "293"


class NOTY_TEXTY(SECTION_HUDBA):
    """SECTION_HUDBA -> NOTY_TEXTY."""

    category_name = "noty"
    category_rss = "295"


class SKUSOBNE(SECTION_HUDBA):
    """SECTION_HUDBA -> SKUSOBNE."""

    category_name = "skusobne"
    category_rss = "296"


class SVETELNA_TECHNIKA(SECTION_HUDBA):
    """SECTION_HUDBA -> SVETELNA_TECHNIKA."""

    category_name = "svetelna"
    category_rss = "297"


class ZVUKOVA_TECHNIKA(SECTION_HUDBA):
    """SECTION_HUDBA -> ZVUKOVA_TECHNIKA."""

    category_name = "zvukova"
    category_rss = "299"


class OSTATNE(SECTION_HUDBA):
    """SECTION_HUDBA -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "300"


class SECTION_VSTUPENKY(Category):
    """SECTION_VSTUPENKY."""

    section_name = "vstupenky"
    section_rss = "vs"

    DARCEKOVE_POUKAZKY: Optional[Type["DARCEKOVE_POUKAZKY"]] = None
    DIALNICNE_ZNAMKY: Optional[Type["DIALNICNE_ZNAMKY"]] = None
    CESTOVNE_LISTKY: Optional[Type["CESTOVNE_LISTKY"]] = None
    LETENKY: Optional[Type["LETENKY"]] = None
    PERMANENTKY: Optional[Type["PERMANENTKY"]] = None
    DIVADLO: Optional[Type["DIVADLO"]] = None
    FESTIVALY: Optional[Type["FESTIVALY"]] = None
    HUDBA_KONCERTY: Optional[Type["HUDBA_KONCERTY"]] = None
    PRE_DETI: Optional[Type["PRE_DETI"]] = None
    SPOLOCENSKE_AKCIE: Optional[Type["SPOLOCENSKE_AKCIE"]] = None
    SPORT: Optional[Type["SPORT"]] = None
    VYSTAVY: Optional[Type["VYSTAVY"]] = None
    OSTATNE: Optional[Type["OSTATNE"]] = None


class DARCEKOVE_POUKAZKY(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> DARCEKOVE_POUKAZKY."""

    category_name = "poukazky"
    category_rss = "231"


class DIALNICNE_ZNAMKY(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> DIALNICNE_ZNAMKY."""

    category_name = "znamky"
    category_rss = "232"


class CESTOVNE_LISTKY(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> CESTOVNE_LISTKY."""

    category_name = "listky"
    category_rss = "225"


class LETENKY(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> LETENKY."""

    category_name = "letenky"
    category_rss = "226"


class PERMANENTKY(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> PERMANENTKY."""

    category_name = "permanentky"
    category_rss = "236"


class DIVADLO(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> DIVADLO."""

    category_name = "divadlo"
    category_rss = "227"


class FESTIVALY(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> FESTIVALY."""

    category_name = "festivaly"
    category_rss = "228"


class HUDBA_KONCERTY(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> HUDBA_KONCERTY."""

    category_name = "hudba"
    category_rss = "229"


class PRE_DETI(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> PRE_DETI."""

    category_name = "deti"
    category_rss = "233"


class SPOLOCENSKE_AKCIE(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> SPOLOCENSKE_AKCIE."""

    category_name = "spolocenske"
    category_rss = "230"


class SPORT(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> SPORT."""

    category_name = "sport"
    category_rss = "234"


class VYSTAVY(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> VYSTAVY."""

    category_name = "vystavy"
    category_rss = "235"


class OSTATNE(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "237"


class SECTION_KNIHY(Category):
    """SECTION_KNIHY."""

    section_name = "knihy"
    section_rss = "kn"

    BELETRIA: Optional[Type["BELETRIA"]] = None
    CUDZOJAZYCNA_LITERATURA: Optional[Type["CUDZOJAZYCNA_LITERATURA"]] = None
    CASOPISY: Optional[Type["CASOPISY"]] = None
    DETEKTIVKY: Optional[Type["DETEKTIVKY"]] = None
    DETSKA_LITERATURA: Optional[Type["DETSKA_LITERATURA"]] = None
    DRAMA: Optional[Type["DRAMA"]] = None
    ENCYKLOPEDIE: Optional[Type["ENCYKLOPEDIE"]] = None
    EZOTERIKA: Optional[Type["EZOTERIKA"]] = None
    HISTORICKE_ROMANY: Optional[Type["HISTORICKE_ROMANY"]] = None
    HOBBY_ODBORNE_KNIHY: Optional[Type["HOBBY_ODBORNE_KNIHY"]] = None
    KUCHARKY: Optional[Type["KUCHARKY"]] = None
    MAPY_CESTOVANIE: Optional[Type["MAPY_CESTOVANIE"]] = None
    POCITACOVA_LITERATURA: Optional[Type["POCITACOVA_LITERATURA"]] = None
    PRE_MLADEZ: Optional[Type["PRE_MLADEZ"]] = None
    ROMANY_PRE_ZENY: Optional[Type["ROMANY_PRE_ZENY"]] = None
    SCIFI_FANTASY: Optional[Type["SCIFI_FANTASY"]] = None
    UCEBNICE_SKRIPTA_ZS: Optional[Type["UCEBNICE_SKRIPTA_ZS"]] = None
    UCEBNICE_SKRIPTA_SS: Optional[Type["UCEBNICE_SKRIPTA_SS"]] = None
    UCEBNICE_SKRIPTA_VS: Optional[Type["UCEBNICE_SKRIPTA_VS"]] = None
    UCEBNICE_SKRIPTA_JAZYKOVE: Optional[Type["UCEBNICE_SKRIPTA_JAZYKOVE"]] = None
    ZABAVNA_LITERATURA: Optional[Type["ZABAVNA_LITERATURA"]] = None
    ZDRAVY_ZIVOTNY_STYL: Optional[Type["ZDRAVY_ZIVOTNY_STYL"]] = None
    OSTATNE: Optional[Type["OSTATNE"]] = None


class BELETRIA(SECTION_KNIHY):
    """SECTION_KNIHY -> BELETRIA."""

    category_name = "beletria"
    category_rss = "366"


class CUDZOJAZYCNA_LITERATURA(SECTION_KNIHY):
    """SECTION_KNIHY -> CUDZOJAZYCNA_LITERATURA."""

    category_name = "cudzojazycna"
    category_rss = "388"


class CASOPISY(SECTION_KNIHY):
    """SECTION_KNIHY -> CASOPISY."""

    category_name = "casopisy"
    category_rss = "367"


class DETEKTIVKY(SECTION_KNIHY):
    """SECTION_KNIHY -> DETEKTIVKY."""

    category_name = "detektivky"
    category_rss = "368"


class DETSKA_LITERATURA(SECTION_KNIHY):
    """SECTION_KNIHY -> DETSKA_LITERATURA."""

    category_name = "detska"
    category_rss = "369"


class DRAMA(SECTION_KNIHY):
    """SECTION_KNIHY -> DRAMA."""

    category_name = "drama"
    category_rss = "370"


class ENCYKLOPEDIE(SECTION_KNIHY):
    """SECTION_KNIHY -> ENCYKLOPEDIE."""

    category_name = "encyklopedie"
    category_rss = "371"


class EZOTERIKA(SECTION_KNIHY):
    """SECTION_KNIHY -> EZOTERIKA."""

    category_name = "ezoterika"
    category_rss = "372"


class HISTORICKE_ROMANY(SECTION_KNIHY):
    """SECTION_KNIHY -> HISTORICKE_ROMANY."""

    category_name = "historicke"
    category_rss = "373"


class HOBBY_ODBORNE_KNIHY(SECTION_KNIHY):
    """SECTION_KNIHY -> HOBBY_ODBORNE_KNIHY."""

    category_name = "hobby"
    category_rss = "374"


class KUCHARKY(SECTION_KNIHY):
    """SECTION_KNIHY -> KUCHARKY."""

    category_name = "kucharky"
    category_rss = "375"


class MAPY_CESTOVANIE(SECTION_KNIHY):
    """SECTION_KNIHY -> MAPY_CESTOVANIE."""

    category_name = "mapy"
    category_rss = "376"


class POCITACOVA_LITERATURA(SECTION_KNIHY):
    """SECTION_KNIHY -> POCITACOVA_LITERATURA."""

    category_name = "pocitacova"
    category_rss = "378"


class PRE_MLADEZ(SECTION_KNIHY):
    """SECTION_KNIHY -> PRE_MLADEZ."""

    category_name = "mladez"
    category_rss = "379"


class ROMANY_PRE_ZENY(SECTION_KNIHY):
    """SECTION_KNIHY -> ROMANY_PRE_ZENY."""

    category_name = "zeny"
    category_rss = "380"


class SCIFI_FANTASY(SECTION_KNIHY):
    """SECTION_KNIHY -> SCIFI_FANTASY."""

    category_name = "scifi"
    category_rss = "381"


class UCEBNICE_SKRIPTA_ZS(SECTION_KNIHY):
    """SECTION_KNIHY -> UCEBNICE_SKRIPTA_ZS."""

    category_name = "ucebnicezs"
    category_rss = "386"


class UCEBNICE_SKRIPTA_SS(SECTION_KNIHY):
    """SECTION_KNIHY -> UCEBNICE_SKRIPTA_SS."""

    category_name = "ucebnice"
    category_rss = "383"


class UCEBNICE_SKRIPTA_VS(SECTION_KNIHY):
    """SECTION_KNIHY -> UCEBNICE_SKRIPTA_VS."""

    category_name = "skripta"
    category_rss = "382"


class UCEBNICE_SKRIPTA_JAZYKOVE(SECTION_KNIHY):
    """SECTION_KNIHY -> UCEBNICE_SKRIPTA_JAZYKOVE."""

    category_name = "ucebnicejazykove"
    category_rss = "387"


class ZABAVNA_LITERATURA(SECTION_KNIHY):
    """SECTION_KNIHY -> ZABAVNA_LITERATURA."""

    category_name = "zabavna"
    category_rss = "384"


class ZDRAVY_ZIVOTNY_STYL(SECTION_KNIHY):
    """SECTION_KNIHY -> ZDRAVY_ZIVOTNY_STYL."""

    category_name = "zdravi"
    category_rss = "385"


class OSTATNE(SECTION_KNIHY):
    """SECTION_KNIHY -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "377"


class SECTION_NABYTOK(Category):
    """SECTION_NABYTOK."""

    section_name = "nabytok"
    section_rss = "na"

    DETSKY_NABYTOK: Optional[Type["DETSKY_NABYTOK"]] = None
    DVERE_BRANY: Optional[Type["DVERE_BRANY"]] = None
    JEDALENSKE_KUTY: Optional[Type["JEDALENSKE_KUTY"]] = None
    KNIZNICE: Optional[Type["KNIZNICE"]] = None
    KOBERCE_A_PODLAHOVA_KRYTINA: Optional[Type["KOBERCE_A_PODLAHOVA_KRYTINA"]] = None
    KRESLA_A_GAUCE: Optional[Type["KRESLA_A_GAUCE"]] = None
    KUCHYNE: Optional[Type["KUCHYNE"]] = None
    KUPELNE: Optional[Type["KUPELNE"]] = None
    LAMPY_OSVETLENIE: Optional[Type["LAMPY_OSVETLENIE"]] = None
    MATRACE: Optional[Type["MATRACE"]] = None
    OBYVACIE_STENY: Optional[Type["OBYVACIE_STENY"]] = None
    POSTELE: Optional[Type["POSTELE"]] = None
    SEDACIE_SUPRAVY: Optional[Type["SEDACIE_SUPRAVY"]] = None
    SKRINE: Optional[Type["SKRINE"]] = None
    SPALNE: Optional[Type["SPALNE"]] = None
    STOLICKY: Optional[Type["STOLICKY"]] = None
    STOLY: Optional[Type["STOLY"]] = None
    ZAHRADNY_NABYTOK: Optional[Type["ZAHRADNY_NABYTOK"]] = None
    DOPLNKY: Optional[Type["DOPLNKY"]] = None
    OSTATNY_NABYTOK: Optional[Type["OSTATNY_NABYTOK"]] = None


class JEDALENSKE_KUTY(SECTION_NABYTOK):
    """SECTION_NABYTOK -> JEDALENSKE_KUTY."""

    category_name = "jedalenske"
    category_rss = "268"


class KNIZNICE(SECTION_NABYTOK):
    """SECTION_NABYTOK -> KNIZNICE."""

    category_name = "kniznice"
    category_rss = "269"


class KOBERCE_A_PODLAHOVA_KRYTINA(SECTION_NABYTOK):
    """SECTION_NABYTOK -> KOBERCE_A_PODLAHOVA_KRYTINA."""

    category_name = "koberce"
    category_rss = "270"


class KRESLA_A_GAUCE(SECTION_NABYTOK):
    """SECTION_NABYTOK -> KRESLA_A_GAUCE."""

    category_name = "kresla"
    category_rss = "271"


class KUCHYNE(SECTION_NABYTOK):
    """SECTION_NABYTOK -> KUCHYNE."""

    category_name = "kuchyne"
    category_rss = "272"


class KUPELNE(SECTION_NABYTOK):
    """SECTION_NABYTOK -> KUPELNE."""

    category_name = "kupelne"
    category_rss = "274"


class LAMPY_OSVETLENIE(SECTION_NABYTOK):
    """SECTION_NABYTOK -> LAMPY_OSVETLENIE."""

    category_name = "lampy"
    category_rss = "275"


class MATRACE(SECTION_NABYTOK):
    """SECTION_NABYTOK -> MATRACE."""

    category_name = "matrace"
    category_rss = "276"


class OBYVACIE_STENY(SECTION_NABYTOK):
    """SECTION_NABYTOK -> OBYVACIE_STENY."""

    category_name = "obyvacie"
    category_rss = "273"


class POSTELE(SECTION_NABYTOK):
    """SECTION_NABYTOK -> POSTELE."""

    category_name = "postele"
    category_rss = "277"


class SEDACIE_SUPRAVY(SECTION_NABYTOK):
    """SECTION_NABYTOK -> SEDACIE_SUPRAVY."""

    category_name = "sedacie"
    category_rss = "278"


class SKRINE(SECTION_NABYTOK):
    """SECTION_NABYTOK -> SKRINE."""

    category_name = "skrine"
    category_rss = "279"


class SPALNE(SECTION_NABYTOK):
    """SECTION_NABYTOK -> SPALNE."""

    category_name = "spalne"
    category_rss = "280"


class STOLICKY(SECTION_NABYTOK):
    """SECTION_NABYTOK -> STOLICKY."""

    category_name = "stolicky"
    category_rss = "281"


class STOLY(SECTION_NABYTOK):
    """SECTION_NABYTOK -> STOLY."""

    category_name = "stoly"
    category_rss = "282"


class ZAHRADNY_NABYTOK(SECTION_NABYTOK):
    """SECTION_NABYTOK -> ZAHRADNY_NABYTOK."""

    category_name = "zahradny"
    category_rss = "283"


class DOPLNKY(SECTION_NABYTOK):
    """SECTION_NABYTOK -> DOPLNKY."""

    category_name = "doplnky"
    category_rss = "425"


class OSTATNY_NABYTOK(SECTION_NABYTOK):
    """SECTION_NABYTOK -> OSTATNY_NABYTOK."""

    category_name = "nabytok"
    category_rss = "284"


class SECTION_OBLECENIE(Category):
    """SECTION_OBLECENIE."""

    section_name = "oblecenie"
    section_rss = "ob"

    BLUZKY: Optional[Type["BLUZKY"]] = None
    BUNDY_A_KABATY: Optional[Type["BUNDY_A_KABATY"]] = None
    CIAPKY_SATKY: Optional[Type["CIAPKY_SATKY"]] = None
    DZINSY: Optional[Type["DZINSY"]] = None
    FUNKCNE_PRADLO: Optional[Type["FUNKCNE_PRADLO"]] = None
    KOSELE: Optional[Type["KOSELE"]] = None
    KOZENE_OBLECENIE: Optional[Type["KOZENE_OBLECENIE"]] = None
    MIKINY: Optional[Type["MIKINY"]] = None
    NOHAVICE: Optional[Type["NOHAVICE"]] = None
    OBLEKY_SAKA: Optional[Type["OBLEKY_SAKA"]] = None
    PLAVKY: Optional[Type["PLAVKY"]] = None
    RUKAVICE_A_SALY: Optional[Type["RUKAVICE_A_SALY"]] = None
    RUSKA: Optional[Type["RUSKA"]] = None
    SPODNA_BIELIZEN: Optional[Type["SPODNA_BIELIZEN"]] = None
    SUKNE: Optional[Type["SUKNE"]] = None
    SVADOBNE_SATY: Optional[Type["SVADOBNE_SATY"]] = None
    SVETRE: Optional[Type["SVETRE"]] = None
    SATY_KOSTYMY: Optional[Type["SATY_KOSTYMY"]] = None
    SORTKY: Optional[Type["SORTKY"]] = None
    SPORTOVE_OBLECENIE: Optional[Type["SPORTOVE_OBLECENIE"]] = None
    TEHOTENSKE_OBLECENIE: Optional[Type["TEHOTENSKE_OBLECENIE"]] = None
    TRICKA_ROLAKY_TIELKA: Optional[Type["TRICKA_ROLAKY_TIELKA"]] = None
    DOPLNKY: Optional[Type["DOPLNKY"]] = None
    HODINKY: Optional[Type["HODINKY"]] = None
    KABELKY: Optional[Type["KABELKY"]] = None
    PLECNIAKY_A_KUFRE: Optional[Type["PLECNIAKY_A_KUFRE"]] = None
    TOPANKY_OBUV: Optional[Type["TOPANKY_OBUV"]] = None
    SPERKY: Optional[Type["SPERKY"]] = None
    OSTATNE: Optional[Type["OSTATNE"]] = None


class BLUZKY(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> BLUZKY."""

    category_name = "bluzky"
    category_rss = "51"


class BUNDY_A_KABATY(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> BUNDY_A_KABATY."""

    category_name = "bundy"
    category_rss = "52"


class CIAPKY_SATKY(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> CIAPKY_SATKY."""

    category_name = "ciapky"
    category_rss = "53"


class DZINSY(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> DZINSY."""

    category_name = "dzinsy"
    category_rss = "54"


class FUNKCNE_PRADLO(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> FUNKCNE_PRADLO."""

    category_name = "pradlo"
    category_rss = "55"


class KOSELE(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> KOSELE."""

    category_name = "kosele"
    category_rss = "56"


class KOZENE_OBLECENIE(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> KOZENE_OBLECENIE."""

    category_name = "kozene"
    category_rss = "57"


class MIKINY(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> MIKINY."""

    category_name = "mikiny"
    category_rss = "58"


class NOHAVICE(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> NOHAVICE."""

    category_name = "nohavice"
    category_rss = "59"


class OBLEKY_SAKA(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> OBLEKY_SAKA."""

    category_name = "obleky"
    category_rss = "60"


class PLAVKY(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> PLAVKY."""

    category_name = "plavky"
    category_rss = "61"


class RUKAVICE_A_SALY(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> RUKAVICE_A_SALY."""

    category_name = "rukavice"
    category_rss = "63"


class RUSKA(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> RUSKA."""

    category_name = "ruska"
    category_rss = "458"


class SPODNA_BIELIZEN(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> SPODNA_BIELIZEN."""

    category_name = "bielizen"
    category_rss = "64"


class SUKNE(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> SUKNE."""

    category_name = "sukne"
    category_rss = "65"


class SVADOBNE_SATY(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> SVADOBNE_SATY."""

    category_name = "svadobne"
    category_rss = "66"


class SVETRE(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> SVETRE."""

    category_name = "svetre"
    category_rss = "67"


class SATY_KOSTYMY(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> SATY_KOSTYMY."""

    category_name = "saty"
    category_rss = "68"


class SORTKY(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> SORTKY."""

    category_name = "sortky"
    category_rss = "69"


class SPORTOVE_OBLECENIE(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> SPORTOVE_OBLECENIE."""

    category_name = "sportove"
    category_rss = "70"


class TEHOTENSKE_OBLECENIE(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> TEHOTENSKE_OBLECENIE."""

    category_name = "tehulky"
    category_rss = "62"


class TRICKA_ROLAKY_TIELKA(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> TRICKA_ROLAKY_TIELKA."""

    category_name = "tricka"
    category_rss = "71"


class DOPLNKY(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> DOPLNKY."""

    category_name = "doplnky"
    category_rss = "72"


class HODINKY(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> HODINKY."""

    category_name = "hodinky"
    category_rss = "73"


class KABELKY(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> KABELKY."""

    category_name = "kabelky"
    category_rss = "74"


class PLECNIAKY_A_KUFRE(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> PLECNIAKY_A_KUFRE."""

    category_name = "plecniaky"
    category_rss = "75"


class TOPANKY_OBUV(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> TOPANKY_OBUV."""

    category_name = "obuv"
    category_rss = "76"


class SPERKY(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> SPERKY."""

    category_name = "sperky"
    category_rss = "77"


class OSTATNE(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "78"


class SECTION_SLUZBY(Category):
    """SECTION_SLUZBY."""

    section_name = "sluzby"
    section_rss = "sl"

    AUTO_MOTO: Optional[Type["AUTO_MOTO"]] = None
    CESTOVANIE: Optional[Type["CESTOVANIE"]] = None
    DOMACE_PRACE: Optional[Type["DOMACE_PRACE"]] = None
    EZOTERIKA: Optional[Type["EZOTERIKA"]] = None
    IT_WEBDESIGN: Optional[Type["IT_WEBDESIGN"]] = None
    KONE_SLUZBY: Optional[Type["KONE_SLUZBY"]] = None
    KURZY_A_SKOLENIA: Optional[Type["KURZY_A_SKOLENIA"]] = None
    OPRAVY_A_SERVIS: Optional[Type["OPRAVY_A_SERVIS"]] = None
    ORGANIZOVANIE_AKCII: Optional[Type["ORGANIZOVANIE_AKCII"]] = None
    POZICOVNE: Optional[Type["POZICOVNE"]] = None
    PRAVO_A_BEZPECNOST: Optional[Type["PRAVO_A_BEZPECNOST"]] = None
    PREKLADATELSTVO: Optional[Type["PREKLADATELSTVO"]] = None
    PREPRAVA_A_STAHOVANIE: Optional[Type["PREPRAVA_A_STAHOVANIE"]] = None
    REALITNE_SLUZBY: Optional[Type["REALITNE_SLUZBY"]] = None
    REKLAMA_NA_AUTO: Optional[Type["REKLAMA_NA_AUTO"]] = None
    REKLAMNE_PLOCHY_OSTATNE: Optional[Type["REKLAMNE_PLOCHY_OSTATNE"]] = None
    REMESELNE_A_STAVEBNE_PRACE: Optional[Type["REMESELNE_A_STAVEBNE_PRACE"]] = None
    SLUZBY_PRE_ZVIERATA: Optional[Type["SLUZBY_PRE_ZVIERATA"]] = None
    SPROSTREDKOVATELSKE_SLUZBY: Optional[Type["SPROSTREDKOVATELSKE_SLUZBY"]] = None
    STRAZENIE_DETI: Optional[Type["STRAZENIE_DETI"]] = None
    TVORIVA_PRACA: Optional[Type["TVORIVA_PRACA"]] = None
    UBYTOVANIE: Optional[Type["UBYTOVANIE"]] = None
    UCTOVNICTVO_PORADENSTVO: Optional[Type["UCTOVNICTVO_PORADENSTVO"]] = None
    UPRATOVANIE: Optional[Type["UPRATOVANIE"]] = None
    VYROBA: Optional[Type["VYROBA"]] = None
    VYUKA_DOUCOVANIE: Optional[Type["VYUKA_DOUCOVANIE"]] = None
    VYUKA_HUDBY: Optional[Type["VYUKA_HUDBY"]] = None
    ZDRAVIE_A_KRASA: Optional[Type["ZDRAVIE_A_KRASA"]] = None
    OSTATNE: Optional[Type["OSTATNE"]] = None


class AUTO_MOTO(SECTION_SLUZBY):
    """SECTION_SLUZBY -> AUTO_MOTO."""

    category_name = "automoto"
    category_rss = "426"


class CESTOVANIE(SECTION_SLUZBY):
    """SECTION_SLUZBY -> CESTOVANIE."""

    category_name = "cestovanie"
    category_rss = "167"


class DOMACE_PRACE(SECTION_SLUZBY):
    """SECTION_SLUZBY -> DOMACE_PRACE."""

    category_name = "domaca"
    category_rss = "168"


class EZOTERIKA(SECTION_SLUZBY):
    """SECTION_SLUZBY -> EZOTERIKA."""

    category_name = "ezoterika"
    category_rss = "427"


class IT_WEBDESIGN(SECTION_SLUZBY):
    """SECTION_SLUZBY -> IT_WEBDESIGN."""

    category_name = "it"
    category_rss = "171"


class KONE_SLUZBY(SECTION_SLUZBY):
    """SECTION_SLUZBY -> KONE_SLUZBY."""

    category_name = "ustajnenie"
    category_rss = "437"


class KURZY_A_SKOLENIA(SECTION_SLUZBY):
    """SECTION_SLUZBY -> KURZY_A_SKOLENIA."""

    category_name = "skolenia"
    category_rss = "172"


class OPRAVY_A_SERVIS(SECTION_SLUZBY):
    """SECTION_SLUZBY -> OPRAVY_A_SERVIS."""

    category_name = "opravy"
    category_rss = "428"


class ORGANIZOVANIE_AKCII(SECTION_SLUZBY):
    """SECTION_SLUZBY -> ORGANIZOVANIE_AKCII."""

    category_name = "organizovanie"
    category_rss = "429"


class POZICOVNE(SECTION_SLUZBY):
    """SECTION_SLUZBY -> POZICOVNE."""

    category_name = "pozicovne"
    category_rss = "430"


class PRAVO_A_BEZPECNOST(SECTION_SLUZBY):
    """SECTION_SLUZBY -> PRAVO_A_BEZPECNOST."""

    category_name = "pravo"
    category_rss = "431"


class PREKLADATELSTVO(SECTION_SLUZBY):
    """SECTION_SLUZBY -> PREKLADATELSTVO."""

    category_name = "prekladatelstvo"
    category_rss = "173"


class PREPRAVA_A_STAHOVANIE(SECTION_SLUZBY):
    """SECTION_SLUZBY -> PREPRAVA_A_STAHOVANIE."""

    category_name = "stahovanie"
    category_rss = "174"


class REALITNE_SLUZBY(SECTION_SLUZBY):
    """SECTION_SLUZBY -> REALITNE_SLUZBY."""

    category_name = "realitne"
    category_rss = "432"


class REKLAMA_NA_AUTO(SECTION_SLUZBY):
    """SECTION_SLUZBY -> REKLAMA_NA_AUTO."""

    category_name = "reklama"
    category_rss = "183"


class REKLAMNE_PLOCHY_OSTATNE(SECTION_SLUZBY):
    """SECTION_SLUZBY -> REKLAMNE_PLOCHY_OSTATNE."""

    category_name = "reklamne"
    category_rss = "184"


class REMESELNE_A_STAVEBNE_PRACE(SECTION_SLUZBY):
    """SECTION_SLUZBY -> REMESELNE_A_STAVEBNE_PRACE."""

    category_name = "remesla"
    category_rss = "175"


class SLUZBY_PRE_ZVIERATA(SECTION_SLUZBY):
    """SECTION_SLUZBY -> SLUZBY_PRE_ZVIERATA."""

    category_name = "zvierata"
    category_rss = "43"


class SPROSTREDKOVATELSKE_SLUZBY(SECTION_SLUZBY):
    """SECTION_SLUZBY -> SPROSTREDKOVATELSKE_SLUZBY."""

    category_name = "sprostredkovatelske"
    category_rss = "176"


class STRAZENIE_DETI(SECTION_SLUZBY):
    """SECTION_SLUZBY -> STRAZENIE_DETI."""

    category_name = "strazenie"
    category_rss = "178"


class TVORIVA_PRACA(SECTION_SLUZBY):
    """SECTION_SLUZBY -> TVORIVA_PRACA."""

    category_name = "tvoriva"
    category_rss = "434"


class UBYTOVANIE(SECTION_SLUZBY):
    """SECTION_SLUZBY -> UBYTOVANIE."""

    category_name = "ubytovanie"
    category_rss = "179"


class UCTOVNICTVO_PORADENSTVO(SECTION_SLUZBY):
    """SECTION_SLUZBY -> UCTOVNICTVO_PORADENSTVO."""

    category_name = "financne"
    category_rss = "170"


class UPRATOVANIE(SECTION_SLUZBY):
    """SECTION_SLUZBY -> UPRATOVANIE."""

    category_name = "upratovanie"
    category_rss = "180"


class VYROBA(SECTION_SLUZBY):
    """SECTION_SLUZBY -> VYROBA."""

    category_name = "vyroba"
    category_rss = "433"


class VYUKA_DOUCOVANIE(SECTION_SLUZBY):
    """SECTION_SLUZBY -> VYUKA_DOUCOVANIE."""

    category_name = "doucovanie"
    category_rss = "169"


class VYUKA_HUDBY(SECTION_SLUZBY):
    """SECTION_SLUZBY -> VYUKA_HUDBY."""

    category_name = "vyuka"
    category_rss = "185"


class ZDRAVIE_A_KRASA(SECTION_SLUZBY):
    """SECTION_SLUZBY -> ZDRAVIE_A_KRASA."""

    category_name = "zdravie"
    category_rss = "182"


class OSTATNE(SECTION_SLUZBY):
    """SECTION_SLUZBY -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "181"


class SECTION_OSTATNE(Category):
    """SECTION_OSTATNE."""

    section_name = "ostatne"
    section_rss = "os"

    MINCE_BANKOVKY: Optional[Type["MINCE_BANKOVKY"]] = None
    MODELARSTVO: Optional[Type["MODELARSTVO"]] = None
    POTRAVINY: Optional[Type["POTRAVINY"]] = None
    SKLO_KERAMIKA: Optional[Type["SKLO_KERAMIKA"]] = None
    STAROZITNOSTI: Optional[Type["STAROZITNOSTI"]] = None
    SPERKY_HODINKY: Optional[Type["SPERKY_HODINKY"]] = None
    UMELECKE_PREDMETY: Optional[Type["UMELECKE_PREDMETY"]] = None
    ZBERATELSTVO: Optional[Type["ZBERATELSTVO"]] = None
    ZDRAVIE_A_KRASA: Optional[Type["ZDRAVIE_A_KRASA"]] = None
    ZNAMKY_POHLADNICE: Optional[Type["ZNAMKY_POHLADNICE"]] = None
    OSTATNE: Optional[Type["OSTATNE"]] = None


class MINCE_BANKOVKY(SECTION_OSTATNE):
    """SECTION_OSTATNE -> MINCE_BANKOVKY."""

    category_name = "numizmatika"
    category_rss = "454"


class MODELARSTVO(SECTION_OSTATNE):
    """SECTION_OSTATNE -> MODELARSTVO."""

    category_name = "modelarstvo"
    category_rss = "453"


class POTRAVINY(SECTION_OSTATNE):
    """SECTION_OSTATNE -> POTRAVINY."""

    category_name = "potraviny"
    category_rss = "201"


class SKLO_KERAMIKA(SECTION_OSTATNE):
    """SECTION_OSTATNE -> SKLO_KERAMIKA."""

    category_name = "sklo"
    category_rss = "203"


class STAROZITNOSTI(SECTION_OSTATNE):
    """SECTION_OSTATNE -> STAROZITNOSTI."""

    category_name = "starozitnosti"
    category_rss = "202"


class UMELECKE_PREDMETY(SECTION_OSTATNE):
    """SECTION_OSTATNE -> UMELECKE_PREDMETY."""

    category_name = "umelecke"
    category_rss = "204"


class ZBERATELSTVO(SECTION_OSTATNE):
    """SECTION_OSTATNE -> ZBERATELSTVO."""

    category_name = "zberatelstvo"
    category_rss = "205"


class ZDRAVIE_A_KRASA(SECTION_OSTATNE):
    """SECTION_OSTATNE -> ZDRAVIE_A_KRASA."""

    category_name = "zdravie"
    category_rss = "206"


class ZNAMKY_POHLADNICE(SECTION_OSTATNE):
    """SECTION_OSTATNE -> ZNAMKY_POHLADNICE."""

    category_name = "filatelia"
    category_rss = "455"


class OSTATNE(SECTION_OSTATNE):
    """SECTION_OSTATNE -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "207"


SECTION_ZVIERATA.AKVARIJNE_RYBICKY = AKVARIJNE_RYBICKY
SECTION_ZVIERATA.DROBNE_CICAVCE = DROBNE_CICAVCE
SECTION_ZVIERATA.KONE = KONE
SECTION_ZVIERATA.KONE_POTREBY = KONE_POTREBY
SECTION_ZVIERATA.KONE_SLUZBY = KONE_SLUZBY
SECTION_ZVIERATA.MACKY = MACKY
SECTION_ZVIERATA.PSY = PSY
SECTION_ZVIERATA.VTACTVO = VTACTVO
SECTION_ZVIERATA.TERARIJNE_ZVIERATA = TERARIJNE_ZVIERATA
SECTION_ZVIERATA.OSTATNE_DOMACE = OSTATNE_DOMACE
SECTION_ZVIERATA.KRYTIE = KRYTIE
SECTION_ZVIERATA.STRATENI_A_NAJDENI = STRATENI_A_NAJDENI
SECTION_ZVIERATA.CHOVATELSKE_POTREBY = CHOVATELSKE_POTREBY
SECTION_ZVIERATA.SLUZBY_PRE_ZVIERATA = SLUZBY_PRE_ZVIERATA
SECTION_ZVIERATA.HYDINA = HYDINA
SECTION_ZVIERATA.KRALIKY = KRALIKY
SECTION_ZVIERATA.OVCE_A_KOZY = OVCE_A_KOZY
SECTION_ZVIERATA.PRASATA = PRASATA
SECTION_ZVIERATA.DOBYTOK = DOBYTOK
SECTION_ZVIERATA.OSTATNE_HOSPODARSKE = OSTATNE_HOSPODARSKE

SECTION_DETI.AUTOSEDACKY = AUTOSEDACKY
SECTION_DETI.BABY_MONITORY = BABY_MONITORY
SECTION_DETI.BICYKLE = BICYKLE
SECTION_DETI.DETSKA_LITERATURA = DETSKA_LITERATURA
SECTION_DETI.HRACKY = HRACKY
SECTION_DETI.CHODITKA_A_HOPSADLA = CHODITKA_A_HOPSADLA
SECTION_DETI.KOCIKY = KOCIKY
SECTION_DETI.KOJENECKE_POTREBY = KOJENECKE_POTREBY
SECTION_DETI.NABYTOK_PRE_DETI = NABYTOK_PRE_DETI
SECTION_DETI.NOSICE = NOSICE
SECTION_DETI.ODRAZADLA = ODRAZADLA
SECTION_DETI.SEDACKY_NA_BICYKEL = SEDACKY_NA_BICYKEL
SECTION_DETI.SPORTOVE_POTREBY = SPORTOVE_POTREBY
SECTION_DETI.SKOLSKE_POTREBY = SKOLSKE_POTREBY
SECTION_DETI.STRAZENIE_DETI = STRAZENIE_DETI
SECTION_DETI.OSTATNE = OSTATNE
SECTION_DETI.BODY_DUPACKY_A_OVERALY = BODY_DUPACKY_A_OVERALY
SECTION_DETI.BUNDY_A_KABATIKY = BUNDY_A_KABATIKY
SECTION_DETI.CIAPKY_A_KLOBUCIKY = CIAPKY_A_KLOBUCIKY
SECTION_DETI.NOHAVICE_KRATASY_A_TEPLAKY = NOHAVICE_KRATASY_A_TEPLAKY
SECTION_DETI.KOMBINEZY = KOMBINEZY
SECTION_DETI.KOMPLETY = KOMPLETY
SECTION_DETI.MIKINY_A_SVETRE = MIKINY_A_SVETRE
SECTION_DETI.OBUV = OBUV
SECTION_DETI.PLAVKY = PLAVKY
SECTION_DETI.PONOZKY_A_PANCUSKY = PONOZKY_A_PANCUSKY
SECTION_DETI.PYZAMKA_A_ZUPANCEKY = PYZAMKA_A_ZUPANCEKY
SECTION_DETI.RUKAVICE_A_SALY = RUKAVICE_A_SALY
SECTION_DETI.SPODNA_BIELIZEN = SPODNA_BIELIZEN
SECTION_DETI.SUKNICKY_A_SATOCKY = SUKNICKY_A_SATOCKY
SECTION_DETI.TEHOTENSKE_OBLECENIE = TEHOTENSKE_OBLECENIE
SECTION_DETI.TRICKA_A_KOSIELKY = TRICKA_A_KOSIELKY
SECTION_DETI.OSTATNE_OBLECENIE = OSTATNE_OBLECENIE

SECTION_REALITY.BYTY = BYTY
SECTION_REALITY.DOMY = DOMY
SECTION_REALITY.NOVE_PROJEKTY = NOVE_PROJEKTY
SECTION_REALITY.GARAZE = GARAZE
SECTION_REALITY.HOTELY_RESTAURACIE = HOTELY_RESTAURACIE
SECTION_REALITY.CHALUPY_CHATY = CHALUPY_CHATY
SECTION_REALITY.KANCELARIE = KANCELARIE
SECTION_REALITY.OBCHODNE_PRIESTORY = OBCHODNE_PRIESTORY
SECTION_REALITY.POZEMKY = POZEMKY
SECTION_REALITY.SKLADY = SKLADY
SECTION_REALITY.ZAHRADY = ZAHRADY
SECTION_REALITY.OSTATNE = OSTATNE
SECTION_REALITY.BYTY = BYTY
SECTION_REALITY.DOMY = DOMY
SECTION_REALITY.NOVE_PROJEKTY = NOVE_PROJEKTY
SECTION_REALITY.PODNAJOM_SPOLUBYVAJUCI = PODNAJOM_SPOLUBYVAJUCI
SECTION_REALITY.GARAZE = GARAZE
SECTION_REALITY.HOTELY_RESTAURACIE = HOTELY_RESTAURACIE
SECTION_REALITY.UBYTOVANIE = UBYTOVANIE
SECTION_REALITY.KANCELARIE = KANCELARIE
SECTION_REALITY.OBCHODNE_PRIESTORY = OBCHODNE_PRIESTORY
SECTION_REALITY.POZEMKY = POZEMKY
SECTION_REALITY.SKLADY = SKLADY
SECTION_REALITY.ZAHRADY = ZAHRADY
SECTION_REALITY.OSTATNE = OSTATNE

SECTION_PRACA.ADMINISTRATIVA = ADMINISTRATIVA
SECTION_PRACA.CHEMIA_A_POTRAVINARSTVO = CHEMIA_A_POTRAVINARSTVO
SECTION_PRACA.DOPRAVA_A_LOGISTIKA = DOPRAVA_A_LOGISTIKA
SECTION_PRACA.FINANCIE_A_EKONOMIKA = FINANCIE_A_EKONOMIKA
SECTION_PRACA.IT_A_TELEKOMUNIKACIE = IT_A_TELEKOMUNIKACIE
SECTION_PRACA.MARKETING_A_REKLAMA = MARKETING_A_REKLAMA
SECTION_PRACA.MANAGEMENT = MANAGEMENT
SECTION_PRACA.OBCHOD_A_PREDAJ = OBCHOD_A_PREDAJ
SECTION_PRACA.OBRANA_A_BEZPECNOST = OBRANA_A_BEZPECNOST
SECTION_PRACA.POHOSTINSTVA_A_UBYTOVANIE = POHOSTINSTVA_A_UBYTOVANIE
SECTION_PRACA.PRACA_V_DOMACNOSTI = PRACA_V_DOMACNOSTI
SECTION_PRACA.PRAVO_LEGISLATIVA = PRAVO_LEGISLATIVA
SECTION_PRACA.PRIEMYSEL_A_VYROBA = PRIEMYSEL_A_VYROBA
SECTION_PRACA.REMESELNE_PRACE = REMESELNE_PRACE
SECTION_PRACA.SERVIS_A_SLUZBY = SERVIS_A_SLUZBY
SECTION_PRACA.STAVEBNICTVO = STAVEBNICTVO
SECTION_PRACA.TECHNIKA_A_ENERGETIKA = TECHNIKA_A_ENERGETIKA
SECTION_PRACA.TLAC_A_POLYGRAFIA = TLAC_A_POLYGRAFIA
SECTION_PRACA.VYSKUM_A_VYVOJ = VYSKUM_A_VYVOJ
SECTION_PRACA.VZDELAVANIE_A_PERSONALISTIKA = VZDELAVANIE_A_PERSONALISTIKA
SECTION_PRACA.ZDRAVOTNICTVO = ZDRAVOTNICTVO
SECTION_PRACA.POLNOHOSPODARSTVO = POLNOHOSPODARSTVO
SECTION_PRACA.BRIGADY = BRIGADY
SECTION_PRACA.OSTATNE = OSTATNE

SECTION_AUTO.ALFA_ROMEO = ALFA_ROMEO
SECTION_AUTO.AUDI = AUDI
SECTION_AUTO.BMW = BMW
SECTION_AUTO.CITROEN = CITROEN
SECTION_AUTO.DACIA = DACIA
SECTION_AUTO.FIAT = FIAT
SECTION_AUTO.FORD = FORD
SECTION_AUTO.HONDA = HONDA
SECTION_AUTO.HYUNDAI = HYUNDAI
SECTION_AUTO.CHEVROLET = CHEVROLET
SECTION_AUTO.KIA = KIA
SECTION_AUTO.MAZDA = MAZDA
SECTION_AUTO.MERCEDESBENZ = MERCEDESBENZ
SECTION_AUTO.MITSUBISHI = MITSUBISHI
SECTION_AUTO.NISSAN = NISSAN
SECTION_AUTO.OPEL = OPEL
SECTION_AUTO.PEUGEOT = PEUGEOT
SECTION_AUTO.RENAULT = RENAULT
SECTION_AUTO.SEAT = SEAT
SECTION_AUTO.SUZUKI = SUZUKI
SECTION_AUTO.SKODA = SKODA
SECTION_AUTO.TOYOTA = TOYOTA
SECTION_AUTO.VOLKSWAGEN = VOLKSWAGEN
SECTION_AUTO.VOLVO = VOLVO
SECTION_AUTO.OSTATNE_ZNACKY = OSTATNE_ZNACKY
SECTION_AUTO.AUTORADIA = AUTORADIA
SECTION_AUTO.GPS_NAVIGACIA = GPS_NAVIGACIA
SECTION_AUTO.HAVAROVANE = HAVAROVANE
SECTION_AUTO.NAHRADNE_DIELY = NAHRADNE_DIELY
SECTION_AUTO.PNEUMATIKY_KOLESA = PNEUMATIKY_KOLESA
SECTION_AUTO.PRISLUSENSTVO = PRISLUSENSTVO
SECTION_AUTO.TUNING = TUNING
SECTION_AUTO.VETERANY = VETERANY
SECTION_AUTO.AUTOBUSY = AUTOBUSY
SECTION_AUTO.DODAVKY = DODAVKY
SECTION_AUTO.MIKROBUSY = MIKROBUSY
SECTION_AUTO.KARAVANY_VOZIKY = KARAVANY_VOZIKY
SECTION_AUTO.NAKLADNE_AUTA = NAKLADNE_AUTA
SECTION_AUTO.PICKUP = PICKUP
SECTION_AUTO.STROJE = SECTION_STROJE
SECTION_AUTO.OSTATNE = OSTATNE
SECTION_AUTO.HAVAROVANE = HAVAROVANE
SECTION_AUTO.NAHRADNE_DIELY = NAHRADNE_DIELY
SECTION_AUTO.MOTOCYKLE_SKUTRE = SECTION_MOTOCYKLE

SECTION_MOTOCYKLE.CESTNE_MOTOCYKLE = CESTNE_MOTOCYKLE
SECTION_MOTOCYKLE.CESTOVNE_MOTOCYKLE = CESTOVNE_MOTOCYKLE
SECTION_MOTOCYKLE.ENDURO = ENDURO
SECTION_MOTOCYKLE.CHOPPER = CHOPPER
SECTION_MOTOCYKLE.MINIBIKE = MINIBIKE
SECTION_MOTOCYKLE.MOPEDY = MOPEDY
SECTION_MOTOCYKLE.SKUTRE = SKUTRE
SECTION_MOTOCYKLE.SKUTRE_VODNE = SKUTRE_VODNE
SECTION_MOTOCYKLE.SKUTRE_SNEZNE = SKUTRE_SNEZNE
SECTION_MOTOCYKLE.STVORKOLKY = STVORKOLKY
SECTION_MOTOCYKLE.TROJKOLKY = TROJKOLKY
SECTION_MOTOCYKLE.VETERANY = VETERANY
SECTION_MOTOCYKLE.NAHRADNE_DIELY = NAHRADNE_DIELY
SECTION_MOTOCYKLE.OBLECENIE_OBUV_HELMY = OBLECENIE_OBUV_HELMY
SECTION_MOTOCYKLE.OSTATNE = OSTATNE

SECTION_STROJE.CERPADLA = CERPADLA
SECTION_STROJE.CISTIACE_STROJE = CISTIACE_STROJE
SECTION_STROJE.DREVOOBRABACIE_STROJE = DREVOOBRABACIE_STROJE
SECTION_STROJE.GENERATORY = GENERATORY
SECTION_STROJE.HISTORICKE_STROJE = HISTORICKE_STROJE
SECTION_STROJE.MOTORY = MOTORY
SECTION_STROJE.KOVOOBRABACIE_STROJE = KOVOOBRABACIE_STROJE
SECTION_STROJE.POLNOHOSPODARSKA_TECHNIKA = POLNOHOSPODARSKA_TECHNIKA
SECTION_STROJE.POTRAVINARSKE_STROJE = POTRAVINARSKE_STROJE
SECTION_STROJE.SKLADOVA_TECHNIKA = SKLADOVA_TECHNIKA
SECTION_STROJE.STAVEBNE_STROJE = STAVEBNE_STROJE
SECTION_STROJE.TEXTILNE_STROJE = TEXTILNE_STROJE
SECTION_STROJE.TLACIARENSKE_STROJE = TLACIARENSKE_STROJE
SECTION_STROJE.VYBAVENIE_PREVADZKARNE = VYBAVENIE_PREVADZKARNE
SECTION_STROJE.VYROBNA_LINKA = VYROBNA_LINKA
SECTION_STROJE.NAHRADNE_DIELY = NAHRADNE_DIELY
SECTION_STROJE.OSTATNE = OSTATNE

SECTION_DOM_A_ZAHRADA.BAZENY = BAZENY
SECTION_DOM_A_ZAHRADA.CERPADLA = CERPADLA
SECTION_DOM_A_ZAHRADA.DVERE_BRANY = DVERE_BRANY
SECTION_DOM_A_ZAHRADA.KLIMATIZACIE = KLIMATIZACIE
SECTION_DOM_A_ZAHRADA.KOSACKY = KOSACKY
SECTION_DOM_A_ZAHRADA.KOTLE_KACHLE_BOJLERY = KOTLE_KACHLE_BOJLERY
SECTION_DOM_A_ZAHRADA.MALOTRAKTORY_KULTIVATORY = MALOTRAKTORY_KULTIVATORY
SECTION_DOM_A_ZAHRADA.MIESACKY = MIESACKY
SECTION_DOM_A_ZAHRADA.NARADIE = NARADIE
SECTION_DOM_A_ZAHRADA.OKNA = OKNA
SECTION_DOM_A_ZAHRADA.PILY = PILY
SECTION_DOM_A_ZAHRADA.SNEZNA_TECHNIKA = SNEZNA_TECHNIKA
SECTION_DOM_A_ZAHRADA.STAVEBNY_MATERIAL = STAVEBNY_MATERIAL
SECTION_DOM_A_ZAHRADA.RADIATORY = RADIATORY
SECTION_DOM_A_ZAHRADA.RASTLINY = RASTLINY
SECTION_DOM_A_ZAHRADA.VYBAVENIE_DIELNE = VYBAVENIE_DIELNE
SECTION_DOM_A_ZAHRADA.VYSAVACE_FUKACE = VYSAVACE_FUKACE
SECTION_DOM_A_ZAHRADA.ZAHRADNE_GRILY = ZAHRADNE_GRILY
SECTION_DOM_A_ZAHRADA.ZAHRADNY_NABYTOK = ZAHRADNY_NABYTOK
SECTION_DOM_A_ZAHRADA.ZAHRADNA_TECHNIKA = ZAHRADNA_TECHNIKA
SECTION_DOM_A_ZAHRADA.OSTATNE = OSTATNE

SECTION_PC.DVD_BLURAY_MECHANIKY = DVD_BLURAY_MECHANIKY
SECTION_PC.FOTOAPARATY = SECTION_FOTO
SECTION_PC.GPS_NAVIGACIA = GPS_NAVIGACIA
SECTION_PC.GRAFICKE_KARTY = GRAFICKE_KARTY
SECTION_PC.HARD_DISKY_SSD = HARD_DISKY_SSD
SECTION_PC.HERNE_KONZOLY = HERNE_KONZOLY
SECTION_PC.HERNE_ZARIADENIA = HERNE_ZARIADENIA
SECTION_PC.HRY = HRY
SECTION_PC.CHLADICE = CHLADICE
SECTION_PC.KLAVESNICE_MYSI = KLAVESNICE_MYSI
SECTION_PC.KOPIROVACIE_STROJE = KOPIROVACIE_STROJE
SECTION_PC.MOBILNE_TELEFONY = SECTION_MOBILY
SECTION_PC.MODEMY = MODEMY
SECTION_PC.LCD_MONITORY = LCD_MONITORY
SECTION_PC.MP3_PREHRAVACE = MP3_PREHRAVACE
SECTION_PC.NOTEBOOKY = NOTEBOOKY
SECTION_PC.PAMATE = PAMATE
SECTION_PC.PC_POCITACE = PC_POCITACE
SECTION_PC.PROCESORY = PROCESORY
SECTION_PC.SIETOVE_KOMPONENTY = SIETOVE_KOMPONENTY
SECTION_PC.SCANERY = SCANERY
SECTION_PC.SKRINE_ZDROJE = SKRINE_ZDROJE
SECTION_PC.SOFTWARE = SOFTWARE
SECTION_PC.SPOTREBNY_MATERIAL = SPOTREBNY_MATERIAL
SECTION_PC.TABLETY_ECITACKY = TABLETY_ECITACKY
SECTION_PC.TLACIARNE = TLACIARNE
SECTION_PC.WIRELESS_WIFI = WIRELESS_WIFI
SECTION_PC.ZAKLADNE_DOSKY = ZAKLADNE_DOSKY
SECTION_PC.ZALOZNE_ZDROJE = ZALOZNE_ZDROJE
SECTION_PC.ZVUKOVE_KARTY = ZVUKOVE_KARTY
SECTION_PC.OSTATNE = OSTATNE

SECTION_MOBILY.APPLE = APPLE
SECTION_MOBILY.HTC = HTC
SECTION_MOBILY.HUAWEI_HONOR = HUAWEI_HONOR
SECTION_MOBILY.LG = LG
SECTION_MOBILY.MOTOROLA_LENOVO = MOTOROLA_LENOVO
SECTION_MOBILY.NOKIA_MICROSOFT = NOKIA_MICROSOFT
SECTION_MOBILY.SAMSUNG = SAMSUNG
SECTION_MOBILY.SONY = SONY
SECTION_MOBILY.XIAOMI = XIAOMI
SECTION_MOBILY.OSTATNE_ZNACKY = OSTATNE_ZNACKY
SECTION_MOBILY.BATERIE = BATERIE
SECTION_MOBILY.BEZDROTOVE_TELEFONY = BEZDROTOVE_TELEFONY
SECTION_MOBILY.DATOVE_KABELY = DATOVE_KABELY
SECTION_MOBILY.FAXY = FAXY
SECTION_MOBILY.GPS_NAVIGACIA = GPS_NAVIGACIA
SECTION_MOBILY.HEADSETY = HEADSETY
SECTION_MOBILY.HF_SADY_DO_AUTA = HF_SADY_DO_AUTA
SECTION_MOBILY.INTELIGENTNE_HODINKY = INTELIGENTNE_HODINKY
SECTION_MOBILY.KLASICKE_TELEFONY = KLASICKE_TELEFONY
SECTION_MOBILY.KRYTY = KRYTY
SECTION_MOBILY.NABIJACKY = NABIJACKY
SECTION_MOBILY.PAMATOVE_KARTY = PAMATOVE_KARTY
SECTION_MOBILY.OSTATNE = OSTATNE

SECTION_FOTO.ANALOGOVE_FOTOAPARATY = ANALOGOVE_FOTOAPARATY
SECTION_FOTO.DIGITALNE_FOTOAPARATY = DIGITALNE_FOTOAPARATY
SECTION_FOTO.DRONY = DRONY
SECTION_FOTO.VIDEOKAMERY = VIDEOKAMERY
SECTION_FOTO.ZRKADLOVKY = ZRKADLOVKY
SECTION_FOTO.BATERIE = BATERIE
SECTION_FOTO.BLESKY_A_OSVETLENIE = BLESKY_A_OSVETLENIE
SECTION_FOTO.BRASNE_A_PUZDRA = BRASNE_A_PUZDRA
SECTION_FOTO.DATOVE_KABLE = DATOVE_KABLE
SECTION_FOTO.FILTRE = FILTRE
SECTION_FOTO.NABIJACKY = NABIJACKY
SECTION_FOTO.OBJEKTIVY = OBJEKTIVY
SECTION_FOTO.PAMATOVE_KARTY = PAMATOVE_KARTY
SECTION_FOTO.STATIVY = STATIVY
SECTION_FOTO.OSTATNE = OSTATNE

SECTION_ELEKTRO.DIGESTORY = DIGESTORY
SECTION_ELEKTRO.CHLADNICKY = CHLADNICKY
SECTION_ELEKTRO.MIKROVLNNE_RURY = MIKROVLNNE_RURY
SECTION_ELEKTRO.MRAZNICKY = MRAZNICKY
SECTION_ELEKTRO.PRACKY = PRACKY
SECTION_ELEKTRO.SPORAKY = SPORAKY
SECTION_ELEKTRO.SUSICKY = SUSICKY
SECTION_ELEKTRO.UMYVACKY_RIADU = UMYVACKY_RIADU
SECTION_ELEKTRO.OSTATNE_BIELA = OSTATNE_BIELA
SECTION_ELEKTRO.AUTORADIA = AUTORADIA
SECTION_ELEKTRO.DOMACE_KINA = DOMACE_KINA
SECTION_ELEKTRO.FOTOAPARATY = SECTION_FOTO
SECTION_ELEKTRO.GPS_NAVIGACIA = GPS_NAVIGACIA
SECTION_ELEKTRO.HIFI_SYSTEMY_RADIA = HIFI_SYSTEMY_RADIA
SECTION_ELEKTRO.HUDOBNE_NASTROJE = SECTION_HUDBA
SECTION_ELEKTRO.MP3_PREHRAVACE = MP3_PREHRAVACE
SECTION_ELEKTRO.PROJEKTORY = PROJEKTORY
SECTION_ELEKTRO.REPRO_SUSTAVY = REPRO_SUSTAVY
SECTION_ELEKTRO.SLUCHADLA = SLUCHADLA
SECTION_ELEKTRO.TELEVIZORY = TELEVIZORY
SECTION_ELEKTRO.VIDEO_DVD_PREHRAVACE = VIDEO_DVD_PREHRAVACE
SECTION_ELEKTRO.VIDEOKAMERY = VIDEOKAMERY
SECTION_ELEKTRO.ZOSILNOVACE = ZOSILNOVACE
SECTION_ELEKTRO.OSTATNE_AUDIO_VIDEO = OSTATNE_AUDIO_VIDEO
SECTION_ELEKTRO.EPILATORY_DEPILATORY = EPILATORY_DEPILATORY
SECTION_ELEKTRO.FENY_KULMY = FENY_KULMY
SECTION_ELEKTRO.HOLIACE_STROJCEKY = HOLIACE_STROJCEKY
SECTION_ELEKTRO.KAVOVARY = KAVOVARY
SECTION_ELEKTRO.NABIJACKY_BATERII = NABIJACKY_BATERII
SECTION_ELEKTRO.RUCNE_SLAHACE_MIXERY = RUCNE_SLAHACE_MIXERY
SECTION_ELEKTRO.SVIETIDLA_LAMPY = SVIETIDLA_LAMPY
SECTION_ELEKTRO.SIJACIE_STROJE = SIJACIE_STROJE
SECTION_ELEKTRO.VYSAVACE = VYSAVACE
SECTION_ELEKTRO.VYSIELACKY = VYSIELACKY
SECTION_ELEKTRO.ZVLHCOVACE_VZDUCHU = ZVLHCOVACE_VZDUCHU
SECTION_ELEKTRO.ZEHLICKY = ZEHLICKY
SECTION_ELEKTRO.OSTATNE_DROBNE = OSTATNE_DROBNE

SECTION_SPORT.FITNESS_JOGGING = FITNESS_JOGGING
SECTION_SPORT.GOLF = GOLF
SECTION_SPORT.FUTBAL = FUTBAL
SECTION_SPORT.INLINES_SKATEBOARDING = INLINES_SKATEBOARDING
SECTION_SPORT.KEMPING = KEMPING
SECTION_SPORT.LETECTVO = LETECTVO
SECTION_SPORT.LOPTOVE_HRY = LOPTOVE_HRY
SECTION_SPORT.POLOVNICTVO_LOV = POLOVNICTVO_LOV
SECTION_SPORT.PAINTBALL = PAINTBALL
SECTION_SPORT.RYBOLOV = RYBOLOV
SECTION_SPORT.SPOLOCENSKE_HRY = SPOLOCENSKE_HRY
SECTION_SPORT.TENIS_SQUASH_BADMINTON = TENIS_SQUASH_BADMINTON
SECTION_SPORT.TURISTIKA_HOROLEZECTVO = TURISTIKA_HOROLEZECTVO
SECTION_SPORT.VODNE_SPORTY_POTAPANIE = VODNE_SPORTY_POTAPANIE
SECTION_SPORT.VSETKO_OSTATNE = VSETKO_OSTATNE
SECTION_SPORT.DETSKE_BICYKLE = BICYKLE
SECTION_SPORT.KOLOBEZKY = KOLOBEZKY
SECTION_SPORT.HORSKE_BICYKLE = HORSKE_BICYKLE
SECTION_SPORT.CESTNE_BICYKLE = CESTNE_BICYKLE
SECTION_SPORT.SUCIASTKY_A_DIELY = SUCIASTKY_A_DIELY
SECTION_SPORT.OSTATNA_CYKLISTIKA = OSTATNA_CYKLISTIKA
SECTION_SPORT.BEZKOVANIE = BEZKOVANIE
SECTION_SPORT.LYZOVANIE = LYZOVANIE
SECTION_SPORT.SKIALPY = SKIALPY
SECTION_SPORT.SNOWBOARDING = SNOWBOARDING
SECTION_SPORT.HOKEJ_KORCULOVANIE = HOKEJ_KORCULOVANIE
SECTION_SPORT.OSTATNE_ZIMNE = OSTATNE_ZIMNE

SECTION_HUDBA.BICIE_NASTROJE = BICIE_NASTROJE
SECTION_HUDBA.DYCHOVE_NASTROJE = DYCHOVE_NASTROJE
SECTION_HUDBA.KLAVESOVE_NASTROJE = KLAVESOVE_NASTROJE
SECTION_HUDBA.SLACIKOVE_NASTROJE = SLACIKOVE_NASTROJE
SECTION_HUDBA.STRUNOVE_NASTROJE = STRUNOVE_NASTROJE
SECTION_HUDBA.OSTATNE_NASTROJE = OSTATNE_NASTROJE
SECTION_HUDBA.DVD_CD_MC_LP = DVD_CD_MC_LP
SECTION_HUDBA.HUDOBNICI_A_SKUPINY = HUDOBNICI_A_SKUPINY
SECTION_HUDBA.KONCERTY = KONCERTY
SECTION_HUDBA.VYUKA_HUDBY = VYUKA_HUDBY
SECTION_HUDBA.NOTY_TEXTY = NOTY_TEXTY
SECTION_HUDBA.SKUSOBNE = SKUSOBNE
SECTION_HUDBA.SVETELNA_TECHNIKA = SVETELNA_TECHNIKA
SECTION_HUDBA.VSTUPENKY = SECTION_VSTUPENKY
SECTION_HUDBA.ZVUKOVA_TECHNIKA = ZVUKOVA_TECHNIKA
SECTION_HUDBA.OSTATNE = OSTATNE

SECTION_VSTUPENKY.DARCEKOVE_POUKAZKY = DARCEKOVE_POUKAZKY
SECTION_VSTUPENKY.DIALNICNE_ZNAMKY = DIALNICNE_ZNAMKY
SECTION_VSTUPENKY.CESTOVNE_LISTKY = CESTOVNE_LISTKY
SECTION_VSTUPENKY.LETENKY = LETENKY
SECTION_VSTUPENKY.PERMANENTKY = PERMANENTKY
SECTION_VSTUPENKY.DIVADLO = DIVADLO
SECTION_VSTUPENKY.FESTIVALY = FESTIVALY
SECTION_VSTUPENKY.HUDBA_KONCERTY = HUDBA_KONCERTY
SECTION_VSTUPENKY.PRE_DETI = PRE_DETI
SECTION_VSTUPENKY.SPOLOCENSKE_AKCIE = SPOLOCENSKE_AKCIE
SECTION_VSTUPENKY.SPORT = SPORT
SECTION_VSTUPENKY.VYSTAVY = VYSTAVY
SECTION_VSTUPENKY.OSTATNE = OSTATNE

SECTION_KNIHY.BELETRIA = BELETRIA
SECTION_KNIHY.CUDZOJAZYCNA_LITERATURA = CUDZOJAZYCNA_LITERATURA
SECTION_KNIHY.CASOPISY = CASOPISY
SECTION_KNIHY.DETEKTIVKY = DETEKTIVKY
SECTION_KNIHY.DETSKA_LITERATURA = DETSKA_LITERATURA
SECTION_KNIHY.DRAMA = DRAMA
SECTION_KNIHY.ENCYKLOPEDIE = ENCYKLOPEDIE
SECTION_KNIHY.EZOTERIKA = EZOTERIKA
SECTION_KNIHY.HISTORICKE_ROMANY = HISTORICKE_ROMANY
SECTION_KNIHY.HOBBY_ODBORNE_KNIHY = HOBBY_ODBORNE_KNIHY
SECTION_KNIHY.KUCHARKY = KUCHARKY
SECTION_KNIHY.MAPY_CESTOVANIE = MAPY_CESTOVANIE
SECTION_KNIHY.POCITACOVA_LITERATURA = POCITACOVA_LITERATURA
SECTION_KNIHY.PRE_MLADEZ = PRE_MLADEZ
SECTION_KNIHY.ROMANY_PRE_ZENY = ROMANY_PRE_ZENY
SECTION_KNIHY.SCIFI_FANTASY = SCIFI_FANTASY
SECTION_KNIHY.UCEBNICE_SKRIPTA_ZS = UCEBNICE_SKRIPTA_ZS
SECTION_KNIHY.UCEBNICE_SKRIPTA_SS = UCEBNICE_SKRIPTA_SS
SECTION_KNIHY.UCEBNICE_SKRIPTA_VS = UCEBNICE_SKRIPTA_VS
SECTION_KNIHY.UCEBNICE_SKRIPTA_JAZYKOVE = UCEBNICE_SKRIPTA_JAZYKOVE
SECTION_KNIHY.ZABAVNA_LITERATURA = ZABAVNA_LITERATURA
SECTION_KNIHY.ZDRAVY_ZIVOTNY_STYL = ZDRAVY_ZIVOTNY_STYL
SECTION_KNIHY.OSTATNE = OSTATNE

SECTION_NABYTOK.DETSKY_NABYTOK = NABYTOK_PRE_DETI
SECTION_NABYTOK.DVERE_BRANY = DVERE_BRANY
SECTION_NABYTOK.JEDALENSKE_KUTY = JEDALENSKE_KUTY
SECTION_NABYTOK.KNIZNICE = KNIZNICE
SECTION_NABYTOK.KOBERCE_A_PODLAHOVA_KRYTINA = KOBERCE_A_PODLAHOVA_KRYTINA
SECTION_NABYTOK.KRESLA_A_GAUCE = KRESLA_A_GAUCE
SECTION_NABYTOK.KUCHYNE = KUCHYNE
SECTION_NABYTOK.KUPELNE = KUPELNE
SECTION_NABYTOK.LAMPY_OSVETLENIE = LAMPY_OSVETLENIE
SECTION_NABYTOK.MATRACE = MATRACE
SECTION_NABYTOK.OBYVACIE_STENY = OBYVACIE_STENY
SECTION_NABYTOK.POSTELE = POSTELE
SECTION_NABYTOK.SEDACIE_SUPRAVY = SEDACIE_SUPRAVY
SECTION_NABYTOK.SKRINE = SKRINE
SECTION_NABYTOK.SPALNE = SPALNE
SECTION_NABYTOK.STOLICKY = STOLICKY
SECTION_NABYTOK.STOLY = STOLY
SECTION_NABYTOK.ZAHRADNY_NABYTOK = ZAHRADNY_NABYTOK
SECTION_NABYTOK.DOPLNKY = DOPLNKY
SECTION_NABYTOK.OSTATNY_NABYTOK = OSTATNY_NABYTOK

SECTION_OBLECENIE.BLUZKY = BLUZKY
SECTION_OBLECENIE.BUNDY_A_KABATY = BUNDY_A_KABATY
SECTION_OBLECENIE.CIAPKY_SATKY = CIAPKY_SATKY
SECTION_OBLECENIE.DZINSY = DZINSY
SECTION_OBLECENIE.FUNKCNE_PRADLO = FUNKCNE_PRADLO
SECTION_OBLECENIE.KOSELE = KOSELE
SECTION_OBLECENIE.KOZENE_OBLECENIE = KOZENE_OBLECENIE
SECTION_OBLECENIE.MIKINY = MIKINY
SECTION_OBLECENIE.NOHAVICE = NOHAVICE
SECTION_OBLECENIE.OBLEKY_SAKA = OBLEKY_SAKA
SECTION_OBLECENIE.PLAVKY = PLAVKY
SECTION_OBLECENIE.RUKAVICE_A_SALY = RUKAVICE_A_SALY
SECTION_OBLECENIE.RUSKA = RUSKA
SECTION_OBLECENIE.SPODNA_BIELIZEN = SPODNA_BIELIZEN
SECTION_OBLECENIE.SUKNE = SUKNE
SECTION_OBLECENIE.SVADOBNE_SATY = SVADOBNE_SATY
SECTION_OBLECENIE.SVETRE = SVETRE
SECTION_OBLECENIE.SATY_KOSTYMY = SATY_KOSTYMY
SECTION_OBLECENIE.SORTKY = SORTKY
SECTION_OBLECENIE.SPORTOVE_OBLECENIE = SPORTOVE_OBLECENIE
SECTION_OBLECENIE.TEHOTENSKE_OBLECENIE = TEHOTENSKE_OBLECENIE
SECTION_OBLECENIE.TRICKA_ROLAKY_TIELKA = TRICKA_ROLAKY_TIELKA
SECTION_OBLECENIE.DOPLNKY = DOPLNKY
SECTION_OBLECENIE.HODINKY = HODINKY
SECTION_OBLECENIE.KABELKY = KABELKY
SECTION_OBLECENIE.PLECNIAKY_A_KUFRE = PLECNIAKY_A_KUFRE
SECTION_OBLECENIE.TOPANKY_OBUV = TOPANKY_OBUV
SECTION_OBLECENIE.SPERKY = SPERKY
SECTION_OBLECENIE.OSTATNE = OSTATNE

SECTION_SLUZBY.AUTO_MOTO = AUTO_MOTO
SECTION_SLUZBY.CESTOVANIE = CESTOVANIE
SECTION_SLUZBY.DOMACE_PRACE = DOMACE_PRACE
SECTION_SLUZBY.EZOTERIKA = EZOTERIKA
SECTION_SLUZBY.IT_WEBDESIGN = IT_WEBDESIGN
SECTION_SLUZBY.KONE_SLUZBY = KONE_SLUZBY
SECTION_SLUZBY.KURZY_A_SKOLENIA = KURZY_A_SKOLENIA
SECTION_SLUZBY.OPRAVY_A_SERVIS = OPRAVY_A_SERVIS
SECTION_SLUZBY.ORGANIZOVANIE_AKCII = ORGANIZOVANIE_AKCII
SECTION_SLUZBY.POZICOVNE = POZICOVNE
SECTION_SLUZBY.PRAVO_A_BEZPECNOST = PRAVO_A_BEZPECNOST
SECTION_SLUZBY.PREKLADATELSTVO = PREKLADATELSTVO
SECTION_SLUZBY.PREPRAVA_A_STAHOVANIE = PREPRAVA_A_STAHOVANIE
SECTION_SLUZBY.REALITNE_SLUZBY = REALITNE_SLUZBY
SECTION_SLUZBY.REKLAMA_NA_AUTO = REKLAMA_NA_AUTO
SECTION_SLUZBY.REKLAMNE_PLOCHY_OSTATNE = REKLAMNE_PLOCHY_OSTATNE
SECTION_SLUZBY.REMESELNE_A_STAVEBNE_PRACE = REMESELNE_A_STAVEBNE_PRACE
SECTION_SLUZBY.SLUZBY_PRE_ZVIERATA = SLUZBY_PRE_ZVIERATA
SECTION_SLUZBY.SPROSTREDKOVATELSKE_SLUZBY = SPROSTREDKOVATELSKE_SLUZBY
SECTION_SLUZBY.STRAZENIE_DETI = STRAZENIE_DETI
SECTION_SLUZBY.TVORIVA_PRACA = TVORIVA_PRACA
SECTION_SLUZBY.UBYTOVANIE = UBYTOVANIE
SECTION_SLUZBY.UCTOVNICTVO_PORADENSTVO = UCTOVNICTVO_PORADENSTVO
SECTION_SLUZBY.UPRATOVANIE = UPRATOVANIE
SECTION_SLUZBY.VYROBA = VYROBA
SECTION_SLUZBY.VYUKA_DOUCOVANIE = VYUKA_DOUCOVANIE
SECTION_SLUZBY.VYUKA_HUDBY = VYUKA_HUDBY
SECTION_SLUZBY.ZDRAVIE_A_KRASA = ZDRAVIE_A_KRASA
SECTION_SLUZBY.OSTATNE = OSTATNE

SECTION_OSTATNE.MINCE_BANKOVKY = MINCE_BANKOVKY
SECTION_OSTATNE.MODELARSTVO = MODELARSTVO
SECTION_OSTATNE.POTRAVINY = POTRAVINY
SECTION_OSTATNE.SKLO_KERAMIKA = SKLO_KERAMIKA
SECTION_OSTATNE.STAROZITNOSTI = STAROZITNOSTI
SECTION_OSTATNE.SPERKY_HODINKY = SPERKY
SECTION_OSTATNE.UMELECKE_PREDMETY = UMELECKE_PREDMETY
SECTION_OSTATNE.ZBERATELSTVO = ZBERATELSTVO
SECTION_OSTATNE.ZDRAVIE_A_KRASA = ZDRAVIE_A_KRASA
SECTION_OSTATNE.ZNAMKY_POHLADNICE = ZNAMKY_POHLADNICE
SECTION_OSTATNE.OSTATNE = OSTATNE
