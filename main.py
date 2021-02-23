from polyglot.text import Text
from pandas import DataFrame
from googletrans import Translator


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
        self.classificationList = []
        for tupla in range(len(self.tagged_text)):
            if self.tagged_text[tupla][0] in ["“", "”", "’", "-", ".",","] or self.tagged_text[tupla][1] == "PUNCT":
                continue
            else:
                self.word_list.append(self.tagged_text[tupla][0])
                self.classificationList.append(replaceTo[self.tagged_text[tupla][1]])

    def createDataframe(self):
        FrenchList = DataFrame(self.word_list, columns=["Français"])
        FrenchList["Classe Gramatical"] = self.classificationList
        translator = Translator()
        #FrenchList["English"] = FrenchList["Français"].apply(translator.translate).apply(getattr, args=("text",))
        FrenchList = FrenchList.drop_duplicates(subset="Français").sort_values(by="Français", )
        print(FrenchList)
    

if __name__ == "__main__":
    objct = FrenchPolyglot()
    objct.getText("Le problème n’est pas tant l’“islamo-gauchisme” que que le dévoiement militant de l’enseignement et de la recherche")
    objct.tagText()
    objct.lTupleToList()
    objct.createDataframe()