from flask import Blueprint, render_template, request
from src.controllers.getters import getTeamNameByID, getUrlsByID


viewRoutes = Blueprint('view', __name__, url_prefix='/view')


@viewRoutes.route("/equipes")
def getTeams():

    return render_template('equipes.html')


@viewRoutes.route("/links/<teamID>", methods=["GET", "POST"])
def getViewTeam(teamID):
    teamName = getTeamNameByID(teamID)
    urls = getUrlsByID(teamID)

    return render_template('links.html', teamID=teamID, teamName=teamName, urls=urls)
