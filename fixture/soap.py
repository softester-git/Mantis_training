from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-2.25.2/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects(self, username, password, pname):
        client = Client("http://localhost/mantisbt-2.25.2/api/soap/mantisconnect.php?wsdl")
        try:
            p = client.service.mc_project_get_id_from_name(username=username, password=password, project_name=str(pname))
            assert p>0
        except:
            assert False

    def get_projects_del(self, username, password, pname):
        client = Client("http://localhost/mantisbt-2.25.2/api/soap/mantisconnect.php?wsdl")
        try:
            p = client.service.mc_project_get_id_from_name(username=username, password=password, project_name=str(pname))
            assert client.service.mc_project_get_id_from_name(username=username, password=password, project_name=str(pname)) is False
        except:
            assert False