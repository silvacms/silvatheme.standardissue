from zope.cachedescriptors.property import CachedProperty
from silva.core.layout.interfaces import ISilvaSkin
from silva.core import conf as silvaconf
from silva.core.layout.porto.porto import Layout as PortoLayout
from silva.core.layout.porto.interfaces import IPorto

class IStandardIssue(IPorto):
    """Layer for standard issue theme
    """

    silvaconf.resource('styles/default.css')

class IStandardIssueSkin(IStandardIssue, ISilvaSkin):
    """Skin for standard issue theme
    """

    silvaconf.skin('Standard Issue')

silvaconf.layer(IStandardIssue)

class Layout(PortoLayout):
    
    @CachedProperty
    def publication_title(self):
        return self.content.get_publication().get_title()
    
    @CachedProperty
    def publication_url(self):
        return self.context.get_publication().absolute_url()
