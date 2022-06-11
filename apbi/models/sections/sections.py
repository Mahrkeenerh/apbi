"""All sections and categories from bazos."""

# pylint: disable=C0103
# pylint: disable=C0302


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

    AKVARIJNE_RYBICKY: "AKVARIJNE_RYBICKY_33" = None
    DROBNE_CICAVCE: "DROBNE_CICAVCE_34" = None
    KONE: "KONE_35" = None
    KONE_POTREBY: "KONE_POTREBY_50" = None
    KONE_SLUZBY: "KONE_SLUZBY" = None
    MACKY: "MACKY_36" = None
    PSY: "PSY_37" = None
    VTACTVO: "VTACTVO_38" = None
    TERARIJNE_ZVIERATA: "TERARIJNE_ZVIERATA_39" = None
    OSTATNE_DOMACE: "OSTATNE_DOMACE_40" = None
    KRYTIE: "KRYTIE_42" = None
    STRATENI_A_NAJDENI: "STRATENI_A_NAJDENI_255" = None
    CHOVATELSKE_POTREBY: "CHOVATELSKE_POTREBY_41" = None
    SLUZBY_PRE_ZVIERATA: "SLUZBY_PRE_ZVIERATA" = None
    HYDINA: "HYDINA_44" = None
    KRALIKY: "KRALIKY_45" = None
    OVCE_A_KOZY: "OVCE_A_KOZY_46" = None
    PRASATA: "PRASATA_47" = None
    DOBYTOK: "DOBYTOK_48" = None
    OSTATNE_HOSPODARSKE: "OSTATNE_HOSPODARSKE_49" = None


class AKVARIJNE_RYBICKY_33(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> AKVARIJNE_RYBICKY."""

    category_name = "ryba"
    category_rss = "33"


class DROBNE_CICAVCE_34(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> DROBNE_CICAVCE."""

    category_name = "cicavec"
    category_rss = "34"


class KONE_35(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> KONE."""

    category_name = "kon"
    category_rss = "35"


class KONE_POTREBY_50(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> KONE_POTREBY."""

    category_name = "konepotreby"
    category_rss = "50"


class MACKY_36(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> MACKY."""

    category_name = "macka"
    category_rss = "36"


class PSY_37(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> PSY."""

    category_name = "pes"
    category_rss = "37"


class VTACTVO_38(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> VTACTVO."""

    category_name = "vtak"
    category_rss = "38"


class TERARIJNE_ZVIERATA_39(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> TERARIJNE_ZVIERATA."""

    category_name = "zviera"
    category_rss = "39"


class OSTATNE_DOMACE_40(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> OSTATNE_DOMACE."""

    category_name = "ostatnidomaci"
    category_rss = "40"


class KRYTIE_42(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> KRYTIE."""

    category_name = "kryti"
    category_rss = "42"


class STRATENI_A_NAJDENI_255(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> STRATENI_A_NAJDENI."""

    category_name = "strateni"
    category_rss = "255"


class CHOVATELSKE_POTREBY_41(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> CHOVATELSKE_POTREBY."""

    category_name = "potreby"
    category_rss = "41"


class HYDINA_44(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> HYDINA."""

    category_name = "hydina"
    category_rss = "44"


class KRALIKY_45(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> KRALIKY."""

    category_name = "kralik"
    category_rss = "45"


class OVCE_A_KOZY_46(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> OVCE_A_KOZY."""

    category_name = "koza"
    category_rss = "46"


class PRASATA_47(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> PRASATA."""

    category_name = "prase"
    category_rss = "47"


class DOBYTOK_48(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> DOBYTOK."""

    category_name = "dobytok"
    category_rss = "48"


class OSTATNE_HOSPODARSKE_49(SECTION_ZVIERATA):
    """SECTION_ZVIERATA -> OSTATNE_HOSPODARSKE."""

    category_name = "ostatnihospodarska"
    category_rss = "49"


class SECTION_DETI(Category):
    """SECTION_DETI."""

    section_name = "deti"
    section_rss = "de"

    AUTOSEDACKY: "AUTOSEDACKY_120" = None
    BABY_MONITORY: "BABY_MONITORY_121" = None
    BICYKLE: "BICYKLE_452" = None
    DETSKA_LITERATURA: "DETSKA_LITERATURA" = None
    HRACKY: "HRACKY_122" = None
    CHODITKA_A_HOPSADLA: "CHODITKA_A_HOPSADLA_123" = None
    KOCIKY: "KOCIKY_124" = None
    KOJENECKE_POTREBY: "KOJENECKE_POTREBY_126" = None
    NABYTOK_PRE_DETI: "NABYTOK_PRE_DETI_127" = None
    NOSICE: "NOSICE_128" = None
    ODRAZADLA: "ODRAZADLA_130" = None
    SEDACKY_NA_BICYKEL: "SEDACKY_NA_BICYKEL_131" = None
    SPORTOVE_POTREBY: "SPORTOVE_POTREBY_132" = None
    SKOLSKE_POTREBY: "SKOLSKE_POTREBY_133" = None
    STRAZENIE_DETI: "STRAZENIE_DETI" = None
    OSTATNE: "OSTATNE_135" = None
    BODY_DUPACKY_A_OVERALY: "BODY_DUPACKY_A_OVERALY_136" = None
    BUNDY_A_KABATIKY: "BUNDY_A_KABATIKY_137" = None
    CIAPKY_A_KLOBUCIKY: "CIAPKY_A_KLOBUCIKY_138" = None
    NOHAVICE_KRATASY_A_TEPLAKY: "NOHAVICE_KRATASY_A_TEPLAKY_139" = None
    KOMBINEZY: "KOMBINEZY_140" = None
    KOMPLETY: "KOMPLETY_438" = None
    MIKINY_A_SVETRE: "MIKINY_A_SVETRE_141" = None
    OBUV: "OBUV_129" = None
    PLAVKY: "PLAVKY_142" = None
    PONOZKY_A_PANCUSKY: "PONOZKY_A_PANCUSKY_143" = None
    PYZAMKA_A_ZUPANCEKY: "PYZAMKA_A_ZUPANCEKY_144" = None
    RUKAVICE_A_SALY: "RUKAVICE_A_SALY_145" = None
    SPODNA_BIELIZEN: "SPODNA_BIELIZEN_146" = None
    SUKNICKY_A_SATOCKY: "SUKNICKY_A_SATOCKY_147" = None
    TEHOTENSKE_OBLECENIE: "TEHOTENSKE_OBLECENIE" = None
    TRICKA_A_KOSIELKY: "TRICKA_A_KOSIELKY_148" = None
    OSTATNE_OBLECENIE: "OSTATNE_OBLECENIE_125" = None


class AUTOSEDACKY_120(SECTION_DETI):
    """SECTION_DETI -> AUTOSEDACKY."""

    category_name = "autosedacky"
    category_rss = "120"


class BABY_MONITORY_121(SECTION_DETI):
    """SECTION_DETI -> BABY_MONITORY."""

    category_name = "baby"
    category_rss = "121"


class BICYKLE_452(SECTION_DETI):
    """SECTION_DETI -> BICYKLE."""

    category_name = "bicykle"
    category_rss = "452"


class HRACKY_122(SECTION_DETI):
    """SECTION_DETI -> HRACKY."""

    category_name = "hracky"
    category_rss = "122"


class CHODITKA_A_HOPSADLA_123(SECTION_DETI):
    """SECTION_DETI -> CHODITKA_A_HOPSADLA."""

    category_name = "choditka"
    category_rss = "123"


class KOCIKY_124(SECTION_DETI):
    """SECTION_DETI -> KOCIKY."""

    category_name = "kociky"
    category_rss = "124"


class KOJENECKE_POTREBY_126(SECTION_DETI):
    """SECTION_DETI -> KOJENECKE_POTREBY."""

    category_name = "kojenecke"
    category_rss = "126"


class NABYTOK_PRE_DETI_127(SECTION_DETI):
    """SECTION_DETI -> NABYTOK_PRE_DETI."""

    category_name = "nabytok"
    category_rss = "127"


class NOSICE_128(SECTION_DETI):
    """SECTION_DETI -> NOSICE."""

    category_name = "nositka"
    category_rss = "128"


class ODRAZADLA_130(SECTION_DETI):
    """SECTION_DETI -> ODRAZADLA."""

    category_name = "odrazadla"
    category_rss = "130"


class SEDACKY_NA_BICYKEL_131(SECTION_DETI):
    """SECTION_DETI -> SEDACKY_NA_BICYKEL."""

    category_name = "sedacky"
    category_rss = "131"


class SPORTOVE_POTREBY_132(SECTION_DETI):
    """SECTION_DETI -> SPORTOVE_POTREBY."""

    category_name = "sportove"
    category_rss = "132"


class SKOLSKE_POTREBY_133(SECTION_DETI):
    """SECTION_DETI -> SKOLSKE_POTREBY."""

    category_name = "skolske"
    category_rss = "133"


class OSTATNE_135(SECTION_DETI):
    """SECTION_DETI -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "135"


class BODY_DUPACKY_A_OVERALY_136(SECTION_DETI):
    """SECTION_DETI -> BODY_DUPACKY_A_OVERALY."""

    category_name = "dupacky"
    category_rss = "136"


class BUNDY_A_KABATIKY_137(SECTION_DETI):
    """SECTION_DETI -> BUNDY_A_KABATIKY."""

    category_name = "bundy"
    category_rss = "137"


class CIAPKY_A_KLOBUCIKY_138(SECTION_DETI):
    """SECTION_DETI -> CIAPKY_A_KLOBUCIKY."""

    category_name = "ciapky"
    category_rss = "138"


class NOHAVICE_KRATASY_A_TEPLAKY_139(SECTION_DETI):
    """SECTION_DETI -> NOHAVICE_KRATASY_A_TEPLAKY."""

    category_name = "nohavice"
    category_rss = "139"


class KOMBINEZY_140(SECTION_DETI):
    """SECTION_DETI -> KOMBINEZY."""

    category_name = "kombinezy"
    category_rss = "140"


class KOMPLETY_438(SECTION_DETI):
    """SECTION_DETI -> KOMPLETY."""

    category_name = "komplety"
    category_rss = "438"


class MIKINY_A_SVETRE_141(SECTION_DETI):
    """SECTION_DETI -> MIKINY_A_SVETRE."""

    category_name = "mikiny"
    category_rss = "141"


class OBUV_129(SECTION_DETI):
    """SECTION_DETI -> OBUV."""

    category_name = "obuv"
    category_rss = "129"


class PLAVKY_142(SECTION_DETI):
    """SECTION_DETI -> PLAVKY."""

    category_name = "plavky"
    category_rss = "142"


class PONOZKY_A_PANCUSKY_143(SECTION_DETI):
    """SECTION_DETI -> PONOZKY_A_PANCUSKY."""

    category_name = "ponozky"
    category_rss = "143"


class PYZAMKA_A_ZUPANCEKY_144(SECTION_DETI):
    """SECTION_DETI -> PYZAMKA_A_ZUPANCEKY."""

    category_name = "pyzamka"
    category_rss = "144"


class RUKAVICE_A_SALY_145(SECTION_DETI):
    """SECTION_DETI -> RUKAVICE_A_SALY."""

    category_name = "rukavice"
    category_rss = "145"


class SPODNA_BIELIZEN_146(SECTION_DETI):
    """SECTION_DETI -> SPODNA_BIELIZEN."""

    category_name = "bielizen"
    category_rss = "146"


class SUKNICKY_A_SATOCKY_147(SECTION_DETI):
    """SECTION_DETI -> SUKNICKY_A_SATOCKY."""

    category_name = "suknicky"
    category_rss = "147"


class TRICKA_A_KOSIELKY_148(SECTION_DETI):
    """SECTION_DETI -> TRICKA_A_KOSIELKY."""

    category_name = "tricka"
    category_rss = "148"


class OSTATNE_OBLECENIE_125(SECTION_DETI):
    """SECTION_DETI -> OSTATNE_OBLECENIE."""

    category_name = "oblecenie"
    category_rss = "125"


class SECTION_REALITY(Category):
    """SECTION_REALITY."""

    section_name = "reality"
    section_rss = "re"

    BYTY: "BYTY_152_typ_1" = None
    DOMY: "DOMY_155_typ_1" = None
    NOVE_PROJEKTY: "NOVE_PROJEKTY_166_typ_1" = None
    GARAZE: "GARAZE_160_typ_1" = None
    HOTELY_RESTAURACIE: "HOTELY_RESTAURACIE_165_typ_1" = None
    CHALUPY_CHATY: "CHALUPY_CHATY_157_typ_1" = None
    KANCELARIE: "KANCELARIE_161_typ_1" = None
    OBCHODNE_PRIESTORY: "OBCHODNE_PRIESTORY_164_typ_1" = None
    POZEMKY: "POZEMKY_158_typ_1" = None
    SKLADY: "SKLADY_162_typ_1" = None
    ZAHRADY: "ZAHRADY_159_typ_1" = None
    OSTATNE: "OSTATNE_163_typ_1" = None
    BYTY: "BYTY_152_typ_3" = None
    DOMY: "DOMY_155_typ_3" = None
    NOVE_PROJEKTY: "NOVE_PROJEKTY_166_typ_3" = None
    PODNAJOM_SPOLUBYVAJUCI: "PODNAJOM_SPOLUBYVAJUCI_156_typ_3" = None
    GARAZE: "GARAZE_160_typ_3" = None
    HOTELY_RESTAURACIE: "HOTELY_RESTAURACIE_165_typ_3" = None
    UBYTOVANIE: "UBYTOVANIE" = None
    KANCELARIE: "KANCELARIE_161_typ_3" = None
    OBCHODNE_PRIESTORY: "OBCHODNE_PRIESTORY_164_typ_3" = None
    POZEMKY: "POZEMKY_158_typ_3" = None
    SKLADY: "SKLADY_162_typ_3" = None
    ZAHRADY: "ZAHRADY_159_typ_3" = None
    OSTATNE: "OSTATNE_163_typ_3" = None


class BYTY_152_typ_1(SECTION_REALITY):
    """SECTION_REALITY -> BYTY."""

    category_name = "predam/byt"
    category_rss = "152&typ=1"


class DOMY_155_typ_1(SECTION_REALITY):
    """SECTION_REALITY -> DOMY."""

    category_name = "predam/dom"
    category_rss = "155&typ=1"


class NOVE_PROJEKTY_166_typ_1(SECTION_REALITY):
    """SECTION_REALITY -> NOVE_PROJEKTY."""

    category_name = "predam/projekty"
    category_rss = "166&typ=1"


class GARAZE_160_typ_1(SECTION_REALITY):
    """SECTION_REALITY -> GARAZE."""

    category_name = "predam/garaz"
    category_rss = "160&typ=1"


class HOTELY_RESTAURACIE_165_typ_1(SECTION_REALITY):
    """SECTION_REALITY -> HOTELY_RESTAURACIE."""

    category_name = "predam/restauracie"
    category_rss = "165&typ=1"


class CHALUPY_CHATY_157_typ_1(SECTION_REALITY):
    """SECTION_REALITY -> CHALUPY_CHATY."""

    category_name = "predam/chata"
    category_rss = "157&typ=1"


class KANCELARIE_161_typ_1(SECTION_REALITY):
    """SECTION_REALITY -> KANCELARIE."""

    category_name = "predam/kancelar"
    category_rss = "161&typ=1"


class OBCHODNE_PRIESTORY_164_typ_1(SECTION_REALITY):
    """SECTION_REALITY -> OBCHODNE_PRIESTORY."""

    category_name = "predam/priestory"
    category_rss = "164&typ=1"


class POZEMKY_158_typ_1(SECTION_REALITY):
    """SECTION_REALITY -> POZEMKY."""

    category_name = "predam/pozemok"
    category_rss = "158&typ=1"


class SKLADY_162_typ_1(SECTION_REALITY):
    """SECTION_REALITY -> SKLADY."""

    category_name = "predam/sklad"
    category_rss = "162&typ=1"


class ZAHRADY_159_typ_1(SECTION_REALITY):
    """SECTION_REALITY -> ZAHRADY."""

    category_name = "predam/zahrada"
    category_rss = "159&typ=1"


class OSTATNE_163_typ_1(SECTION_REALITY):
    """SECTION_REALITY -> OSTATNE."""

    category_name = "predam/ostatni"
    category_rss = "163&typ=1"


class BYTY_152_typ_3(SECTION_REALITY):
    """SECTION_REALITY -> BYTY."""

    category_name = "prenajmu/byt"
    category_rss = "152&typ=3"


class DOMY_155_typ_3(SECTION_REALITY):
    """SECTION_REALITY -> DOMY."""

    category_name = "prenajmu/dom"
    category_rss = "155&typ=3"


class NOVE_PROJEKTY_166_typ_3(SECTION_REALITY):
    """SECTION_REALITY -> NOVE_PROJEKTY."""

    category_name = "prenajmu/projekty"
    category_rss = "166&typ=3"


class PODNAJOM_SPOLUBYVAJUCI_156_typ_3(SECTION_REALITY):
    """SECTION_REALITY -> PODNAJOM_SPOLUBYVAJUCI."""

    category_name = "prenajmu/podnajom"
    category_rss = "156&typ=3"


class GARAZE_160_typ_3(SECTION_REALITY):
    """SECTION_REALITY -> GARAZE."""

    category_name = "prenajmu/garaz"
    category_rss = "160&typ=3"


class HOTELY_RESTAURACIE_165_typ_3(SECTION_REALITY):
    """SECTION_REALITY -> HOTELY_RESTAURACIE."""

    category_name = "prenajmu/restauracie"
    category_rss = "165&typ=3"


class KANCELARIE_161_typ_3(SECTION_REALITY):
    """SECTION_REALITY -> KANCELARIE."""

    category_name = "prenajmu/kancelar"
    category_rss = "161&typ=3"


class OBCHODNE_PRIESTORY_164_typ_3(SECTION_REALITY):
    """SECTION_REALITY -> OBCHODNE_PRIESTORY."""

    category_name = "prenajmu/priestory"
    category_rss = "164&typ=3"


class POZEMKY_158_typ_3(SECTION_REALITY):
    """SECTION_REALITY -> POZEMKY."""

    category_name = "prenajmu/pozemok"
    category_rss = "158&typ=3"


class SKLADY_162_typ_3(SECTION_REALITY):
    """SECTION_REALITY -> SKLADY."""

    category_name = "prenajmu/sklad"
    category_rss = "162&typ=3"


class ZAHRADY_159_typ_3(SECTION_REALITY):
    """SECTION_REALITY -> ZAHRADY."""

    category_name = "prenajmu/zahrada"
    category_rss = "159&typ=3"


class OSTATNE_163_typ_3(SECTION_REALITY):
    """SECTION_REALITY -> OSTATNE."""

    category_name = "prenajmu/ostatni"
    category_rss = "163&typ=3"


class SECTION_PRACA(Category):
    """SECTION_PRACA."""

    section_name = "praca"
    section_rss = "pr"

    ADMINISTRATIVA: "ADMINISTRATIVA_341" = None
    CHEMIA_A_POTRAVINARSTVO: "CHEMIA_A_POTRAVINARSTVO_342" = None
    DOPRAVA_A_LOGISTIKA: "DOPRAVA_A_LOGISTIKA_343" = None
    FINANCIE_A_EKONOMIKA: "FINANCIE_A_EKONOMIKA_344" = None
    IT_A_TELEKOMUNIKACIE: "IT_A_TELEKOMUNIKACIE_345" = None
    MARKETING_A_REKLAMA: "MARKETING_A_REKLAMA_346" = None
    MANAGEMENT: "MANAGEMENT_347" = None
    OBCHOD_A_PREDAJ: "OBCHOD_A_PREDAJ_348" = None
    OBRANA_A_BEZPECNOST: "OBRANA_A_BEZPECNOST_349" = None
    POHOSTINSTVA_A_UBYTOVANIE: "POHOSTINSTVA_A_UBYTOVANIE_350" = None
    PRACA_V_DOMACNOSTI: "PRACA_V_DOMACNOSTI_351" = None
    PRAVO_LEGISLATIVA: "PRAVO_LEGISLATIVA_352" = None
    PRIEMYSEL_A_VYROBA: "PRIEMYSEL_A_VYROBA_353" = None
    REMESELNE_PRACE: "REMESELNE_PRACE_354" = None
    SERVIS_A_SLUZBY: "SERVIS_A_SLUZBY_355" = None
    STAVEBNICTVO: "STAVEBNICTVO_357" = None
    TECHNIKA_A_ENERGETIKA: "TECHNIKA_A_ENERGETIKA_358" = None
    TLAC_A_POLYGRAFIA: "TLAC_A_POLYGRAFIA_359" = None
    VYSKUM_A_VYVOJ: "VYSKUM_A_VYVOJ_360" = None
    VZDELAVANIE_A_PERSONALISTIKA: "VZDELAVANIE_A_PERSONALISTIKA_361" = None
    ZDRAVOTNICTVO: "ZDRAVOTNICTVO_362" = None
    POLNOHOSPODARSTVO: "POLNOHOSPODARSTVO_363" = None
    BRIGADY: "BRIGADY_364" = None
    OSTATNE: "OSTATNE_365" = None


class ADMINISTRATIVA_341(SECTION_PRACA):
    """SECTION_PRACA -> ADMINISTRATIVA."""

    category_name = "administrativa"
    category_rss = "341"


class CHEMIA_A_POTRAVINARSTVO_342(SECTION_PRACA):
    """SECTION_PRACA -> CHEMIA_A_POTRAVINARSTVO."""

    category_name = "potravinarstvo"
    category_rss = "342"


class DOPRAVA_A_LOGISTIKA_343(SECTION_PRACA):
    """SECTION_PRACA -> DOPRAVA_A_LOGISTIKA."""

    category_name = "logistika"
    category_rss = "343"


class FINANCIE_A_EKONOMIKA_344(SECTION_PRACA):
    """SECTION_PRACA -> FINANCIE_A_EKONOMIKA."""

    category_name = "financie"
    category_rss = "344"


class IT_A_TELEKOMUNIKACIE_345(SECTION_PRACA):
    """SECTION_PRACA -> IT_A_TELEKOMUNIKACIE."""

    category_name = "it"
    category_rss = "345"


class MARKETING_A_REKLAMA_346(SECTION_PRACA):
    """SECTION_PRACA -> MARKETING_A_REKLAMA."""

    category_name = "marketing"
    category_rss = "346"


class MANAGEMENT_347(SECTION_PRACA):
    """SECTION_PRACA -> MANAGEMENT."""

    category_name = "management"
    category_rss = "347"


class OBCHOD_A_PREDAJ_348(SECTION_PRACA):
    """SECTION_PRACA -> OBCHOD_A_PREDAJ."""

    category_name = "obchod"
    category_rss = "348"


class OBRANA_A_BEZPECNOST_349(SECTION_PRACA):
    """SECTION_PRACA -> OBRANA_A_BEZPECNOST."""

    category_name = "bezpecnost"
    category_rss = "349"


class POHOSTINSTVA_A_UBYTOVANIE_350(SECTION_PRACA):
    """SECTION_PRACA -> POHOSTINSTVA_A_UBYTOVANIE."""

    category_name = "ubytovanie"
    category_rss = "350"


class PRACA_V_DOMACNOSTI_351(SECTION_PRACA):
    """SECTION_PRACA -> PRACA_V_DOMACNOSTI."""

    category_name = "domacnost"
    category_rss = "351"


class PRAVO_LEGISLATIVA_352(SECTION_PRACA):
    """SECTION_PRACA -> PRAVO_LEGISLATIVA."""

    category_name = "pravo"
    category_rss = "352"


class PRIEMYSEL_A_VYROBA_353(SECTION_PRACA):
    """SECTION_PRACA -> PRIEMYSEL_A_VYROBA."""

    category_name = "priemysel"
    category_rss = "353"


class REMESELNE_PRACE_354(SECTION_PRACA):
    """SECTION_PRACA -> REMESELNE_PRACE."""

    category_name = "remeslo"
    category_rss = "354"


class SERVIS_A_SLUZBY_355(SECTION_PRACA):
    """SECTION_PRACA -> SERVIS_A_SLUZBY."""

    category_name = "sluzby"
    category_rss = "355"


class STAVEBNICTVO_357(SECTION_PRACA):
    """SECTION_PRACA -> STAVEBNICTVO."""

    category_name = "stavebnictvo"
    category_rss = "357"


class TECHNIKA_A_ENERGETIKA_358(SECTION_PRACA):
    """SECTION_PRACA -> TECHNIKA_A_ENERGETIKA."""

    category_name = "technika"
    category_rss = "358"


class TLAC_A_POLYGRAFIA_359(SECTION_PRACA):
    """SECTION_PRACA -> TLAC_A_POLYGRAFIA."""

    category_name = "tlac"
    category_rss = "359"


class VYSKUM_A_VYVOJ_360(SECTION_PRACA):
    """SECTION_PRACA -> VYSKUM_A_VYVOJ."""

    category_name = "vyskum"
    category_rss = "360"


class VZDELAVANIE_A_PERSONALISTIKA_361(SECTION_PRACA):
    """SECTION_PRACA -> VZDELAVANIE_A_PERSONALISTIKA."""

    category_name = "personalistika"
    category_rss = "361"


class ZDRAVOTNICTVO_362(SECTION_PRACA):
    """SECTION_PRACA -> ZDRAVOTNICTVO."""

    category_name = "zdravotnictvo"
    category_rss = "362"


class POLNOHOSPODARSTVO_363(SECTION_PRACA):
    """SECTION_PRACA -> POLNOHOSPODARSTVO."""

    category_name = "polnohospodarstvo"
    category_rss = "363"


class BRIGADY_364(SECTION_PRACA):
    """SECTION_PRACA -> BRIGADY."""

    category_name = "brigada"
    category_rss = "364"


class OSTATNE_365(SECTION_PRACA):
    """SECTION_PRACA -> OSTATNE."""

    category_name = "ostatni"
    category_rss = "365"


class SECTION_AUTO(Category):
    """SECTION_AUTO."""

    section_name = "auto"
    section_rss = "au"

    ALFA_ROMEO: "ALFA_ROMEO_439" = None
    AUDI: "AUDI_79" = None
    BMW: "BMW_80" = None
    CITROEN: "CITROEN_81" = None
    DACIA: "DACIA_457" = None
    FIAT: "FIAT_82" = None
    FORD: "FORD_83" = None
    HONDA: "HONDA_116" = None
    HYUNDAI: "HYUNDAI_84" = None
    CHEVROLET: "CHEVROLET_117" = None
    KIA: "KIA_118" = None
    MAZDA: "MAZDA_85" = None
    MERCEDESBENZ: "MERCEDESBENZ_86" = None
    MITSUBISHI: "MITSUBISHI_441" = None
    NISSAN: "NISSAN_87" = None
    OPEL: "OPEL_88" = None
    PEUGEOT: "PEUGEOT_89" = None
    RENAULT: "RENAULT_90" = None
    SEAT: "SEAT_91" = None
    SUZUKI: "SUZUKI_119" = None
    SKODA: "SKODA_92" = None
    TOYOTA: "TOYOTA_93" = None
    VOLKSWAGEN: "VOLKSWAGEN_94" = None
    VOLVO: "VOLVO_95" = None
    OSTATNE_ZNACKY: "OSTATNE_ZNACKY_96" = None
    AUTORADIA: "AUTORADIA" = None
    GPS_NAVIGACIA: "GPS_NAVIGACIA" = None
    HAVAROVANE: "HAVAROVANE_97" = None
    NAHRADNE_DIELY: "NAHRADNE_DIELY_98" = None
    PNEUMATIKY_KOLESA: "PNEUMATIKY_KOLESA_115" = None
    PRISLUSENSTVO: "PRISLUSENSTVO_424" = None
    TUNING: "TUNING_113" = None
    VETERANY: "VETERANY_114" = None
    AUTOBUSY: "AUTOBUSY_107" = None
    DODAVKY: "DODAVKY_100" = None
    MIKROBUSY: "MIKROBUSY_101" = None
    KARAVANY_VOZIKY: "KARAVANY_VOZIKY_111" = None
    NAKLADNE_AUTA: "NAKLADNE_AUTA_112" = None
    PICKUP: "PICKUP_99" = None
    STROJE: "STROJE" = None
    OSTATNE: "OSTATNE_102" = None
    HAVAROVANE: "HAVAROVANE_103" = None
    NAHRADNE_DIELY: "NAHRADNE_DIELY_104" = None
    MOTOCYKLE_SKUTRE: "MOTOCYKLE_SKUTRE" = None


class ALFA_ROMEO_439(SECTION_AUTO):
    """SECTION_AUTO -> ALFA_ROMEO."""

    category_name = "alfa"
    category_rss = "439"


class AUDI_79(SECTION_AUTO):
    """SECTION_AUTO -> AUDI."""

    category_name = "audi"
    category_rss = "79"


class BMW_80(SECTION_AUTO):
    """SECTION_AUTO -> BMW."""

    category_name = "bmw"
    category_rss = "80"


class CITROEN_81(SECTION_AUTO):
    """SECTION_AUTO -> CITROEN."""

    category_name = "citroen"
    category_rss = "81"


class DACIA_457(SECTION_AUTO):
    """SECTION_AUTO -> DACIA."""

    category_name = "dacia"
    category_rss = "457"


class FIAT_82(SECTION_AUTO):
    """SECTION_AUTO -> FIAT."""

    category_name = "fiat"
    category_rss = "82"


class FORD_83(SECTION_AUTO):
    """SECTION_AUTO -> FORD."""

    category_name = "ford"
    category_rss = "83"


class HONDA_116(SECTION_AUTO):
    """SECTION_AUTO -> HONDA."""

    category_name = "honda"
    category_rss = "116"


class HYUNDAI_84(SECTION_AUTO):
    """SECTION_AUTO -> HYUNDAI."""

    category_name = "hyundai"
    category_rss = "84"


class CHEVROLET_117(SECTION_AUTO):
    """SECTION_AUTO -> CHEVROLET."""

    category_name = "chevrolet"
    category_rss = "117"


class KIA_118(SECTION_AUTO):
    """SECTION_AUTO -> KIA."""

    category_name = "kia"
    category_rss = "118"


class MAZDA_85(SECTION_AUTO):
    """SECTION_AUTO -> MAZDA."""

    category_name = "mazda"
    category_rss = "85"


class MERCEDESBENZ_86(SECTION_AUTO):
    """SECTION_AUTO -> MERCEDESBENZ."""

    category_name = "mercedes"
    category_rss = "86"


class MITSUBISHI_441(SECTION_AUTO):
    """SECTION_AUTO -> MITSUBISHI."""

    category_name = "mitsubishi"
    category_rss = "441"


class NISSAN_87(SECTION_AUTO):
    """SECTION_AUTO -> NISSAN."""

    category_name = "nissan"
    category_rss = "87"


class OPEL_88(SECTION_AUTO):
    """SECTION_AUTO -> OPEL."""

    category_name = "opel"
    category_rss = "88"


class PEUGEOT_89(SECTION_AUTO):
    """SECTION_AUTO -> PEUGEOT."""

    category_name = "peugeot"
    category_rss = "89"


class RENAULT_90(SECTION_AUTO):
    """SECTION_AUTO -> RENAULT."""

    category_name = "renault"
    category_rss = "90"


class SEAT_91(SECTION_AUTO):
    """SECTION_AUTO -> SEAT."""

    category_name = "seat"
    category_rss = "91"


class SUZUKI_119(SECTION_AUTO):
    """SECTION_AUTO -> SUZUKI."""

    category_name = "suzuki"
    category_rss = "119"


class SKODA_92(SECTION_AUTO):
    """SECTION_AUTO -> SKODA."""

    category_name = "skoda"
    category_rss = "92"


class TOYOTA_93(SECTION_AUTO):
    """SECTION_AUTO -> TOYOTA."""

    category_name = "toyota"
    category_rss = "93"


class VOLKSWAGEN_94(SECTION_AUTO):
    """SECTION_AUTO -> VOLKSWAGEN."""

    category_name = "volkswagen"
    category_rss = "94"


class VOLVO_95(SECTION_AUTO):
    """SECTION_AUTO -> VOLVO."""

    category_name = "volvo"
    category_rss = "95"


class OSTATNE_ZNACKY_96(SECTION_AUTO):
    """SECTION_AUTO -> OSTATNE_ZNACKY."""

    category_name = "ostatni"
    category_rss = "96"


class HAVAROVANE_97(SECTION_AUTO):
    """SECTION_AUTO -> HAVAROVANE."""

    category_name = "havarovana"
    category_rss = "97"


class NAHRADNE_DIELY_98(SECTION_AUTO):
    """SECTION_AUTO -> NAHRADNE_DIELY."""

    category_name = "nahradnidily"
    category_rss = "98"


class PNEUMATIKY_KOLESA_115(SECTION_AUTO):
    """SECTION_AUTO -> PNEUMATIKY_KOLESA."""

    category_name = "pneumatiky"
    category_rss = "115"


class PRISLUSENSTVO_424(SECTION_AUTO):
    """SECTION_AUTO -> PRISLUSENSTVO."""

    category_name = "prislusenstvo"
    category_rss = "424"


class TUNING_113(SECTION_AUTO):
    """SECTION_AUTO -> TUNING."""

    category_name = "tuning"
    category_rss = "113"


class VETERANY_114(SECTION_AUTO):
    """SECTION_AUTO -> VETERANY."""

    category_name = "veterany"
    category_rss = "114"


class AUTOBUSY_107(SECTION_AUTO):
    """SECTION_AUTO -> AUTOBUSY."""

    category_name = "autobusy"
    category_rss = "107"


class DODAVKY_100(SECTION_AUTO):
    """SECTION_AUTO -> DODAVKY."""

    category_name = "dodavka"
    category_rss = "100"


class MIKROBUSY_101(SECTION_AUTO):
    """SECTION_AUTO -> MIKROBUSY."""

    category_name = "mikrobus"
    category_rss = "101"


class KARAVANY_VOZIKY_111(SECTION_AUTO):
    """SECTION_AUTO -> KARAVANY_VOZIKY."""

    category_name = "karavany"
    category_rss = "111"


class NAKLADNE_AUTA_112(SECTION_AUTO):
    """SECTION_AUTO -> NAKLADNE_AUTA."""

    category_name = "nakladne"
    category_rss = "112"


class PICKUP_99(SECTION_AUTO):
    """SECTION_AUTO -> PICKUP."""

    category_name = "pickup"
    category_rss = "99"


class OSTATNE_102(SECTION_AUTO):
    """SECTION_AUTO -> OSTATNE."""

    category_name = "ostatniuzitkova"
    category_rss = "102"


class HAVAROVANE_103(SECTION_AUTO):
    """SECTION_AUTO -> HAVAROVANE."""

    category_name = "havarovanauzitkova"
    category_rss = "103"


class NAHRADNE_DIELY_104(SECTION_AUTO):
    """SECTION_AUTO -> NAHRADNE_DIELY."""

    category_name = "nahradnidilyuzitkova"
    category_rss = "104"


class SECTION_MOTOCYKLE(Category):
    """SECTION_MOTOCYKLE."""

    section_name = "motocykle"
    section_rss = "mt"

    CESTNE_MOTOCYKLE: "CESTNE_MOTOCYKLE_186" = None
    CESTOVNE_MOTOCYKLE: "CESTOVNE_MOTOCYKLE_187" = None
    ENDURO: "ENDURO_188" = None
    CHOPPER: "CHOPPER_189" = None
    MINIBIKE: "MINIBIKE_190" = None
    MOPEDY: "MOPEDY_192" = None
    SKUTRE: "SKUTRE_193" = None
    SKUTRE_VODNE: "SKUTRE_VODNE_194" = None
    SKUTRE_SNEZNE: "SKUTRE_SNEZNE_191" = None
    STVORKOLKY: "STVORKOLKY_195" = None
    TROJKOLKY: "TROJKOLKY_196" = None
    VETERANY: "VETERANY_197" = None
    NAHRADNE_DIELY: "NAHRADNE_DIELY_198" = None
    OBLECENIE_OBUV_HELMY: "OBLECENIE_OBUV_HELMY_199" = None
    OSTATNE: "OSTATNE_200" = None


class CESTNE_MOTOCYKLE_186(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> CESTNE_MOTOCYKLE."""

    category_name = "cestne"
    category_rss = "186"


class CESTOVNE_MOTOCYKLE_187(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> CESTOVNE_MOTOCYKLE."""

    category_name = "cestovne"
    category_rss = "187"


class ENDURO_188(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> ENDURO."""

    category_name = "enduro"
    category_rss = "188"


class CHOPPER_189(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> CHOPPER."""

    category_name = "chopper"
    category_rss = "189"


class MINIBIKE_190(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> MINIBIKE."""

    category_name = "minibike"
    category_rss = "190"


class MOPEDY_192(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> MOPEDY."""

    category_name = "mopedy"
    category_rss = "192"


class SKUTRE_193(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> SKUTRE."""

    category_name = "skutre"
    category_rss = "193"


class SKUTRE_VODNE_194(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> SKUTRE_VODNE."""

    category_name = "vodne"
    category_rss = "194"


class SKUTRE_SNEZNE_191(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> SKUTRE_SNEZNE."""

    category_name = "snezne"
    category_rss = "191"


class STVORKOLKY_195(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> STVORKOLKY."""

    category_name = "stvorkolky"
    category_rss = "195"


class TROJKOLKY_196(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> TROJKOLKY."""

    category_name = "trojkolky"
    category_rss = "196"


class VETERANY_197(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> VETERANY."""

    category_name = "veterany"
    category_rss = "197"


class NAHRADNE_DIELY_198(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> NAHRADNE_DIELY."""

    category_name = "diely"
    category_rss = "198"


class OBLECENIE_OBUV_HELMY_199(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> OBLECENIE_OBUV_HELMY."""

    category_name = "helmy"
    category_rss = "199"


class OSTATNE_200(SECTION_MOTOCYKLE):
    """SECTION_MOTOCYKLE -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "200"


class SECTION_STROJE(Category):
    """SECTION_STROJE."""

    section_name = "stroje"
    section_rss = "st"

    CERPADLA: "CERPADLA_208" = None
    CISTIACE_STROJE: "CISTIACE_STROJE_209" = None
    DREVOOBRABACIE_STROJE: "DREVOOBRABACIE_STROJE_210" = None
    GENERATORY: "GENERATORY_211" = None
    HISTORICKE_STROJE: "HISTORICKE_STROJE_212" = None
    MOTORY: "MOTORY_214" = None
    KOVOOBRABACIE_STROJE: "KOVOOBRABACIE_STROJE_215" = None
    POLNOHOSPODARSKA_TECHNIKA: "POLNOHOSPODARSKA_TECHNIKA_216" = None
    POTRAVINARSKE_STROJE: "POTRAVINARSKE_STROJE_213" = None
    SKLADOVA_TECHNIKA: "SKLADOVA_TECHNIKA_217" = None
    STAVEBNE_STROJE: "STAVEBNE_STROJE_218" = None
    TEXTILNE_STROJE: "TEXTILNE_STROJE_219" = None
    TLACIARENSKE_STROJE: "TLACIARENSKE_STROJE_220" = None
    VYBAVENIE_PREVADZKARNE: "VYBAVENIE_PREVADZKARNE_221" = None
    VYROBNA_LINKA: "VYROBNA_LINKA_222" = None
    NAHRADNE_DIELY: "NAHRADNE_DIELY_223" = None
    OSTATNE: "OSTATNE_224" = None


class CERPADLA_208(SECTION_STROJE):
    """SECTION_STROJE -> CERPADLA."""

    category_name = "cerpadla"
    category_rss = "208"


class CISTIACE_STROJE_209(SECTION_STROJE):
    """SECTION_STROJE -> CISTIACE_STROJE."""

    category_name = "cistiace"
    category_rss = "209"


class DREVOOBRABACIE_STROJE_210(SECTION_STROJE):
    """SECTION_STROJE -> DREVOOBRABACIE_STROJE."""

    category_name = "drevoobrabacie"
    category_rss = "210"


class GENERATORY_211(SECTION_STROJE):
    """SECTION_STROJE -> GENERATORY."""

    category_name = "generatory"
    category_rss = "211"


class HISTORICKE_STROJE_212(SECTION_STROJE):
    """SECTION_STROJE -> HISTORICKE_STROJE."""

    category_name = "historicke"
    category_rss = "212"


class MOTORY_214(SECTION_STROJE):
    """SECTION_STROJE -> MOTORY."""

    category_name = "motory"
    category_rss = "214"


class KOVOOBRABACIE_STROJE_215(SECTION_STROJE):
    """SECTION_STROJE -> KOVOOBRABACIE_STROJE."""

    category_name = "kovoobrabacie"
    category_rss = "215"


class POLNOHOSPODARSKA_TECHNIKA_216(SECTION_STROJE):
    """SECTION_STROJE -> POLNOHOSPODARSKA_TECHNIKA."""

    category_name = "polnohospodarska"
    category_rss = "216"


class POTRAVINARSKE_STROJE_213(SECTION_STROJE):
    """SECTION_STROJE -> POTRAVINARSKE_STROJE."""

    category_name = "potravinarske"
    category_rss = "213"


class SKLADOVA_TECHNIKA_217(SECTION_STROJE):
    """SECTION_STROJE -> SKLADOVA_TECHNIKA."""

    category_name = "skladova"
    category_rss = "217"


class STAVEBNE_STROJE_218(SECTION_STROJE):
    """SECTION_STROJE -> STAVEBNE_STROJE."""

    category_name = "stavebne"
    category_rss = "218"


class TEXTILNE_STROJE_219(SECTION_STROJE):
    """SECTION_STROJE -> TEXTILNE_STROJE."""

    category_name = "textilne"
    category_rss = "219"


class TLACIARENSKE_STROJE_220(SECTION_STROJE):
    """SECTION_STROJE -> TLACIARENSKE_STROJE."""

    category_name = "tlaciarenske"
    category_rss = "220"


class VYBAVENIE_PREVADZKARNE_221(SECTION_STROJE):
    """SECTION_STROJE -> VYBAVENIE_PREVADZKARNE."""

    category_name = "prevadzkarne"
    category_rss = "221"


class VYROBNA_LINKA_222(SECTION_STROJE):
    """SECTION_STROJE -> VYROBNA_LINKA."""

    category_name = "linka"
    category_rss = "222"


class NAHRADNE_DIELY_223(SECTION_STROJE):
    """SECTION_STROJE -> NAHRADNE_DIELY."""

    category_name = "diely"
    category_rss = "223"


class OSTATNE_224(SECTION_STROJE):
    """SECTION_STROJE -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "224"


class SECTION_DOM_A_ZAHRADA(Category):
    """SECTION_DOM_A_ZAHRADA."""

    section_name = "dom"
    section_rss = "du"

    BAZENY: "BAZENY_238" = None
    CERPADLA: "CERPADLA_239" = None
    DVERE_BRANY: "DVERE_BRANY_447" = None
    KLIMATIZACIE: "KLIMATIZACIE_240" = None
    KOSACKY: "KOSACKY_247" = None
    KOTLE_KACHLE_BOJLERY: "KOTLE_KACHLE_BOJLERY_241" = None
    MALOTRAKTORY_KULTIVATORY: "MALOTRAKTORY_KULTIVATORY_242" = None
    MIESACKY: "MIESACKY_244" = None
    NARADIE: "NARADIE_245" = None
    OKNA: "OKNA_448" = None
    PILY: "PILY_449" = None
    SNEZNA_TECHNIKA: "SNEZNA_TECHNIKA_248" = None
    STAVEBNY_MATERIAL: "STAVEBNY_MATERIAL_249" = None
    RADIATORY: "RADIATORY_246" = None
    RASTLINY: "RASTLINY_243" = None
    VYBAVENIE_DIELNE: "VYBAVENIE_DIELNE_250" = None
    VYSAVACE_FUKACE: "VYSAVACE_FUKACE_251" = None
    ZAHRADNE_GRILY: "ZAHRADNE_GRILY_252" = None
    ZAHRADNY_NABYTOK: "ZAHRADNY_NABYTOK" = None
    ZAHRADNA_TECHNIKA: "ZAHRADNA_TECHNIKA_253" = None
    OSTATNE: "OSTATNE_254" = None


class BAZENY_238(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> BAZENY."""

    category_name = "bazeny"
    category_rss = "238"


class CERPADLA_239(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> CERPADLA."""

    category_name = "cerpadla"
    category_rss = "239"


class DVERE_BRANY_447(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> DVERE_BRANY."""

    category_name = "dvere"
    category_rss = "447"


class KLIMATIZACIE_240(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> KLIMATIZACIE."""

    category_name = "klimatizacie"
    category_rss = "240"


class KOSACKY_247(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> KOSACKY."""

    category_name = "kosacky"
    category_rss = "247"


class KOTLE_KACHLE_BOJLERY_241(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> KOTLE_KACHLE_BOJLERY."""

    category_name = "kotle"
    category_rss = "241"


class MALOTRAKTORY_KULTIVATORY_242(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> MALOTRAKTORY_KULTIVATORY."""

    category_name = "malotraktory"
    category_rss = "242"


class MIESACKY_244(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> MIESACKY."""

    category_name = "miesacky"
    category_rss = "244"


class NARADIE_245(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> NARADIE."""

    category_name = "naradie"
    category_rss = "245"


class OKNA_448(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> OKNA."""

    category_name = "okna"
    category_rss = "448"


class PILY_449(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> PILY."""

    category_name = "pily"
    category_rss = "449"


class SNEZNA_TECHNIKA_248(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> SNEZNA_TECHNIKA."""

    category_name = "snezna"
    category_rss = "248"


class STAVEBNY_MATERIAL_249(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> STAVEBNY_MATERIAL."""

    category_name = "stavebny"
    category_rss = "249"


class RADIATORY_246(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> RADIATORY."""

    category_name = "radiatory"
    category_rss = "246"


class RASTLINY_243(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> RASTLINY."""

    category_name = "rastliny"
    category_rss = "243"


class VYBAVENIE_DIELNE_250(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> VYBAVENIE_DIELNE."""

    category_name = "vybavenie"
    category_rss = "250"


class VYSAVACE_FUKACE_251(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> VYSAVACE_FUKACE."""

    category_name = "vysavace"
    category_rss = "251"


class ZAHRADNE_GRILY_252(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> ZAHRADNE_GRILY."""

    category_name = "grily"
    category_rss = "252"


class ZAHRADNA_TECHNIKA_253(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> ZAHRADNA_TECHNIKA."""

    category_name = "technika"
    category_rss = "253"


class OSTATNE_254(SECTION_DOM_A_ZAHRADA):
    """SECTION_DOM_A_ZAHRADA -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "254"


class SECTION_PC(Category):
    """SECTION_PC."""

    section_name = "pc"
    section_rss = "pc"

    DVD_BLURAY_MECHANIKY: "DVD_BLURAY_MECHANIKY_1" = None
    FOTOAPARATY: "FOTOAPARATY" = None
    GPS_NAVIGACIA: "GPS_NAVIGACIA_32" = None
    GRAFICKE_KARTY: "GRAFICKE_KARTY_4" = None
    HARD_DISKY_SSD: "HARD_DISKY_SSD_5" = None
    HERNE_KONZOLY: "HERNE_KONZOLY_25" = None
    HERNE_ZARIADENIA: "HERNE_ZARIADENIA_29" = None
    HRY: "HRY_30" = None
    CHLADICE: "CHLADICE_27" = None
    KLAVESNICE_MYSI: "KLAVESNICE_MYSI_6" = None
    KOPIROVACIE_STROJE: "KOPIROVACIE_STROJE_7" = None
    MOBILNE_TELEFONY: "MOBILNE_TELEFONY" = None
    MODEMY: "MODEMY_2" = None
    LCD_MONITORY: "LCD_MONITORY_9" = None
    MP3_PREHRAVACE: "MP3_PREHRAVACE_26" = None
    NOTEBOOKY: "NOTEBOOKY_10" = None
    PAMATE: "PAMATE_11" = None
    PC_POCITACE: "PC_POCITACE_12" = None
    PROCESORY: "PROCESORY_13" = None
    SIETOVE_KOMPONENTY: "SIETOVE_KOMPONENTY_14" = None
    SCANERY: "SCANERY_15" = None
    SKRINE_ZDROJE: "SKRINE_ZDROJE_16" = None
    SOFTWARE: "SOFTWARE_17" = None
    SPOTREBNY_MATERIAL: "SPOTREBNY_MATERIAL_31" = None
    TABLETY_ECITACKY: "TABLETY_ECITACKY_24" = None
    TLACIARNE: "TLACIARNE_18" = None
    WIRELESS_WIFI: "WIRELESS_WIFI_28" = None
    ZAKLADNE_DOSKY: "ZAKLADNE_DOSKY_19" = None
    ZALOZNE_ZDROJE: "ZALOZNE_ZDROJE_20" = None
    ZVUKOVE_KARTY: "ZVUKOVE_KARTY_21" = None
    OSTATNE: "OSTATNE_22" = None


class DVD_BLURAY_MECHANIKY_1(SECTION_PC):
    """SECTION_PC -> DVD_BLURAY_MECHANIKY."""

    category_name = "cd"
    category_rss = "1"


class GPS_NAVIGACIA_32(SECTION_PC):
    """SECTION_PC -> GPS_NAVIGACIA."""

    category_name = "gps"
    category_rss = "32"


class GRAFICKE_KARTY_4(SECTION_PC):
    """SECTION_PC -> GRAFICKE_KARTY."""

    category_name = "graficka"
    category_rss = "4"


class HARD_DISKY_SSD_5(SECTION_PC):
    """SECTION_PC -> HARD_DISKY_SSD."""

    category_name = "hdd"
    category_rss = "5"


class HERNE_KONZOLY_25(SECTION_PC):
    """SECTION_PC -> HERNE_KONZOLY."""

    category_name = "playstation"
    category_rss = "25"


class HERNE_ZARIADENIA_29(SECTION_PC):
    """SECTION_PC -> HERNE_ZARIADENIA."""

    category_name = "volanty"
    category_rss = "29"


class HRY_30(SECTION_PC):
    """SECTION_PC -> HRY."""

    category_name = "hry"
    category_rss = "30"


class CHLADICE_27(SECTION_PC):
    """SECTION_PC -> CHLADICE."""

    category_name = "chladic"
    category_rss = "27"


class KLAVESNICE_MYSI_6(SECTION_PC):
    """SECTION_PC -> KLAVESNICE_MYSI."""

    category_name = "mys"
    category_rss = "6"


class KOPIROVACIE_STROJE_7(SECTION_PC):
    """SECTION_PC -> KOPIROVACIE_STROJE."""

    category_name = "kopirka"
    category_rss = "7"


class MODEMY_2(SECTION_PC):
    """SECTION_PC -> MODEMY."""

    category_name = "modem"
    category_rss = "2"


class LCD_MONITORY_9(SECTION_PC):
    """SECTION_PC -> LCD_MONITORY."""

    category_name = "monitor"
    category_rss = "9"


class MP3_PREHRAVACE_26(SECTION_PC):
    """SECTION_PC -> MP3_PREHRAVACE."""

    category_name = "mp3"
    category_rss = "26"


class NOTEBOOKY_10(SECTION_PC):
    """SECTION_PC -> NOTEBOOKY."""

    category_name = "notebook"
    category_rss = "10"


class PAMATE_11(SECTION_PC):
    """SECTION_PC -> PAMATE."""

    category_name = "pamet"
    category_rss = "11"


class PC_POCITACE_12(SECTION_PC):
    """SECTION_PC -> PC_POCITACE."""

    category_name = "pc"
    category_rss = "12"


class PROCESORY_13(SECTION_PC):
    """SECTION_PC -> PROCESORY."""

    category_name = "procesor"
    category_rss = "13"


class SIETOVE_KOMPONENTY_14(SECTION_PC):
    """SECTION_PC -> SIETOVE_KOMPONENTY."""

    category_name = "sit"
    category_rss = "14"


class SCANERY_15(SECTION_PC):
    """SECTION_PC -> SCANERY."""

    category_name = "scaner"
    category_rss = "15"


class SKRINE_ZDROJE_16(SECTION_PC):
    """SECTION_PC -> SKRINE_ZDROJE."""

    category_name = "case"
    category_rss = "16"


class SOFTWARE_17(SECTION_PC):
    """SECTION_PC -> SOFTWARE."""

    category_name = "software"
    category_rss = "17"


class SPOTREBNY_MATERIAL_31(SECTION_PC):
    """SECTION_PC -> SPOTREBNY_MATERIAL."""

    category_name = "spotrebny"
    category_rss = "31"


class TABLETY_ECITACKY_24(SECTION_PC):
    """SECTION_PC -> TABLETY_ECITACKY."""

    category_name = "tablet"
    category_rss = "24"


class TLACIARNE_18(SECTION_PC):
    """SECTION_PC -> TLACIARNE."""

    category_name = "tlaciaren"
    category_rss = "18"


class WIRELESS_WIFI_28(SECTION_PC):
    """SECTION_PC -> WIRELESS_WIFI."""

    category_name = "wifi"
    category_rss = "28"


class ZAKLADNE_DOSKY_19(SECTION_PC):
    """SECTION_PC -> ZAKLADNE_DOSKY."""

    category_name = "motherboard"
    category_rss = "19"


class ZALOZNE_ZDROJE_20(SECTION_PC):
    """SECTION_PC -> ZALOZNE_ZDROJE."""

    category_name = "ups"
    category_rss = "20"


class ZVUKOVE_KARTY_21(SECTION_PC):
    """SECTION_PC -> ZVUKOVE_KARTY."""

    category_name = "sound"
    category_rss = "21"


class OSTATNE_22(SECTION_PC):
    """SECTION_PC -> OSTATNE."""

    category_name = "ostatni"
    category_rss = "22"


class SECTION_MOBILY(Category):
    """SECTION_MOBILY."""

    section_name = "mobil"
    section_rss = "mo"

    APPLE: "APPLE_435" = None
    HTC: "HTC_436" = None
    HUAWEI_HONOR: "HUAWEI_HONOR_305" = None
    LG: "LG_301" = None
    MOTOROLA_LENOVO: "MOTOROLA_LENOVO_302" = None
    NOKIA_MICROSOFT: "NOKIA_MICROSOFT_303" = None
    SAMSUNG: "SAMSUNG_304" = None
    SONY: "SONY_306" = None
    XIAOMI: "XIAOMI_451" = None
    OSTATNE_ZNACKY: "OSTATNE_ZNACKY_307" = None
    BATERIE: "BATERIE_308" = None
    BEZDROTOVE_TELEFONY: "BEZDROTOVE_TELEFONY_316" = None
    DATOVE_KABELY: "DATOVE_KABELY_309" = None
    FAXY: "FAXY_317" = None
    GPS_NAVIGACIA: "GPS_NAVIGACIA" = None
    HEADSETY: "HEADSETY_310" = None
    HF_SADY_DO_AUTA: "HF_SADY_DO_AUTA_311" = None
    INTELIGENTNE_HODINKY: "INTELIGENTNE_HODINKY_450" = None
    KLASICKE_TELEFONY: "KLASICKE_TELEFONY_318" = None
    KRYTY: "KRYTY_440" = None
    NABIJACKY: "NABIJACKY_312" = None
    PAMATOVE_KARTY: "PAMATOVE_KARTY_313" = None
    OSTATNE: "OSTATNE_315" = None


class APPLE_435(SECTION_MOBILY):
    """SECTION_MOBILY -> APPLE."""

    category_name = "apple"
    category_rss = "435"


class HTC_436(SECTION_MOBILY):
    """SECTION_MOBILY -> HTC."""

    category_name = "htc"
    category_rss = "436"


class HUAWEI_HONOR_305(SECTION_MOBILY):
    """SECTION_MOBILY -> HUAWEI_HONOR."""

    category_name = "huawei"
    category_rss = "305"


class LG_301(SECTION_MOBILY):
    """SECTION_MOBILY -> LG."""

    category_name = "lg"
    category_rss = "301"


class MOTOROLA_LENOVO_302(SECTION_MOBILY):
    """SECTION_MOBILY -> MOTOROLA_LENOVO."""

    category_name = "motorola"
    category_rss = "302"


class NOKIA_MICROSOFT_303(SECTION_MOBILY):
    """SECTION_MOBILY -> NOKIA_MICROSOFT."""

    category_name = "nokia"
    category_rss = "303"


class SAMSUNG_304(SECTION_MOBILY):
    """SECTION_MOBILY -> SAMSUNG."""

    category_name = "samsung"
    category_rss = "304"


class SONY_306(SECTION_MOBILY):
    """SECTION_MOBILY -> SONY."""

    category_name = "ericsson"
    category_rss = "306"


class XIAOMI_451(SECTION_MOBILY):
    """SECTION_MOBILY -> XIAOMI."""

    category_name = "xiaomi"
    category_rss = "451"


class OSTATNE_ZNACKY_307(SECTION_MOBILY):
    """SECTION_MOBILY -> OSTATNE_ZNACKY."""

    category_name = "mobily"
    category_rss = "307"


class BATERIE_308(SECTION_MOBILY):
    """SECTION_MOBILY -> BATERIE."""

    category_name = "baterie"
    category_rss = "308"


class BEZDROTOVE_TELEFONY_316(SECTION_MOBILY):
    """SECTION_MOBILY -> BEZDROTOVE_TELEFONY."""

    category_name = "bezdrotove"
    category_rss = "316"


class DATOVE_KABELY_309(SECTION_MOBILY):
    """SECTION_MOBILY -> DATOVE_KABELY."""

    category_name = "kabely"
    category_rss = "309"


class FAXY_317(SECTION_MOBILY):
    """SECTION_MOBILY -> FAXY."""

    category_name = "faxy"
    category_rss = "317"


class HEADSETY_310(SECTION_MOBILY):
    """SECTION_MOBILY -> HEADSETY."""

    category_name = "headsety"
    category_rss = "310"


class HF_SADY_DO_AUTA_311(SECTION_MOBILY):
    """SECTION_MOBILY -> HF_SADY_DO_AUTA."""

    category_name = "hf"
    category_rss = "311"


class INTELIGENTNE_HODINKY_450(SECTION_MOBILY):
    """SECTION_MOBILY -> INTELIGENTNE_HODINKY."""

    category_name = "smartwatch"
    category_rss = "450"


class KLASICKE_TELEFONY_318(SECTION_MOBILY):
    """SECTION_MOBILY -> KLASICKE_TELEFONY."""

    category_name = "telefony"
    category_rss = "318"


class KRYTY_440(SECTION_MOBILY):
    """SECTION_MOBILY -> KRYTY."""

    category_name = "kryty"
    category_rss = "440"


class NABIJACKY_312(SECTION_MOBILY):
    """SECTION_MOBILY -> NABIJACKY."""

    category_name = "nabijacky"
    category_rss = "312"


class PAMATOVE_KARTY_313(SECTION_MOBILY):
    """SECTION_MOBILY -> PAMATOVE_KARTY."""

    category_name = "karty"
    category_rss = "313"


class OSTATNE_315(SECTION_MOBILY):
    """SECTION_MOBILY -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "315"


class SECTION_FOTO(Category):
    """SECTION_FOTO."""

    section_name = "foto"
    section_rss = "fo"

    ANALOGOVE_FOTOAPARATY: "ANALOGOVE_FOTOAPARATY_443" = None
    DIGITALNE_FOTOAPARATY: "DIGITALNE_FOTOAPARATY_256" = None
    DRONY: "DRONY_456" = None
    VIDEOKAMERY: "VIDEOKAMERY_258" = None
    ZRKADLOVKY: "ZRKADLOVKY_257" = None
    BATERIE: "BATERIE_259" = None
    BLESKY_A_OSVETLENIE: "BLESKY_A_OSVETLENIE_442" = None
    BRASNE_A_PUZDRA: "BRASNE_A_PUZDRA_260" = None
    DATOVE_KABLE: "DATOVE_KABLE_262" = None
    FILTRE: "FILTRE_263" = None
    NABIJACKY: "NABIJACKY_264" = None
    OBJEKTIVY: "OBJEKTIVY_261" = None
    PAMATOVE_KARTY: "PAMATOVE_KARTY_265" = None
    STATIVY: "STATIVY_266" = None
    OSTATNE: "OSTATNE_267" = None


class ANALOGOVE_FOTOAPARATY_443(SECTION_FOTO):
    """SECTION_FOTO -> ANALOGOVE_FOTOAPARATY."""

    category_name = "kinofilm"
    category_rss = "443"


class DIGITALNE_FOTOAPARATY_256(SECTION_FOTO):
    """SECTION_FOTO -> DIGITALNE_FOTOAPARATY."""

    category_name = "digitalne"
    category_rss = "256"


class DRONY_456(SECTION_FOTO):
    """SECTION_FOTO -> DRONY."""

    category_name = "drony"
    category_rss = "456"


class VIDEOKAMERY_258(SECTION_FOTO):
    """SECTION_FOTO -> VIDEOKAMERY."""

    category_name = "videokamery"
    category_rss = "258"


class ZRKADLOVKY_257(SECTION_FOTO):
    """SECTION_FOTO -> ZRKADLOVKY."""

    category_name = "zrkadlovky"
    category_rss = "257"


class BATERIE_259(SECTION_FOTO):
    """SECTION_FOTO -> BATERIE."""

    category_name = "baterie"
    category_rss = "259"


class BLESKY_A_OSVETLENIE_442(SECTION_FOTO):
    """SECTION_FOTO -> BLESKY_A_OSVETLENIE."""

    category_name = "blesky"
    category_rss = "442"


class BRASNE_A_PUZDRA_260(SECTION_FOTO):
    """SECTION_FOTO -> BRASNE_A_PUZDRA."""

    category_name = "brasne"
    category_rss = "260"


class DATOVE_KABLE_262(SECTION_FOTO):
    """SECTION_FOTO -> DATOVE_KABLE."""

    category_name = "kable"
    category_rss = "262"


class FILTRE_263(SECTION_FOTO):
    """SECTION_FOTO -> FILTRE."""

    category_name = "filtre"
    category_rss = "263"


class NABIJACKY_264(SECTION_FOTO):
    """SECTION_FOTO -> NABIJACKY."""

    category_name = "nabijacky"
    category_rss = "264"


class OBJEKTIVY_261(SECTION_FOTO):
    """SECTION_FOTO -> OBJEKTIVY."""

    category_name = "objektivy"
    category_rss = "261"


class PAMATOVE_KARTY_265(SECTION_FOTO):
    """SECTION_FOTO -> PAMATOVE_KARTY."""

    category_name = "karty"
    category_rss = "265"


class STATIVY_266(SECTION_FOTO):
    """SECTION_FOTO -> STATIVY."""

    category_name = "stativy"
    category_rss = "266"


class OSTATNE_267(SECTION_FOTO):
    """SECTION_FOTO -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "267"


class SECTION_ELEKTRO(Category):
    """SECTION_ELEKTRO."""

    section_name = "elektro"
    section_rss = "el"

    DIGESTORY: "DIGESTORY_389" = None
    CHLADNICKY: "CHLADNICKY_390" = None
    MIKROVLNNE_RURY: "MIKROVLNNE_RURY_391" = None
    MRAZNICKY: "MRAZNICKY_392" = None
    PRACKY: "PRACKY_394" = None
    SPORAKY: "SPORAKY_395" = None
    SUSICKY: "SUSICKY_396" = None
    UMYVACKY_RIADU: "UMYVACKY_RIADU_393" = None
    OSTATNE_BIELA: "OSTATNE_BIELA_397" = None
    AUTORADIA: "AUTORADIA_398" = None
    DOMACE_KINA: "DOMACE_KINA_400" = None
    FOTOAPARATY: "FOTOAPARATY" = None
    GPS_NAVIGACIA: "GPS_NAVIGACIA" = None
    HIFI_SYSTEMY_RADIA: "HIFI_SYSTEMY_RADIA_402" = None
    HUDOBNE_NASTROJE: "HUDOBNE_NASTROJE" = None
    MP3_PREHRAVACE: "MP3_PREHRAVACE" = None
    PROJEKTORY: "PROJEKTORY_404" = None
    REPRO_SUSTAVY: "REPRO_SUSTAVY_405" = None
    SLUCHADLA: "SLUCHADLA_399" = None
    TELEVIZORY: "TELEVIZORY_406" = None
    VIDEO_DVD_PREHRAVACE: "VIDEO_DVD_PREHRAVACE_407" = None
    VIDEOKAMERY: "VIDEOKAMERY" = None
    ZOSILNOVACE: "ZOSILNOVACE_409" = None
    OSTATNE_AUDIO_VIDEO: "OSTATNE_AUDIO_VIDEO_410" = None
    EPILATORY_DEPILATORY: "EPILATORY_DEPILATORY_411" = None
    FENY_KULMY: "FENY_KULMY_412" = None
    HOLIACE_STROJCEKY: "HOLIACE_STROJCEKY_413" = None
    KAVOVARY: "KAVOVARY_414" = None
    NABIJACKY_BATERII: "NABIJACKY_BATERII_415" = None
    RUCNE_SLAHACE_MIXERY: "RUCNE_SLAHACE_MIXERY_421" = None
    SVIETIDLA_LAMPY: "SVIETIDLA_LAMPY_416" = None
    SIJACIE_STROJE: "SIJACIE_STROJE_417" = None
    VYSAVACE: "VYSAVACE_418" = None
    VYSIELACKY: "VYSIELACKY_419" = None
    ZVLHCOVACE_VZDUCHU: "ZVLHCOVACE_VZDUCHU_420" = None
    ZEHLICKY: "ZEHLICKY_422" = None
    OSTATNE_DROBNE: "OSTATNE_DROBNE_423" = None


class DIGESTORY_389(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> DIGESTORY."""

    category_name = "digestory"
    category_rss = "389"


class CHLADNICKY_390(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> CHLADNICKY."""

    category_name = "chladnicky"
    category_rss = "390"


class MIKROVLNNE_RURY_391(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> MIKROVLNNE_RURY."""

    category_name = "mikrovlnky"
    category_rss = "391"


class MRAZNICKY_392(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> MRAZNICKY."""

    category_name = "mraznicky"
    category_rss = "392"


class PRACKY_394(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> PRACKY."""

    category_name = "pracky"
    category_rss = "394"


class SPORAKY_395(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> SPORAKY."""

    category_name = "sporaky"
    category_rss = "395"


class SUSICKY_396(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> SUSICKY."""

    category_name = "susicky"
    category_rss = "396"


class UMYVACKY_RIADU_393(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> UMYVACKY_RIADU."""

    category_name = "umyvacky"
    category_rss = "393"


class OSTATNE_BIELA_397(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> OSTATNE_BIELA."""

    category_name = "ostatnebila"
    category_rss = "397"


class AUTORADIA_398(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> AUTORADIA."""

    category_name = "autoradia"
    category_rss = "398"


class DOMACE_KINA_400(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> DOMACE_KINA."""

    category_name = "kina"
    category_rss = "400"


class HIFI_SYSTEMY_RADIA_402(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> HIFI_SYSTEMY_RADIA."""

    category_name = "hifi"
    category_rss = "402"


class PROJEKTORY_404(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> PROJEKTORY."""

    category_name = "projektory"
    category_rss = "404"


class REPRO_SUSTAVY_405(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> REPRO_SUSTAVY."""

    category_name = "repro"
    category_rss = "405"


class SLUCHADLA_399(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> SLUCHADLA."""

    category_name = "sluchadla"
    category_rss = "399"


class TELEVIZORY_406(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> TELEVIZORY."""

    category_name = "televizory"
    category_rss = "406"


class VIDEO_DVD_PREHRAVACE_407(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> VIDEO_DVD_PREHRAVACE."""

    category_name = "dvd"
    category_rss = "407"


class ZOSILNOVACE_409(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> ZOSILNOVACE."""

    category_name = "zosilnovace"
    category_rss = "409"


class OSTATNE_AUDIO_VIDEO_410(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> OSTATNE_AUDIO_VIDEO."""

    category_name = "ostatneav"
    category_rss = "410"


class EPILATORY_DEPILATORY_411(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> EPILATORY_DEPILATORY."""

    category_name = "depilatory"
    category_rss = "411"


class FENY_KULMY_412(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> FENY_KULMY."""

    category_name = "feny"
    category_rss = "412"


class HOLIACE_STROJCEKY_413(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> HOLIACE_STROJCEKY."""

    category_name = "holiace"
    category_rss = "413"


class KAVOVARY_414(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> KAVOVARY."""

    category_name = "kavovary"
    category_rss = "414"


class NABIJACKY_BATERII_415(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> NABIJACKY_BATERII."""

    category_name = "nabijacky"
    category_rss = "415"


class RUCNE_SLAHACE_MIXERY_421(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> RUCNE_SLAHACE_MIXERY."""

    category_name = "mixery"
    category_rss = "421"


class SVIETIDLA_LAMPY_416(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> SVIETIDLA_LAMPY."""

    category_name = "lampy"
    category_rss = "416"


class SIJACIE_STROJE_417(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> SIJACIE_STROJE."""

    category_name = "sijacie"
    category_rss = "417"


class VYSAVACE_418(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> VYSAVACE."""

    category_name = "vysavace"
    category_rss = "418"


class VYSIELACKY_419(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> VYSIELACKY."""

    category_name = "vysielacky"
    category_rss = "419"


class ZVLHCOVACE_VZDUCHU_420(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> ZVLHCOVACE_VZDUCHU."""

    category_name = "zvlhcovace"
    category_rss = "420"


class ZEHLICKY_422(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> ZEHLICKY."""

    category_name = "zehlicky"
    category_rss = "422"


class OSTATNE_DROBNE_423(SECTION_ELEKTRO):
    """SECTION_ELEKTRO -> OSTATNE_DROBNE."""

    category_name = "ostatne"
    category_rss = "423"


class SECTION_SPORT(Category):
    """SECTION_SPORT."""

    section_name = "sport"
    section_rss = "sp"

    FITNESS_JOGGING: "FITNESS_JOGGING_320" = None
    GOLF: "GOLF_321" = None
    FUTBAL: "FUTBAL_322" = None
    INLINES_SKATEBOARDING: "INLINES_SKATEBOARDING_323" = None
    KEMPING: "KEMPING_319" = None
    LETECTVO: "LETECTVO_446" = None
    LOPTOVE_HRY: "LOPTOVE_HRY_324" = None
    POLOVNICTVO_LOV: "POLOVNICTVO_LOV_325" = None
    PAINTBALL: "PAINTBALL_326" = None
    RYBOLOV: "RYBOLOV_327" = None
    SPOLOCENSKE_HRY: "SPOLOCENSKE_HRY_328" = None
    TENIS_SQUASH_BADMINTON: "TENIS_SQUASH_BADMINTON_329" = None
    TURISTIKA_HOROLEZECTVO: "TURISTIKA_HOROLEZECTVO_330" = None
    VODNE_SPORTY_POTAPANIE: "VODNE_SPORTY_POTAPANIE_331" = None
    VSETKO_OSTATNE: "VSETKO_OSTATNE_332" = None
    DETSKE_BICYKLE: "DETSKE_BICYKLE" = None
    KOLOBEZKY: "KOLOBEZKY_444" = None
    HORSKE_BICYKLE: "HORSKE_BICYKLE_333" = None
    CESTNE_BICYKLE: "CESTNE_BICYKLE_334" = None
    SUCIASTKY_A_DIELY: "SUCIASTKY_A_DIELY_335" = None
    OSTATNA_CYKLISTIKA: "OSTATNA_CYKLISTIKA_336" = None
    BEZKOVANIE: "BEZKOVANIE_445" = None
    LYZOVANIE: "LYZOVANIE_337" = None
    SKIALPY: "SKIALPY_459" = None
    SNOWBOARDING: "SNOWBOARDING_338" = None
    HOKEJ_KORCULOVANIE: "HOKEJ_KORCULOVANIE_339" = None
    OSTATNE_ZIMNE: "OSTATNE_ZIMNE_340" = None


class FITNESS_JOGGING_320(SECTION_SPORT):
    """SECTION_SPORT -> FITNESS_JOGGING."""

    category_name = "fitness"
    category_rss = "320"


class GOLF_321(SECTION_SPORT):
    """SECTION_SPORT -> GOLF."""

    category_name = "golf"
    category_rss = "321"


class FUTBAL_322(SECTION_SPORT):
    """SECTION_SPORT -> FUTBAL."""

    category_name = "futbal"
    category_rss = "322"


class INLINES_SKATEBOARDING_323(SECTION_SPORT):
    """SECTION_SPORT -> INLINES_SKATEBOARDING."""

    category_name = "korcule"
    category_rss = "323"


class KEMPING_319(SECTION_SPORT):
    """SECTION_SPORT -> KEMPING."""

    category_name = "kemping"
    category_rss = "319"


class LETECTVO_446(SECTION_SPORT):
    """SECTION_SPORT -> LETECTVO."""

    category_name = "letectvo"
    category_rss = "446"


class LOPTOVE_HRY_324(SECTION_SPORT):
    """SECTION_SPORT -> LOPTOVE_HRY."""

    category_name = "loptove"
    category_rss = "324"


class POLOVNICTVO_LOV_325(SECTION_SPORT):
    """SECTION_SPORT -> POLOVNICTVO_LOV."""

    category_name = "lov"
    category_rss = "325"


class PAINTBALL_326(SECTION_SPORT):
    """SECTION_SPORT -> PAINTBALL."""

    category_name = "paintball"
    category_rss = "326"


class RYBOLOV_327(SECTION_SPORT):
    """SECTION_SPORT -> RYBOLOV."""

    category_name = "rybareni"
    category_rss = "327"


class SPOLOCENSKE_HRY_328(SECTION_SPORT):
    """SECTION_SPORT -> SPOLOCENSKE_HRY."""

    category_name = "hry"
    category_rss = "328"


class TENIS_SQUASH_BADMINTON_329(SECTION_SPORT):
    """SECTION_SPORT -> TENIS_SQUASH_BADMINTON."""

    category_name = "tenis"
    category_rss = "329"


class TURISTIKA_HOROLEZECTVO_330(SECTION_SPORT):
    """SECTION_SPORT -> TURISTIKA_HOROLEZECTVO."""

    category_name = "turistika"
    category_rss = "330"


class VODNE_SPORTY_POTAPANIE_331(SECTION_SPORT):
    """SECTION_SPORT -> VODNE_SPORTY_POTAPANIE."""

    category_name = "vodni"
    category_rss = "331"


class VSETKO_OSTATNE_332(SECTION_SPORT):
    """SECTION_SPORT -> VSETKO_OSTATNE."""

    category_name = "ostatni"
    category_rss = "332"


class KOLOBEZKY_444(SECTION_SPORT):
    """SECTION_SPORT -> KOLOBEZKY."""

    category_name = "kolobezky"
    category_rss = "444"


class HORSKE_BICYKLE_333(SECTION_SPORT):
    """SECTION_SPORT -> HORSKE_BICYKLE."""

    category_name = "horska"
    category_rss = "333"


class CESTNE_BICYKLE_334(SECTION_SPORT):
    """SECTION_SPORT -> CESTNE_BICYKLE."""

    category_name = "cestne"
    category_rss = "334"


class SUCIASTKY_A_DIELY_335(SECTION_SPORT):
    """SECTION_SPORT -> SUCIASTKY_A_DIELY."""

    category_name = "soucastky"
    category_rss = "335"


class OSTATNA_CYKLISTIKA_336(SECTION_SPORT):
    """SECTION_SPORT -> OSTATNA_CYKLISTIKA."""

    category_name = "cyklistika"
    category_rss = "336"


class BEZKOVANIE_445(SECTION_SPORT):
    """SECTION_SPORT -> BEZKOVANIE."""

    category_name = "bezky"
    category_rss = "445"


class LYZOVANIE_337(SECTION_SPORT):
    """SECTION_SPORT -> LYZOVANIE."""

    category_name = "lyze"
    category_rss = "337"


class SKIALPY_459(SECTION_SPORT):
    """SECTION_SPORT -> SKIALPY."""

    category_name = "skialpy"
    category_rss = "459"


class SNOWBOARDING_338(SECTION_SPORT):
    """SECTION_SPORT -> SNOWBOARDING."""

    category_name = "snowboard"
    category_rss = "338"


class HOKEJ_KORCULOVANIE_339(SECTION_SPORT):
    """SECTION_SPORT -> HOKEJ_KORCULOVANIE."""

    category_name = "hokej"
    category_rss = "339"


class OSTATNE_ZIMNE_340(SECTION_SPORT):
    """SECTION_SPORT -> OSTATNE_ZIMNE."""

    category_name = "zimni"
    category_rss = "340"


class SECTION_HUDBA(Category):
    """SECTION_HUDBA."""

    section_name = "hudba"
    section_rss = "hu"

    BICIE_NASTROJE: "BICIE_NASTROJE_285" = None
    DYCHOVE_NASTROJE: "DYCHOVE_NASTROJE_286" = None
    KLAVESOVE_NASTROJE: "KLAVESOVE_NASTROJE_287" = None
    SLACIKOVE_NASTROJE: "SLACIKOVE_NASTROJE_288" = None
    STRUNOVE_NASTROJE: "STRUNOVE_NASTROJE_289" = None
    OSTATNE_NASTROJE: "OSTATNE_NASTROJE_290" = None
    DVD_CD_MC_LP: "DVD_CD_MC_LP_291" = None
    HUDOBNICI_A_SKUPINY: "HUDOBNICI_A_SKUPINY_292" = None
    KONCERTY: "KONCERTY_293" = None
    VYUKA_HUDBY: "VYUKA_HUDBY" = None
    NOTY_TEXTY: "NOTY_TEXTY_295" = None
    SKUSOBNE: "SKUSOBNE_296" = None
    SVETELNA_TECHNIKA: "SVETELNA_TECHNIKA_297" = None
    VSTUPENKY: "VSTUPENKY" = None
    ZVUKOVA_TECHNIKA: "ZVUKOVA_TECHNIKA_299" = None
    OSTATNE: "OSTATNE_300" = None


class BICIE_NASTROJE_285(SECTION_HUDBA):
    """SECTION_HUDBA -> BICIE_NASTROJE."""

    category_name = "bicie"
    category_rss = "285"


class DYCHOVE_NASTROJE_286(SECTION_HUDBA):
    """SECTION_HUDBA -> DYCHOVE_NASTROJE."""

    category_name = "dychove"
    category_rss = "286"


class KLAVESOVE_NASTROJE_287(SECTION_HUDBA):
    """SECTION_HUDBA -> KLAVESOVE_NASTROJE."""

    category_name = "klavesove"
    category_rss = "287"


class SLACIKOVE_NASTROJE_288(SECTION_HUDBA):
    """SECTION_HUDBA -> SLACIKOVE_NASTROJE."""

    category_name = "slacikove"
    category_rss = "288"


class STRUNOVE_NASTROJE_289(SECTION_HUDBA):
    """SECTION_HUDBA -> STRUNOVE_NASTROJE."""

    category_name = "strunove"
    category_rss = "289"


class OSTATNE_NASTROJE_290(SECTION_HUDBA):
    """SECTION_HUDBA -> OSTATNE_NASTROJE."""

    category_name = "nastroje"
    category_rss = "290"


class DVD_CD_MC_LP_291(SECTION_HUDBA):
    """SECTION_HUDBA -> DVD_CD_MC_LP."""

    category_name = "nahravky"
    category_rss = "291"


class HUDOBNICI_A_SKUPINY_292(SECTION_HUDBA):
    """SECTION_HUDBA -> HUDOBNICI_A_SKUPINY."""

    category_name = "skupiny"
    category_rss = "292"


class KONCERTY_293(SECTION_HUDBA):
    """SECTION_HUDBA -> KONCERTY."""

    category_name = "koncerty"
    category_rss = "293"


class NOTY_TEXTY_295(SECTION_HUDBA):
    """SECTION_HUDBA -> NOTY_TEXTY."""

    category_name = "noty"
    category_rss = "295"


class SKUSOBNE_296(SECTION_HUDBA):
    """SECTION_HUDBA -> SKUSOBNE."""

    category_name = "skusobne"
    category_rss = "296"


class SVETELNA_TECHNIKA_297(SECTION_HUDBA):
    """SECTION_HUDBA -> SVETELNA_TECHNIKA."""

    category_name = "svetelna"
    category_rss = "297"


class ZVUKOVA_TECHNIKA_299(SECTION_HUDBA):
    """SECTION_HUDBA -> ZVUKOVA_TECHNIKA."""

    category_name = "zvukova"
    category_rss = "299"


class OSTATNE_300(SECTION_HUDBA):
    """SECTION_HUDBA -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "300"


class SECTION_VSTUPENKY(Category):
    """SECTION_VSTUPENKY."""

    section_name = "vstupenky"
    section_rss = "vs"

    DARCEKOVE_POUKAZKY: "DARCEKOVE_POUKAZKY_231" = None
    DIALNICNE_ZNAMKY: "DIALNICNE_ZNAMKY_232" = None
    CESTOVNE_LISTKY: "CESTOVNE_LISTKY_225" = None
    LETENKY: "LETENKY_226" = None
    PERMANENTKY: "PERMANENTKY_236" = None
    DIVADLO: "DIVADLO_227" = None
    FESTIVALY: "FESTIVALY_228" = None
    HUDBA_KONCERTY: "HUDBA_KONCERTY_229" = None
    PRE_DETI: "PRE_DETI_233" = None
    SPOLOCENSKE_AKCIE: "SPOLOCENSKE_AKCIE_230" = None
    SPORT: "SPORT_234" = None
    VYSTAVY: "VYSTAVY_235" = None
    OSTATNE: "OSTATNE_237" = None


class DARCEKOVE_POUKAZKY_231(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> DARCEKOVE_POUKAZKY."""

    category_name = "poukazky"
    category_rss = "231"


class DIALNICNE_ZNAMKY_232(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> DIALNICNE_ZNAMKY."""

    category_name = "znamky"
    category_rss = "232"


class CESTOVNE_LISTKY_225(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> CESTOVNE_LISTKY."""

    category_name = "listky"
    category_rss = "225"


class LETENKY_226(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> LETENKY."""

    category_name = "letenky"
    category_rss = "226"


class PERMANENTKY_236(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> PERMANENTKY."""

    category_name = "permanentky"
    category_rss = "236"


class DIVADLO_227(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> DIVADLO."""

    category_name = "divadlo"
    category_rss = "227"


class FESTIVALY_228(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> FESTIVALY."""

    category_name = "festivaly"
    category_rss = "228"


class HUDBA_KONCERTY_229(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> HUDBA_KONCERTY."""

    category_name = "hudba"
    category_rss = "229"


class PRE_DETI_233(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> PRE_DETI."""

    category_name = "deti"
    category_rss = "233"


class SPOLOCENSKE_AKCIE_230(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> SPOLOCENSKE_AKCIE."""

    category_name = "spolocenske"
    category_rss = "230"


class SPORT_234(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> SPORT."""

    category_name = "sport"
    category_rss = "234"


class VYSTAVY_235(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> VYSTAVY."""

    category_name = "vystavy"
    category_rss = "235"


class OSTATNE_237(SECTION_VSTUPENKY):
    """SECTION_VSTUPENKY -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "237"


class SECTION_KNIHY(Category):
    """SECTION_KNIHY."""

    section_name = "knihy"
    section_rss = "kn"

    BELETRIA: "BELETRIA_366" = None
    CUDZOJAZYCNA_LITERATURA: "CUDZOJAZYCNA_LITERATURA_388" = None
    CASOPISY: "CASOPISY_367" = None
    DETEKTIVKY: "DETEKTIVKY_368" = None
    DETSKA_LITERATURA: "DETSKA_LITERATURA_369" = None
    DRAMA: "DRAMA_370" = None
    ENCYKLOPEDIE: "ENCYKLOPEDIE_371" = None
    EZOTERIKA: "EZOTERIKA_372" = None
    HISTORICKE_ROMANY: "HISTORICKE_ROMANY_373" = None
    HOBBY_ODBORNE_KNIHY: "HOBBY_ODBORNE_KNIHY_374" = None
    KUCHARKY: "KUCHARKY_375" = None
    MAPY_CESTOVANIE: "MAPY_CESTOVANIE_376" = None
    POCITACOVA_LITERATURA: "POCITACOVA_LITERATURA_378" = None
    PRE_MLADEZ: "PRE_MLADEZ_379" = None
    ROMANY_PRE_ZENY: "ROMANY_PRE_ZENY_380" = None
    SCIFI_FANTASY: "SCIFI_FANTASY_381" = None
    UCEBNICE_SKRIPTA_ZS: "UCEBNICE_SKRIPTA_ZS_386" = None
    UCEBNICE_SKRIPTA_SS: "UCEBNICE_SKRIPTA_SS_383" = None
    UCEBNICE_SKRIPTA_VS: "UCEBNICE_SKRIPTA_VS_382" = None
    UCEBNICE_SKRIPTA_JAZYKOVE: "UCEBNICE_SKRIPTA_JAZYKOVE_387" = None
    ZABAVNA_LITERATURA: "ZABAVNA_LITERATURA_384" = None
    ZDRAVY_ZIVOTNY_STYL: "ZDRAVY_ZIVOTNY_STYL_385" = None
    OSTATNE: "OSTATNE_377" = None


class BELETRIA_366(SECTION_KNIHY):
    """SECTION_KNIHY -> BELETRIA."""

    category_name = "beletria"
    category_rss = "366"


class CUDZOJAZYCNA_LITERATURA_388(SECTION_KNIHY):
    """SECTION_KNIHY -> CUDZOJAZYCNA_LITERATURA."""

    category_name = "cudzojazycna"
    category_rss = "388"


class CASOPISY_367(SECTION_KNIHY):
    """SECTION_KNIHY -> CASOPISY."""

    category_name = "casopisy"
    category_rss = "367"


class DETEKTIVKY_368(SECTION_KNIHY):
    """SECTION_KNIHY -> DETEKTIVKY."""

    category_name = "detektivky"
    category_rss = "368"


class DETSKA_LITERATURA_369(SECTION_KNIHY):
    """SECTION_KNIHY -> DETSKA_LITERATURA."""

    category_name = "detska"
    category_rss = "369"


class DRAMA_370(SECTION_KNIHY):
    """SECTION_KNIHY -> DRAMA."""

    category_name = "drama"
    category_rss = "370"


class ENCYKLOPEDIE_371(SECTION_KNIHY):
    """SECTION_KNIHY -> ENCYKLOPEDIE."""

    category_name = "encyklopedie"
    category_rss = "371"


class EZOTERIKA_372(SECTION_KNIHY):
    """SECTION_KNIHY -> EZOTERIKA."""

    category_name = "ezoterika"
    category_rss = "372"


class HISTORICKE_ROMANY_373(SECTION_KNIHY):
    """SECTION_KNIHY -> HISTORICKE_ROMANY."""

    category_name = "historicke"
    category_rss = "373"


class HOBBY_ODBORNE_KNIHY_374(SECTION_KNIHY):
    """SECTION_KNIHY -> HOBBY_ODBORNE_KNIHY."""

    category_name = "hobby"
    category_rss = "374"


class KUCHARKY_375(SECTION_KNIHY):
    """SECTION_KNIHY -> KUCHARKY."""

    category_name = "kucharky"
    category_rss = "375"


class MAPY_CESTOVANIE_376(SECTION_KNIHY):
    """SECTION_KNIHY -> MAPY_CESTOVANIE."""

    category_name = "mapy"
    category_rss = "376"


class POCITACOVA_LITERATURA_378(SECTION_KNIHY):
    """SECTION_KNIHY -> POCITACOVA_LITERATURA."""

    category_name = "pocitacova"
    category_rss = "378"


class PRE_MLADEZ_379(SECTION_KNIHY):
    """SECTION_KNIHY -> PRE_MLADEZ."""

    category_name = "mladez"
    category_rss = "379"


class ROMANY_PRE_ZENY_380(SECTION_KNIHY):
    """SECTION_KNIHY -> ROMANY_PRE_ZENY."""

    category_name = "zeny"
    category_rss = "380"


class SCIFI_FANTASY_381(SECTION_KNIHY):
    """SECTION_KNIHY -> SCIFI_FANTASY."""

    category_name = "scifi"
    category_rss = "381"


class UCEBNICE_SKRIPTA_ZS_386(SECTION_KNIHY):
    """SECTION_KNIHY -> UCEBNICE_SKRIPTA_ZS."""

    category_name = "ucebnicezs"
    category_rss = "386"


class UCEBNICE_SKRIPTA_SS_383(SECTION_KNIHY):
    """SECTION_KNIHY -> UCEBNICE_SKRIPTA_SS."""

    category_name = "ucebnice"
    category_rss = "383"


class UCEBNICE_SKRIPTA_VS_382(SECTION_KNIHY):
    """SECTION_KNIHY -> UCEBNICE_SKRIPTA_VS."""

    category_name = "skripta"
    category_rss = "382"


class UCEBNICE_SKRIPTA_JAZYKOVE_387(SECTION_KNIHY):
    """SECTION_KNIHY -> UCEBNICE_SKRIPTA_JAZYKOVE."""

    category_name = "ucebnicejazykove"
    category_rss = "387"


class ZABAVNA_LITERATURA_384(SECTION_KNIHY):
    """SECTION_KNIHY -> ZABAVNA_LITERATURA."""

    category_name = "zabavna"
    category_rss = "384"


class ZDRAVY_ZIVOTNY_STYL_385(SECTION_KNIHY):
    """SECTION_KNIHY -> ZDRAVY_ZIVOTNY_STYL."""

    category_name = "zdravi"
    category_rss = "385"


class OSTATNE_377(SECTION_KNIHY):
    """SECTION_KNIHY -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "377"


class SECTION_NABYTOK(Category):
    """SECTION_NABYTOK."""

    section_name = "nabytok"
    section_rss = "na"

    DETSKY_NABYTOK: "DETSKY_NABYTOK" = None
    DVERE_BRANY: "DVERE_BRANY" = None
    JEDALENSKE_KUTY: "JEDALENSKE_KUTY_268" = None
    KNIZNICE: "KNIZNICE_269" = None
    KOBERCE_A_PODLAHOVA_KRYTINA: "KOBERCE_A_PODLAHOVA_KRYTINA_270" = None
    KRESLA_A_GAUCE: "KRESLA_A_GAUCE_271" = None
    KUCHYNE: "KUCHYNE_272" = None
    KUPELNE: "KUPELNE_274" = None
    LAMPY_OSVETLENIE: "LAMPY_OSVETLENIE_275" = None
    MATRACE: "MATRACE_276" = None
    OBYVACIE_STENY: "OBYVACIE_STENY_273" = None
    POSTELE: "POSTELE_277" = None
    SEDACIE_SUPRAVY: "SEDACIE_SUPRAVY_278" = None
    SKRINE: "SKRINE_279" = None
    SPALNE: "SPALNE_280" = None
    STOLICKY: "STOLICKY_281" = None
    STOLY: "STOLY_282" = None
    ZAHRADNY_NABYTOK: "ZAHRADNY_NABYTOK_283" = None
    DOPLNKY: "DOPLNKY_425" = None
    OSTATNY_NABYTOK: "OSTATNY_NABYTOK_284" = None


class JEDALENSKE_KUTY_268(SECTION_NABYTOK):
    """SECTION_NABYTOK -> JEDALENSKE_KUTY."""

    category_name = "jedalenske"
    category_rss = "268"


class KNIZNICE_269(SECTION_NABYTOK):
    """SECTION_NABYTOK -> KNIZNICE."""

    category_name = "kniznice"
    category_rss = "269"


class KOBERCE_A_PODLAHOVA_KRYTINA_270(SECTION_NABYTOK):
    """SECTION_NABYTOK -> KOBERCE_A_PODLAHOVA_KRYTINA."""

    category_name = "koberce"
    category_rss = "270"


class KRESLA_A_GAUCE_271(SECTION_NABYTOK):
    """SECTION_NABYTOK -> KRESLA_A_GAUCE."""

    category_name = "kresla"
    category_rss = "271"


class KUCHYNE_272(SECTION_NABYTOK):
    """SECTION_NABYTOK -> KUCHYNE."""

    category_name = "kuchyne"
    category_rss = "272"


class KUPELNE_274(SECTION_NABYTOK):
    """SECTION_NABYTOK -> KUPELNE."""

    category_name = "kupelne"
    category_rss = "274"


class LAMPY_OSVETLENIE_275(SECTION_NABYTOK):
    """SECTION_NABYTOK -> LAMPY_OSVETLENIE."""

    category_name = "lampy"
    category_rss = "275"


class MATRACE_276(SECTION_NABYTOK):
    """SECTION_NABYTOK -> MATRACE."""

    category_name = "matrace"
    category_rss = "276"


class OBYVACIE_STENY_273(SECTION_NABYTOK):
    """SECTION_NABYTOK -> OBYVACIE_STENY."""

    category_name = "obyvacie"
    category_rss = "273"


class POSTELE_277(SECTION_NABYTOK):
    """SECTION_NABYTOK -> POSTELE."""

    category_name = "postele"
    category_rss = "277"


class SEDACIE_SUPRAVY_278(SECTION_NABYTOK):
    """SECTION_NABYTOK -> SEDACIE_SUPRAVY."""

    category_name = "sedacie"
    category_rss = "278"


class SKRINE_279(SECTION_NABYTOK):
    """SECTION_NABYTOK -> SKRINE."""

    category_name = "skrine"
    category_rss = "279"


class SPALNE_280(SECTION_NABYTOK):
    """SECTION_NABYTOK -> SPALNE."""

    category_name = "spalne"
    category_rss = "280"


class STOLICKY_281(SECTION_NABYTOK):
    """SECTION_NABYTOK -> STOLICKY."""

    category_name = "stolicky"
    category_rss = "281"


class STOLY_282(SECTION_NABYTOK):
    """SECTION_NABYTOK -> STOLY."""

    category_name = "stoly"
    category_rss = "282"


class ZAHRADNY_NABYTOK_283(SECTION_NABYTOK):
    """SECTION_NABYTOK -> ZAHRADNY_NABYTOK."""

    category_name = "zahradny"
    category_rss = "283"


class DOPLNKY_425(SECTION_NABYTOK):
    """SECTION_NABYTOK -> DOPLNKY."""

    category_name = "doplnky"
    category_rss = "425"


class OSTATNY_NABYTOK_284(SECTION_NABYTOK):
    """SECTION_NABYTOK -> OSTATNY_NABYTOK."""

    category_name = "nabytok"
    category_rss = "284"


class SECTION_OBLECENIE(Category):
    """SECTION_OBLECENIE."""

    section_name = "oblecenie"
    section_rss = "ob"

    BLUZKY: "BLUZKY_51" = None
    BUNDY_A_KABATY: "BUNDY_A_KABATY_52" = None
    CIAPKY_SATKY: "CIAPKY_SATKY_53" = None
    DZINSY: "DZINSY_54" = None
    FUNKCNE_PRADLO: "FUNKCNE_PRADLO_55" = None
    KOSELE: "KOSELE_56" = None
    KOZENE_OBLECENIE: "KOZENE_OBLECENIE_57" = None
    MIKINY: "MIKINY_58" = None
    NOHAVICE: "NOHAVICE_59" = None
    OBLEKY_SAKA: "OBLEKY_SAKA_60" = None
    PLAVKY: "PLAVKY_61" = None
    RUKAVICE_A_SALY: "RUKAVICE_A_SALY_63" = None
    RUSKA: "RUSKA_458" = None
    SPODNA_BIELIZEN: "SPODNA_BIELIZEN_64" = None
    SUKNE: "SUKNE_65" = None
    SVADOBNE_SATY: "SVADOBNE_SATY_66" = None
    SVETRE: "SVETRE_67" = None
    SATY_KOSTYMY: "SATY_KOSTYMY_68" = None
    SORTKY: "SORTKY_69" = None
    SPORTOVE_OBLECENIE: "SPORTOVE_OBLECENIE_70" = None
    TEHOTENSKE_OBLECENIE: "TEHOTENSKE_OBLECENIE_62" = None
    TRICKA_ROLAKY_TIELKA: "TRICKA_ROLAKY_TIELKA_71" = None
    DOPLNKY: "DOPLNKY_72" = None
    HODINKY: "HODINKY_73" = None
    KABELKY: "KABELKY_74" = None
    PLECNIAKY_A_KUFRE: "PLECNIAKY_A_KUFRE_75" = None
    TOPANKY_OBUV: "TOPANKY_OBUV_76" = None
    SPERKY: "SPERKY_77" = None
    OSTATNE: "OSTATNE_78" = None


class BLUZKY_51(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> BLUZKY."""

    category_name = "bluzky"
    category_rss = "51"


class BUNDY_A_KABATY_52(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> BUNDY_A_KABATY."""

    category_name = "bundy"
    category_rss = "52"


class CIAPKY_SATKY_53(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> CIAPKY_SATKY."""

    category_name = "ciapky"
    category_rss = "53"


class DZINSY_54(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> DZINSY."""

    category_name = "dzinsy"
    category_rss = "54"


class FUNKCNE_PRADLO_55(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> FUNKCNE_PRADLO."""

    category_name = "pradlo"
    category_rss = "55"


class KOSELE_56(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> KOSELE."""

    category_name = "kosele"
    category_rss = "56"


class KOZENE_OBLECENIE_57(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> KOZENE_OBLECENIE."""

    category_name = "kozene"
    category_rss = "57"


class MIKINY_58(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> MIKINY."""

    category_name = "mikiny"
    category_rss = "58"


class NOHAVICE_59(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> NOHAVICE."""

    category_name = "nohavice"
    category_rss = "59"


class OBLEKY_SAKA_60(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> OBLEKY_SAKA."""

    category_name = "obleky"
    category_rss = "60"


class PLAVKY_61(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> PLAVKY."""

    category_name = "plavky"
    category_rss = "61"


class RUKAVICE_A_SALY_63(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> RUKAVICE_A_SALY."""

    category_name = "rukavice"
    category_rss = "63"


class RUSKA_458(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> RUSKA."""

    category_name = "ruska"
    category_rss = "458"


class SPODNA_BIELIZEN_64(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> SPODNA_BIELIZEN."""

    category_name = "bielizen"
    category_rss = "64"


class SUKNE_65(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> SUKNE."""

    category_name = "sukne"
    category_rss = "65"


class SVADOBNE_SATY_66(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> SVADOBNE_SATY."""

    category_name = "svadobne"
    category_rss = "66"


class SVETRE_67(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> SVETRE."""

    category_name = "svetre"
    category_rss = "67"


class SATY_KOSTYMY_68(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> SATY_KOSTYMY."""

    category_name = "saty"
    category_rss = "68"


class SORTKY_69(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> SORTKY."""

    category_name = "sortky"
    category_rss = "69"


class SPORTOVE_OBLECENIE_70(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> SPORTOVE_OBLECENIE."""

    category_name = "sportove"
    category_rss = "70"


class TEHOTENSKE_OBLECENIE_62(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> TEHOTENSKE_OBLECENIE."""

    category_name = "tehulky"
    category_rss = "62"


class TRICKA_ROLAKY_TIELKA_71(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> TRICKA_ROLAKY_TIELKA."""

    category_name = "tricka"
    category_rss = "71"


class DOPLNKY_72(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> DOPLNKY."""

    category_name = "doplnky"
    category_rss = "72"


class HODINKY_73(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> HODINKY."""

    category_name = "hodinky"
    category_rss = "73"


class KABELKY_74(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> KABELKY."""

    category_name = "kabelky"
    category_rss = "74"


class PLECNIAKY_A_KUFRE_75(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> PLECNIAKY_A_KUFRE."""

    category_name = "plecniaky"
    category_rss = "75"


class TOPANKY_OBUV_76(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> TOPANKY_OBUV."""

    category_name = "obuv"
    category_rss = "76"


class SPERKY_77(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> SPERKY."""

    category_name = "sperky"
    category_rss = "77"


class OSTATNE_78(SECTION_OBLECENIE):
    """SECTION_OBLECENIE -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "78"


class SECTION_SLUZBY(Category):
    """SECTION_SLUZBY."""

    section_name = "sluzby"
    section_rss = "sl"

    AUTO_MOTO: "AUTO_MOTO_426" = None
    CESTOVANIE: "CESTOVANIE_167" = None
    DOMACE_PRACE: "DOMACE_PRACE_168" = None
    EZOTERIKA: "EZOTERIKA_427" = None
    IT_WEBDESIGN: "IT_WEBDESIGN_171" = None
    KONE_SLUZBY: "KONE_SLUZBY_437" = None
    KURZY_A_SKOLENIA: "KURZY_A_SKOLENIA_172" = None
    OPRAVY_A_SERVIS: "OPRAVY_A_SERVIS_428" = None
    ORGANIZOVANIE_AKCII: "ORGANIZOVANIE_AKCII_429" = None
    POZICOVNE: "POZICOVNE_430" = None
    PRAVO_A_BEZPECNOST: "PRAVO_A_BEZPECNOST_431" = None
    PREKLADATELSTVO: "PREKLADATELSTVO_173" = None
    PREPRAVA_A_STAHOVANIE: "PREPRAVA_A_STAHOVANIE_174" = None
    REALITNE_SLUZBY: "REALITNE_SLUZBY_432" = None
    REKLAMA_NA_AUTO: "REKLAMA_NA_AUTO_183" = None
    REKLAMNE_PLOCHY_OSTATNE: "REKLAMNE_PLOCHY_OSTATNE_184" = None
    REMESELNE_A_STAVEBNE_PRACE: "REMESELNE_A_STAVEBNE_PRACE_175" = None
    SLUZBY_PRE_ZVIERATA: "SLUZBY_PRE_ZVIERATA_43" = None
    SPROSTREDKOVATELSKE_SLUZBY: "SPROSTREDKOVATELSKE_SLUZBY_176" = None
    STRAZENIE_DETI: "STRAZENIE_DETI_178" = None
    TVORIVA_PRACA: "TVORIVA_PRACA_434" = None
    UBYTOVANIE: "UBYTOVANIE_179" = None
    UCTOVNICTVO_PORADENSTVO: "UCTOVNICTVO_PORADENSTVO_170" = None
    UPRATOVANIE: "UPRATOVANIE_180" = None
    VYROBA: "VYROBA_433" = None
    VYUKA_DOUCOVANIE: "VYUKA_DOUCOVANIE_169" = None
    VYUKA_HUDBY: "VYUKA_HUDBY_185" = None
    ZDRAVIE_A_KRASA: "ZDRAVIE_A_KRASA_182" = None
    OSTATNE: "OSTATNE_181" = None


class AUTO_MOTO_426(SECTION_SLUZBY):
    """SECTION_SLUZBY -> AUTO_MOTO."""

    category_name = "automoto"
    category_rss = "426"


class CESTOVANIE_167(SECTION_SLUZBY):
    """SECTION_SLUZBY -> CESTOVANIE."""

    category_name = "cestovanie"
    category_rss = "167"


class DOMACE_PRACE_168(SECTION_SLUZBY):
    """SECTION_SLUZBY -> DOMACE_PRACE."""

    category_name = "domaca"
    category_rss = "168"


class EZOTERIKA_427(SECTION_SLUZBY):
    """SECTION_SLUZBY -> EZOTERIKA."""

    category_name = "ezoterika"
    category_rss = "427"


class IT_WEBDESIGN_171(SECTION_SLUZBY):
    """SECTION_SLUZBY -> IT_WEBDESIGN."""

    category_name = "it"
    category_rss = "171"


class KONE_SLUZBY_437(SECTION_SLUZBY):
    """SECTION_SLUZBY -> KONE_SLUZBY."""

    category_name = "ustajnenie"
    category_rss = "437"


class KURZY_A_SKOLENIA_172(SECTION_SLUZBY):
    """SECTION_SLUZBY -> KURZY_A_SKOLENIA."""

    category_name = "skolenia"
    category_rss = "172"


class OPRAVY_A_SERVIS_428(SECTION_SLUZBY):
    """SECTION_SLUZBY -> OPRAVY_A_SERVIS."""

    category_name = "opravy"
    category_rss = "428"


class ORGANIZOVANIE_AKCII_429(SECTION_SLUZBY):
    """SECTION_SLUZBY -> ORGANIZOVANIE_AKCII."""

    category_name = "organizovanie"
    category_rss = "429"


class POZICOVNE_430(SECTION_SLUZBY):
    """SECTION_SLUZBY -> POZICOVNE."""

    category_name = "pozicovne"
    category_rss = "430"


class PRAVO_A_BEZPECNOST_431(SECTION_SLUZBY):
    """SECTION_SLUZBY -> PRAVO_A_BEZPECNOST."""

    category_name = "pravo"
    category_rss = "431"


class PREKLADATELSTVO_173(SECTION_SLUZBY):
    """SECTION_SLUZBY -> PREKLADATELSTVO."""

    category_name = "prekladatelstvo"
    category_rss = "173"


class PREPRAVA_A_STAHOVANIE_174(SECTION_SLUZBY):
    """SECTION_SLUZBY -> PREPRAVA_A_STAHOVANIE."""

    category_name = "stahovanie"
    category_rss = "174"


class REALITNE_SLUZBY_432(SECTION_SLUZBY):
    """SECTION_SLUZBY -> REALITNE_SLUZBY."""

    category_name = "realitne"
    category_rss = "432"


class REKLAMA_NA_AUTO_183(SECTION_SLUZBY):
    """SECTION_SLUZBY -> REKLAMA_NA_AUTO."""

    category_name = "reklama"
    category_rss = "183"


class REKLAMNE_PLOCHY_OSTATNE_184(SECTION_SLUZBY):
    """SECTION_SLUZBY -> REKLAMNE_PLOCHY_OSTATNE."""

    category_name = "reklamne"
    category_rss = "184"


class REMESELNE_A_STAVEBNE_PRACE_175(SECTION_SLUZBY):
    """SECTION_SLUZBY -> REMESELNE_A_STAVEBNE_PRACE."""

    category_name = "remesla"
    category_rss = "175"


class SLUZBY_PRE_ZVIERATA_43(SECTION_SLUZBY):
    """SECTION_SLUZBY -> SLUZBY_PRE_ZVIERATA."""

    category_name = "zvierata"
    category_rss = "43"


class SPROSTREDKOVATELSKE_SLUZBY_176(SECTION_SLUZBY):
    """SECTION_SLUZBY -> SPROSTREDKOVATELSKE_SLUZBY."""

    category_name = "sprostredkovatelske"
    category_rss = "176"


class STRAZENIE_DETI_178(SECTION_SLUZBY):
    """SECTION_SLUZBY -> STRAZENIE_DETI."""

    category_name = "strazenie"
    category_rss = "178"


class TVORIVA_PRACA_434(SECTION_SLUZBY):
    """SECTION_SLUZBY -> TVORIVA_PRACA."""

    category_name = "tvoriva"
    category_rss = "434"


class UBYTOVANIE_179(SECTION_SLUZBY):
    """SECTION_SLUZBY -> UBYTOVANIE."""

    category_name = "ubytovanie"
    category_rss = "179"


class UCTOVNICTVO_PORADENSTVO_170(SECTION_SLUZBY):
    """SECTION_SLUZBY -> UCTOVNICTVO_PORADENSTVO."""

    category_name = "financne"
    category_rss = "170"


class UPRATOVANIE_180(SECTION_SLUZBY):
    """SECTION_SLUZBY -> UPRATOVANIE."""

    category_name = "upratovanie"
    category_rss = "180"


class VYROBA_433(SECTION_SLUZBY):
    """SECTION_SLUZBY -> VYROBA."""

    category_name = "vyroba"
    category_rss = "433"


class VYUKA_DOUCOVANIE_169(SECTION_SLUZBY):
    """SECTION_SLUZBY -> VYUKA_DOUCOVANIE."""

    category_name = "doucovanie"
    category_rss = "169"


class VYUKA_HUDBY_185(SECTION_SLUZBY):
    """SECTION_SLUZBY -> VYUKA_HUDBY."""

    category_name = "vyuka"
    category_rss = "185"


class ZDRAVIE_A_KRASA_182(SECTION_SLUZBY):
    """SECTION_SLUZBY -> ZDRAVIE_A_KRASA."""

    category_name = "zdravie"
    category_rss = "182"


class OSTATNE_181(SECTION_SLUZBY):
    """SECTION_SLUZBY -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "181"


class SECTION_OSTATNE(Category):
    """SECTION_OSTATNE."""

    section_name = "ostatne"
    section_rss = "os"

    MINCE_BANKOVKY: "MINCE_BANKOVKY_454" = None
    MODELARSTVO: "MODELARSTVO_453" = None
    POTRAVINY: "POTRAVINY_201" = None
    SKLO_KERAMIKA: "SKLO_KERAMIKA_203" = None
    STAROZITNOSTI: "STAROZITNOSTI_202" = None
    SPERKY_HODINKY: "SPERKY_HODINKY" = None
    UMELECKE_PREDMETY: "UMELECKE_PREDMETY_204" = None
    ZBERATELSTVO: "ZBERATELSTVO_205" = None
    ZDRAVIE_A_KRASA: "ZDRAVIE_A_KRASA_206" = None
    ZNAMKY_POHLADNICE: "ZNAMKY_POHLADNICE_455" = None
    OSTATNE: "OSTATNE_207" = None


class MINCE_BANKOVKY_454(SECTION_OSTATNE):
    """SECTION_OSTATNE -> MINCE_BANKOVKY."""

    category_name = "numizmatika"
    category_rss = "454"


class MODELARSTVO_453(SECTION_OSTATNE):
    """SECTION_OSTATNE -> MODELARSTVO."""

    category_name = "modelarstvo"
    category_rss = "453"


class POTRAVINY_201(SECTION_OSTATNE):
    """SECTION_OSTATNE -> POTRAVINY."""

    category_name = "potraviny"
    category_rss = "201"


class SKLO_KERAMIKA_203(SECTION_OSTATNE):
    """SECTION_OSTATNE -> SKLO_KERAMIKA."""

    category_name = "sklo"
    category_rss = "203"


class STAROZITNOSTI_202(SECTION_OSTATNE):
    """SECTION_OSTATNE -> STAROZITNOSTI."""

    category_name = "starozitnosti"
    category_rss = "202"


class UMELECKE_PREDMETY_204(SECTION_OSTATNE):
    """SECTION_OSTATNE -> UMELECKE_PREDMETY."""

    category_name = "umelecke"
    category_rss = "204"


class ZBERATELSTVO_205(SECTION_OSTATNE):
    """SECTION_OSTATNE -> ZBERATELSTVO."""

    category_name = "zberatelstvo"
    category_rss = "205"


class ZDRAVIE_A_KRASA_206(SECTION_OSTATNE):
    """SECTION_OSTATNE -> ZDRAVIE_A_KRASA."""

    category_name = "zdravie"
    category_rss = "206"


class ZNAMKY_POHLADNICE_455(SECTION_OSTATNE):
    """SECTION_OSTATNE -> ZNAMKY_POHLADNICE."""

    category_name = "filatelia"
    category_rss = "455"


class OSTATNE_207(SECTION_OSTATNE):
    """SECTION_OSTATNE -> OSTATNE."""

    category_name = "ostatne"
    category_rss = "207"


SECTION_ZVIERATA.AKVARIJNE_RYBICKY = AKVARIJNE_RYBICKY_33
SECTION_ZVIERATA.DROBNE_CICAVCE = DROBNE_CICAVCE_34
SECTION_ZVIERATA.KONE = KONE_35
SECTION_ZVIERATA.KONE_POTREBY = KONE_POTREBY_50
SECTION_ZVIERATA.KONE_SLUZBY = KONE_SLUZBY_437
SECTION_ZVIERATA.MACKY = MACKY_36
SECTION_ZVIERATA.PSY = PSY_37
SECTION_ZVIERATA.VTACTVO = VTACTVO_38
SECTION_ZVIERATA.TERARIJNE_ZVIERATA = TERARIJNE_ZVIERATA_39
SECTION_ZVIERATA.OSTATNE_DOMACE = OSTATNE_DOMACE_40
SECTION_ZVIERATA.KRYTIE = KRYTIE_42
SECTION_ZVIERATA.STRATENI_A_NAJDENI = STRATENI_A_NAJDENI_255
SECTION_ZVIERATA.CHOVATELSKE_POTREBY = CHOVATELSKE_POTREBY_41
SECTION_ZVIERATA.SLUZBY_PRE_ZVIERATA = SLUZBY_PRE_ZVIERATA_43
SECTION_ZVIERATA.HYDINA = HYDINA_44
SECTION_ZVIERATA.KRALIKY = KRALIKY_45
SECTION_ZVIERATA.OVCE_A_KOZY = OVCE_A_KOZY_46
SECTION_ZVIERATA.PRASATA = PRASATA_47
SECTION_ZVIERATA.DOBYTOK = DOBYTOK_48
SECTION_ZVIERATA.OSTATNE_HOSPODARSKE = OSTATNE_HOSPODARSKE_49

SECTION_DETI.AUTOSEDACKY = AUTOSEDACKY_120
SECTION_DETI.BABY_MONITORY = BABY_MONITORY_121
SECTION_DETI.BICYKLE = BICYKLE_452
SECTION_DETI.DETSKA_LITERATURA = DETSKA_LITERATURA_369
SECTION_DETI.HRACKY = HRACKY_122
SECTION_DETI.CHODITKA_A_HOPSADLA = CHODITKA_A_HOPSADLA_123
SECTION_DETI.KOCIKY = KOCIKY_124
SECTION_DETI.KOJENECKE_POTREBY = KOJENECKE_POTREBY_126
SECTION_DETI.NABYTOK_PRE_DETI = NABYTOK_PRE_DETI_127
SECTION_DETI.NOSICE = NOSICE_128
SECTION_DETI.ODRAZADLA = ODRAZADLA_130
SECTION_DETI.SEDACKY_NA_BICYKEL = SEDACKY_NA_BICYKEL_131
SECTION_DETI.SPORTOVE_POTREBY = SPORTOVE_POTREBY_132
SECTION_DETI.SKOLSKE_POTREBY = SKOLSKE_POTREBY_133
SECTION_DETI.STRAZENIE_DETI = STRAZENIE_DETI_178
SECTION_DETI.OSTATNE = OSTATNE_135
SECTION_DETI.BODY_DUPACKY_A_OVERALY = BODY_DUPACKY_A_OVERALY_136
SECTION_DETI.BUNDY_A_KABATIKY = BUNDY_A_KABATIKY_137
SECTION_DETI.CIAPKY_A_KLOBUCIKY = CIAPKY_A_KLOBUCIKY_138
SECTION_DETI.NOHAVICE_KRATASY_A_TEPLAKY = NOHAVICE_KRATASY_A_TEPLAKY_139
SECTION_DETI.KOMBINEZY = KOMBINEZY_140
SECTION_DETI.KOMPLETY = KOMPLETY_438
SECTION_DETI.MIKINY_A_SVETRE = MIKINY_A_SVETRE_141
SECTION_DETI.OBUV = OBUV_129
SECTION_DETI.PLAVKY = PLAVKY_142
SECTION_DETI.PONOZKY_A_PANCUSKY = PONOZKY_A_PANCUSKY_143
SECTION_DETI.PYZAMKA_A_ZUPANCEKY = PYZAMKA_A_ZUPANCEKY_144
SECTION_DETI.RUKAVICE_A_SALY = RUKAVICE_A_SALY_145
SECTION_DETI.SPODNA_BIELIZEN = SPODNA_BIELIZEN_146
SECTION_DETI.SUKNICKY_A_SATOCKY = SUKNICKY_A_SATOCKY_147
SECTION_DETI.TEHOTENSKE_OBLECENIE = TEHOTENSKE_OBLECENIE_62
SECTION_DETI.TRICKA_A_KOSIELKY = TRICKA_A_KOSIELKY_148
SECTION_DETI.OSTATNE_OBLECENIE = OSTATNE_OBLECENIE_125

SECTION_REALITY.BYTY = BYTY_152_typ_1
SECTION_REALITY.DOMY = DOMY_155_typ_1
SECTION_REALITY.NOVE_PROJEKTY = NOVE_PROJEKTY_166_typ_1
SECTION_REALITY.GARAZE = GARAZE_160_typ_1
SECTION_REALITY.HOTELY_RESTAURACIE = HOTELY_RESTAURACIE_165_typ_1
SECTION_REALITY.CHALUPY_CHATY = CHALUPY_CHATY_157_typ_1
SECTION_REALITY.KANCELARIE = KANCELARIE_161_typ_1
SECTION_REALITY.OBCHODNE_PRIESTORY = OBCHODNE_PRIESTORY_164_typ_1
SECTION_REALITY.POZEMKY = POZEMKY_158_typ_1
SECTION_REALITY.SKLADY = SKLADY_162_typ_1
SECTION_REALITY.ZAHRADY = ZAHRADY_159_typ_1
SECTION_REALITY.OSTATNE = OSTATNE_163_typ_1
SECTION_REALITY.BYTY = BYTY_152_typ_3
SECTION_REALITY.DOMY = DOMY_155_typ_3
SECTION_REALITY.NOVE_PROJEKTY = NOVE_PROJEKTY_166_typ_3
SECTION_REALITY.PODNAJOM_SPOLUBYVAJUCI = PODNAJOM_SPOLUBYVAJUCI_156_typ_3
SECTION_REALITY.GARAZE = GARAZE_160_typ_3
SECTION_REALITY.HOTELY_RESTAURACIE = HOTELY_RESTAURACIE_165_typ_3
SECTION_REALITY.UBYTOVANIE = UBYTOVANIE_179
SECTION_REALITY.KANCELARIE = KANCELARIE_161_typ_3
SECTION_REALITY.OBCHODNE_PRIESTORY = OBCHODNE_PRIESTORY_164_typ_3
SECTION_REALITY.POZEMKY = POZEMKY_158_typ_3
SECTION_REALITY.SKLADY = SKLADY_162_typ_3
SECTION_REALITY.ZAHRADY = ZAHRADY_159_typ_3
SECTION_REALITY.OSTATNE = OSTATNE_163_typ_3

SECTION_PRACA.ADMINISTRATIVA = ADMINISTRATIVA_341
SECTION_PRACA.CHEMIA_A_POTRAVINARSTVO = CHEMIA_A_POTRAVINARSTVO_342
SECTION_PRACA.DOPRAVA_A_LOGISTIKA = DOPRAVA_A_LOGISTIKA_343
SECTION_PRACA.FINANCIE_A_EKONOMIKA = FINANCIE_A_EKONOMIKA_344
SECTION_PRACA.IT_A_TELEKOMUNIKACIE = IT_A_TELEKOMUNIKACIE_345
SECTION_PRACA.MARKETING_A_REKLAMA = MARKETING_A_REKLAMA_346
SECTION_PRACA.MANAGEMENT = MANAGEMENT_347
SECTION_PRACA.OBCHOD_A_PREDAJ = OBCHOD_A_PREDAJ_348
SECTION_PRACA.OBRANA_A_BEZPECNOST = OBRANA_A_BEZPECNOST_349
SECTION_PRACA.POHOSTINSTVA_A_UBYTOVANIE = POHOSTINSTVA_A_UBYTOVANIE_350
SECTION_PRACA.PRACA_V_DOMACNOSTI = PRACA_V_DOMACNOSTI_351
SECTION_PRACA.PRAVO_LEGISLATIVA = PRAVO_LEGISLATIVA_352
SECTION_PRACA.PRIEMYSEL_A_VYROBA = PRIEMYSEL_A_VYROBA_353
SECTION_PRACA.REMESELNE_PRACE = REMESELNE_PRACE_354
SECTION_PRACA.SERVIS_A_SLUZBY = SERVIS_A_SLUZBY_355
SECTION_PRACA.STAVEBNICTVO = STAVEBNICTVO_357
SECTION_PRACA.TECHNIKA_A_ENERGETIKA = TECHNIKA_A_ENERGETIKA_358
SECTION_PRACA.TLAC_A_POLYGRAFIA = TLAC_A_POLYGRAFIA_359
SECTION_PRACA.VYSKUM_A_VYVOJ = VYSKUM_A_VYVOJ_360
SECTION_PRACA.VZDELAVANIE_A_PERSONALISTIKA = VZDELAVANIE_A_PERSONALISTIKA_361
SECTION_PRACA.ZDRAVOTNICTVO = ZDRAVOTNICTVO_362
SECTION_PRACA.POLNOHOSPODARSTVO = POLNOHOSPODARSTVO_363
SECTION_PRACA.BRIGADY = BRIGADY_364
SECTION_PRACA.OSTATNE = OSTATNE_365

SECTION_AUTO.ALFA_ROMEO = ALFA_ROMEO_439
SECTION_AUTO.AUDI = AUDI_79
SECTION_AUTO.BMW = BMW_80
SECTION_AUTO.CITROEN = CITROEN_81
SECTION_AUTO.DACIA = DACIA_457
SECTION_AUTO.FIAT = FIAT_82
SECTION_AUTO.FORD = FORD_83
SECTION_AUTO.HONDA = HONDA_116
SECTION_AUTO.HYUNDAI = HYUNDAI_84
SECTION_AUTO.CHEVROLET = CHEVROLET_117
SECTION_AUTO.KIA = KIA_118
SECTION_AUTO.MAZDA = MAZDA_85
SECTION_AUTO.MERCEDESBENZ = MERCEDESBENZ_86
SECTION_AUTO.MITSUBISHI = MITSUBISHI_441
SECTION_AUTO.NISSAN = NISSAN_87
SECTION_AUTO.OPEL = OPEL_88
SECTION_AUTO.PEUGEOT = PEUGEOT_89
SECTION_AUTO.RENAULT = RENAULT_90
SECTION_AUTO.SEAT = SEAT_91
SECTION_AUTO.SUZUKI = SUZUKI_119
SECTION_AUTO.SKODA = SKODA_92
SECTION_AUTO.TOYOTA = TOYOTA_93
SECTION_AUTO.VOLKSWAGEN = VOLKSWAGEN_94
SECTION_AUTO.VOLVO = VOLVO_95
SECTION_AUTO.OSTATNE_ZNACKY = OSTATNE_ZNACKY_96
SECTION_AUTO.AUTORADIA = AUTORADIA_398
SECTION_AUTO.GPS_NAVIGACIA = GPS_NAVIGACIA_32
SECTION_AUTO.HAVAROVANE = HAVAROVANE_97
SECTION_AUTO.NAHRADNE_DIELY = NAHRADNE_DIELY_98
SECTION_AUTO.PNEUMATIKY_KOLESA = PNEUMATIKY_KOLESA_115
SECTION_AUTO.PRISLUSENSTVO = PRISLUSENSTVO_424
SECTION_AUTO.TUNING = TUNING_113
SECTION_AUTO.VETERANY = VETERANY_114
SECTION_AUTO.AUTOBUSY = AUTOBUSY_107
SECTION_AUTO.DODAVKY = DODAVKY_100
SECTION_AUTO.MIKROBUSY = MIKROBUSY_101
SECTION_AUTO.KARAVANY_VOZIKY = KARAVANY_VOZIKY_111
SECTION_AUTO.NAKLADNE_AUTA = NAKLADNE_AUTA_112
SECTION_AUTO.PICKUP = PICKUP_99
SECTION_AUTO.STROJE = SECTION_STROJE
SECTION_AUTO.OSTATNE = OSTATNE_102
SECTION_AUTO.HAVAROVANE = HAVAROVANE_103
SECTION_AUTO.NAHRADNE_DIELY = NAHRADNE_DIELY_104
SECTION_AUTO.MOTOCYKLE_SKUTRE = SECTION_MOTOCYKLE

SECTION_MOTOCYKLE.CESTNE_MOTOCYKLE = CESTNE_MOTOCYKLE_186
SECTION_MOTOCYKLE.CESTOVNE_MOTOCYKLE = CESTOVNE_MOTOCYKLE_187
SECTION_MOTOCYKLE.ENDURO = ENDURO_188
SECTION_MOTOCYKLE.CHOPPER = CHOPPER_189
SECTION_MOTOCYKLE.MINIBIKE = MINIBIKE_190
SECTION_MOTOCYKLE.MOPEDY = MOPEDY_192
SECTION_MOTOCYKLE.SKUTRE = SKUTRE_193
SECTION_MOTOCYKLE.SKUTRE_VODNE = SKUTRE_VODNE_194
SECTION_MOTOCYKLE.SKUTRE_SNEZNE = SKUTRE_SNEZNE_191
SECTION_MOTOCYKLE.STVORKOLKY = STVORKOLKY_195
SECTION_MOTOCYKLE.TROJKOLKY = TROJKOLKY_196
SECTION_MOTOCYKLE.VETERANY = VETERANY_197
SECTION_MOTOCYKLE.NAHRADNE_DIELY = NAHRADNE_DIELY_198
SECTION_MOTOCYKLE.OBLECENIE_OBUV_HELMY = OBLECENIE_OBUV_HELMY_199
SECTION_MOTOCYKLE.OSTATNE = OSTATNE_200

SECTION_STROJE.CERPADLA = CERPADLA_208
SECTION_STROJE.CISTIACE_STROJE = CISTIACE_STROJE_209
SECTION_STROJE.DREVOOBRABACIE_STROJE = DREVOOBRABACIE_STROJE_210
SECTION_STROJE.GENERATORY = GENERATORY_211
SECTION_STROJE.HISTORICKE_STROJE = HISTORICKE_STROJE_212
SECTION_STROJE.MOTORY = MOTORY_214
SECTION_STROJE.KOVOOBRABACIE_STROJE = KOVOOBRABACIE_STROJE_215
SECTION_STROJE.POLNOHOSPODARSKA_TECHNIKA = POLNOHOSPODARSKA_TECHNIKA_216
SECTION_STROJE.POTRAVINARSKE_STROJE = POTRAVINARSKE_STROJE_213
SECTION_STROJE.SKLADOVA_TECHNIKA = SKLADOVA_TECHNIKA_217
SECTION_STROJE.STAVEBNE_STROJE = STAVEBNE_STROJE_218
SECTION_STROJE.TEXTILNE_STROJE = TEXTILNE_STROJE_219
SECTION_STROJE.TLACIARENSKE_STROJE = TLACIARENSKE_STROJE_220
SECTION_STROJE.VYBAVENIE_PREVADZKARNE = VYBAVENIE_PREVADZKARNE_221
SECTION_STROJE.VYROBNA_LINKA = VYROBNA_LINKA_222
SECTION_STROJE.NAHRADNE_DIELY = NAHRADNE_DIELY_223
SECTION_STROJE.OSTATNE = OSTATNE_224

SECTION_DOM_A_ZAHRADA.BAZENY = BAZENY_238
SECTION_DOM_A_ZAHRADA.CERPADLA = CERPADLA_239
SECTION_DOM_A_ZAHRADA.DVERE_BRANY = DVERE_BRANY_447
SECTION_DOM_A_ZAHRADA.KLIMATIZACIE = KLIMATIZACIE_240
SECTION_DOM_A_ZAHRADA.KOSACKY = KOSACKY_247
SECTION_DOM_A_ZAHRADA.KOTLE_KACHLE_BOJLERY = KOTLE_KACHLE_BOJLERY_241
SECTION_DOM_A_ZAHRADA.MALOTRAKTORY_KULTIVATORY = MALOTRAKTORY_KULTIVATORY_242
SECTION_DOM_A_ZAHRADA.MIESACKY = MIESACKY_244
SECTION_DOM_A_ZAHRADA.NARADIE = NARADIE_245
SECTION_DOM_A_ZAHRADA.OKNA = OKNA_448
SECTION_DOM_A_ZAHRADA.PILY = PILY_449
SECTION_DOM_A_ZAHRADA.SNEZNA_TECHNIKA = SNEZNA_TECHNIKA_248
SECTION_DOM_A_ZAHRADA.STAVEBNY_MATERIAL = STAVEBNY_MATERIAL_249
SECTION_DOM_A_ZAHRADA.RADIATORY = RADIATORY_246
SECTION_DOM_A_ZAHRADA.RASTLINY = RASTLINY_243
SECTION_DOM_A_ZAHRADA.VYBAVENIE_DIELNE = VYBAVENIE_DIELNE_250
SECTION_DOM_A_ZAHRADA.VYSAVACE_FUKACE = VYSAVACE_FUKACE_251
SECTION_DOM_A_ZAHRADA.ZAHRADNE_GRILY = ZAHRADNE_GRILY_252
SECTION_DOM_A_ZAHRADA.ZAHRADNY_NABYTOK = ZAHRADNY_NABYTOK_283
SECTION_DOM_A_ZAHRADA.ZAHRADNA_TECHNIKA = ZAHRADNA_TECHNIKA_253
SECTION_DOM_A_ZAHRADA.OSTATNE = OSTATNE_254

SECTION_PC.DVD_BLURAY_MECHANIKY = DVD_BLURAY_MECHANIKY_1
SECTION_PC.FOTOAPARATY = SECTION_FOTO
SECTION_PC.GPS_NAVIGACIA = GPS_NAVIGACIA_32
SECTION_PC.GRAFICKE_KARTY = GRAFICKE_KARTY_4
SECTION_PC.HARD_DISKY_SSD = HARD_DISKY_SSD_5
SECTION_PC.HERNE_KONZOLY = HERNE_KONZOLY_25
SECTION_PC.HERNE_ZARIADENIA = HERNE_ZARIADENIA_29
SECTION_PC.HRY = HRY_30
SECTION_PC.CHLADICE = CHLADICE_27
SECTION_PC.KLAVESNICE_MYSI = KLAVESNICE_MYSI_6
SECTION_PC.KOPIROVACIE_STROJE = KOPIROVACIE_STROJE_7
SECTION_PC.MOBILNE_TELEFONY = SECTION_MOBILY
SECTION_PC.MODEMY = MODEMY_2
SECTION_PC.LCD_MONITORY = LCD_MONITORY_9
SECTION_PC.MP3_PREHRAVACE = MP3_PREHRAVACE_26
SECTION_PC.NOTEBOOKY = NOTEBOOKY_10
SECTION_PC.PAMATE = PAMATE_11
SECTION_PC.PC_POCITACE = PC_POCITACE_12
SECTION_PC.PROCESORY = PROCESORY_13
SECTION_PC.SIETOVE_KOMPONENTY = SIETOVE_KOMPONENTY_14
SECTION_PC.SCANERY = SCANERY_15
SECTION_PC.SKRINE_ZDROJE = SKRINE_ZDROJE_16
SECTION_PC.SOFTWARE = SOFTWARE_17
SECTION_PC.SPOTREBNY_MATERIAL = SPOTREBNY_MATERIAL_31
SECTION_PC.TABLETY_ECITACKY = TABLETY_ECITACKY_24
SECTION_PC.TLACIARNE = TLACIARNE_18
SECTION_PC.WIRELESS_WIFI = WIRELESS_WIFI_28
SECTION_PC.ZAKLADNE_DOSKY = ZAKLADNE_DOSKY_19
SECTION_PC.ZALOZNE_ZDROJE = ZALOZNE_ZDROJE_20
SECTION_PC.ZVUKOVE_KARTY = ZVUKOVE_KARTY_21
SECTION_PC.OSTATNE = OSTATNE_22

SECTION_MOBILY.APPLE = APPLE_435
SECTION_MOBILY.HTC = HTC_436
SECTION_MOBILY.HUAWEI_HONOR = HUAWEI_HONOR_305
SECTION_MOBILY.LG = LG_301
SECTION_MOBILY.MOTOROLA_LENOVO = MOTOROLA_LENOVO_302
SECTION_MOBILY.NOKIA_MICROSOFT = NOKIA_MICROSOFT_303
SECTION_MOBILY.SAMSUNG = SAMSUNG_304
SECTION_MOBILY.SONY = SONY_306
SECTION_MOBILY.XIAOMI = XIAOMI_451
SECTION_MOBILY.OSTATNE_ZNACKY = OSTATNE_ZNACKY_307
SECTION_MOBILY.BATERIE = BATERIE_308
SECTION_MOBILY.BEZDROTOVE_TELEFONY = BEZDROTOVE_TELEFONY_316
SECTION_MOBILY.DATOVE_KABELY = DATOVE_KABELY_309
SECTION_MOBILY.FAXY = FAXY_317
SECTION_MOBILY.GPS_NAVIGACIA = GPS_NAVIGACIA_32
SECTION_MOBILY.HEADSETY = HEADSETY_310
SECTION_MOBILY.HF_SADY_DO_AUTA = HF_SADY_DO_AUTA_311
SECTION_MOBILY.INTELIGENTNE_HODINKY = INTELIGENTNE_HODINKY_450
SECTION_MOBILY.KLASICKE_TELEFONY = KLASICKE_TELEFONY_318
SECTION_MOBILY.KRYTY = KRYTY_440
SECTION_MOBILY.NABIJACKY = NABIJACKY_312
SECTION_MOBILY.PAMATOVE_KARTY = PAMATOVE_KARTY_313
SECTION_MOBILY.OSTATNE = OSTATNE_315

SECTION_FOTO.ANALOGOVE_FOTOAPARATY = ANALOGOVE_FOTOAPARATY_443
SECTION_FOTO.DIGITALNE_FOTOAPARATY = DIGITALNE_FOTOAPARATY_256
SECTION_FOTO.DRONY = DRONY_456
SECTION_FOTO.VIDEOKAMERY = VIDEOKAMERY_258
SECTION_FOTO.ZRKADLOVKY = ZRKADLOVKY_257
SECTION_FOTO.BATERIE = BATERIE_259
SECTION_FOTO.BLESKY_A_OSVETLENIE = BLESKY_A_OSVETLENIE_442
SECTION_FOTO.BRASNE_A_PUZDRA = BRASNE_A_PUZDRA_260
SECTION_FOTO.DATOVE_KABLE = DATOVE_KABLE_262
SECTION_FOTO.FILTRE = FILTRE_263
SECTION_FOTO.NABIJACKY = NABIJACKY_264
SECTION_FOTO.OBJEKTIVY = OBJEKTIVY_261
SECTION_FOTO.PAMATOVE_KARTY = PAMATOVE_KARTY_265
SECTION_FOTO.STATIVY = STATIVY_266
SECTION_FOTO.OSTATNE = OSTATNE_267

SECTION_ELEKTRO.DIGESTORY = DIGESTORY_389
SECTION_ELEKTRO.CHLADNICKY = CHLADNICKY_390
SECTION_ELEKTRO.MIKROVLNNE_RURY = MIKROVLNNE_RURY_391
SECTION_ELEKTRO.MRAZNICKY = MRAZNICKY_392
SECTION_ELEKTRO.PRACKY = PRACKY_394
SECTION_ELEKTRO.SPORAKY = SPORAKY_395
SECTION_ELEKTRO.SUSICKY = SUSICKY_396
SECTION_ELEKTRO.UMYVACKY_RIADU = UMYVACKY_RIADU_393
SECTION_ELEKTRO.OSTATNE_BIELA = OSTATNE_BIELA_397
SECTION_ELEKTRO.AUTORADIA = AUTORADIA_398
SECTION_ELEKTRO.DOMACE_KINA = DOMACE_KINA_400
SECTION_ELEKTRO.FOTOAPARATY = SECTION_FOTO
SECTION_ELEKTRO.GPS_NAVIGACIA = GPS_NAVIGACIA_32
SECTION_ELEKTRO.HIFI_SYSTEMY_RADIA = HIFI_SYSTEMY_RADIA_402
SECTION_ELEKTRO.HUDOBNE_NASTROJE = SECTION_HUDBA
SECTION_ELEKTRO.MP3_PREHRAVACE = MP3_PREHRAVACE_26
SECTION_ELEKTRO.PROJEKTORY = PROJEKTORY_404
SECTION_ELEKTRO.REPRO_SUSTAVY = REPRO_SUSTAVY_405
SECTION_ELEKTRO.SLUCHADLA = SLUCHADLA_399
SECTION_ELEKTRO.TELEVIZORY = TELEVIZORY_406
SECTION_ELEKTRO.VIDEO_DVD_PREHRAVACE = VIDEO_DVD_PREHRAVACE_407
SECTION_ELEKTRO.VIDEOKAMERY = VIDEOKAMERY_258
SECTION_ELEKTRO.ZOSILNOVACE = ZOSILNOVACE_409
SECTION_ELEKTRO.OSTATNE_AUDIO_VIDEO = OSTATNE_AUDIO_VIDEO_410
SECTION_ELEKTRO.EPILATORY_DEPILATORY = EPILATORY_DEPILATORY_411
SECTION_ELEKTRO.FENY_KULMY = FENY_KULMY_412
SECTION_ELEKTRO.HOLIACE_STROJCEKY = HOLIACE_STROJCEKY_413
SECTION_ELEKTRO.KAVOVARY = KAVOVARY_414
SECTION_ELEKTRO.NABIJACKY_BATERII = NABIJACKY_BATERII_415
SECTION_ELEKTRO.RUCNE_SLAHACE_MIXERY = RUCNE_SLAHACE_MIXERY_421
SECTION_ELEKTRO.SVIETIDLA_LAMPY = SVIETIDLA_LAMPY_416
SECTION_ELEKTRO.SIJACIE_STROJE = SIJACIE_STROJE_417
SECTION_ELEKTRO.VYSAVACE = VYSAVACE_418
SECTION_ELEKTRO.VYSIELACKY = VYSIELACKY_419
SECTION_ELEKTRO.ZVLHCOVACE_VZDUCHU = ZVLHCOVACE_VZDUCHU_420
SECTION_ELEKTRO.ZEHLICKY = ZEHLICKY_422
SECTION_ELEKTRO.OSTATNE_DROBNE = OSTATNE_DROBNE_423

SECTION_SPORT.FITNESS_JOGGING = FITNESS_JOGGING_320
SECTION_SPORT.GOLF = GOLF_321
SECTION_SPORT.FUTBAL = FUTBAL_322
SECTION_SPORT.INLINES_SKATEBOARDING = INLINES_SKATEBOARDING_323
SECTION_SPORT.KEMPING = KEMPING_319
SECTION_SPORT.LETECTVO = LETECTVO_446
SECTION_SPORT.LOPTOVE_HRY = LOPTOVE_HRY_324
SECTION_SPORT.POLOVNICTVO_LOV = POLOVNICTVO_LOV_325
SECTION_SPORT.PAINTBALL = PAINTBALL_326
SECTION_SPORT.RYBOLOV = RYBOLOV_327
SECTION_SPORT.SPOLOCENSKE_HRY = SPOLOCENSKE_HRY_328
SECTION_SPORT.TENIS_SQUASH_BADMINTON = TENIS_SQUASH_BADMINTON_329
SECTION_SPORT.TURISTIKA_HOROLEZECTVO = TURISTIKA_HOROLEZECTVO_330
SECTION_SPORT.VODNE_SPORTY_POTAPANIE = VODNE_SPORTY_POTAPANIE_331
SECTION_SPORT.VSETKO_OSTATNE = VSETKO_OSTATNE_332
SECTION_SPORT.DETSKE_BICYKLE = BICYKLE_452
SECTION_SPORT.KOLOBEZKY = KOLOBEZKY_444
SECTION_SPORT.HORSKE_BICYKLE = HORSKE_BICYKLE_333
SECTION_SPORT.CESTNE_BICYKLE = CESTNE_BICYKLE_334
SECTION_SPORT.SUCIASTKY_A_DIELY = SUCIASTKY_A_DIELY_335
SECTION_SPORT.OSTATNA_CYKLISTIKA = OSTATNA_CYKLISTIKA_336
SECTION_SPORT.BEZKOVANIE = BEZKOVANIE_445
SECTION_SPORT.LYZOVANIE = LYZOVANIE_337
SECTION_SPORT.SKIALPY = SKIALPY_459
SECTION_SPORT.SNOWBOARDING = SNOWBOARDING_338
SECTION_SPORT.HOKEJ_KORCULOVANIE = HOKEJ_KORCULOVANIE_339
SECTION_SPORT.OSTATNE_ZIMNE = OSTATNE_ZIMNE_340

SECTION_HUDBA.BICIE_NASTROJE = BICIE_NASTROJE_285
SECTION_HUDBA.DYCHOVE_NASTROJE = DYCHOVE_NASTROJE_286
SECTION_HUDBA.KLAVESOVE_NASTROJE = KLAVESOVE_NASTROJE_287
SECTION_HUDBA.SLACIKOVE_NASTROJE = SLACIKOVE_NASTROJE_288
SECTION_HUDBA.STRUNOVE_NASTROJE = STRUNOVE_NASTROJE_289
SECTION_HUDBA.OSTATNE_NASTROJE = OSTATNE_NASTROJE_290
SECTION_HUDBA.DVD_CD_MC_LP = DVD_CD_MC_LP_291
SECTION_HUDBA.HUDOBNICI_A_SKUPINY = HUDOBNICI_A_SKUPINY_292
SECTION_HUDBA.KONCERTY = KONCERTY_293
SECTION_HUDBA.VYUKA_HUDBY = VYUKA_HUDBY_185
SECTION_HUDBA.NOTY_TEXTY = NOTY_TEXTY_295
SECTION_HUDBA.SKUSOBNE = SKUSOBNE_296
SECTION_HUDBA.SVETELNA_TECHNIKA = SVETELNA_TECHNIKA_297
SECTION_HUDBA.VSTUPENKY = HUDBA_KONCERTY_229
SECTION_HUDBA.ZVUKOVA_TECHNIKA = ZVUKOVA_TECHNIKA_299
SECTION_HUDBA.OSTATNE = OSTATNE_300

SECTION_VSTUPENKY.DARCEKOVE_POUKAZKY = DARCEKOVE_POUKAZKY_231
SECTION_VSTUPENKY.DIALNICNE_ZNAMKY = DIALNICNE_ZNAMKY_232
SECTION_VSTUPENKY.CESTOVNE_LISTKY = CESTOVNE_LISTKY_225
SECTION_VSTUPENKY.LETENKY = LETENKY_226
SECTION_VSTUPENKY.PERMANENTKY = PERMANENTKY_236
SECTION_VSTUPENKY.DIVADLO = DIVADLO_227
SECTION_VSTUPENKY.FESTIVALY = FESTIVALY_228
SECTION_VSTUPENKY.HUDBA_KONCERTY = HUDBA_KONCERTY_229
SECTION_VSTUPENKY.PRE_DETI = PRE_DETI_233
SECTION_VSTUPENKY.SPOLOCENSKE_AKCIE = SPOLOCENSKE_AKCIE_230
SECTION_VSTUPENKY.SPORT = SPORT_234
SECTION_VSTUPENKY.VYSTAVY = VYSTAVY_235
SECTION_VSTUPENKY.OSTATNE = OSTATNE_237

SECTION_KNIHY.BELETRIA = BELETRIA_366
SECTION_KNIHY.CUDZOJAZYCNA_LITERATURA = CUDZOJAZYCNA_LITERATURA_388
SECTION_KNIHY.CASOPISY = CASOPISY_367
SECTION_KNIHY.DETEKTIVKY = DETEKTIVKY_368
SECTION_KNIHY.DETSKA_LITERATURA = DETSKA_LITERATURA_369
SECTION_KNIHY.DRAMA = DRAMA_370
SECTION_KNIHY.ENCYKLOPEDIE = ENCYKLOPEDIE_371
SECTION_KNIHY.EZOTERIKA = EZOTERIKA_372
SECTION_KNIHY.HISTORICKE_ROMANY = HISTORICKE_ROMANY_373
SECTION_KNIHY.HOBBY_ODBORNE_KNIHY = HOBBY_ODBORNE_KNIHY_374
SECTION_KNIHY.KUCHARKY = KUCHARKY_375
SECTION_KNIHY.MAPY_CESTOVANIE = MAPY_CESTOVANIE_376
SECTION_KNIHY.POCITACOVA_LITERATURA = POCITACOVA_LITERATURA_378
SECTION_KNIHY.PRE_MLADEZ = PRE_MLADEZ_379
SECTION_KNIHY.ROMANY_PRE_ZENY = ROMANY_PRE_ZENY_380
SECTION_KNIHY.SCIFI_FANTASY = SCIFI_FANTASY_381
SECTION_KNIHY.UCEBNICE_SKRIPTA_ZS = UCEBNICE_SKRIPTA_ZS_386
SECTION_KNIHY.UCEBNICE_SKRIPTA_SS = UCEBNICE_SKRIPTA_SS_383
SECTION_KNIHY.UCEBNICE_SKRIPTA_VS = UCEBNICE_SKRIPTA_VS_382
SECTION_KNIHY.UCEBNICE_SKRIPTA_JAZYKOVE = UCEBNICE_SKRIPTA_JAZYKOVE_387
SECTION_KNIHY.ZABAVNA_LITERATURA = ZABAVNA_LITERATURA_384
SECTION_KNIHY.ZDRAVY_ZIVOTNY_STYL = ZDRAVY_ZIVOTNY_STYL_385
SECTION_KNIHY.OSTATNE = OSTATNE_377

SECTION_NABYTOK.DETSKY_NABYTOK = NABYTOK_PRE_DETI_127
SECTION_NABYTOK.DVERE_BRANY = DVERE_BRANY_447
SECTION_NABYTOK.JEDALENSKE_KUTY = JEDALENSKE_KUTY_268
SECTION_NABYTOK.KNIZNICE = KNIZNICE_269
SECTION_NABYTOK.KOBERCE_A_PODLAHOVA_KRYTINA = KOBERCE_A_PODLAHOVA_KRYTINA_270
SECTION_NABYTOK.KRESLA_A_GAUCE = KRESLA_A_GAUCE_271
SECTION_NABYTOK.KUCHYNE = KUCHYNE_272
SECTION_NABYTOK.KUPELNE = KUPELNE_274
SECTION_NABYTOK.LAMPY_OSVETLENIE = LAMPY_OSVETLENIE_275
SECTION_NABYTOK.MATRACE = MATRACE_276
SECTION_NABYTOK.OBYVACIE_STENY = OBYVACIE_STENY_273
SECTION_NABYTOK.POSTELE = POSTELE_277
SECTION_NABYTOK.SEDACIE_SUPRAVY = SEDACIE_SUPRAVY_278
SECTION_NABYTOK.SKRINE = SKRINE_279
SECTION_NABYTOK.SPALNE = SPALNE_280
SECTION_NABYTOK.STOLICKY = STOLICKY_281
SECTION_NABYTOK.STOLY = STOLY_282
SECTION_NABYTOK.ZAHRADNY_NABYTOK = ZAHRADNY_NABYTOK_283
SECTION_NABYTOK.DOPLNKY = DOPLNKY_425
SECTION_NABYTOK.OSTATNY_NABYTOK = OSTATNY_NABYTOK_284

SECTION_OBLECENIE.BLUZKY = BLUZKY_51
SECTION_OBLECENIE.BUNDY_A_KABATY = BUNDY_A_KABATY_52
SECTION_OBLECENIE.CIAPKY_SATKY = CIAPKY_SATKY_53
SECTION_OBLECENIE.DZINSY = DZINSY_54
SECTION_OBLECENIE.FUNKCNE_PRADLO = FUNKCNE_PRADLO_55
SECTION_OBLECENIE.KOSELE = KOSELE_56
SECTION_OBLECENIE.KOZENE_OBLECENIE = KOZENE_OBLECENIE_57
SECTION_OBLECENIE.MIKINY = MIKINY_58
SECTION_OBLECENIE.NOHAVICE = NOHAVICE_59
SECTION_OBLECENIE.OBLEKY_SAKA = OBLEKY_SAKA_60
SECTION_OBLECENIE.PLAVKY = PLAVKY_61
SECTION_OBLECENIE.RUKAVICE_A_SALY = RUKAVICE_A_SALY_63
SECTION_OBLECENIE.RUSKA = RUSKA_458
SECTION_OBLECENIE.SPODNA_BIELIZEN = SPODNA_BIELIZEN_64
SECTION_OBLECENIE.SUKNE = SUKNE_65
SECTION_OBLECENIE.SVADOBNE_SATY = SVADOBNE_SATY_66
SECTION_OBLECENIE.SVETRE = SVETRE_67
SECTION_OBLECENIE.SATY_KOSTYMY = SATY_KOSTYMY_68
SECTION_OBLECENIE.SORTKY = SORTKY_69
SECTION_OBLECENIE.SPORTOVE_OBLECENIE = SPORTOVE_OBLECENIE_70
SECTION_OBLECENIE.TEHOTENSKE_OBLECENIE = TEHOTENSKE_OBLECENIE_62
SECTION_OBLECENIE.TRICKA_ROLAKY_TIELKA = TRICKA_ROLAKY_TIELKA_71
SECTION_OBLECENIE.DOPLNKY = DOPLNKY_72
SECTION_OBLECENIE.HODINKY = HODINKY_73
SECTION_OBLECENIE.KABELKY = KABELKY_74
SECTION_OBLECENIE.PLECNIAKY_A_KUFRE = PLECNIAKY_A_KUFRE_75
SECTION_OBLECENIE.TOPANKY_OBUV = TOPANKY_OBUV_76
SECTION_OBLECENIE.SPERKY = SPERKY_77
SECTION_OBLECENIE.OSTATNE = OSTATNE_78

SECTION_SLUZBY.AUTO_MOTO = AUTO_MOTO_426
SECTION_SLUZBY.CESTOVANIE = CESTOVANIE_167
SECTION_SLUZBY.DOMACE_PRACE = DOMACE_PRACE_168
SECTION_SLUZBY.EZOTERIKA = EZOTERIKA_427
SECTION_SLUZBY.IT_WEBDESIGN = IT_WEBDESIGN_171
SECTION_SLUZBY.KONE_SLUZBY = KONE_SLUZBY_437
SECTION_SLUZBY.KURZY_A_SKOLENIA = KURZY_A_SKOLENIA_172
SECTION_SLUZBY.OPRAVY_A_SERVIS = OPRAVY_A_SERVIS_428
SECTION_SLUZBY.ORGANIZOVANIE_AKCII = ORGANIZOVANIE_AKCII_429
SECTION_SLUZBY.POZICOVNE = POZICOVNE_430
SECTION_SLUZBY.PRAVO_A_BEZPECNOST = PRAVO_A_BEZPECNOST_431
SECTION_SLUZBY.PREKLADATELSTVO = PREKLADATELSTVO_173
SECTION_SLUZBY.PREPRAVA_A_STAHOVANIE = PREPRAVA_A_STAHOVANIE_174
SECTION_SLUZBY.REALITNE_SLUZBY = REALITNE_SLUZBY_432
SECTION_SLUZBY.REKLAMA_NA_AUTO = REKLAMA_NA_AUTO_183
SECTION_SLUZBY.REKLAMNE_PLOCHY_OSTATNE = REKLAMNE_PLOCHY_OSTATNE_184
SECTION_SLUZBY.REMESELNE_A_STAVEBNE_PRACE = REMESELNE_A_STAVEBNE_PRACE_175
SECTION_SLUZBY.SLUZBY_PRE_ZVIERATA = SLUZBY_PRE_ZVIERATA_43
SECTION_SLUZBY.SPROSTREDKOVATELSKE_SLUZBY = SPROSTREDKOVATELSKE_SLUZBY_176
SECTION_SLUZBY.STRAZENIE_DETI = STRAZENIE_DETI_178
SECTION_SLUZBY.TVORIVA_PRACA = TVORIVA_PRACA_434
SECTION_SLUZBY.UBYTOVANIE = UBYTOVANIE_179
SECTION_SLUZBY.UCTOVNICTVO_PORADENSTVO = UCTOVNICTVO_PORADENSTVO_170
SECTION_SLUZBY.UPRATOVANIE = UPRATOVANIE_180
SECTION_SLUZBY.VYROBA = VYROBA_433
SECTION_SLUZBY.VYUKA_DOUCOVANIE = VYUKA_DOUCOVANIE_169
SECTION_SLUZBY.VYUKA_HUDBY = VYUKA_HUDBY_185
SECTION_SLUZBY.ZDRAVIE_A_KRASA = ZDRAVIE_A_KRASA_182
SECTION_SLUZBY.OSTATNE = OSTATNE_181

SECTION_OSTATNE.MINCE_BANKOVKY = MINCE_BANKOVKY_454
SECTION_OSTATNE.MODELARSTVO = MODELARSTVO_453
SECTION_OSTATNE.POTRAVINY = POTRAVINY_201
SECTION_OSTATNE.SKLO_KERAMIKA = SKLO_KERAMIKA_203
SECTION_OSTATNE.STAROZITNOSTI = STAROZITNOSTI_202
SECTION_OSTATNE.SPERKY_HODINKY = SPERKY_77
SECTION_OSTATNE.UMELECKE_PREDMETY = UMELECKE_PREDMETY_204
SECTION_OSTATNE.ZBERATELSTVO = ZBERATELSTVO_205
SECTION_OSTATNE.ZDRAVIE_A_KRASA = ZDRAVIE_A_KRASA_206
SECTION_OSTATNE.ZNAMKY_POHLADNICE = ZNAMKY_POHLADNICE_455
SECTION_OSTATNE.OSTATNE = OSTATNE_207
