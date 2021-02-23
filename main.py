import polyglot
from polyglot.text import Text

class  FrenchPolyglot():
    def getText(self, text):
        self.text = Text(text, hint_language_code="fr")
    def tagText(self):
        print(self.text.pos_tags)



if __name__ == "__main__":
    objct = FrenchPolyglot()
    objct.getText("Le problème n’est pas tant l’“islamo-gauchisme” que le dévoiement militant de l’enseignement et de la recherche")
    objct.tagText()


