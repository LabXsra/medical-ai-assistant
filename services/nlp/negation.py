NEGATIONS=[

"no",

"not",

"without",

"never",

"denies",

"don't"

]


def is_negated(text,symptom):

    text=text.lower()

    symptom=symptom.lower()

    index=text.find(symptom)

    if index==-1:

        return False

    context=text[max(0,index-35):index]

    for word in NEGATIONS:

        if word in context:

            return True

    return False