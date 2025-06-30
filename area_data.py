# area_data.py

# This dictionary maps a main city/town/county to a list of all its associated areas.
# All names are stored in lowercase to make searching case-insensitive and reliable.
# Now includes both English and Welsh names and expanded regions.
AREA_MAP = {
    'cardiff': [
        'cardiff', 'caerdydd', 'adamsdown', 'butetown', 'caerau', 'canton', 'castle', 'cathays', 
        'cyncoed', 'ely', 'fairwater', 'gabalfa', 'grangetown', 'heath', 'llandaff', 
        'llandaff north', 'llanedeyrn', 'llanishen', 'llanrumney', 'lisvane', 'pentwyn', 'penylan', 
        'pontcanna', 'pontprennau', 'radyr & morganstown', 'rhiwbina', 'riverside', 
        'roath', 'rumney', 'splott', 'st fagans', 'sain ffagan', 'thornhill', 'tongwynlais', 
        'tremorfa', 'trowbridge', 'whitchurch'
    ],
    'newport': [
        'newport', 'casnewydd', 'newport city centre', 'allt-yr-yn', 'alway', 'bassaleg', 'beechwood', 
        'bettws', 'bishton', 'caerleon', 'christchurch', 'coedkernew', 'duffryn', 'gaer', 'goldcliff', 
        'graig', 'langstone', 'liswerry', 'llanishen', 'llanmartin', 'llanwern', 
        'lower machen', 'maesglas', 'maindee', 'malpas', 'marshfield', 'michaelstone-y-fedw', 
        'nash', 'penhow', 'peterstone wentlooge', 'pillgwenlly', 'redwick', 'rhiwderin', 
        'ridgeway', 'rogerstone', 'somerton', 'st brides wentlooge', 'st julians', 'stelvio', 
        'peterstone', 'uskmouth', 'wentwood', 'whitson'
    ],
    'swansea': [
        'swansea', 'abertawe', 'uplands', 'maritime quarter', 'brynmill', 'gorseinon', 'gowerton', 
        'dunvant', 'morriston', 'treforys', 'clydach', 'cockett', 'bishopston', 'killay', 
        'caswell bay', 'langland', 'mumbles', 'mwmbwls', 'loughor', 'casllwchwr', 'oxwich', 'llanmadoc', 
        'llanrhidian', 'penllergaer', 'pontarddulais', 'port tennant', 'sketty', 'llansamlet', 'three crosses'
    ],
    'vale of glamorgan': [
        'vale of glamorgan', 'bro morgannwg', 'barry', 'y barri', 'barry island', 'bonvilston', 'boverton', 
        'cadoxton', 'clemenstone', 'colwinston', 'corntown', 'cowbridge', 'y bont-faen', 
        'dinas powys', 'dyffryn', 'ewenny', 'font-y-gary', 'fonmon', 'gileston', 'llancadle', 
        'llancarfan', 'llandough', 'llandow', 'llanmaes', 'llantwit major', 'llanilltud fawr', 
        'monknash', 'ogmore-by-sea', 'palmerstown', 'penarth', 'pendoylan', 
        'penmark', 'peterston-super-ely', 'porthkerry', 'rhoose', 'sigingstone', 'southerndown', 'st athan', 
        'sain tathan', 'st brides major', 'st donats', 'st hilary', 'st nicholas', 'sully', 'wenvoe', 'wick'
    ],
    'bridgend': [
        'bridgend', 'pen-y-bont ar ogwr', 'aberkenfig', 'bettws', 'blaengarw', 'brackla', 'bryncethin', 
        'brynmenyn', 'caerau', 'cefn cribwr', 'cefn glas', 'coity', 'cornelly', 'coychurch', 'cwmfelin', 'garw valley', 
        'heol-y-cyw', 'kenfig', 'kenfig hill', 'laleston', 'llangeinor', 'llangynwyd', 'maesteg', 'merthyr mawr', 
        'nantymoel', 'newcastle', 'ogmore vale', 'pencoed', 'pen-y-fai', 'pontycymer', 'porthcawl', 
        'pyle', 'sarn', 'st brides major', 'st brides minor', 'tondu', 'wildmill', 'ynysawdre'
    ],
    'rhondda cynon taf': [
        'rhondda cynon taf', 'rhondda cynon tâf', 'pontypridd', 'abercwmboi', 'abercynon', 'aberdare', 'beddau', 
        'blaenclydach', 'blaenrhondda', 'brynna', 'church village', 'clydach vale', 'coedely', 
        'cwmaman', 'cwmbach', 'cwmdare', 'cwmparc', 'cymmer', 'efail isaf', 'ferndale', 'gelli', 
        'gilfach goch', 'glyncoch', 'glynhafod', 'graig', 'groes-faen', 'hirwaun', 'llanharan', 'llanharry', 
        'llantrisant', 'llantwit fardre', 'llwydcoed', 'llwynypia', 'maerdy', 'miskin', 'mountain ash', 
        'nantgarw', 'penrhiwceiber', 'penrhys', 'pentre', 'penygraig', 'penywaun', 'pontyclun', 
        'pontygwaith', 'porth', 'rhigos', 'rhydyfelin', 'stanleytown', 'taffs well', 'talbot green', 'ton-teg',
        'tonypandy', 'tonyrefail', 'trealaw', 'trebanog', 'trehafod', 'treherbert', 'treorchy', 'tylorstown', 
        'wattstown', 'ynyshir', 'ynysybwl', 'ystrad'
    ],
    'merthyr tydfil': [
        'merthyr tydfil', 'merthyr tudful', 'abercanaid', 'bedlinog', 'cyfarthfa', 'dowlais', 'gurnos', 'heolgerrig', 
        'merthyr vale', 'pant', 'park', 'penydarren', 'pontsticill', 'pontsarn', 'quakers yard', 
        'town', 'treharris', 'trelewis', 'troed-y-rhiw', 'vaynor'
    ],
    'caerphilly': [
        'caerphilly', 'caerffili', 'abergarn', 'aberbargoed', 'abercarn', 'abertridwr', 'aberdysswg', 
        'argoed', 'bargoed', 'bedwas', 'bedwas, trethomas and machen', 'bedwellty', 
        'blackwood', 'cefn fforest', 'cefnhengoed', 'chapel of ease', 'croespenmaen', 
        'crosskeys', 'crumlin', 'cwmbargoed', 'cwmcarn', 'cwmfelinfach', 'cwmsyfiog', 
        'deri', 'draethen', 'fleur-de-lis', 'fochriw', 'gelligaer', 'gelligroes', 
        'gilfach', 'graig-y-rhacca', 'groes-faen', 'hafodyrynys', 'hengoed', 'hollybush', 
        'llanbradach', 'llancaiach', 'machen', 'maesycwmmer', 'markham', 'nelson', 'newbridge', 
        'new tredegar', 'oakdale', 'penallta', 'pengam', 'penmaen', 'penpedairheol', 'pentwynmawr', 
        'penyrheol', 'phillipstown', 'pontllanfraith', 'pontlottyn', 'pwllypant', 'rhymney', 
        'risca', 'rudry', 'senghenydd', 'tir-phil', 'tir-y-berth', 'trethomas', 'wyllie', 'ynysddu', 'ystrad mynach'
    ],
    'monmouthshire': [
        'monmouthshire', 'sir fynwy', 'abergavenny', 'y fenni', 'bettws newydd', 'blaenavon', 'caerwent', 'caldicot', 
        'catbrook', 'chepstow', 'cas-gwent', 'clydach', 'cwmcarvan', 'cwmyoy', 'devauden', 'dingestow', 'gilwern', 'glascoed', 
        'govilon', 'goytre', 'grosmont', 'llanarth', 'llanbadoc', 'llandegveth', 'llandenny', 
        'llandogo', 'llanellen', 'llanfoist', 'llangattock', 'llangattock-vibon-avel', 'llangybi', 'llanhennock', 'llanishen', 
        'llanover', 'llantilio crossenny', 'llantilio pertholey', 'llantrisant', 'llanvair discoed', 'llanvapley', 'magor', 
        'mardy', 'mathern', 'mitchel troy', 'monmouth', 'trefynwy', 'pandy', 'penallt', 'portskewett', 
        'raglan', 'redwick', 'rogiet', 'skenfrith', 'st arvans', 'sudbrook', 'tintern', 'tyndyrn',
        'trellech', 'undy', 'usk', 'brynbuga', 'whitebrook', 'wonastow'
    ],
    'blaenau gwent': [
        'blaenau gwent', 'abertillery', 'badminton', 'beaufort', 'blaina', 'brynmawr', 'cwm', 
        'cwmtillery', 'ebbw vale', 'glynebwy', 'georgetown', 'llanhilleth', 'nantyglo', 'rassau', 
        'sirhowy', 'six bells', 'tredegar', 'trefil'
    ],
    'torfaen': [
        'torfaen', 'abersychan', 'blaenavon', 'croesyceiliog', 'cwmavon', 'cwmbran', 
        'garndiffaith', 'griffithstown', 'henllys', 'llanyrafon', 'new inn', 'pontnewydd', 
        'ponthir', 'pontypool', 'pont-y-pŵl', 'sebastopol', 'talywain', 'trevethin', 'upper cwmbran', 'varteg'
    ],
    'pembrokeshire': [
        'pembrokeshire', 'sir benfro', 'abercastle', 'abereiddy', 'amroth', 'angle', 'begelly', 'boncath', 
        'brawdy', 'broad haven', 'burton', 'caldey island', 'carew', 'castlemartin', 'cilgerran', 'cosheston', 'crymych',
        'dale', 'dinbych-y-pysgod', 'fishguard', 'abergwaun', 'goodwick', 'haverfordwest', 'hwlffordd', 'jeffreyston', 
        'johnston', 'lamphey', 'little haven', 'llangwm', 'maenclochog', 'manorbier', 'marloes', 'mathry', 'milford haven', 'aberllun-ddu', 
        'narberth', 'arberth', 'newgale', 'newport', 'trefdraeth', 'neyland', 'pembroke', 'penfro', 'pembroke dock', 'penally', 
        'puncheston', 'roch', 'saundersfoot', 'solva', 'st davids', 'tyddewi', 'st dogmaels', 'st ishmaels', 'stepaside', 'tenby'
    ],
    'carmarthenshire': [
        'carmarthenshire', 'sir gaerfyrddin', 'carmarthen', 'caerfyrddin', 'llanelli', 'ammanford', 'rhydaman', 'burry port', 
        'porth tywyn', 'carmel', 'kidwelly', 'cidweli', 'laugharne', 'talacharn', 'llandeilo', 'llandovery', 'llanymddyfri', 'newcastle emlyn', 
        'castell newydd emlyn', 'st clears', 'sanclêr', 'whitland', 'hendy-gwyn', 'quarter bach', 'pembrey', 'pencarreg', 
        'pendine', 'pontyberem', 'trelech', 'trimsaran', 'talley', 'st ishmael', 'llangain', 'llangadog', 'llangyndeyrn', 
        'abergwili', 'abernant', 'bancyfelin', 'betws', 'brechfa', 'bronwydd', 'brynamman', 'bynea', 'caeo', 
        'cenarth', 'cilycwm', 'cross hands', 'cwmamman', 'cynwyl elfed', 'ferryside', 'glanamman', 'gorslas', 'henllanfallteg', 
        'llandybie', 'llanedi', 'llangan', 'llangennech', 'llangynog', 'llansteffan', 'llanwinio', 'llanwrda', 
        'llanybydder', 'meinciau', 'myddfai', 'pencader', 'pontyates', 'tumble'
    ],
    'powys / brecon beacons': [
        'powys', 'brecon beacons', 'bannau brycheiniog', 'aber-craf', 'brecon', 'aberhonddu', 'builth wells', 'llanfair-ym-muallt', 
        'caersws', 'crickhowell', 'crucywel', 'erwood', 'glangrwyney', 'glasbury', 'hay-on-wye', 'y gelli gandryll', 'knighton', 'tref-y-clawdd', 
        'llandrindod wells', 'llangammarch wells', 'llangynidr', 'llanwrtyd wells', 'llanfyllin', 'llanidloes', 'machynlleth', 'montgomery', 
        'newtown', 'y drenewydd', 'presteigne', 'llanandras', 'rhayader', 'rhaeadr gwy', 'sennybridge', 'talgarth', 
        'welshpool', 'y trallwng', 'ystradgynlais'
    ],
    'ceredigion': [
        'ceredigion', 'aberystwyth', 'aberteifi', 'cardigan', 'aberporth', 'aberaeron', 'beulah', 'borth', 'capel celyn', 
        'devil\'s bridge', 'lampeter', 'llanbedr pont steffan', 'llandrindod', 'llandysul', 'llangrannog', 
        'llanrhystud', 'new quay', 'ceinewydd', 'ponterwyd', 'strata florida', 'talybont', 'tregaron'
    ],
    'herefordshire': [
        'herefordshire', 'hereford', 'bromyard', 'colwall', 'eardisley', 'fownhope', 'kington', 'ledbury', 
        'leintwardine', 'leominster', 'madley', 'pembridge', 'ross-on-wye', 'weobley', 'whitney-on-wye'
    ],
    'gloucestershire': [
        'gloucestershire', 'gloucester', 'cheltenham', 'cinderford', 'cirencester', 'coleford', 'dursley', 
        'forest of dean', 'lydney', 'newent', 'stow-on-the-wold', 'stroud', 'tewkesbury', 'wye valley'
    ]
}