SNOMED={

"fever":{

"code":"386661006",

"name":"Fever"

},

"cough":{

"code":"49727002",

"name":"Cough"

},

"headache":{

"code":"25064002",

"name":"Headache"

},

"hypertension":{

"code":"38341003",

"name":"Hypertensive disorder"

},

"myocardial infarction":{

"code":"22298006",

"name":"Myocardial infarction"

}

}


def map_concept(entity):

    return SNOMED.get(

        entity,

        {

            "code":"UNKNOWN",

            "name":entity

        }

    )