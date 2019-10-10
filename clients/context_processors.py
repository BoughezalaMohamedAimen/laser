from .forms import ClientForm
import datetime
from caisse.models import Caisse
def add_client_form_to_context(request):
    clientForm=ClientForm()

    return {
        'AddClientForm': clientForm
    }
