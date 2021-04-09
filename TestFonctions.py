from GBE import Load, Basics, Save

#Pour des fins de test :
page = "0.Book_Description.json"
LoadedBook = "The gardians of the Bookshelves' Adventure"
LoadedPage = Load.loadPage(LoadedBook, page)

Basics.clear()
#Project Root
print(Load.get_project_root())

# Liste des livres
print(Load.listBook())

# Liste des pages
print(Load.listPages(LoadedBook))

# Load Page
print(Load.loadPage(LoadedBook, page))

# Numéro de page suivant 
print(Load.pageNumber(LoadedBook))

# pour les tests on change manuellement le numero de la page :
LoadedPage["ID"] = Load.pageNumber(LoadedBook)
#On change le titre :
LoadedPage["title"] = "Enregistrement test: Essai: " + str(LoadedPage["ID"])

# Test Save d'une page :
Save.savePage(LoadedPage)