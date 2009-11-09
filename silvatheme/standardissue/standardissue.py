from silva.core.layout.interfaces import ISilvaSkin
from silva.core.layout.porto.interfaces import IPorto
from silva.core import conf as silvaconf

class IStandardIssue(IPorto):
    """Layer for standard issue theme
    """

    silvaconf.resource('styles/default.css')

class IStandardIssueSkin(IStandardIssue, ISilvaSkin):
    """Skin for standard issue theme
    """

    silvaconf.skin('Standard Issue')

silvaconf.layer(IStandardIssue)

class Layout(porto.Layout):
    
    @CachedProperty
    def publication_title(self):
        return self.content.get_publication().get_title()
    
    @CachedProperty
    def publication_url(self):
        return self.context.get_publication().absolute_url()
