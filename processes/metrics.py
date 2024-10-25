from assisteds.models import AssistedDocumentModel
from processes import utils
from processes.models import ProcessesModel, ProcessDocumentModel, ProcessesNotesModel
from processes.forms import ProcessesDocumentForm,  ProcessesNotesForm
from requireds.forms import RequiredsForm
from responsibles.models import ResponsiblesDocumentsModel


def get_context_data(request, instance, context):
    document_assisted = AssistedDocumentModel.objects.filter(id_assisted=instance.id_assisted)
    document_responsible = ResponsiblesDocumentsModel.objects.filter(id_responsible=instance.id_responsible)
    required = ProcessesModel.objects.filter(id_required=instance.id_required).first()
    note_waring = ProcessesNotesModel.objects.filter(id_process=instance.pk, status='0')


    if request.POST:
        context['requireds_form'] = RequiredsForm(request.POST)
        context['form_notes'] = ProcessesNotesForm(request.POST)
    else:
        context['requireds_form'] = RequiredsForm(initial={'id_assisted': instance.id_assisted})
        context['form_notes'] = ProcessesNotesForm(initial={'id_process': instance.pk})

    print(note_waring)

    action_mapping = utils.action_mapping()
    context['categories'] = action_mapping
    context['required'] = required
    context['document_assisted'] = document_assisted
    context['document_responsibles'] = document_responsible
    context['note_waring'] = note_waring
    return context

def get_context_data_document(instance, context):
    documents_assisted = AssistedDocumentModel.objects.filter(id_assisted=instance.get('id_assisted') )
    documents_responsible = ResponsiblesDocumentsModel.objects.filter(id_responsible=instance.get('id_responsible'))
    context['documents_assisted'] = documents_assisted
    context['documents_responsible'] = documents_responsible

    print(instance.id_assisted)
    return context