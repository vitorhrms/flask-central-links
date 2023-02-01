from flask import Flask, render_template
from src.routes.viewRoutes import viewRoutes
from src.routes.editRoutes import editRoutes
from src.controllers.getters import getAllTeams

app = Flask(__name__, template_folder='src/templates',  static_folder='src/static')

app.config['SECRET_KEY'] = '59371830d4ba99ddf9ff52a4d02dd56a6daf130c4417b9f7'

app.register_blueprint(viewRoutes)
app.register_blueprint(editRoutes)


@app.context_processor
def setMenuGlobalVariables():
  allTeams = getAllTeams()
  return {"allTeams":allTeams}

@app.route("/", methods=['POST', 'GET'])
def index():
  return render_template('home.html')


if __name__=='__main__':
  app.run(debug=True, port=3000)

