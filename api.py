#Import library flask
import flask
from flask import request, jsonify

#Création de l'objet flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Quelques données tests pour l’annuaire sous la forme d’une liste de dictionnaires
employees=[
   {
    'id': 0,
	'Nom': 'Dupont',
	'Prenom': 'Jean',
	'Fonction': 'Développeur',
	'Anciennete': '5'
    },
   {
    'id': 1,
	'Nom': 'Durand',
	'Prenom': 'Elodie',
	'Fonction': 'Directrice Commerciale',
	'Anciennete': '4'
    },
   {
    'id': 2,
	'Nom': 'Lucas',
	'Prenom': "Jérémie",
	'Fonction': 'DRH',
	'Anciennete': '4'
    }
]

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'matteoz',
    'password': 'matteoz',
    'database': 'demo'
}

#GET hello world
@app.route('/matteo', methods=['GET'])
def home():
   return "<h1>Hello world !</h1>"

#GET all employees
@app.route('/api/v1/resources/employees/all', methods=['GET'])
def api_all():
   return jsonify(employees)

#GET employees with ID
@app.route('/api/v1/resources/employees/<int:id>', methods=['GET'])
def get_entry(id):
    # Rechercher l'entrée avec l'ID spécifié
    for entry in employees:
        if entry['id'] == id:
            return jsonify(entry)
    # Si l'entrée n'a pas été trouvée   
    return jsonify({'error': 'L\'entrée n\'a pas été trouvée.'}), 404

#DELETE employees with ID
@app.route('/api/v1/resources/employees/delete/<int:id>', methods=['DELETE'])
def delete_entry(id):
    # Rechercher l'entrée avec l'ID spécifié
    for entry in employees:
        if entry['id'] == id:
            employees.remove(entry) 
            return jsonify({'message': 'L\'entrée a été supprimée.'})
    # Si l'entrée n'a pas été trouvée
    return jsonify({'error': 'L\'entrée n\'a pas été trouvée.'}), 404

#Execute l'application
app.run()