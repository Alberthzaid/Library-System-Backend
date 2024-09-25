from config.index import Connect
from flask import jsonify , request
from objects.Library import Library

supabase = Connect.connect()
tableLibrary = supabase.table("library")

class LibraryControllers:
    def __init__():
        pass
    


    def getLibrary() -> jsonify:
        response = tableLibrary.select('*').execute()
        print("==== GETTING LIBRARY ====")
        return jsonify(response.data)

    def addLibrary(data:request):
        library  = Library(data.get("name"), data.get("location") )
        response = tableLibrary.insert(library.getBody()).execute()
        print(f'=== LIBRARY CREATED {library.getName()}')
        return jsonify(response.data)

    def updateLibrary( id:int ,req : request) -> jsonify:
        library = Library(req.get("name") , req.get("location"))
        response = tableLibrary.update(library.getBody()).eq('id' , id).execute()
        print(f"=== LIBRARY UPDATED {id}")
        return jsonify(response.data)
    
    def deleteLibrary(id : int) -> jsonify:
        response = tableLibrary.delete().eq('id',id).execute()
        return jsonify(response.data)
    






