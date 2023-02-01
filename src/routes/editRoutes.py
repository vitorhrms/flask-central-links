from flask import Blueprint, render_template, request, redirect, url_for
from src.controllers.getters import getTeamNameByID, getUrlsByID
from src.controllers.setters import addUrl, deleteUrlByID

editRoutes = Blueprint('edit', __name__, url_prefix='/edit')

@editRoutes.route("/equipes")
def edit():

    return render_template('editEquipes.html')

@editRoutes.route("/links/<teamID>", methods=["GET", "POST"])
def editLinks(teamID):
    if request.method == "POST":
        URL_id = request.form['URL_id']
        deleteUrlByID(URL_id)
    teamName = getTeamNameByID(teamID)
    urls = getUrlsByID(teamID)

    return render_template("editLinks.html", teamID=teamID, teamName=teamName, urls=urls)


@editRoutes.route("/links/<teamID>/add", methods=["GET", "POST"])
def addUrls(teamID):
    teamName = getTeamNameByID(teamID)
    if request.method=="POST":
        try:
            url = request.form
            addedUrl = addUrl(url["titulo"], url["url"], teamID)
            if addedUrl==True:
                return redirect(url_for('edit.editLinks', teamID=teamID))
            else:
                return render_template('addLinks.html',teamName=teamName, teamID=teamID, blockToShow="Erro")
        except Exception as e:
            print(e)
            return render_template('addLinks.html',teamName=teamName, teamID=teamID, blockToShow="Erro")

    return render_template("addLinks.html", teamName=teamName, teamID=teamID)
