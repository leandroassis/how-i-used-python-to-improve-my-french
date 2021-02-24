from polyglot.text import Text
from pandas import DataFrame
from google_trans_new import google_translator


class  FrenchPolyglot():
    def getText(self, text):
        self.text = Text(text, hint_language_code="fr")

    def tagText(self):
        self.tagged_text = self.text.pos_tags
        
    def lTupleToList(self):

        replaceTo = {
            "ADJ": "Adjective",
            "ADP": "Adposition",
            "ADV": "Adverb",
            "AUX": "Auxiliary verb",
            "CONJ": "Coor. Conjunction",
            "DET": "Determiner",
            "INTJ": "Interjection",
            "NOUN": "Noun",
            "NUM": "Numeral",
            "PART":"Particle",
            "PRON": "Pronoun",
            "PROPN": "Proper noun",
            "PUNCT": "Punctuation",
            "SCONJ": "Sub. Conjunction",
            "SYM": "Symbol",
            "VERB": "Verb",
            "X": "Other"
        }

        self.word_list = []
        self.classification_list = []
        for tupla in range(len(self.tagged_text)):
            if self.tagged_text[tupla][0] in ["“", "”", "’", "-", ".",","] or self.tagged_text[tupla][1] == "PUNCT":
                continue
            else:
                self.classification_list.append(replaceTo[self.tagged_text[tupla][1]])
                self.word_list.append(self.tagged_text[tupla][0])

    def createDataframe(self):
        FrenchList = DataFrame(self.word_list, columns=["Français"])
        FrenchList["Classification"] = self.classification_list
        self.FrenchList = FrenchList.drop_duplicates(subset="Français")
    def translateTo(self):
        translator = google_translator()
        self.FrenchList["English"] = self.FrenchList["Français"].apply(translator.translate)
        self.FrenchList["Deutch"] = self.FrenchList["Français"].apply(translator.translate, args=("de", "fr"))
        self.FrenchList["Português"] = self.FrenchList["Français"].apply(translator.translate, args=("pt-br", "fr"))
    def exports(self):
        self.FrenchList.to_html('FrenchWordList.html')
    

if __name__ == "__main__":
    objct = FrenchPolyglot()
    objct.getText("Le problème n’est pas tant l’“islamo-gauchisme” que que le dévoiement militant de l’enseignement et de la recherche")
    objct.tagText()
    objct.lTupleToList()
    objct.createDataframe()
    objct.translateTo()
    objct.exports()