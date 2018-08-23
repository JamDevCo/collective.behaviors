import uuid
from Products.CMFCore.interfaces import IDublinCore
from plone.autoform import directives
from zope.schema.interfaces import IFromUnicode
from plone.autoform.interfaces import IFormFieldProvider
from zope import schema
from plone.supermodel import model
from plone.autoform import directives
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider
from plone.schema import Email
from plone.app.users.schema import checkEmailAddress
from plone.namedfile.field import NamedBlobImage
from zope.interface import Interface
from plone.app.z3cform.widget import AjaxSelectFieldWidget, SelectFieldWidget

from plone.formwidget.namedfile.widget import NamedImageFieldWidget
from collective.z3cform.datagridfield import BlockDataGridFieldFactory
from collective.z3cform.datagridfield import DictRow
from collective.behaviors import _, util


class IEntity(Interface):
    """Abstract marker interface.
    """


@provider(IFormFieldProvider)
class IOrganisation(model.Schema, IEntity):
    organisation_type = schema.Choice(
        title=_(u"Organisation Type"),
        vocabulary=u"collective.vocabularies.organisation.types",
        required=True,
    )
    industry = schema.Choice(
        title=_(u"Industry"),
        vocabulary=u"collective.vocabularies.organisation.industries",
        required=True,
    )
    directives.widget(
        'industry',
        SelectFieldWidget
    )
    date_founded = schema.Date(
        title=_(u"Date Founded"),
        required=False
    )
    organisation_size = schema.Choice(
        title=_(u"Organisation Size"),
        vocabulary=u"collective.vocabularies.organisation.sizes",
        required=True,
    )